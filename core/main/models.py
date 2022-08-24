from django.db import models

# Create your models here.
class Slider(models.Model):
    name = models.CharField('Slider name', max_length=30)
    about = models.TextField('Slider text')
    img = models.ImageField('Slider image', upload_to='media')
    date = models.DateField('Slider date')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'


class About1(models.Model):
    name = models.CharField('Post name', max_length=30)
    about = models.TextField('Post text')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About1'
        verbose_name_plural = 'Abouts1'


class About2(models.Model):
    name = models.CharField('Post name', max_length=30)
    about = models.TextField('Post text')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About2'
        verbose_name_plural = 'Abouts2'


class About3(models.Model):
    name = models.CharField('Post name', max_length=30)
    about = models.TextField('Post text')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About3'
        verbose_name_plural = 'Abouts3'