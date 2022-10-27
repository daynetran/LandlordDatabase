from django.db import models
class LandLords (models.model):
    first_name = models.CharField(max_length-50)
    last_name = models.CharField(max_length-50)
    ratingOfLord = models.IntegerField()
    class Meta:
        ordering = ['last_name', 'first_name']
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    def get_absolute_url(self):
        return reverse('landlord-detail', args=[str(self.id)])

class ReviewsOfLandLords (models.Model):
    dateOfReview = models.DateField()
    textOfReview = models.CharField(max_length-500)
    reviewOfLord = models.ForeignKey(LandLords)
    typingReview = models.TextField()



class ReviewsOfHome (models.Model):
    dateOfReview = models.DateField()
    textOfReview = models.CharField(max_length-500)
    reviewOfLord = models.ForeignKey(home)
    typingReview = models.TextField()

class photosForReviews (models.Model):
    Review = models.ForeignKey(home)
    datePhotos = models.DateField()

class home ():
    address = models.CharField(max_length-250)
    ratingOfHome = models.IntegerField()
    reviewOfHome = models.ForeignKey(LandLords)
    class Meta:
        ordering = ['address']
    def get_absolute_url(self):
        return reverse('home-detail', args=[str(self.id)])
    def __str__(self):
        return f'{self.address}'

class user (models.Model):
    FirstName = models.CharField(max_length-50)
    LastName = models.CharField(max_length-50)
    class Meta:
        ordering = ['last_name', 'first_name']
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])