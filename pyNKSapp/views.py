from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from pyNKSapp.models import signupdetails,staff_details,student_enroll,number_of_students,enrolled,institutes,degree,specialization,cardpayment
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponseRedirect
# from random import random
# Create your views here.

def error_404_view(request,exception):
    return render(request,'404.html')

def payment(request):
    return render(request,'payments.html')

def addingdeg(request):   
    return render(request,'addingDegree.html')

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

def student(request):
    stu=False
    print(stu)
    return render(request,'signup.html',{'di':stu})
def institute(request):
    stu=True
    print(stu)
    return render(request,'signup.html',{'di':stu})


def logindata(request):
    # inst_degrees(request)
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
            # print("Username=",userdetails)
            request.session['email']=userdetails.email
            # print("id=",userdetails.ins_stu_id)
            if(userdetails.ins_stu_id==2):
                userdet = signupdetails.objects.get(email=request.session['email'])
                user_id=userdet.id
                instituten=institutes.objects.get(chairman_id_id=user_id)
                degs=degree.objects.filter(institute_id_id=instituten)
                print(degs)
                instt_degree={
                    "deggs":degs
                }
                return render(request,'addingDegree.html',instt_degree)
            else:
                stu_det = True
                return render(request,'home.html',{'stu_d':stu_det})
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

otp="873426"
def payment(request):
    if request.method=="POST":
        savepayment=cardpayment()
        savepayment.name=request.POST.get('cardname')
        savepayment.card_num=request.POST.get('cardnumber')
        savepayment.mnth=request.POST.get('expmonth')
        savepayment.year=request.POST.get('expyear')
        savepayment.cvv=request.POST.get('cvv')
        savepayment.gmail=request.POST.get('gmail')
        send_mail(
            'password',
            otp,
            'srinadhkotha8@gmail.com',
            [request.POST.get('gmail')],
            fail_silently=False,
        )
        optsent=True
        return render(request,'payments.html',{'otp':optsent})        

def verify(request):
    if request.method=="POST":
        try:
            if request.POST.get("otp")==otp:
                return render(request,'home.html')
        except signupdetails.DoesNotExist as e :
            messages.success(request,'OTP is incorrect')
            return render(request,'forgotpass.html')


def logout(request):
    try:
        del request.session['email']
    except:
        return render(request,'home.html')
    return render(request,'home.html')
  
def adddegree(request):
    if request.method=='POST':
        if request.POST.get('degreename') and request.POST.get('duration') and request.POST.get('startdate') and request.POST.get('enddate') and request.POST.get('fee') and request.POST.get('advancefee') and request.POST.get('reqpercentage') and request.POST.get('specialization') and request.POST.get('specializtiondesc') and request.POST.get('seats'):
            savedegree=degree()
            savedegree.degree_name=request.POST.get('degreename')
            savedegree.duration=request.POST.get('duration')
            savedegree.start_date=request.POST.get('startdate')
            savedegree.end_date=request.POST.get('enddate')
            savedegree.fee=request.POST.get('fee')
            savedegree.advance_fee=request.POST.get('advancefee')
            savedegree.req_percentage=request.POST.get('reqpercentage')
            userdet = signupdetails.objects.get(email=request.session['email'])
            user_id=userdet.id
            instituten=institutes.objects.get(chairman_id_id=user_id)
            savedegree.institute_id=instituten
            savedegree.save()
            deg_id = degree.objects.get(degree_name=request.POST.get('degreename'))
            savespecialization=specialization()
            savespecialization.specialization_name=request.POST.get('specialization')
            savespecialization.description=request.POST.get('specializtiondesc')
            savespecialization.seats_available=request.POST.get('seats')
            savespecialization.degree_id=deg_id
            savespecialization.institute_id=instituten
            savespecialization.save()
            userdet = signupdetails.objects.get(email=request.session['email'])
            user_id=userdet.id
            instituten=institutes.objects.get(chairman_id_id=user_id)
            degs=degree.objects.filter(institute_id_id=instituten)
            instt_degree={
                    "deggs":degs
            }
            messages.success(request,'submitted...!')
        return render(request,'addingDegree.html',instt_degree)
    else:
        return render(request,'addingDegree.html')

def addspecialization(request):
    if request.method=='POST':
        if request.POST.get('select')=='':
            messages.success(request,'select Degree...!')
            return render(request,'addingDegree.html')
        if request.POST.get('select') and request.POST.get('specialization') and request.POST.get('specializtiondesc') and request.POST.get('seats'):
            savespecialization=specialization()
            deg=degree.objects.get(degree_name=request.POST.get('select'))
            userdet = signupdetails.objects.get(email=request.session['email'])
            user_id=userdet.id
            instituten=institutes.objects.get(chairman_id_id=user_id)
            savespecialization.specialization_name=request.POST.get('specialization')
            savespecialization.description=request.POST.get('specializtiondesc')
            savespecialization.seats_available=request.POST.get('seats')
            savespecialization.degree_id=deg
            savespecialization.institute_id=instituten
            savespecialization.save()
            userdet = signupdetails.objects.get(email=request.session['email'])
            user_id=userdet.id
            instituten=institutes.objects.get(chairman_id_id=user_id)
            degs=degree.objects.filter(institute_id_id=instituten)
            instt_degree={
                    "deggs":degs
            }
            messages.success(request,'submitted...!')

        return render(request,'addingDegree.html',instt_degree)
    else:
        return render(request,'addingDegree.html')

            
def insertrecord(request):
    if request.method=='POST':
        # t=0
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('dob') and request.POST.get('gender'):
            t=1
            if request.POST.get('institutename'):
                t=2
            saverecord=signupdetails()
            saverecord.ins_stu_id=t
            saverecord.firstname=request.POST.get('firstname')
            saverecord.lastname=request.POST.get('lastname')
            saverecord.phone=request.POST.get('phone')
            saverecord.email=request.POST.get('email')
            saverecord.dob=request.POST.get('dob')
            saverecord.password=request.POST.get('password')
            saverecord.reenterpassword=request.POST.get('reenterpassword')
            saverecord.gender=request.POST.get('gender')
            if t==1:
                saverecord.prev_edu_percentage=request.POST.get('percentage')
            else:
                saverecord.prev_edu_percentage=0
            print(t)
            if saverecord.password!=saverecord.reenterpassword:
                return redirect('insertrecord')
            else:
                saverecord.save()
            #saverecord.save()
            if t==2:
                print("nkdjnfkjsdnkjfksdfksdkf dsjnv cjds jvh jsdh vjh jh")
                saverec=institutes()
                id_c = signupdetails.objects.get(email=request.POST.get('email'))
                saverec.chairman_id=id_c
                saverec.institute_name=request.POST.get('institutename')
                saverec.ins_photo=id_c.id%20
                saverec.save()
            messages.success(request,'submitted...!')

        return render(request,'signup.html')
    else:
        return render(request,'signup.html')


def my_degress(request):
    userdet = signupdetails.objects.get(email=request.session['email'])
    user_id=userdet.id
    instituten=institutes.objects.get(chairman_id_id=user_id)
    degs=degree.objects.filter(institute_id_id=instituten)
    instt_degree={
            "deggs":degs
    }
    print(degs)
    return render(request,'inst_degree_list.html',instt_degree)

def ins_degrees(request,p):
    studentd=signupdetails.objects.get(email=request.session['email'])
    z = institutes.objects.filter(id=p)
    y = degree.objects.filter(institute_id=p)
    deg_ava=y.filter(req_percentage__lte = studentd.prev_edu_percentage)
    print(deg_ava)
    x=z[0].institute_name
    
    inst_degs={
        "degs":deg_ava,
        "ins_name":x
    }
    print(y)
    return render(request,'institute_degrees.html',inst_degs)

def inst_specializations(request,i,p=None):
    y = specialization.objects.filter(degree_id=i)
    inst_spec={
        "specs":y
    }
    print(y)
    return render(request,'deg_specs.html',inst_spec)

# def inst_stu_specializations(request,p,a):
#     y = specialization.objects.filter(degree_id=a)
#     inst_spec={
#         "specs":y
#     }
#     print(y)
#     return render(request,'deg_specs.html',inst_spec)

def show_institutes(request):
    degs=degree.objects.all()
    a=institutes.objects.all()

    print(a)
    ins_det={
        "ins":a,
        "deggs":degs
    }
    return render(request,'institutes.html',ins_det)

def payment_degree(request,p,i,k):
    print("id of degree==",k)
    y = degree.objects.filter(id=i)[0]
    feee=y.advance_fee
    print("Amount",feee)
    return render(request,'payments.html',{'adv_amt':feee})

# def payment(request):



    # todo=signupdetails.objects.get(email=request.session['email'])
# def courselist1(request):
#     return render(request,"courselist1.html")

# def courselist2(request):
#     return render(request,"courselist2.html")

# def courselist3(request):
#     return render(request,"courselist3.html")

# def courselist4(request):
#     return render(request,"courselist4.html")

def institutesone(request):
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


# def booking_1_1(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="SARJAPURA",course="PYTHON")   
#     booking.save()
#     return render(request,'register.html')

# def booking_1_2(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="SARJAPURA",course="CCNA")   
#     booking.save()
#     return render(request,'register.html')

# def booking_1_3(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="SARJAPURA",course="MACHINE LANGUAGE")   
#     booking.save()
#     return render(request,'register.html')

# def booking_1_4(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="SARJAPURA",course="DATA SCIENCE")   
#     booking.save()
#     return render(request,'register.html')

# def booking_1_5(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="SARJAPURA",course="ARTIFICIAL INTELLIGENCE")   
#     booking.save()
#     return render(request,'register.html')

# def booking_1_6(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="SARJAPURA",course="JAVA")   
#     booking.save()
#     return render(request,'register.html')

# def booking_1_7(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="SARJAPURA",course="C PROGRAMMING")   
#     booking.save()
#     return render(request,'register.html')

# def booking_1_8(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="SARJAPURA",course="WEB DEVELOPMENT")   
#     booking.save()
#     return render(request,'register.html')


# def booking_2_1(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="YESWANTHPUR",course="PYTHON")   
#     booking.save()
#     return render(request,'register.html')

# def booking_2_2(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="YESWANTHPUR",course="CCNA")   
#     booking.save()
#     return render(request,'register.html')

# def booking_2_3(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="YESWANTHPUR",course="MACHINE LANGUAGE")   
#     booking.save()
#     return render(request,'register.html')

# def booking_2_4(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="YESWANTHPUR",course="DATA SCIENCE")   
#     booking.save()
#     return render(request,'register.html')

# def booking_2_5(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="YESWANTHPUR",course="ARTIFICIAL INTELLIGENCE")   
#     booking.save()
#     return render(request,'register.html')

# def booking_2_6(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="YESWANTHPUR",course="JAVA")   
#     booking.save()
#     return render(request,'register.html')

# def booking_2_7(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="YESWANTHPUR",course="C PROGRAMMING")   
#     booking.save()
#     return render(request,'register.html')

# def booking_2_8(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="YESWANTHPUR",course="WEB DEVELOPMENT")   
#     booking.save()
#     return render(request,'register.html')



# def booking_3_1(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="KORAMANGALA",course="PYTHON")   
#     booking.save()
#     return render(request,'register.html')

# def booking_3_2(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="KORAMANGALA",course="CCNA")   
#     booking.save()
#     return render(request,'register.html')

# def booking_3_3(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="KORAMANGALA",course="MACHINE LANGUAGE")   
#     booking.save()
#     return render(request,'register.html')

# def booking_3_4(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="KORAMANGALA",course="DATA SCIENCE")   
#     booking.save()
#     return render(request,'register.html')

# def booking_3_5(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="KORAMANGALA",course="ARTIFICIAL INTELLIGENCE")   
#     booking.save()
#     return render(request,'register.html')

# def booking_3_6(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="KORAMANGALA",course="JAVA")   
#     booking.save()
#     return render(request,'register.html')

# def booking_3_7(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="KORAMANGALA",course="C PROGRAMMING")   
#     booking.save()
#     return render(request,'register.html')

# def booking_3_8(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="KORAMANGALA",course="WEB DEVELOPMENT")   
#     booking.save()
#     return render(request,'register.html')



# def booking_4_1(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="MARTHAHALLI",course="PYTHON")   
#     booking.save()
#     return render(request,'register.html')

# def booking_4_2(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="MARTHAHALLI",course="CCNA")   
#     booking.save()
#     return render(request,'register.html')

# def booking_4_3(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="MARTHAHALLI",course="MACHINE LANGUAGE")   
#     booking.save()
#     return render(request,'register.html')

# def booking_4_4(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="MARTHAHALLI",course="DATA SCIENCE")   
#     booking.save()
#     return render(request,'register.html')

# def booking_4_5(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="MARTHAHALLI",course="ARTIFICIAL INTELLIGENCE")   
#     booking.save()
#     return render(request,'register.html')

# def booking_4_6(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="MARTHAHALLI",course="JAVA")   
#     booking.save()
#     return render(request,'register.html')

# def booking_4_7(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="MARTHAHALLI",course="C PROGRAMMING")   
#     booking.save()
#     return render(request,'register.html')

# def booking_4_8(request):
#     user=signupdetails.objects.get(email=request.session['email'])
#     booking=enrolled(user=user,institute="MARTHAHALLI",course="WEB DEVELOPMENT")   
#     booking.save()
#     return render(request,'register.html')



    








