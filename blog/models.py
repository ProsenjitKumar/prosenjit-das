from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# *************** simple blog start ************************
from django.urls import reverse


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class BlogCategory(models.Model):
    title = models.CharField(max_length=255, null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=255, blank=False)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    description = RichTextField()
    post_date = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=True)
    objects = EntryQuerySet.as_manager()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog_home/%s/" %(self.id)
        #return reverse('home_blog', args=[str(self.id)])


    class Meta:
        ordering = ['-post_date']
# *************** simple blog end ************************


# *************** question blog start ************************
class QuestionPost(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=True)
    objects = EntryQuerySet.as_manager()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(QuestionPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/question_list/%s/" %(self.id)

    class Meta:
        ordering = ['-post_date']
# *************** question blog end ************************


