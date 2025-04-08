from django.contrib import admin
from .models import AllNews, MainNews, Categories, Featured,Business,Technology,Entertainment,Sports,Popular,Latest, Single_news , Comment, Comment_form, GetİnTouch, Contact_form, Follow_us, Tags, Quick_links, Header_info
from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.register(AllNews)
admin.site.register(MainNews)
admin.site.register(Categories)
admin.site.register(Featured)
admin.site.register(Business)
admin.site.register(Technology)
admin.site.register(Entertainment)
admin.site.register(Sports)
admin.site.register(Popular)
admin.site.register(Latest)
admin.site.register(Single_news)
admin.site.register(Comment)
admin.site.register(Comment_form)
admin.site.register(GetİnTouch)
admin.site.register(Contact_form)
admin.site.register(Follow_us)
admin.site.register(Tags)
admin.site.register(Quick_links)
admin.site.register(Header_info)



# Register your models here.
