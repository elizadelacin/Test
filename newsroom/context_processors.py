from .models import Follow_us, Categories, Popular, Tags, Quick_links, Header_info

def social_platforms(request):
    platforms = Follow_us.objects.all()
    return {'platforms': platforms}

def site_categories(request):
    all_categories = Categories.objects.all()
    return {'all_categories': all_categories}

def popular_news(request):
    populars = Popular.objects.filter(is_featured=True)
    popular_list = list(populars)
    left_column = popular_list[::2]
    right_column = popular_list[1::2]
    return {'populars': populars,
            "left_column": left_column,
            "right_column": right_column}
def tags(request):
    tags = Tags.objects.all()
    return {'tags': tags}

def quick_links(request):
    links = Quick_links.objects.all()
    return {'links': links}

def header_info(request):
    information = Header_info.objects.last()
    return {'information': information}
