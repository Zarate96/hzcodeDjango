from django.shortcuts import render, redirect
from .models import Mensajes, Demo
from .decorators import check_recaptcha
from django.contrib import messages

# Create your views here.

def home(request):
    demos = Demo.objects.order_by('-fecha')
    return render(request, 'pages/home.html', {'demos':demos,})

@check_recaptcha
def mensaje(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
    
    if request.recaptcha_is_valid:    
        mensaje = Mensajes(nombre=name, email=email, telefono=phone,
        asunto=subject, mensaje=message)
        mensaje.save()
        messages.success(request, 'Tu mensaje ha sido enviado, nos pondremos en contacto contigo en breve.')
        #return redirect('home')

    else:
        messages.error(request, 'Porfavor verifique la información')
        #return redirect('home')

    return redirect('home')
    #return render(request, 'pages/home.html', {})