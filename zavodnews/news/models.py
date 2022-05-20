from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=200)
    tag = models.ForeignKey(
        Tag,
        on_delete=models.SET_NULL,
        related_name='news',
        blank=True,
        null=True
    )
    image = models.ImageField(
        'Картинка',
        upload_to='news/',
        blank=True
    )