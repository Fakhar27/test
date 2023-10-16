from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib import messages
from .forms import Createuserform,Loginform
from .models import Medicine,IssuedMedicine,UserProfile
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils.dateparse import parse_date
from django.core.exceptions import ValidationError
from django.db.models import F
from django.db.models import ExpressionWrapper, fields
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User  # Add this import statement at the top of your views.py file




 
def register(request):
    form = Createuserform
    if request.method == "POST":
        form = Createuserform(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data.get('email')  
            user.save()
            return redirect('login')
    context = {'form': form}
    return render(request, "register.html", context=context)


def login(request):
    form = Loginform
    if request.method == "POST":
        form = Loginform(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dash')
    context = {"form":form}
    return render(request,"login.html",context=context)

def send_password_reset_email(request, user):
    email_subject = "Password Reset Request"

    uidb64 = urlsafe_base64_encode(user.email.encode())
    token = default_token_generator.make_token(user)

    reset_link = request.build_absolute_uri(reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token}))

    email_message = f"Click the following link to reset your password: <a href='{reset_link}'>Reset Password</a>"

    user_email = user.email

    send_mail(
        email_subject,
        email_message,
        settings.EMAIL_HOST_USER,  # Use the email from your settings
        [user_email],  # Use the user's email address as the recipient
        fail_silently=False,
    )
    
def password_reset(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')  # Get the user's email from the form
            try:
                user = User.objects.get(email=email)  # Find the user by email
            except User.DoesNotExist:
                # Handle the case where the user doesn't exist
                pass
            else:
                # Generate uidb64 and token here
                uidb64 = urlsafe_base64_encode(user.email.encode())
                token = default_token_generator.make_token(user)
                send_password_reset_email(request, user)
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset_form.html', {'form': form})

@login_required(login_url='login')
def dash(request):
    return render(request,"dash.html")

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def addmedicine(request):
    if request.method == 'POST':
        medicinename = request.POST.get('medicinename')
        expirydate_str = request.POST.get('expirydate') 
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        
        expirydate = datetime.strptime(expirydate_str, '%d/%m/%Y').date()

        if not medicinename or not expirydate or not category or not quantity:
            messages.error(request, 'PLEASE FILL IN ALL THE DETAILS, THANK YOU')
            return redirect('medicine')
        
        medicine = Medicine(
            medicinename=medicinename,
            expirydate=expirydate,
            category=category,
            quantity=quantity
        )
        medicine.save()
        return redirect('record')
    
    return render(request, "medicine.html")

@login_required(login_url='login')
def record(request):
    medicines = Medicine.objects.all()
    context = {'medicines': medicines}
    return render(request, 'record.html', context=context)

def delete_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    if request.method == 'POST':
        medicine.delete()
        return redirect('record')
    return render(request, 'confirm_delete.html', {'medicine': medicine})

@login_required(login_url='login')
def issue(request):
    if request.method == 'POST':
        visitno = request.POST.get('visitno')
        medicine_id = request.POST.get('medicine')  
        quantity = request.POST.get('quantityissue')

        try:
            medicine = Medicine.objects.get(id=medicine_id)
        except Medicine.DoesNotExist:
            messages.error(request, 'SELECTED MEDICINE DOESNT EXIST')
            return redirect('issue')

        if quantity is None or not quantity.isdigit():
            messages.error(request, 'PLEASE PROVIDE VALID QUANTITY')
            return redirect('issue')

        quantity = int(quantity)

        if quantity <= 0:
            messages.error(request, 'QUANTITY MUST BE POSITIVE')
            return redirect('issue')

        if quantity > medicine.quantity:
            messages.error(request, 'INSUFFICENT STOCK FOR SELECTED MEDICINE')
            return redirect('issue')

        issued_medicine = IssuedMedicine(
            visit_number=visitno,
            medicine=medicine,
            quantity_issued=quantity
        )
        issued_medicine.save()

        medicine.quantity -= quantity
        medicine.save()

        return redirect('record')

    medicines = Medicine.objects.all()
    context = {'medicines': medicines}
    return render(request, 'issue.html', context)

@login_required
def issuedmedicine(request):
    issuedmedicine = IssuedMedicine.objects.all()
    context = {'issuedmedicine': issuedmedicine}
    return render(request, 'issuedmedicine.html', context=context)

def delete_issuedmedicine(request, medicine_id):
    issued_medicine = get_object_or_404(IssuedMedicine, id=medicine_id)
    if request.method == 'POST':
        issued_medicine.delete()
        return redirect('issuedmedicine')
    return render(request, 'confirm_delete.html', {'issued_medicine': issued_medicine})

def recordsmall(request, medicine_id):
    medicine = get_object_or_404(Medicine, pk=medicine_id)
    context = {'medicine': medicine}
    return render(request, 'recordsmall.html', context=context)

def issuedmedsmall(request, medicine_id):
    issued_medicine = get_object_or_404(IssuedMedicine, pk=medicine_id)
    context = {'issued_medicine': issued_medicine}
    return render(request, 'issuedmedsmall.html', context=context)


# from_email = settings.EMAIL_HOST_USER
# connection = mail.get_connection()
# connection.open()
# email_message=mail.EmailMessage(f'EMAIL FROM {fname}',f'USEREMAIL: {email}',['reaperfakharmursaleen@gmail.com'],connection=connection)
# connection.send_messages([email_message])
# connection.close() 
