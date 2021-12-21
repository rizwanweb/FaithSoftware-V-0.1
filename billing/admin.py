from django.contrib import admin

from .models import Header, Bill, Particular, PIDBill, PIDParticular
# Register your models here.

admin.site.register(Header)
#admin.site.register(Bill)
#admin.site.register(PIDBill)
admin.site.register(Particular)
admin.site.register(PIDParticular)

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('billNo', 'client', 'gdNo', 'cashNo', 'salesTaxInvoice', 'salesTax', 'netBalance')


@admin.register(PIDBill)
class PIDBillAdmin(admin.ModelAdmin):
    list_display = ('pidbillNo', 'client', 'gdNo', 'cashNo', 'netBalance')