from django.db import models
# Create your models here.
class CommonFeatures(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    release_date=models.DateTimeField()
    poster_image = models.ImageField(upload_to='photos%y%m%d',null=True,blank=True)
    categories=models.ManyToManyField('Category')
    actors=models.ManyToManyField('Casts')

class Movie(CommonFeatures):
    running_time = models.IntegerField()
    class Meta:
        ordering=['title']

    def __str__(self):  # to replace Movie object that appear in UI by name of the movie
        return self.title


class Series(CommonFeatures):
    episodes_num = models.IntegerField()


class Category(models.Model):
    type=models.CharField(max_length=150)
    #rel=models.OneToManyField(Movie,on_delete=models.CASCADE)
    class Meta:
        verbose_name='Categorie'
        ordering=['type']

    def __str__(self):  # to replace Movie object that appear in UI by name of the movie
        return self.type


class Casts(models.Model):
    cast_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Cast'

    def __str__(self):  # to replace Movie object that appear in UI by name of the movie
         return self.cast_name
