from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.test import force_authenticate, APIRequestFactory, APITestCase

from atomic_habits.permissions import UserOrStuff
from atomic_habits.serlizers import HabitSerializer
from atomic_habits.validatodrs import RelatedHabitValidator, TimeValidator, ExceptionForRelatedValidators, \
    PerformanceIntervalValidator, EliminatingLeasurableValidator
from atomic_habits.views import HabitViewSet
from users.models import User
from atomic_habits.models import Habit


class HabitModelTestCase(TestCase):
    # Тесты моделей
    def setUp(self):
        self.user = User.objects.create(email='test@example.com')
        self.habit = Habit.objects.create(
            user=self.user,
            place='Дом',
            time='12:00:00',
            action='Спорт',
            pleasurable_habit='Yes',
            linked_habit='Связанные привычки ',
            frequency='2023-08-04',
            reward='Вознаграждение',
            time_to_complete='00:30:00',
            sign_of_publicity='Public'
        )

    def test_habit_str(self):
        self.assertEqual(str(self.habit), 'я буду Спорт в 12:00:00 в Дом')


class ValidatorsTestCase(TestCase):
    # Тесты валидаторов
    def test_related_habit_validator(self):
        validator = RelatedHabitValidator(field=None)
        data = {'linked_habit': 'Linked Habit', 'reward': 'Reward'}
        with self.assertRaises(ValidationError):
            validator(data)

    def test_time_validator(self):
        validator = TimeValidator(field=None)
        data = {'time_to_complete': 150}
        with self.assertRaises(ValidationError):
            validator(data)


class EliminatingLeasurableValidatorTestCase(TestCase):

    def test_eliminating_leasurable_validator(self):
        validator = EliminatingLeasurableValidator(field=None)
        data = {'pleasurable_habit': 'Pleasurable', 'reward': 'Reward', 'linked_habit': 'Linked Habit'}
        with self.assertRaises(ValidationError):
            validator(data)

    def test_eliminating_leasurable_no_exception(self):
        validator = EliminatingLeasurableValidator(field=None)
        data = {'pleasurable_habit': 'Pleasurable', 'reward': 'Reward'}
        try:
            validator(data)
        except ValidationError:
            self.fail("EliminatingLeasurableValidator raised ValidationError unexpectedly")


class ExceptionForRelatedValidators:
    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        linked_habit = data.get('linked_habit')
        pleasurable_habit = data.get('pleasurable_habit')
        if linked_habit and pleasurable_habit and linked_habit not in pleasurable_habit:
            raise serializers.ValidationError(
                'Ошибка: в связанные привычки могут попадать только привычки с признаком приятной привычки')


class PerformanceIntervalValidatorTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@example.com')

    def test_performance_interval_no_exception(self):
        validator = PerformanceIntervalValidator(field=None)

        data = {'user': self.user, 'frequency': self.user.date_joined + timedelta(days=8)}
        try:
            validator.__call__(data)  # Используем __call__ метод явно
        except serializers.ValidationError:
            self.fail("PerformanceIntervalValidator raised ValidationError unexpectedly")


class SerializerTestCase(TestCase):
    # Тесты сериализаторов
    def setUp(self):
        self.user = User.objects.create(email='test@example.com')
        self.habit = Habit.objects.create(
            user=self.user,
            place='Дом',
            time='12:00:00',
            action='Спорт',
            pleasurable_habit='Yes',
            linked_habit='Связанные привычки ',
            frequency='2023-08-04',
            reward='Вознаграждение',
            time_to_complete='00:30:00',
            sign_of_publicity='Public'
        )

    def test_habit_serializer(self):
        serializer = HabitSerializer(instance=self.habit)
        data = serializer.data
        self.assertEqual(data['place'], 'Дом')
        self.assertEqual(data['action'], 'Спорт')


class ViewPermissionTestCase(TestCase):
    # Тесты представлений (Views) и разрешений (Permissions)
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(email='test@example.com')
        self.habit = Habit.objects.create(
            user=self.user,
            place='Дом',
            time='12:00:00',
            action='Спорт',
            pleasurable_habit='Yes',
            linked_habit='Связанные привычки ',
            frequency='2023-08-04',
            reward='Вознаграждение',
            time_to_complete='00:30:00',
            sign_of_publicity='Public'
        )

    def test_user_or_stuff_permission(self):
        view = HabitViewSet.as_view({'get': 'list'})
        request = self.factory.get('/habits/')
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, 200)
