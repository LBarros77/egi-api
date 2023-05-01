from .models import Event, Category
from .serializers import EventSerializer, CategorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class Overview(generics.ListAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
	filterset_fields = ['name', 'category']
	ordering_fields = ['name']
	search_fields = ['name']


class EventList(APIView):
	def get(self, request, format=None):
		events = Event.objects.all()
		serializer = EventSerializer(events, many=True)
		return Response(serializer.data)

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