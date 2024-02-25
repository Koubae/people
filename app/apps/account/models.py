from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from people.models import BaseModel


class Account(BaseModel):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	# we should add relation with auth
	# Add About
	# work and education

	# country
	# city
	# address
	# phone
	# birthday
	# job

	# TODO: Add validation to check if user has email , username and so on.

	def __str__(self) -> str:
		return self.fullname

	@property
	def fullname(self) -> str:
		return self.user.get_full_name()
