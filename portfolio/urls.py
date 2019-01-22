from django.conf.urls import re_path
from portfolio.views import *


urlpatterns = [
    re_path('portfolio/', PortfolioView.as_view(),  name='portfolio'),
    re_path('gallery-view/', GalleryView.as_view(), name='gallery'),
]