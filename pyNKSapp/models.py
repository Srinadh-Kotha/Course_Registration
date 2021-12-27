from django.db import models

# from semProjectDjango.pyNKSapp.views import courselist1

# Create your models here.
class signupdetails(models.Model):
    ins_stu_id=models.IntegerField(max_length=10)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    dob=models.CharField(max_length=30)
    password=models.CharField(max_length=50)
    reenterpassword=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    prev_edu_percentage=models.IntegerField(max_length=10)
    class Meta:
        db_table="signupdetails"


class number_of_students(models.Model):
    no_of_students=models.IntegerField()
    class Meta:
        db_table="number_of_students"



class staff_details(models.Model):
    staff_name=models.CharField(max_length=25)
    subject=models.CharField(max_length=25)
    class Meta:
        db_table="staff_details"

class student_enroll(models.Model):
    institute=models.CharField(max_length=25)
    course=models.CharField(max_length=25)
    class Meta:
        db_table="student_enroll"

class institutes(models.Model):                     
    chairman_id=models.ForeignKey(signupdetails,on_delete=models.CASCADE) 
    institute_name=models.CharField(max_length=50)
    ins_photo=models.CharField(max_length=50)
    class Meta:
        db_table="institutes"

class degree(models.Model):
    institute_id=models.ForeignKey(institutes,on_delete=models.CASCADE)
    degree_name=models.CharField(max_length=50)
    duration=models.CharField(max_length=20)
    start_date=models.CharField(max_length=20)
    end_date=models.CharField(max_length=20)
    fee=models.CharField(max_length=20)
    advance_fee=models.CharField(max_length=20)
    req_percentage=models.IntegerField(max_length=10)
    class Meta:
        db_table="degree"

class specialization(models.Model):
    degree_id=models.ForeignKey(degree,on_delete=models.CASCADE)
    institute_id=models.ForeignKey(institutes,on_delete=models.CASCADE)
    specialization_name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    seats_available=models.IntegerField(max_length=50)
    class Meta:
        db_table="specialization"

class enrolled(models.Model):
    user=models.IntegerField(max_length=10)
    institute_id=models.IntegerField(max_length=10)
    degree_id=models.IntegerField(max_length=10)
    specialization_id=models.IntegerField(max_length=10)
    class Meta:
        db_table="enrolled"

class cardpayment(models.Model):
    name=models.CharField(max_length=50)
    card_num=models.CharField(max_length=50)
    mnth=models.CharField(max_length=10)
    year=models.IntegerField(max_length=10)
    cvv=models.IntegerField(max_length=10)
    gmail=models.CharField(max_length=50)
    class Meta:
        db_table="cardpayment"


