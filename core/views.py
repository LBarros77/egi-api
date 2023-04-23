from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer


@api_view(['GET'])
def events_overview(request):
	overview = {
		'Categorias': ['Cultura', 'Esportes', 'Lazer', 'Outros'],
		'Promoções': [1, 2, 3, 4],
		'Destaques': ['img1', 'img2', 'img3']
	}

	return Response(overview)

@api_view(['GET'])
def event_list(request):
	try:
		events = Event.objects.all()
		serializer = EventSerializer(Event, many=True)
		return Response(serializer.data)
	except Exception as err:
		return Response(f'Has not content: {err}')

@api_view(['GET'])
def event_detail(request, pk):
	event = Event.objects.get(id=pk)
	serializer = EventSerializer(event, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def event_create(request):
	serializer = EventSerializer(date=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def event_update(request, pk):
	event = Event.objects.get(id=pk)
	serializer = EventSerializer(instance=event, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def event_delete(request, pk):
	event = Event.objects.get(id=pk)
	event.delete()
	return Response('Evento excluído com sucesso!')