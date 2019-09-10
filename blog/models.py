from django.db import models

# Create your models here.
class Blog (models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    Image = models.ImageField(upload_to ='images/')

    def short_summary(self):
        return self.body[0:100]

    def __str__(self):
        return self.title

    def shortDate(self):
        return self.pub_date.strftime('%b %e %Y')    
