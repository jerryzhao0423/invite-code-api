from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from UserRefer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('invitation/', views.InvitationView.as_view()),
    path('user/', views.UserListView.as_view()),
    path('match/', views.InvitationMatchView.as_view())
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]
