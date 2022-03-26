from django.urls import path
from .views import CookiesList, CookiesDetail

urlpatterns = [
    path("", CookiesList.as_view(), name="cookie_list"),
    path("<int:pk>/", CookiesDetail.as_view(), name="cookie_detail"),
]
