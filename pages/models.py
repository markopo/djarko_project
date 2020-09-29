from django.db import models
from django.template.defaultfilters import slugify


class Page(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(null=True, blank=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content', blank=True)
    photo = models.ImageField('Photo', upload_to='pages', blank=True)
    published = models.BooleanField(default=False)
    is_front_page = models.BooleanField('Set as front page', default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        if self.is_front_page:
            pages = Page.objects.all()
            for page in pages:
                if page.id != self.id:
                    page.is_front_page = False
                    page.save()

        super(Page, self).save(*args, **kwargs)



