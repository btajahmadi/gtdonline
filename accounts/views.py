from django.shortcuts import redirect, render
from django.contrib import auth
# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            # SHOULD RETURN ERROR MESSAGE[S] TO LOGIN FORM
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.user is not None:
        auth.logout(request)
        return redirect('login')
    
