from django.db import models
class LandLords (models.model):
    first_name = models.CharField(max_length-50)
    last_name = models.CharField(max_length-50)
    ratingOfLord = models.IntegerField()

class ReviewsOfLandLords (models.Model):
    dateOfReview = models.DateField()
    textOfReview = models.CharField(max_length-500)
    reviewOfLord = model.ForeignKey(Home)
    typingReview = null

class ReviewsOfHome (models.Model):
    dateOfReview = models.DateField()
    textOfReview = models.CharField(max_length-500)
    reviewOfLord = model.ForeignKey(LandLords)
    typingReview = null

class photosForReviews (models.Model):
    Review = models.ForeignKey(Reviews)
    datePhotos = models.DateField()

class home ():
    address = models.CharField(max_length-250)
    ratingOfHome = models.IntegerField()
    reviewOfHome = model.ForeignKey(LandLords)

class user (models.Model):
    FirstName = models.CharField(max_length-50)
    LastName = models.CharField(max_length-50)
