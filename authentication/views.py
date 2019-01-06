from django.shortcuts import render, redirect
from .import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# login users


def loginUser(request):

    parseData = {}
    loginErrors = []

    # when user enter username & password
    if request.method == 'POST':

        loginForm = forms.LoginForm(request.POST)

        # is form is valid
        if loginForm.is_valid():

            email, password = loginForm.cleaned_data.values()
            user = authenticate(username=email, password=password)

            # is auth user
            if user is not None:

                # check user status
                if user.is_active:

                    login(request, user)

                    # flash msg
                    loginMsg = "Hello {}".format(user.email)
                    messages.success(request, loginMsg)

                    return redirect('dashboard:home')
                else:
                    loginErrors.append(
                        'you have been banned from the system.. please contact an admin')

            else:
                loginErrors.append(
                    'Please enter the correct email and password')

    # when pages load
    elif request.method == 'GET':
        loginForm = forms.LoginForm()

    parseData['loginForm'] = loginForm
    parseData['loginErrors'] = loginErrors

    return render(request, 'authentication/login.html', parseData)


# logout user
def logoutUser(request):

    logout(request)
    return redirect('auth:login')
