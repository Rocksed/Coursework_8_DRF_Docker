from rest_framework import viewsets

from atomic_habits.models import Habit
from atomic_habits.serlizers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
