from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Bu username ishlatilgan')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name, username=username,password=password1)
                user.save()
                return redirect('home')
            messages.info(request, 'muvaffaqqiyatli ro\'yxatdan o\'tdingiz !')
        
        else:
            print('parol xato')

    else:
        pass
    
    return render(request, 'register.html')