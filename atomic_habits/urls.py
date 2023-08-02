from rest_framework.routers import DefaultRouter

from atomic_habits.apps import AtomicHabitsConfig
from atomic_habits.views import HabitViewSet

app_name = AtomicHabitsConfig.name

router = DefaultRouter()
router.register(r'habit', HabitViewSet, basename='habits')
urlpatterns = [

              ] + router.urls
