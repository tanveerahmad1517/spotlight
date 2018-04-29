from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# LOGIN GATE
# ---------------------
# Desc: This is a gate that seperates staff members from curious eyes
def login_gate(request):
    invalid_user_credits = False
    if request.POST.get('login_submit_button'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home/dashboard/')
        else:
            invalid_user_credits = True
    data = {
        'invalid_user_credits': invalid_user_credits,
    }
    return render(request, 'home_app/login_gate.html', context=data)


# DASHBOARD
# --------------------
# Desc:


# DESK
# ---------------------
