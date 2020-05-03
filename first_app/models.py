from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.pastword

class Registry(models.Model):
    userId = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    musicbrainzArtistId = models.CharField(max_length=100, null=True, blank=True)
    artistName = models.CharField(max_length=100, null=True, blank=True)
    musicbrainzTrackId = models.CharField(max_length=100,null=True, blank=True)
    trackName = models.CharField(max_length=100, null=True, blank=True)


class PREDICTION_CHART(models.Model):
    userId = models.CharField(max_length=100, null=True, blank=True)
    artistId = models.CharField(max_length=200, null=True, blank=True)
    prediction = models.CharField(max_length=200, null=True, blank=True)


class  business(models.Model):
    business_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    stars = models.CharField(max_length=100)
    review_count = models.CharField(max_length=100)
    is_open = models.CharField(max_length=100)
    attributes = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'business'


class  review(models.Model):
    review_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    business_id = models.CharField(max_length=100)
    stars = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    useful = models.CharField(max_length=100)
    funny = models.CharField(max_length=100)
    cool = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'review'

class tip(models.Model):
    text = models.CharField(max_length=1000)
    date = models.CharField(max_length=100)
    compliment_count = models.CharField(max_length=100)
    business_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tip'


class userData(models.Model):
    user_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    review_count = models.CharField(max_length=100)
    yelping_since = models.CharField(max_length=100)
    friends = models.CharField(max_length=100)
    useful = models.CharField(max_length=100)
    funny = models.CharField(max_length=100)
    cool = models.CharField(max_length=100)
    fans = models.CharField(max_length=100)
    elite = models.CharField(max_length=100)
    average_stars = models.CharField(max_length=100)
    compliment_hot = models.CharField(max_length=100)
    compliment_more = models.CharField(max_length=100)
    compliment_profile = models.CharField(max_length=100)
    compliment_cute = models.CharField(max_length=100)
    compliment_list = models.CharField(max_length=100)
    compliment_note = models.CharField(max_length=100)
    compliment_plain = models.CharField(max_length=100)
    compliment_cool = models.CharField(max_length=100)
    compliment_funny = models.CharField(max_length=100)
    compliment_writer = models.CharField(max_length=100)
    compliment_photos = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'userData'


class Document_features(models.Model):
    id_busines = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    id_categorie = models.CharField(max_length=200, null=True, blank=True)
    categorie = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Document_features'

class Categorie(models.Model):
    id_categorie = models.CharField(max_length=200, null=True, blank=True)
    categorie = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Categorie'

class DfReview_train(models.Model):
    user_id = models.CharField(max_length=100, null=True, blank=True)
    business_id = models.CharField(max_length=100, null=True, blank=True)
    stars = models.CharField(max_length=100, null=True, blank=True)
    mean = models.CharField(max_length=100, null=True, blank=True)
    mark = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'DfReview_train'

class DfReview_test(models.Model):
    user_id = models.CharField(max_length=100, null=True, blank=True)
    business_id = models.CharField(max_length=100, null=True, blank=True)
    stars = models.CharField(max_length=100, null=True, blank=True)
    mean = models.CharField(max_length=100, null=True, blank=True)
    mark = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'DfReview_test'

class Prediction(models.Model):
    user_id = models.CharField(max_length=100, null=True, blank=True)
    business_id = models.CharField(max_length=100, null=True, blank=True)
    mark = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Prediction'


class ItemItem(models.Model):
    user_id = models.CharField(max_length=100, null=True, blank=True)
    business_id = models.CharField(max_length=100, null=True, blank=True)
    score = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ItemItem'
