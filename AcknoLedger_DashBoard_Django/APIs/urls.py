# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('google-api/', GoogleTrendAPI.as_view(), name='google-api'), #done
    # path('cmclatest-api/', CMCListingsLatestAPI.as_view(), name='CMC-Listing-Latest-api'),#done 
    # path('cmchistorical-api/', CMCListingshistoricalAPI.as_view(), name='CMC-Listings-historical-api'),#Not now
    # path('cmccryptomap-api/', CMCcryptomapAPI.as_view(), name='CMC-cryptocurrency-map-api'), #done
    # path('cmcinfo-api/', CMCInfo.as_view(), name='CMC-Info-api'), #done
    # path('category-api/', CategoryAPI.as_view(), name='CategoryAPI-api'),#Done
    # # path('particluarCategory/', particluarCategory.as_view(), name='CategoryAPI-api'),
    # path('topcategory/', TopCategoryAPI.as_view(), name='TopCategoryAPI-api'),#Done
  
]
