""" URLs for this module """
from django.conf.urls.static import static
from django.urls import path, include

from kasten import views

kasten_urlpatterns = [
    path('overview', views.Overview.as_view()),
    path('directory', views.AddDirectory.as_view()),
]

urlpatterns = [
    path('kasten/', include(kasten_urlpatterns)),
]
