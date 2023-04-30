from .models import Event
from .serializers import EventSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# class Overview(APIView):
# 	def get(self, request):
# 		overview = {
# 			'Categorias': ['Cultura', 'Esportes', 'Lazer', 'Outros'],
# 			'Promoções': [1, 2, 3, 4],
# 			'Destaques': ['img1', 'img2', 'img3']
# 		}

# 		return Response(overview)


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

	# def delete(self, request, pk):
	# 	event = Event.objects.get(pk=pk)
	# 	event.delete()
	# 	return Response('Evento excluído com sucesso!')


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