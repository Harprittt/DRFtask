from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid 
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
TEACHER = 'TE'
STUDENT = 'ST'
UNKNOWN = 'UN'
TYPE_CHOICES = (
    (TEACHER, 'Teacher'),
    (STUDENT, 'Student'),
    (UNKNOWN, 'Unknown'),
    )



# Create your models here.

class User(AbstractUser):
    type = models.CharField(choices=TYPE_CHOICES, max_length=20, default=UNKNOWN)
   

    def __str__(self):
        return self.username






@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)








class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=1000)
    description = models.CharField(blank=True, null=True, max_length=5000)
    order = models.IntegerField(default=0, blank=False, null=False)
    created_utc = models.DateTimeField(null=True, blank=True)
    modified_utc = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name
 
 
class CourseChapter(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey('Course', related_name='course_chapter', on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=False, blank=False)
    order = models.IntegerField(default=0, blank=False, null=False)
    created_utc = models.DateTimeField()
    modified_utc = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
 
 
class Assignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(blank=True, null=True, max_length=5000)
    course = models.ForeignKey('Course', related_name='course_assignments', on_delete=models.CASCADE)
    course_chapter = models.ForeignKey('CourseChapter', related_name='course_chapter_assignments', on_delete=models.CASCADE)


    def __str__(self):
        return self.title



