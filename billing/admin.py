from django.contrib import admin

from .models import Header, Bill, Particular, PIDBill, PIDParticular
# Register your models here.

admin.site.register(Header)
admin.site.register(Bill)
admin.site.register(PIDBill)
admin.site.register(Particular)
admin.site.register(PIDParticular)