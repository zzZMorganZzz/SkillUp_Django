from django.urls import path
from . import views

app_name = 'TwitterProject'
urlpatterns=[
    path('collectionUser/UserInfo/<int:account_id>/', views.userInfo , name = 'UserInfo'),
    path('collectionUser/',views.get_accounts, name= 'collection_accounts'),
    path('',views.index, name = 'Home'),
    path('Posts/<int:account_id>/',views.get_posts),
    path('Tags/',views.get_tags,name='tags'),
    path('Tags/<int:tag_id>/',views.get_post_tag),
]