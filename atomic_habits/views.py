from rest_framework import viewsets

from atomic_habits.models import Habit
from atomic_habits.pagination import MyPagination
from atomic_habits.permissions import UserOrStuff
from atomic_habits.serlizers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [UserOrStuff]
    pagination_class = MyPagination
