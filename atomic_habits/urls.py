from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from atomic_habits.apps import AtomicHabitsConfig
from atomic_habits.views import HabitViewSet

app_name = AtomicHabitsConfig.name

router = DefaultRouter()
router.register(r'habit', HabitViewSet, basename='habits')
urlpatterns = [
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

              ] + router.urls
