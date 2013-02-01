from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, editable=False)
    phone_number = models.CharField(max_length=30, null=True)

    def __unicode__(self):
        return self.user.username

class Tweet(models.Model):
    """
    Tweets, this is a nearly complete, but simplified set which we get from the api
    """
    tweet_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    from_user_id = models.BigIntegerField()
    from_user = models.CharField(max_length=15)
    from_user_name = models.CharField(max_length=20, null=True)
    geo = models.TextField(null=True)
    iso_language_code = models.CharField(max_length=10, null=True)
    profile_image_url = models.CharField(max_length=255, null=True)
    source = models.TextField(null=True)
    text = models.TextField(max_length=200, null=True)
    to_user_id = models.BigIntegerField(null=True)
    to_user_name = models.CharField(max_length=20, null=True)
    keyword = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.text

class CleanedTweet(models.Model):
    """
    Tweets, this is a nearly complete, but simplified set which we get from the api
    """
    tweet_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    from_user_id = models.BigIntegerField()
    from_user = models.CharField(max_length=15)
    from_user_name = models.CharField(max_length=20, null=True)
    geo = models.TextField(null=True)
    iso_language_code = models.CharField(max_length=10, null=True)
    profile_image_url = models.CharField(max_length=255, null=True)
    source = models.TextField(null=True)
    text = models.TextField(max_length=200, null=True)
    to_user_id = models.BigIntegerField(null=True)
    to_user_name = models.CharField(max_length=20, null=True)
    keyword = models.CharField(max_length=255, null=True)
    count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text



class Query(models.Model):
    keywords = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.keywords

