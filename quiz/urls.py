from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quizeslist import views


router = routers.DefaultRouter()
router.register(r'quize', views.QuizeNameViewSet),
router.register(r'answer', views.ClientViewSet),
router.register(r'all-answer', views.ClientAllAnswersViewSet),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += router.urls