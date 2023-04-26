from django.contrib import admin

from .models import (
	Addrees,
	Category,
	Event
)


admin.site.register(Addrees)
admin.site.register(Category)
admin.site.register(Event)