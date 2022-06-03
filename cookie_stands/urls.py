from django.urls import path
from .views import CookieStandList, CookieDetail

urlpatterns = [
    path("", CookieStandList.as_view(), name="cookie_list"),
    path("<int:pk>/", CookieDetail.as_view(), name="cookie_detail"),
]
