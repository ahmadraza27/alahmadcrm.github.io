from django.contrib import admin

# Register your models here.
from .models import *

# class stock_in_admin(admin.ModelAdmin):
#     list_display= ['company name',
#                    'Tile Code',
#                    'Tile Size',
#                    'Tile Picture',
#                    'Box Quantity',
#                    'Box Capacity',
#                    'By Person']

admin.site.register(Person)
admin.site.register(User)
# admin.site.register(Stock)
@admin.register(Stock)
class Stock_in_admin(admin.ModelAdmin):
    list_display = ["company_name",
                    "tile_code",
                    "tile_size",
                    "tile_picture",
                    "box_quantity",
                    "box_capacity"]


# admin.site.register(Stock_in) #,stock_in_admin

@admin.register(Stock_in)
class Stock_in_admin(admin.ModelAdmin):
    list_display = ["company_name",
                    "tile_code",
                    "tile_size",
                    "tile_picture",
                    "box_quantity_in",
                    "box_capacity",
                    "by_person",
                    "date_and_time"]


# admin.site.register(Stock_out)
@admin.register(Stock_out)
class Stock_out_admin(admin.ModelAdmin):
    list_display = ["company_name",
                    "tile_code",
                    "tile_size",
                    "tile_picture",
                    "box_quantity_out",
                    "box_capacity",
                    "by_person",
                    "date_and_time"]
