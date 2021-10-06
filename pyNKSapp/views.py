from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from pyNKSapp.models import signupdetails,staff_details,student_enroll,number_of_students,enrolled
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponseRedirect
# Create your views here.

def error_404_view(request,exception):
    return render(request,'404.html')

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def forgotpass(request):
    return render(request,'forgotpass.html')

def passSent(request):
    return render(request,'passSent.html')

def logindata(request):
    if request.method=="POST":
        try:
            # if(request.POST['password']==""):
            #     # userPassword = signupdetails.objects.get(email=request.POST['email'])
            #     userPassword = signupdetails.objects.get(email=request.POST['email'])
            #     # for i in userPassword:
            #         # if(request.POST['email']==userPassword.email):
            #         #     passw=userPassword.password
            #     print("user details=",userPassword.password)
            #     # request.session['email']=userPassword.email
            #     return render(request,'login.html')
            userdetails=signupdetails.objects.get(email=request.POST['email'],password=request.POST['password'])
            print("Username=",userdetails)
            request.session['email']=userdetails.email
            return render(request,'home.html')
        except signupdetails.DoesNotExist as e :
            messages.success(request,'username/password invalid...!')
    return render(request,'login.html')

def forgotPassword(request):
    if request.method=="POST":
        try:
                userPassword = signupdetails.objects.get(email=request.POST['email'])
                print("user details=",userPassword.password,'email=',userPassword.email)
                # mailsender = srinadhkotha8@gmail.com

                send_mail(
                        'password',
                        userPassword.password,
                        'srinadhkotha8@gmail.com',
                        [userPassword.email],
                        fail_silently=False,
                )
                return render(request,'passSent.html')

        except signupdetails.DoesNotExist as e :
            messages.success(request,'username is not registered...!')
    return render(request,'forgotpass.html')


def logout(request):
    try:
        del request.session['email']
    except:
        return render(request,'home.html')
    return render(request,'home.html')


def insertrecord(request):
    if request.method=='POST':
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('dob') and request.POST.get('gender'):
            saverecord=signupdetails()
            saverecord.firstname=request.POST.get('firstname')
            saverecord.lastname=request.POST.get('lastname')
            saverecord.phone=request.POST.get('phone')
            saverecord.email=request.POST.get('email')
            saverecord.dob=request.POST.get('dob')
            saverecord.password=request.POST.get('password')
            saverecord.reenterpassword=request.POST.get('reenterpassword')
            saverecord.gender=request.POST.get('gender')
            if saverecord.password!=saverecord.reenterpassword:
                return redirect('insertrecord')
            else:
                saverecord.save()
            #saverecord.save()
            messages.success(request,'submitted...!')
        return render(request,'signup.html')
    else:
        return render(request,'signup.html')

def courselist1(request):
    return render(request,"courselist1.html")

def courselist2(request):
    return render(request,"courselist2.html")

def courselist3(request):
    return render(request,"courselist3.html")

def courselist4(request):
    return render(request,"courselist4.html")

def institutes(request):
    return render(request,"institutes.html")

def contactus(request):
    return render(request,"contactus.html")

def Aboutus(request):
    return render(request,"Aboutus.html")

def getinstitute(request):
    q = request.GET['institutes']
    return HttpResponse(q)

def studentscount(request):
    a=enrolled.objects.all().order_by("user")
    b=list(a.user)

    

def myenroll_list(request):
    user=signupdetails.objects.get(email=request.session['email'])
    c=enrolled.objects.filter(user=user).all()
    stu={
        "student":c
    }
    print(c)
    return render(request,'student_enroll1.html',stu)


def booking_1_1(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="SARJAPURA",course="PYTHON")   
    booking.save()
    return render(request,'register.html')

def booking_1_2(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="SARJAPURA",course="CCNA")   
    booking.save()
    return render(request,'register.html')

def booking_1_3(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="SARJAPURA",course="MACHINE LANGUAGE")   
    booking.save()
    return render(request,'register.html')

def booking_1_4(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="SARJAPURA",course="DATA SCIENCE")   
    booking.save()
    return render(request,'register.html')

def booking_1_5(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="SARJAPURA",course="ARTIFICIAL INTELLIGENCE")   
    booking.save()
    return render(request,'register.html')

def booking_1_6(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="SARJAPURA",course="JAVA")   
    booking.save()
    return render(request,'register.html')

def booking_1_7(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="SARJAPURA",course="C PROGRAMMING")   
    booking.save()
    return render(request,'register.html')

def booking_1_8(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="SARJAPURA",course="WEB DEVELOPMENT")   
    booking.save()
    return render(request,'register.html')


def booking_2_1(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="YESWANTHPUR",course="PYTHON")   
    booking.save()
    return render(request,'register.html')

def booking_2_2(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="YESWANTHPUR",course="CCNA")   
    booking.save()
    return render(request,'register.html')

def booking_2_3(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="YESWANTHPUR",course="MACHINE LANGUAGE")   
    booking.save()
    return render(request,'register.html')

def booking_2_4(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="YESWANTHPUR",course="DATA SCIENCE")   
    booking.save()
    return render(request,'register.html')

def booking_2_5(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="YESWANTHPUR",course="ARTIFICIAL INTELLIGENCE")   
    booking.save()
    return render(request,'register.html')

def booking_2_6(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="YESWANTHPUR",course="JAVA")   
    booking.save()
    return render(request,'register.html')

def booking_2_7(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="YESWANTHPUR",course="C PROGRAMMING")   
    booking.save()
    return render(request,'register.html')

def booking_2_8(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="YESWANTHPUR",course="WEB DEVELOPMENT")   
    booking.save()
    return render(request,'register.html')



def booking_3_1(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="KORAMANGALA",course="PYTHON")   
    booking.save()
    return render(request,'register.html')

def booking_3_2(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="KORAMANGALA",course="CCNA")   
    booking.save()
    return render(request,'register.html')

def booking_3_3(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="KORAMANGALA",course="MACHINE LANGUAGE")   
    booking.save()
    return render(request,'register.html')

def booking_3_4(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="KORAMANGALA",course="DATA SCIENCE")   
    booking.save()
    return render(request,'register.html')

def booking_3_5(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="KORAMANGALA",course="ARTIFICIAL INTELLIGENCE")   
    booking.save()
    return render(request,'register.html')

def booking_3_6(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="KORAMANGALA",course="JAVA")   
    booking.save()
    return render(request,'register.html')

def booking_3_7(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="KORAMANGALA",course="C PROGRAMMING")   
    booking.save()
    return render(request,'register.html')

def booking_3_8(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="KORAMANGALA",course="WEB DEVELOPMENT")   
    booking.save()
    return render(request,'register.html')



def booking_4_1(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="MARTHAHALLI",course="PYTHON")   
    booking.save()
    return render(request,'register.html')

def booking_4_2(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="MARTHAHALLI",course="CCNA")   
    booking.save()
    return render(request,'register.html')

def booking_4_3(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="MARTHAHALLI",course="MACHINE LANGUAGE")   
    booking.save()
    return render(request,'register.html')

def booking_4_4(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="MARTHAHALLI",course="DATA SCIENCE")   
    booking.save()
    return render(request,'register.html')

def booking_4_5(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="MARTHAHALLI",course="ARTIFICIAL INTELLIGENCE")   
    booking.save()
    return render(request,'register.html')

def booking_4_6(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="MARTHAHALLI",course="JAVA")   
    booking.save()
    return render(request,'register.html')

def booking_4_7(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="MARTHAHALLI",course="C PROGRAMMING")   
    booking.save()
    return render(request,'register.html')

def booking_4_8(request):
    user=signupdetails.objects.get(email=request.session['email'])
    booking=enrolled(user=user,institute="MARTHAHALLI",course="WEB DEVELOPMENT")   
    booking.save()
    return render(request,'register.html')



    








