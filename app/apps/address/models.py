from django.db import models
from django.db.models import functions
from django.utils.translation import gettext_lazy as _

from apps.base.models import BaseModel, LowerCaseCharField


class Continent(BaseModel):
	name = LowerCaseCharField(_("name"), max_length=50, primary_key=True)
	code = models.PositiveSmallIntegerField(_("code"), unique=True)

	def __str__(self):
		return self.name.capitalize()


class SubRegion(BaseModel):
	name = LowerCaseCharField(_("name"), max_length=50)
	code = models.PositiveSmallIntegerField(_("code"))
	continent = models.ForeignKey(Continent, on_delete=models.CASCADE, blank=False)

	intermediate_region = LowerCaseCharField(_("intermediate region"), max_length=50)
	intermediate_region_code = models.PositiveSmallIntegerField(_("intermediate region code"))

	class Meta:
		constraints = [
			models.UniqueConstraint(
				functions.Lower('name'),
				functions.Lower('intermediate_region'),
				name='sub_region_name_intermediate_region_name__unique',
			),
			models.UniqueConstraint(
				"code",
				"intermediate_region_code",
				name='sub_region_code_intermediate_region_code__unique',
			),
		]

	def __str__(self):
		return self.name.capitalize()


class Country(BaseModel):
	name = LowerCaseCharField(_("name"), max_length=100, primary_key=True)
	iso_alpha2 = LowerCaseCharField(_("iso_alpha2"), max_length=2, unique=True)
	iso_alpha3 = LowerCaseCharField(_("iso_alpha3"), max_length=3, unique=True)
	iso_3116_2 = LowerCaseCharField(_("iso_3116_2"), max_length=6, unique=True)
	code = models.PositiveSmallIntegerField(_("code"), unique=True)
	continent = models.ForeignKey(SubRegion, on_delete=models.CASCADE, blank=False)

	def __str__(self):
		return self.name.capitalize()


class City(BaseModel):
	name = LowerCaseCharField(_("name"), max_length=255)
	country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=False)

	def __str__(self):
		return self.name.capitalize()

	class Meta:
		constraints = [
			models.UniqueConstraint(
				functions.Lower('name'),
				"country",
				name='city_country__unique',
			),
		]


class Address(BaseModel):
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	street = models.CharField(max_length=255)
	zip = models.CharField(max_length=100)
