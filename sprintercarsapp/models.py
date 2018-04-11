from datetime import datetime

from django.db import models


def upload_product_image(instance, filename):
    now_time = datetime.now().microsecond
    return '{}/{}'.format("Products", '%s.jpg' % now_time)


class Products(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_product_image, null=True, blank=True)
    description = models.CharField(max_length=300)
    specification = models.CharField(max_length=200)
    is_latest = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return str(self.id)

