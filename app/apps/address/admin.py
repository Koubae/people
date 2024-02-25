from django.contrib import admin


from .models import Continent, SubRegion, Country, City, Address


admin.site.register(Continent)
admin.site.register(SubRegion)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Address)
