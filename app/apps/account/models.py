from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True
	)
	# we should add relation with auth
	# Add About
	# work and education

	def __str__(self) -> str:
		return self.fullname

	@property
	def fullname(self) -> str:
		return self.user.get_full_name()
