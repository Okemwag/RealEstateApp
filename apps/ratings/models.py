from django.db import models
from django.utils.translation import gettext_lazy as _
from real_estate.settings.base import AUTH_USER_MODEL
from apps.common.models import TimeStampedUUIDModel
from apps.profiles.models import Profile

# Create your models here.


class Rating(TimeStampedUUIDModel):
    
    class Range(models.TextChoices):
        RATING_1 = "1", _("Poor")
        RATING_2 = "2", _("Fair")
        RATING_3 = "3", _("Good")
        RATING_4 = "4", _("Very Good")
        RATING_5 = "5", _("Excellent")
        
    rater = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_("User Providing the ratings"),on_delete=models.SET_NULL, related_name="rater", null=True)
    agent = models.ForeignKey(Profile, verbose_name=_("Agent being rated"),on_delete=models.SET_NULL, related_name="agent", null=True)   
    rating = models.CharField(verbose_name=_("Rating"), max_length=1, choices=Range.choices, default=0) 
    comment = models.TextField(verbose_name=_("Comment"), blank=True, null=True)
    
    
    class Meta:
        unique_together = ["rater", "agent"]
        
        
    def __str__(self):
        return f"{self.agent} rated at {self.rating}"