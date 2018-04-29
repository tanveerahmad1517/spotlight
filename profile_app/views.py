from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import ProfileSettings


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

    data = {
        'current_user': current_user,
        'has_profile_navbar': True,
        'current_user_settings': current_user_settings,
    }
    return render(request, 'profile_app/settings.html', context=data)
