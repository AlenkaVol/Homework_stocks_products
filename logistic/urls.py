from rest_framework.routers import DefaultRouter
from logistic.views import ProductViewSet, StockViewSet, sample_view
from django.urls import path

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [
    path('test/', sample_view, name='sample'),
] + router.urls
