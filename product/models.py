from django.db import models
from django.core.validators import FileExtensionValidator
from django.template.defaultfilters import slugify


class OrganizationProduct(models.Model):
    """
    products made by organizations
    """

    class Meta:
        verbose_name = "محصول تولیدی"
        verbose_name_plural = "محصولات تولیدی"

    name = models.CharField(max_length=100, verbose_name='نام محصول تولیدی')

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    tools
    """

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    name = models.CharField(max_length=100, verbose_name='نام محصول')
    price = models.PositiveIntegerField(verbose_name='قیمت محصول')
    tax = models.BooleanField(verbose_name='آیا مشمول مالیات است؟')
    catalogue_pdf = models.FileField(upload_to='catalogue_pdf', validators=[FileExtensionValidator(['pdf'])],
                                     help_text='pdf :فرمت های قابل قبول', verbose_name='کاتالوگ pdf',
                                     blank=True, null=True)
    catalogue_image = models.ImageField(upload_to='catalogue_image', height_field=None, width_field=None,
                                        max_length=100, verbose_name='عکس کاتالوگ', blank=True, null=True)
    technical_features = models.TextField(verbose_name='ویژگی های فنی')
    can_use_for = models.ManyToManyField(OrganizationProduct, verbose_name='قابل استفاده برای تولید محصول تولیدی')

    def __str__(self):
        return self.name

