from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_pic=models.ImageField(upload_to='profilepics', null=True)
    bio=models.CharField(max_length=200)
    adress=models.CharField(max_length=200)
    dob=models.DateTimeField(null=True)
    following=models.ManyToManyField('self',related_name='followed_by')
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Posts(models.Model):
    tittle=models.CharField(max_length=200)
    images=models.ImageField(upload_to='post images',null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='userposts')
    created_date=models.DateTimeField(auto_now_add=True)
    linked_by=models.ManyToManyField(User,related_name='post_like')

    def __str__(self):
        return self.tittle
    
class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    comment_text=models.CharField(max_length=200)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='post_comment')
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text