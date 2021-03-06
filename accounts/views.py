from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User,auth

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already exists')
                    return redirect("accounts:register")
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already exists')
                    return redirect("accounts:register")
                else:
                    user = User.objects.create_user(first_name=firstname,
                                            last_name=lastname,
                                            username=username,
                                            password=password1,
                                            email=email)
                    user.save()
                    print("User Created")
                    return redirect('/')
            else:
                messages.info(request,'Password not matching')
                return redirect("accounts:register")

    else:
        form = RegisterForm()
    return render(request,'accounts/register.html',{'form':form})