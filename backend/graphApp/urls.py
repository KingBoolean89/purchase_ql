from django.conf.urls import url, include
from django.contrib import admin
from graphene_django.views import GraphQLView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductModelViewset

router = DefaultRouter()

router.register('api', ProductModelViewset)

urlpatterns = [
    # ...
    path('graphql', GraphQLView.as_view(graphiql=True)),

] + router.urls
