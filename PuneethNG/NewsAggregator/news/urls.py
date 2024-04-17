from django.urls import path
from news.views import scrape, news_list,statichome,about_page
urlpatterns = [
  path('scrape/<str:name>', scrape, name="scrape"),
  path('news/', news_list, name="home"),
  path('', statichome, name="breakinghome"),
  path('page/', about_page, name="about_page"),

]