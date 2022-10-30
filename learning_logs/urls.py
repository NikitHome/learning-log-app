# url to learning_logs

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # topic page
    path('topics/', views.topics, name='topics'),
    # topic/id page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # page to add new theme
    path('new_topic/', views.new_topic, name='new_topic'),
    # page to add new post
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # page to edit posts
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]