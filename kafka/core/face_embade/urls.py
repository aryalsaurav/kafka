from django.urls import path

from . import views


app_name = "face_embed"

urlpatterns = [
    path('face_embed/',views.FaceEmbedListView.as_view(),name="face-embed-list")
]
