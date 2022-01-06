from django.db import models

# Create your models here.
class FirstSection(models.Model):
    personal_photo_link = models.TextField()
    name = models.TextField()
    bio = models.TextField()   
    resume_link = models.TextField()
    facebook_link = models.TextField()
    twitter_link = models.TextField()
    google_link = models.TextField()
    instagram_link = models.TextField()
    background_img = models.TextField()
    


class About_Basic_Information(models.Model):
    about = models.TextField()
    age = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    address = models.TextField()
    language = models.TextField()

class Skills(models.Model):
    skill = models.CharField(max_length=255)
    percentage = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.skill}"
     
class Projects(models.Model):
    photo = models.TextField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.TextField()
    
    def __str__(self):
        return f"{self.title}"

class Experience(models.Model):
    from_to = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.company_name}"

class Education(models.Model):
    from_to = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    instituation = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.major}"



   

 


