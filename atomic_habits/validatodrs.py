from datetime import timedelta

from rest_framework import serializers

from atomic_habits.models import Habit


class RelatedHabitValidator:
    # Исключает одновременный выбор связанной привычки и указания вознаграждения.
    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        if data.get('linked_habit') and data.get('reward'):
            raise serializers.ValidationError(
                "Ошибка: нельзя выбирать связанную привычку, и вознаграждение одновременно.")


class TimeValidator:
    # Ограничивает выполнения должно быть не больше 120 секунд.
    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        if data.get('time_to_complete') > 120:
            raise serializers.ValidationError(
                "Ошибка: время выполнения должно быть не больше 120 секунд")


class ExceptionForRelatedValidators:
    # В связанные привычки могут попадать только привычки с признаком приятной привычки.
    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        if data.get('linked_habit') not in data.get('pleasurable_habit'):
            raise serializers.ValidationError(
                'Ошибка: в связанные привычки могут попадать только привычки с признаком приятной привычки')


class EliminatingLeasurableValidator:
    # Исключение для приятной привычки она не может быть вознаграждена или связанной привычки
    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        if data.get('pleasurable_habit') and data.get('reward') and data.get('linked_habit'):
            raise serializers.ValidationError(
                "Ошибка: у приятной привычки не может быть вознаграждения или связанной привычки.")


class PerformanceIntervalValidator:
    # Переодичность выполнения
    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        user = data['user']
        last_habit = Habit.objects.filter(user=user).order_by('-frequency').first()
        if last_habit:
            min_allowed_date = last_habit.frequency + timedelta(days=7)
            if data['frequency'] < min_allowed_date:
                raise serializers.ValidationError("Привычка не может выполняться реже, чем раз в 7 дней.")
