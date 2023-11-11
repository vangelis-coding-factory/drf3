from django.urls import path, include
from rest_framework.routers import DefaultRouter

#from profiles.api.views import ProfileList

from profiles.api.views import ProfileViewSet, ProfileStatusViewSet, AvatarUpdateView

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"status", ProfileStatusViewSet, basename="status")

#profile_list = ProfileViewSet.as_view({"get":"list"})
#profile_detail = ProfileViewSet.as_view({"get":"retrieve"})

urlpatterns = [
    #path('profiles/', ProfileList.as_view(), name="profiles-list")
    #path('profiles/', profile_list, name="profiles-list"),
    #path('profiles/<int:pk>/', profile_detail, name="profile-detail"),
    path("", include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update")
]