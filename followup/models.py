import random
import string

from django.db import models
from django.utils.text import slugify

from organization.models import Organization


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class FollowUp(models.Model):
    """
    user will write follow up for organizations
    """

    class Meta:
        verbose_name = "پیگیری"
        verbose_name_plural = "پیگیری ها"

    organization_name = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='سازمان')
    descriptions = models.TextField(verbose_name='توضیحات')
    creator = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name='کاربر ثبت کننده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    slug = models.SlugField(unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug())
        super(FollowUp, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.organization_name.name} {self.created_at}'

