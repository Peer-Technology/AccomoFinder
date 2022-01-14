from django.conf.urls import url
# from .import views
from .serializers import *
from .views import *
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]
# Routers provide an easy way of automatically determining the URL conf.
app_name = 'api'
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'rental_listings', RentalListingViewSet)
router.register(r'bookings', BookingViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]