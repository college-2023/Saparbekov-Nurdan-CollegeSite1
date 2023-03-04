from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, filters
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .serializers import *
from .models import *
from .service import ItemFilter


class ItemDetail(mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    lookup_field = 'slug'
    lookup_url_kwarg = 'article_slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get(self.lookup_field)
        if slug:
            queryset = queryset.filter(slug=slug)
        return queryset


class ItemList(mixins.ListModelMixin,
               GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ShortItemSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ItemFilter

    search_fields = ['title']
    lookup_field = 'slug'


class CategoryList(mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TypeList(mixins.ListModelMixin,
               GenericViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class CompanyList(mixins.ListModelMixin,
               GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
