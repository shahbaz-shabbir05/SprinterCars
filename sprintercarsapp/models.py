from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


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


def upload_slider_image(instance, filename):
    now_time = datetime.now().microsecond
    return '{}/{}'.format("Slider Images", '%s.jpg' % now_time)


class SliderImages(models.Model):
    slider_image = models.ImageField(upload_to=upload_slider_image, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Testimonial(models.Model):
    title = models.CharField('Title', max_length=100)
    content = RichTextField('Content')
    date = models.DateTimeField('Date', auto_now_add=True)
    url_slug = models.SlugField(editable=False)

    # def __str__(self):
    #     return str(self.id)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_slug = slugify(self.title)
            super(Testimonial, self).save(*args, **kwargs)
        else:
            super(Testimonial, self).save(*args, **kwargs)
