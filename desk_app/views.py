from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from home_app.models import Announcament
from profile_app.models import ProfileSettings
from desk_app.models import Desk, DeskWorkers, DeskToDo, Article


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


# NEW ARTICLE
# --------------------------
# Des: In this page each user can create a new article that they wish to write
@login_required
def new_article(request, deskname):
    current_user = get_object_or_404(User, pk=request.user.id)
    desk = get_object_or_404(Desk, name=deskname)

    # Creating a new article mechanism
    if request.POST.get("new_article_submit_button"):
        title = request.POST.get("title")
        content = request.POST.get("content")
        new_article = Article(
            author=current_user, title=title, content=content,
            category=desk.category, desk=desk
        )
        new_article.save()

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
    return render(request, 'desk_app/new_article.html', context=data)


# IN PROGRESS
# ------------------
# Desc: Shows all of the articles written in that desk and lets the other users
#       to edit, delete, push them to review
@login_required
def in_progress(request, deskname):
    current_user = get_object_or_404(User, pk=request.user.id)
    desk = get_object_or_404(Desk, name=deskname)

    # Article pushing to done button checking mechanism
    if request.POST.get("check_button"):
        hidden_id = request.POST.get("hidden_id")
        current_article = get_object_or_404(Article, pk=hidden_id)
        current_article.pushed_to_done = True
        current_article.save()
    # Article object
    try:
        all_articles = Article.objects.filter(pushed_to_done=False).order_by('-publish_date')
    except ObjectDoesNotExist:
        all_articles = None

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
        'all_articles': all_articles,
    }
    return render(request, 'desk_app/in_progress.html', context=data)


# ARTICLE EDIT PAGE
# ------------------------
# Desc: Shows the article edit page where you can make additions deletions
#       and comment
@login_required
def article_edit(request, deskname, article_id):
    current_user = get_object_or_404(User, pk=request.user.id)
    desk = get_object_or_404(Desk, name=deskname)
    article = get_object_or_404(Article, pk=article_id)

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
        'article': article,
    }
    return render(request, 'desk_app/article_edit.html', context=data)
