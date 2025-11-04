from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    success = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New Contact Message from {name}"
        message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]

        try:
            send_mail(subject, message_body, from_email, recipient_list)
            success = True
        except:
            success = False

    return render(request, 'contact.html', {'success': success, 'name': request.POST.get('name', '')})
