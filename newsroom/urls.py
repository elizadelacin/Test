from django.urls import path
from .views import home, categories, single_news, contact, quick_links_view, register, login_view, logout_view, search_article

app_name = 'newsroom'
urlpatterns = [
    path('', home, name="home"),
    path('categories/', categories, name="categories" ),
    path('single_news/', single_news, name="single_news"),
    path('contact/', contact, name='contact'),
    path('quick_links/', quick_links_view, name='quick_links'),
    path('login/', login_view, name= 'login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('search/', search_article, name='search')

]