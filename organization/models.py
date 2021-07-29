from django.core.validators import RegexValidator
from django.db import models
from django.utils.text import slugify

from product import models as product_models

phone_regex = RegexValidator(regex=r"^[0][9]\d{9}$", message='شماره اشتباه است.')
organ_phone_regex = RegexValidator(regex=r"^0[0-9]{2,}[0-9]{7,}$", message='شماره اشتباه است.')


class Organization(models.Model):
    """
    users will create organizations
    """
    class Meta:
        verbose_name = "سازمان"
        verbose_name_plural = "سازمان ها"

    name = models.CharField(max_length=100, unique=True,
                            error_messages={'unique': "این نام در سیستم ثبت شده است."}, verbose_name='نام سازمان')
    province = models.CharField(max_length=100, verbose_name='استان')
    phone_number = models.CharField(unique=True, validators=[organ_phone_regex], max_length=11,
                                    verbose_name='تلفن سازمان')
    number_of_employees = models.PositiveIntegerField(verbose_name='تعداد کارمندان')
    organization_product = models.ManyToManyField(product_models.OrganizationProduct, verbose_name='محصولات تولیدی')
    audience_full_name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی مخاطب')
    audience_phone_number = models.CharField(validators=[phone_regex], max_length=11, verbose_name='تلفن مخاطب')
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    creator = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name='کاربر ثبت کننده')
    slug = models.SlugField(unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.phone_number + "-" + self.email)
        super(Organization, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/"

    def suggestion(self):
        op = product_models.OrganizationProduct.objects.all()
        return product_models.Product.objects.filter(can_use_for__organization__organization_product__in=op).distinct()

    def __str__(self):
        return self.name
