from rest_framework.routers import DefaultRouter
from django.urls import path
from logistic.views import ProductViewSet, StockViewSet, hello_world

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [
    *router.urls,
    path('sayhello/', hello_world, name='sayhello')
]
