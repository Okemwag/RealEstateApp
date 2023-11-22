from django.db import models
import uuid

class TimeStampedUUIDModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created_at`` and ``updated_at`` fields with UUID as primary key.
    """
    pkid = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        