from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import ProfileSettings
from desk_app.models import Desk, DeskWorkers, Article


# CONTRIBUTIONS
# ------------------
# Desc: This is the overall summary page of the each user containing contribu-
#       -tions and and publised articles and so on.
@login_required
def contributions(request):
    current_user = get_object_or_404(User, pk=request.user.id)

    # Article objects
    try:
        current_user_articles = Article.objects.filter(author=current_user)\
                                    .order_by('-publish_date')
    except ObjectDoesNotExist:
        current_user_articles = None

    # Settings Objects
    try:
        current_user_settings = ProfileSettings.objects.get(user=current_user)
    except ObjectDoesNotExist:
        current_user_settings = None

    # Desk objects
    try:
        current_user_desks = DeskWorkers.objects.filter(worker=current_user)
    except ObjectDoesNotExist:
        current_user_desks = None

    data = {
        'current_user': current_user,
        'has_profile_navbar': True,
        'current_user_settings': current_user_settings,
        'current_user_desks': current_user_desks,
        'current_user_articles': current_user_articles,
    }
    return render(request, 'profile_app/contributions.html', context=data)


# DESK MANAGEMENT
# ------------------
# Desc: This is where the user can manage its deks weather it want delete the
#       desk that it has joined earlier
@login_required
def desk_management(request):
    current_user = get_object_or_404(User, pk=request.user.id)

    # Settings Objects
    try:
        current_user_settings = ProfileSettings.objects.get(user=current_user)
    except ObjectDoesNotExist:
        current_user_settings = None

    # Desk objects
    try:
        current_user_desks = DeskWorkers.objects.filter(worker=current_user)
    except ObjectDoesNotExist:
        current_user_desks = None

    # Desk quit mechanism
    if request.POST.get("delete_desk_submit_btn"):
        hidden_id = request.POST.get("hidden_desk_id")
        desk = DeskWorkers.objects.get(pk=hidden_id)
        desk.delete()

    data = {
        'current_user': current_user,
        'has_profile_navbar': True,
        'current_user_settings': current_user_settings,
        'current_user_desks': current_user_desks,
    }
    return render(request, 'profile_app/desk_management.html', context=data)


# SETTINGS
# ------------------
# Desc: This is the section in your profile that contains the settings form th-
#       -at is used to change your profiles settings
@login_required
def settings(request):
    current_user = get_object_or_404(User, pk=request.user.id)

    # Settings Mechanism
    if request.POST.get('settings_submit_button'):
        profile_photo = request.FILES.get('profile_photo')
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        personal_link = request.POST.get('personal_link')
        try:
            update_settings = ProfileSettings.objects.get(user=current_user)
            update_settings.profile_photo = profile_photo
            update_settings.name = name
            update_settings.bio = bio
            update_settings.personal_link = personal_link
            update_settings.save()
        except ObjectDoesNotExist:
            new_settings = ProfileSettings(user=current_user, bio=bio, name=name,
                                           profile_photo=profile_photo,
                                           personal_link=personal_link,)
            new_settings.save()

    # Settings Objects
    try:
        current_user_settings = ProfileSettings.objects.get(user=current_user)
    except ObjectDoesNotExist:
        current_user_settings = None

    # Desk objects
    try:
        current_user_desks = DeskWorkers.objects.filter(worker=current_user)
    except ObjectDoesNotExist:
        current_user_desks = None

    data = {
        'current_user': current_user,
        'has_profile_navbar': True,
        'current_user_settings': current_user_settings,
        'current_user_desks': current_user_desks,
    }
    return render(request, 'profile_app/settings.html', context=data)
