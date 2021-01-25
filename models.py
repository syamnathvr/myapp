from django.db import models

# Create your models here.
class user_login(models.Model):
   # id
   uname = models.CharField(max_length=50)
   passwd = models.CharField(max_length=25)
   utype = models.CharField(max_length=10)

   def __str__(self):
       return self.uname

class user_profile(models.Model):
   # id
   user_id = models.IntegerField()
   profile_name = models.CharField(max_length=50)
   fname = models.CharField(max_length=50)
   lname = models.CharField(max_length=50)
   dob = models.CharField(max_length=20)
   gender = models.CharField(max_length=10)
   addr1 = models.CharField(max_length=250)
   addr2 = models.CharField(max_length=250)
   addr3 = models.CharField(max_length=250)
   pin = models.CharField(max_length=10)
   contact = models.CharField(max_length=20)
   email = models.CharField(max_length=50)
   about_user = models.CharField(max_length=200)
   dt = models.CharField(max_length=10)
   tm = models.CharField(max_length=10)
   status = models.CharField(max_length=10)

   def __str__(self):
       return self.profile_name

class job_profile(models.Model):
   # id
   user_id = models.IntegerField()
   job_type_id = models.IntegerField()
   fname = models.CharField(max_length=50)
   lname = models.CharField(max_length=50)
   dob = models.CharField(max_length=20)
   gender = models.CharField(max_length=10)
   addr1 = models.CharField(max_length=250)
   addr2 = models.CharField(max_length=250)
   addr3 = models.CharField(max_length=250)
   pin = models.CharField(max_length=10)
   contact = models.CharField(max_length=20)
   email = models.CharField(max_length=50)
   about_job = models.CharField(max_length=200)
   dt = models.CharField(max_length=10)
   tm = models.CharField(max_length=10)
   status = models.CharField(max_length=10)

   def __str__(self):
       return self.job_type_id

class user_searches(models.Model):
   # id
   user_id = models.IntegerField()
   query = models.CharField(max_length=200)
   dt = models.CharField(max_length=10)
   tm = models.CharField(max_length=10)
   status = models.CharField(max_length=10)

   def __str__(self):
       return self.user_id

class user_searches_result(models.Model):
   # id
   user_search_id = models.IntegerField()
   job_profile_id = models.IntegerField()
   status = models.CharField(max_length=10)

   def __str__(self):
       return self.job_profile_id

class user_messages(models.Model):
   # id
   user_id = models.IntegerField()
   job_profile_id = models.IntegerField()
   msg = models.CharField(max_length=200)
   reply = models.CharField(max_length=200)
   dt = models.CharField(max_length=10)
   tm = models.CharField(max_length=10)
   status = models.CharField(max_length=10)

   def __str__(self):
       return self.job_profile_id

class job_master(models.Model):
   # id
   label = models.CharField(max_length=100)

   def __str__(self):
       return self.label

class data_set(models.Model):
   # id
   label_id = models.IntegerField()
   keywords= models.CharField(max_length=1000)

   def __str__(self):
       return self.label_id

class blocked_messages(models.Model):
   # id
   user_id = models.IntegerField()
   user_post_id = models.IntegerField()
   msg = models.CharField(max_length=200)
   dt = models.CharField(max_length=10)
   tm = models.CharField(max_length=10)
   status = models.CharField(max_length=10)

   def __str__(self):
       return self.user_post_id

class user_photos(models.Model):
   # id
   user_id = models.IntegerField()
   pic_path = models.CharField(max_length=200)
   dt = models.CharField(max_length=10)
   tm = models.CharField(max_length=10)
   status = models.CharField(max_length=10)

   def __str__(self):
       return self.pic_path

class job_profile_photos(models.Model):
   # id
   user_id = models.IntegerField()
   pic_path = models.CharField(max_length=200)
   dt = models.CharField(max_length=10)
   tm = models.CharField(max_length=10)
   status = models.CharField(max_length=10)

   def __str__(self):
       return self.user_id