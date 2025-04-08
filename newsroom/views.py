from django.shortcuts import render
from flask import redirect
from django.contrib.auth import authenticate, logout, login
from .models import AllNews, MainNews, Categories, Featured, Business, Technology, Entertainment, Sports, Latest, Comment, GetİnTouch, Single_news
from .forms import CommentForm, ContactForm, UserCreation, LoginForm


def home(request):
    all_news = AllNews.objects.all()
    main_news = MainNews.objects.all()
    categories = Categories.objects.filter(is_featured=True)
    featureds = Featured.objects.all()
    businesses = Business.objects.all()
    technologies = Technology.objects.filter(is_featured=True)
    entertainments = Entertainment.objects.all()
    sports = Sports.objects.all()

    all_latest = list(Latest.objects.all())
    left_side = all_latest[::2]
    right_side = all_latest[1::2]

    context = {"all_news": all_news,
               "main_news": main_news,
               "categories": categories,
               "featureds": featureds,
               "businesses": businesses,
               "technologies": technologies,
               "entertainments": entertainments,
               "sports": sports,
               "left_side": left_side,
               "right_side": right_side}

    return render(request, "index.html", context)


def categories(request):
    featured_tech = list(Technology.objects.filter(is_featured=True))
    featured_left = featured_tech[::2]
    featured_right = featured_tech[1::2]
    remaining_tech = list(Technology.objects.filter(is_featured=False))
    remaining_left = remaining_tech[::2]
    remaining_right = remaining_tech[1::2]
    context = {
        "featured_left": featured_left,
        "featured_right": featured_right,
        "remaining_left": remaining_left,
        "remaining_right": remaining_right}

    return render(request, 'categories.html', context)


def single_news(request):
    main_part = Single_news.objects.first()
    my_news = Single_news.objects.exclude(id=main_part.id)
    user_comments = Comment.objects.all()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            form = CommentForm()

    return render(request, 'single_news.html', {'user_comments': user_comments,
                                                'form': form,
                                                'my_news': my_news,
                                                'main_part':main_part})

def contact(request):
    contact = GetİnTouch.objects.first()
    contact_form = ContactForm()

    if request.method == 'POST':

        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            
            contact_form.save()
            contact_form = ContactForm()

    return render(request, 'contact.html', {'contact': contact,
                                            'contact_form': contact_form})

def quick_links_view(request):
    return  render(request, 'quick_links.html')

def register(request):
    if request.method == 'POST':

        register_form = UserCreation(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('newsroom:login')
        else:
            print(register_form.errors)

    else:
        register_form = UserCreation()
    return render(request, 'register.html', {'register_form': register_form})

def login_view(request):
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('newsroom:home')


    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return  redirect('newsroom:home')
# Create your views here.
