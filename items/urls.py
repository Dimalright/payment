from django.urls import path

from .views import (CancelView, IndexView, ItemDetailView, PaymentView,
                    SuccessView)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("item/<int:pk>/", ItemDetailView.as_view(), name="itemdetail"),
    # path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path("buy/<int:pk>/", PaymentView.as_view(), name="buy"),
    path("cancel/", CancelView.as_view(), name="cancel"),
    path("success/", SuccessView.as_view(), name="success"),
]
