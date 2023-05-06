from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event, Category


class CategorySerializer(serializers.ModelSerializer):	
	class Meta:
		model = Category
		fields = ['id', 'name', 'image']
		read_only_fields = ['id']


class EventSerializer(serializers.ModelSerializer):
	manager = serializers.ReadOnlyField(source='manager.username')
	category = CategorySerializer()
	
	class Meta:
		model = Event
		fields = '__all__'
		read_only_fields = ['id']

	def create_event(self, validated_data):
		return Event.objects.create(**validated_data)
	
	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.start = validated_data.get('start', instance.start)
		instance.finish = validated_data.get('finish', instance.finish)
		instance.category = validated_data.get('category', instance.category)
		instance.description = validated_data.get('description', instance.description)
		instance.ticket = validated_data.get('ticket', instance.ticket)
		instance.price = validated_data.get('price', instance.price)
		instance.star = validated_data.get('star', instance.star)
		instance.capacity = validated_data.get('capacity', instance.capacity)
		instance.image = validated_data.get('photo_url', instance.image)
		instance.video_url = validated_data.get('video_url', instance.video_url)
		instance.save()
		return instance


# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Comment.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('email', instance.email)
#         instance.content = validated_data.get('content', instance.content)
#         instance.created = validated_data.get('created', instance.created)
#         instance.save()
#         return instance


class UserSerializer(serializers.ModelSerializer):
    name = models.CharField(max_length=120)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(required=True, max_length=160)
    password = modles.CharField(required=True, max_length=16)
    password2 = serializers.CharField(required=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/users')
    skills = models.CharField(null=True, blank=True)
    star = models.IntegerField(max_length=5)
    created = models.DateTimeField(auto_now_add)
    # events = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2'] #events

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     user = User.objects.create(**validated_data)
    #     Profile.objects.create(user=user, **profile_data)
    #     return user

    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     # Unless the application properly enforces that this field is
    #     # always set, the following could raise a `DoesNotExist`, which
    #     # would need to be handled.
    #     profile = instance.profile

    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()

    #     profile.is_premium_member = profile_data.get(
    #         'is_premium_member',
    #         profile.is_premium_member
    #     )
    #     profile.has_support_contract = profile_data.get(
    #         'has_support_contract',
    #         profile.has_support_contract
    #      )
    #     profile.save()

    #     return instance


