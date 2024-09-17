from django.db import models

# Create your models here

class Brain(models.Model):
    
    si_no = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Production_link = models.CharField(max_length=300)
    Description = models.TextField()

def __str__(self):
    return self.Name







# class Child(models.Model):
    
    
#     child_name = models.CharField(max_length=100)
#     child_view_ID  = models.IntegerField()
#     child_id = models.AutoField(primary_key=True)

#     class Meta:
#         db_table = '3rlabs_child'





































































# class User(models.Model):
   
#     Users_FirstName = models.CharField(max_length=100)
#     Users_id = models.AutoField(primary_key=True)

#     class Meta:
#         db_table = '3rlabs_users'



# class InterventionFeedback(models.Model):
    
#     child  = models.ForeignKey(Child,on_delete=models.CASCADE)
#     enabler = models.ForeignKey(User,on_delete=models.CASCADE)
#     meeting_record_id = models.AutoField(primary_key=True)
    
    
#     class Meta:
        
#         db_table = '3rlabs_intervention_feedback'


# class InterventionMeetingRecord(models.Model):
    
#     si_no = models.AutoField(primary_key=True)
#     # feedback = models.ForeignKey(InterventionFeedback,on_delete=models.CASCADE)
#     scheduled_time = models.DateTimeField()

#     class Meta:
        
#         db_table = '3rlabs_intervention_meeting_record'




# class Child(models.Model):
    
    
#     child_name = models.CharField(max_length=100)
#     child_view_ID  = models.IntegerField()
#     child_id = models.AutoField(primary_key=True)

#     class Meta:
#         db_table = '3rlabs_child'

# class User(models.Model):
   
#     Users_FirstName = models.CharField(max_length=100)
#     Users_id = models.AutoField(primary_key=True)

#     class Meta:
#         db_table = '3rlabs_users'



# class InterventionFeedback(models.Model):
    
#     child  = models.ForeignKey(Child,on_delete=models.CASCADE)
#     enabler = models.ForeignKey(User,on_delete=models.CASCADE)
#     meeting_record_id = models.IntegerField(primary_key=True) 
    
#     class Meta:
        
#         db_table = '3rlabs_intervention_feedback'

