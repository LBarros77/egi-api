from .models import Event, Category
from .serializers import EventSerializer, CategorySerializer, UserSerializer
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	GenericAPIView,
	RetrieveModelMixin,
	UpdateModelMixin, DestroyModelMixin
)
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User


class Overview(ListAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
	filterset_fields = ['name', 'category']
	ordering_fields = ['name']
	search_fields = ['name']


class CategoryList(ListAPIView);
    queryset = Category.objects.all()
    serializer_class = [CategorySerializer]
    filter_backends = [OrderingFilter]
    ordering_fields = ['name']
    

class EventList(APIView):
	def get(self, request, format=None):
		events = Event.objects.all()
		serializer = EventSerializer(events, many=True)
		return Response(serializer.data)


class EventDetail(APIView):
	def get_by(self, pk):
		try:
			return Event.objects.get(pk=pk)
		except:
			raise Http404

	def get(self, request, pk, format=None):
		event = self.get_by(pk)
		serializer = EventSerializer(event)
		return Response(serializer.data)


class EventManage(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	permission_classes = [permissions.IsAdminUser]

	def get_by(self, pk):
		try:
			return Event.objects.get(pk=pk)
		except:
			raise Http404

	def post(self, request, format=None):
		serializer = EventSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def update(self, request, pk):
		event = Event.objects.get(pk=pk)
		serializer = EventSerializer(instance=event, data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)

	def delete(self, request, pk):
		event = Event.objects.get(pk=pk)
		event.delete()
		return Response('Evento excluído com sucesso!')

	def put(self, request, pk, format=None):
		event = self.get_by(pk)
		serializer = EventSerializer(event, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		event = self.get_by(pk)
		event.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def perform_create(self, serializer):
		serializer.save(manager=self.request.user)



class UserList(ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def get_serializer_class(self):
	    if self.request.user.is_staff:
	        return FullAccountSerializer
	    return BasicAccountSerializer

	def perform_create(self, serializer):
	    queryset = SignupRequest.objects.filter(user=self.request.user)
	    if queryset.exists():
	        raise ValidationError('You have already signed up')
	    serializer.save(user=self.request.user)

	def perform_update(self, serializer):
	    instance = serializer.save()
	    send_email_confirmation(user=self.request.user, modified=instance)