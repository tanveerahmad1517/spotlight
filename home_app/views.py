from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Announcament
from profile_app.models import ProfileSettings
from desk_app.models import Desk


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
# Desc: Home page showing the announcaments of every user
@login_required
def dashboard(request):
    current_user = get_object_or_404(User, pk=request.user.id)

    # Settings Objects
    try:
        current_user_settings = ProfileSettings.objects.get(user=current_user)
    except ObjectDoesNotExist:
        current_user_settings = None

    # Announcament Mechanism
    if request.POST.get('announcament_submit_button'):
        content = request.POST.get('content')
        new_announcament = Announcament(
            user=current_user, profile_settings=current_user_settings,
            content=content,
        )
        new_announcament.save()
    # Announcament Objects
    try:
        all_announcaments = Announcament.objects.order_by('-publish_date')
    except ObjectDoesNotExist:
        all_announcaments = None

    data = {
        'current_user': current_user,
        'has_home_navbar': True,
        'current_user_settings': current_user_settings,
        'all_announcaments': all_announcaments,
    }
    return render(request, 'home_app/dashboard.html', context=data)


# DESK
# ---------------------
# Desc: This is a page where you can create new desks(departments) for your
#       newspaper or browse some to join them
@login_required
def desk_browse(request):
    current_user = get_object_or_404(User, pk=request.user.id)

    # Settings Objects
    try:
        current_user_settings = ProfileSettings.objects.get(user=current_user)
    except ObjectDoesNotExist:
        current_user_settings = None

    # Desk Create Mechanism
    if request.POST.get('desk_create_button'):
        desk_create_image = request.FILES.get('desk_create_image')
        desk_create_category = request.POST.get('desk_create_category')
        desk_creat_name = request.POST.get('desk_create_category')
        desk_create_desc = request.POST.get('desk_create_desc')
        new_desk = Desk(
            sub_editor=current_user, image=desk_create_image,
            category=desk_create_category, name=desk_creat_name,
            description=desk_create_desc,
        )
        new_desk.save()


    data = {
        'current_user': current_user,
        'has_home_navbar': True,
        'current_user_settings': current_user_settings,
    }
    return render(request, 'home_app/desk.html', context=data)
