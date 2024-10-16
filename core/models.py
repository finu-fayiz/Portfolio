from django.db import models

# Create your models here.
# about-model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField()

    class Meta :
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"
    

# service model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Service name ")
    description = models.TextField(verbose_name = "About service")
   

    def __str__(self):
        return self.name
    

# recent work-model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name = "Work Title ")
    image = models.ImageField(upload_to="works")
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


