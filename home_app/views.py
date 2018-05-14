from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Announcament
from profile_app.models import ProfileSettings
from desk_app.models import Desk, DeskWorkers, Article


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

    # Desk Objects
    try:
        current_user_desks = DeskWorkers.objects.filter(worker=current_user)
    except ObjectDoesNotExist:
        current_user_desks = None

    data = {
        'current_user': current_user,
        'has_home_navbar': True,
        'current_user_settings': current_user_settings,
        'all_announcaments': all_announcaments,
        'current_user_desks': current_user_desks,
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
        desk_create_category_color = request.POST.get('desk_create_category')
        desk_creat_name = request.POST.get('desk_create_name')
        desk_create_desc = request.POST.get('desk_create_desc')
        new_desk = Desk(
            sub_editor=current_user, image=desk_create_image,
            category=desk_create_category, name=desk_creat_name,
            description=desk_create_desc,
            category_color=desk_create_category_color,
        )
        new_desk.save()

    # Joining a desk mechanism
    if request.POST.get('join_desk_button'):
        worker_that_joined = current_user
        hidden_name = request.POST.get('hidden_value')
        joined_desk = Desk.objects.get(pk=hidden_name)

        try:
            DeskWorkers.objects.get(
                worker=worker_that_joined, joined_desk=joined_desk
            )
            # if it exists Do nothing
        except ObjectDoesNotExist:
            new_worker = DeskWorkers(
                worker=worker_that_joined, joined_desk=joined_desk
            )
            new_worker.save()

    #  Desk objects
    try:
        all_desks = Desk.objects.order_by('-creation_date')
        current_user_desks = DeskWorkers.objects.filter(worker=current_user)
    except ObjectDoesNotExist:
        all_desks = None
        current_user_desks = None

    data = {
        'current_user': current_user,
        'has_home_navbar': True,
        'current_user_settings': current_user_settings,
        'all_desks': all_desks,
        'current_user_desks': current_user_desks,
    }
    return render(request, 'home_app/desk.html', context=data)


# SEARCH
# ----------
# Desc: A search page for the requested articles by the authors @username
@login_required
def search(request):
    current_user = get_object_or_404(User, pk=request.user.id)

    filtered_user_articles = None
    # Search Mechanism
    if request.GET.get("search_submit_btn"):
        username = request.GET.get('search_name')
        user = get_object_or_404(User, username=username)
        try:
            filtered_user_articles = Article.objects.filter(author=user)\
                                        .order_by('-publish_date')
        except ObjectDoesNotExist:
            filtered_user_articles = None

    # Settings Objects
    try:
        current_user_settings = ProfileSettings.objects.get(user=current_user)
    except ObjectDoesNotExist:
        current_user_settings = None

    #  Desk objects
    try:
        all_desks = Desk.objects.order_by('-creation_date')
        current_user_desks = DeskWorkers.objects.filter(worker=current_user)
    except ObjectDoesNotExist:
        all_desks = None
        current_user_desks = None

    data = {
        'current_user': current_user,
        'has_home_navbar': True,
        'current_user_settings': current_user_settings,
        'all_desks': all_desks,
        'current_user_desks': current_user_desks,
        'filtered_user_articles': filtered_user_articles,
    }
    return render(request, 'home_app/search.html', context=data)


# PUBLISH
# -----------
# Desc: Page that has all of the finished articles that are ready to publish
@login_required
def publish(request):
    current_user = get_object_or_404(User, pk=request.user.id)

    # All articles
    try:
        all_articles = Article.objects.filter(pushed_to_publish=True)\
                        .order_by('-publish_date')
    except ObjectDoesNotExist:
        all_articles = None

    # Settings Objects
    try:
        current_user_settings = ProfileSettings.objects.get(user=current_user)
    except ObjectDoesNotExist:
        current_user_settings = None

    #  Desk objects
    try:
        all_desks = Desk.objects.order_by('-creation_date')
        current_user_desks = DeskWorkers.objects.filter(worker=current_user)
    except ObjectDoesNotExist:
        all_desks = None
        current_user_desks = None

    data = {
        'current_user': current_user,
        'has_home_navbar': True,
        'current_user_settings': current_user_settings,
        'all_desks': all_desks,
        'current_user_desks': current_user_desks,
        'all_articles': all_articles,
    }
    return render(request, 'home_app/publish.html', context=data)
