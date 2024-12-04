from django.urls import path
from rest_framework.routers import DefaultRouter

from feedbacks.apps import FeedbacksConfig
from feedbacks.views import (
    FeedbackListAPIView,
    FeedbackCreateAPIView,
    MyFeedbackListAPIView,
    FeedbackRetrieveAPIView,
    FeedbackUpdateAPIView,
    FeedbackDestroyAPIView,
)

app_name = FeedbacksConfig.name

router = DefaultRouter()

urlpatterns = [
    path("list/", FeedbackListAPIView.as_view(), name="feedback_list"),
    path("create/", FeedbackCreateAPIView.as_view(), name="feedback_create"),
    path("my_list_feedbacks/", MyFeedbackListAPIView.as_view(), name="feedback_mylist"),
    path("<int:pk>/", FeedbackRetrieveAPIView.as_view(), name="feedback_retrieve"),
    path("<int:pk>/update/", FeedbackUpdateAPIView.as_view(), name="feedback_update"),
    path("<int:pk>/delete/", FeedbackDestroyAPIView.as_view(), name="feedback_delete"),
] + router.urls
