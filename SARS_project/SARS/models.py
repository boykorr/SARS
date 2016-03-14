from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
#from django.contrib.postgres.fields import ArrayField

"""class Researcher(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

class Review(models.Model):
    user = models.ForeignKey(Researcher)
    title = models.CharField(max_length=100) #forms.CharField(max_length=100)
    description = models.CharField(max_length=2000) #widget=forms.Textarea
    #date_started =
    query_string = models.ForeignKey(Query)
    pool_size = models.IntegerField() #forms.NumberInput()
    abstracts_judged = models.IntegerField() #forms.NumberInput()
    documents_judged = models.IntegerField() #forms.NumberInput()

    def __unicode__(self):
        return self.user.username

class Paper(models.Model):
    review = models.ForeignKey(Review)
    title = models.CharField(max_length=100) #forms.CharField(max_length=100)
    authors = ArrayField(models.CharField(max_length=20)) #SimpleArrayField(forms.CharField(max_length=20))
    abstract = models.CharField(max_length=2000) #widget=forms.Textarea"""

class Query(models.Model):
    query = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
