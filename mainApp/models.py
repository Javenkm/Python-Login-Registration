from django.db import models


class UserManager(models.Model):
    def registration_validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters."

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):   #test whether a field matches the pattern
            errors['email'] = "Invalid email address!"

        if len(postData['password'] < 4:
            errors['password'] = "Password must be at least 4 characters.")
        
        if len(postData['password'] < 4:
            errors['password'] = "Password")
        return errors


    def login_validator(self, postData):
        pass


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)