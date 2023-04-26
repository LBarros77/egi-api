from django.shortcuts import render

# from rest_framework import APIView
# from rest_framework.response import Response

# from .models import Event
# from .serializers import EventSerializer


# class Overview(APIView):
# 	def get(self, request):
# 		overview = {
# 			'Categorias': ['Cultura', 'Esportes', 'Lazer', 'Outros'],
# 			'Promoções': [1, 2, 3, 4],
# 			'Destaques': ['img1', 'img2', 'img3']
# 		}

# 		return Response(overview)


# class Event(APIView):
# 	def get(self, request):
# 		try:
# 			events = Event.objects.all()
# 			serializer = EventSerializer(Event, many=True)
# 			return Response(serializer.data)
# 		except Exception as err:
# 			return Response(f'Has not content: {err}')

# 	def get(self, request, pk):
# 		event = Event.objects.get(id=pk)
# 		serializer = EventSerializer(event, many=False)
# 		return Response(serializer.data)

# 	def post(self, request):
# 		serializer = EventSerializer(data=request.data)

# 		if serializer.is_valid():
# 			serializer.save()

# 		return Response(serializer.data)

# 	def update(self, request, pk):
# 		event = Event.objects.get(id=pk)
# 		serializer = EventSerializer(instance=event, data=request.data)

# 		if serializer.is_valid():
# 			serializer.save()

# 		return Response(serializer.data)

# 	def delete(request, pk):
# 		event = Event.objects.get(id=pk)
# 		event.delete()
# 		return Response('Evento excluído com sucesso!')