from django.urls import path, include
from rest_framework.routers import DefaultRouter

from userapp import views

# router for two admin ViewSets
router = DefaultRouter()
router.register('poll', views.AdminPollViewSet)
router.register('question', views.AdminPollQuestionViewSet)

urlpatterns = [
    path('admin/', include(router.urls)),
    path('active/', views.ActivePollsView.as_view()),
    path('complete/', views.TakePollView.as_view()),
    path('completed/<pk>/', views.UsersCompletedPollsView.as_view()),
]
