from django.urls import path
from . import views

urlpatterns = [

]
urlpatterns = [
	path('',views.index, name='index')
]

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^books/$', views.BookListView.as_view(), name='books'),
]
