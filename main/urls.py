from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'item', views.ItemDetail, basename='item')
router.register(r'items', views.ItemList, basename='item')
router.register(r'category', views.CategoryList)
router.register(r'types', views.TypeList)
router.register(r'companies', views.CompanyList)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(router.urls)),
]
