from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.models import User,auth
# Create your views here.
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
                    print("Same Username")
                    return redirect("accounts:register")
                elif User.objects.filter(email=email).exists():
                    print("Same Email")
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
        form = RegisterForm()
    return render(request,'accounts/register.html',{'form':form})