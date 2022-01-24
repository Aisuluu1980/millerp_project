from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Project')
    image = models.ImageField(upload_to='projects_images', null=True, blank=True, verbose_name='Image')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation project')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Message(models.Model):
    name=models.CharField(max_length=70, verbose_name='')
    email=models.EmailField(max_length=70, blank=True, verbose_name='')
    phone= models.CharField(max_length=30, blank=True, verbose_name='')
    subject=models.CharField(max_length=400, blank=True, verbose_name='')
    message=models.CharField(max_length=1000, blank=True, verbose_name='')

    def __str__(self):
        return self.name

