from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from home_app.models import Announcament
from profile_app.models import ProfileSettings
from desk_app.models import Desk, DeskWorkers


# TO-DO PAGE
# ----------------
# Desc: Shows the to do list of the pointed desks list.
@login_required
def to_do(request, deskname):
    current_user = get_object_or_404(User, pk=request.user.id)
    desk = get_object_or_404(Desk, name=deskname)

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
        'has_desk_navbar': True,
        'current_user': current_user,
        'desk': desk,
        'current_user_settings': current_user_settings,
        'current_user_desks': current_user_desks,
    }
    return render(request, 'desk_app/to_do.html', context=data)
