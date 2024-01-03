from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from app_habits.models import Habit
from app_habits.paginators import HabitPaginator
from app_habits.serializers import HabitNiceCreateSerializer, HabitGoodCreateSerializer, HabitListAllSerializer, \
    HabitListSerializer, HabitSerializer, HabitGoodUpdateSerializer
from app_users.permissions import IsModerator, IsPublic, IsOwner


class HabitNiceCreateAPIView(CreateAPIView):
    """Habit Nice Create"""
    queryset = Habit.objects.all()
    serializer_class = HabitNiceCreateSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.is_nice = True
        new_habit.save()


class HabitGoodCreateAPIView(CreateAPIView):

    queryset = Habit.objects.all()
    serializer_class = HabitGoodCreateSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitListAPIView(ListAPIView):

    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = None
    filterset_fields = ('is_nice', )
    pagination_class = HabitPaginator

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Habit.objects.all()
        else:
            queryset = Habit.objects.filter(owner=self.request.user)

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        return queryset

    def get_serializer_class(self):
        if self.request.user.is_staff:
            serializer_class = HabitListAllSerializer
            self.ordering_fields = ('id', 'task', 'start_time', 'location', 'periodic', 'is_nice', 'owner_email', )
        else:
            serializer_class = HabitListSerializer
            self.ordering_fields = ('id', 'task', 'start_time', 'location', 'periodic', 'is_nice', )

        return serializer_class


class HabitRetrieveAPIView(RetrieveAPIView):

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsPublic | IsOwner | IsModerator]


class HabitPublicListAPIView(ListAPIView):

    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitListAllSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('id', 'task', 'start_time', 'location', 'periodic', 'is_nice', 'owner_email', )
    filterset_fields = ('is_nice', )
    pagination_class = HabitPaginator


class HabitUpdateAPIView(UpdateAPIView):

    queryset = Habit.objects.all()
    permission_classes = [IsOwner | IsModerator]

    def get_serializer_class(self):
        if self.get_object().is_nice:
            return HabitNiceCreateSerializer
        return HabitGoodUpdateSerializer


class HabitDestroyAPIView(DestroyAPIView):

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]
