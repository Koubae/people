from django.db import models


class BaseModel(models.Model):
	"""Custom base model with common fields and functionalities"""

	class Meta:
		abstract = True

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
