from django.db import models

class AllNews(models.Model):
    image = models.ImageField(upload_to='all_news_images/', null=True, blank=True)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class MainNews(models.Model):
    image = models.ImageField(upload_to='main_news_images/',null=True, blank=True)
    category = models.CharField(max_length=50)
    published_at = models.DateField()
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Categories(models.Model):
    image = models.ImageField(upload_to="category_images/", null=True, blank=True)
    name = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Featured(models.Model):
    image = models.ImageField(upload_to='featured_images/',null=True, blank=True)
    category = models.CharField(max_length=50)
    published_at = models.DateField()
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Business(models.Model):
    image = models.ImageField(upload_to="business_images/", null=True, blank=True)
    category = models.CharField(max_length=50)
    published_at = models.DateField()
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Technology(models.Model):
    image = models.ImageField(upload_to="technology_images/", null=True, blank=True)
    category = models.CharField(max_length=50)
    published_at = models.DateField()
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Entertainment(models.Model):
    image = models.ImageField(upload_to="entertainment_images/", null=True, blank=True)
    category = models.CharField(max_length=50)
    published_at = models.DateField()
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Sports(models.Model):
    image = models.ImageField(upload_to="sports_images/", null=True, blank=True)
    category = models.CharField(max_length=50)
    published_at = models.DateField()
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Popular(models.Model):
    image = models.ImageField(upload_to="popular_images/", null=True, blank=True)
    category = models.CharField(max_length=50)
    published_at = models.DateField()
    content = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Latest(models.Model):
    image = models.ImageField(upload_to="latest_images/", null=True, blank=True)
    category = models.CharField(max_length=50)
    published_at = models.DateField()
    content = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Comment(models.Model):
    image = models.ImageField(upload_to='comment_images/', null=True, blank=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return self.name

class Single_news(models.Model):
    main_image = models.ImageField(upload_to='single_news_images/', null=True, blank=True)
    news_image = models.ImageField(upload_to='single_news_images/', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    published_at = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

class Comment_form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

class GetİnTouch(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.address

class Contact_form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

class Follow_us(models.Model):
    platform = models.CharField(max_length=20)
    followers = models.CharField(max_length=255)
    icons = models.CharField(max_length=20)
    bg_color = models.CharField(max_length=20)
    platform_link = models.CharField(max_length=255)

    def  __str__(self):
        return self.platform

class Tags(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Quick_links(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Header_info(models.Model):
    weather = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    date_time = models.DateField()
    link_weather = models.CharField(max_length=255)
    link_currency = models.CharField(max_length=255)


    def __str__(self):
        return self.weather
# Create your models here.
