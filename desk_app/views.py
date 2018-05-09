from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from home_app.models import Announcament
from profile_app.models import ProfileSettings
from desk_app.models import Desk, DeskWorkers, DeskToDo


# TO-DO PAGE
# ----------------
# Desc: Shows the to do list of the pointed desks list.
@login_required
def to_do(request, deskname):
    current_user = get_object_or_404(User, pk=request.user.id)
    desk = get_object_or_404(Desk, name=deskname)

    # Creating a To Do task mechanism
    if request.POST.get("to_do_form_submit_button"):
        content = request.POST.get("to_do_task_input")
        new_task = DeskToDo(desk=desk, user=current_user, content=content)
        new_task.save()
    # To Do check mechanism
    if request.POST.get("check_button"):
        task_id = request.POST.get("hidden_id")
        current_task = DeskToDo.objects.get(pk=task_id)
        current_task.task_completed = True
        current_task.save()
    # To Do delete task mechanism
    if request.POST.get("delete_button"):
        task_id = request.POST.get("hidden_id")
        current_task = DeskToDo.objects.get(pk=task_id)
        current_task.delete()
    # To Do task objects
    try:
        desk_to_do_tasks = DeskToDo.objects.filter(desk=desk)\
            .order_by('-publish_date')
    except ObjectDoesNotExist:
        desk_to_do_tasks = None

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
        'desk_to_do_tasks': desk_to_do_tasks,
    }
    return render(request, 'desk_app/to_do.html', context=data)
