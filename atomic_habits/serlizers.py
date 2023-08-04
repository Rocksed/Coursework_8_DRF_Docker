from rest_framework import serializers
from .models import Habit

from .validatodrs import RelatedHabitValidator, TimeValidator, ExceptionForRelatedValidators, \
    EliminatingLeasurableValidator, PerformanceIntervalValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [RelatedHabitValidator, TimeValidator, ExceptionForRelatedValidators,
                      EliminatingLeasurableValidator, PerformanceIntervalValidator]
