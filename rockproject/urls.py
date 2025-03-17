from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rockapi.views import register_user, login_user, TypeView, RockView

router = routers.DefaultRouter(trailing_slash=False)
# Pattern for below: URL, View to Use, base name (nickname for the resource used in errors)
router.register(r"types", TypeView, "type")
router.register(r"rocks", RockView, "rock")

urlpatterns = [
    path("", include(router.urls)),
    path("register", register_user),
    path("login", login_user),
    path("admin/", admin.site.urls),
]
