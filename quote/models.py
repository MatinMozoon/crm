import random
import string

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Sum, F, Case, When
from django.urls import reverse
from django.utils.text import slugify

from organization.models import Organization
from product.models import Product


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Quote(models.Model):
    """
    quote will be create by user
    """

    class Meta:
        verbose_name = "پیش فاکتور"
        verbose_name_plural = "پیش فاکتور ها"

    organization_name = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='انتخاب سازمان')
    creator = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name='کاربر ثبت کننده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    slug = models.SlugField(unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug())
        super(Quote, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.organization_name} ({self.created_at}) {self.creator}"

    def get_absolute_url(self):
        return reverse('quote:quote-detail', kwargs={'pk': self.pk})

    def get_total_quantity(self):
        return self.quote_item.all().aggregate(Sum('quantity')).get('quantity__sum', 0)

    def total_price(self):
        return self.quote_item.all().annotate(each_item_price=F('quantity') * F('product_name__price')) \
            .aggregate(Sum('each_item_price'))['each_item_price__sum']

    def get_quote_discount(self):
        return self.quote_item.all().annotate(
            total_price=F('quantity') * F('product_name__price')).annotate(
                total_discount=(F('discount') * F('total_price') / 100)) \
            .aggregate(Sum('total_discount'))['total_discount__sum']

    def get_quote_tax(self):
        return self.quote_item.all().annotate(
            total_base_price=F('quantity') * F('product_name__price')).annotate(
            total_price=F('total_base_price') - (F('discount') * F('total_base_price') / 100)).annotate(
            total_tax=Case(
                When(product_name__tax=True, then=(F('total_price') * 9 / 100)),
                When(product_name__tax=False, then=0),
                output_field=models.PositiveIntegerField()
            )
        ).aggregate(Sum('total_tax'))['total_tax__sum']

    def total_price_with_tax(self):
        return self.quote_item.all().annotate(
            total_base_price=F('quantity') * F('product_name__price')).annotate(
            total_price=F('total_base_price') - (F('discount') * F('total_base_price') / 100)).annotate(
            total_price=Case(
                When(product_name__tax=True, then=F('total_price') + (F('total_price') * 9 / 100)),
                When(product_name__tax=False, then=F('total_price')),
                output_field=models.PositiveIntegerField()
            )
        ).aggregate(Sum('total_price'))['total_price__sum']

    # def total_price_with_tax(self):
    #     ip = self.quote_item.all().annotate(each_item_price=F('quantity') * F('product_name__price')) \
    #         .aggregate(Sum('each_item_price'))['each_item_price__sum'] or 0
    #     return ip + ((ip * 9) / 100)


class QuoteItem(models.Model):
    """
    items in a quote
    """

    class Meta:
        verbose_name = "دستگاه مورد درخواست"
        verbose_name_plural = "دستگاه های مورد درخواست"

    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, verbose_name='پیش فاکتور', related_name='quote_item')
    product_name = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='انتخاب دستگاه')
    quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1)], verbose_name='تعداد')
    discount = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], verbose_name='درصد تخفیف')

    def each_item_price(self):
        return self.product_name.price * self.quantity

