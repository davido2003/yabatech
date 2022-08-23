from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.core.validators import RegexValidator
from datetime import datetime

class Meta:

    app_label = 'GRsystem'
class Profile(models.Model):
    typeuser =(('student','student'),('grievance', 'grievance'))
    email = models.EmailField(max_length=30, blank=True)
    COL=(('College1','College1'),('College2','College2')) #change college names
    user =models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    collegename=models.CharField(max_length=29,choices=COL,blank=False)
    contactnumber = models.CharField( max_length=15, blank=True) 
    matricnumber = models.CharField(max_length=15) 
    type_user=models.CharField(max_length=20,default='student',choices=typeuser)
    CB=(('ComputerScience',"ComputerScience"),('FoodTechnology',"FoodTechnology"),('Statistics',"Statistics"),('Business Administration',"Business Administration"))
    Department=models.CharField(choices=CB,max_length=29,default='ComputerScience')
    LS=(('ND1 FT',"ND1 FT"),('ND1 PT',"ND1 PT"),('ND2 FT',"ND2 FT"),('ND2 PT',"ND2 PT"),('ND3 PT',"ND3 PT"),('HND1 FT',"HND1 FT"),('HND1 PT',"HND1 PT"),('HND2 FT',"HND2 FT"),('HND2 PT',"HND2 PT"),('HND3 PT',"HND3 PT"))
    Levels=models.CharField(choices=LS,max_length=29,default='NDI')
    
    def __str__(self):
        return self.collegename
    def __str__(self):
        return self.user.username
    
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

'''@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()'''


class Complaint(models.Model):
    STATUS =((1,'Solved'),(2, 'InProgress'),(3,'Pending'))
    TYPE=(('ClassRoom',"ClassRoom"),('Teacher',"Teacher"),('Management',"Management"),('College',"College"),('Other',"Other"))
    
    Subject=models.CharField(max_length=200,blank=False,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    image = models.ImageField(upload_to ='uploads/')
    Type_of_complaint=models.CharField(choices=TYPE,null=True,max_length=200)
    Description=models.TextField(max_length=4000,blank=False,null=True)
    Time = models.DateField(auto_now=True)
    status=models.IntegerField(choices=STATUS,default=3)
    
   
    def __init__(self, *args, **kwargs):
        super(Complaint, self).__init__(*args, **kwargs)
        self.__status = self.status

    def save(self, *args, **kwargs):
        if self.status and not self.__status:
            self.active_from = datetime.now()
        super(Complaint, self).save(*args, **kwargs)
    
    def __str__(self):
     	return self.get_Type_of_complaint_display()
    def __str__(self):
 	    return str(self.user)

class Grievance(models.Model):
    guser=models.OneToOneField(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.guser