from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class UserManager(models.Manager):
    def validateUser(self, postData):
        # PASSWORD_REGEX = re.compile(r'[A-Za-z]$')
        errors = {}
        
        if len(postData['name']) < 3:
            errors['name'] = "Name must be more than 3 characters"
        if len(postData['username']) < 3:
            errors['username'] = "Username must be more than 3 characters"
        if len(postData['password']) <1:
            errors['password'] ="Password must be more than 1 character"
        if postData['password'] != postData['confirm_pw']:
            errors['password'] = "Passwords does not match"
        if User.objects.filter(username=postData['username']).exists():
            errors['username'] = "This Username already exist"
        if User.objects.filter(name=postData['name']).exists():
            errors['name'] = "This Name already exsist"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_hired = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

class WishManager(models.Manager):
    def validateWish(self, postData, user_id):
        errors = {}
       
        if len(postData['item']) < 3:
            errors['item'] = "Must contain more than 3 character"
            return errors
            
        else:
            added_by = User.objects.get(id = user_id)
            new_wish = Wish.objects.create(
                item = postData['item'],
                added_by = added_by)
            new_wish.wishers.add(added_by)
            return

class Wish(models.Model):
    item = models.CharField(max_length=255)
    added_by = models.ForeignKey(User, related_name= 'added_joined')
    wishers = models.ManyToManyField(User, related_name='wish_joined')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = WishManager()
    

