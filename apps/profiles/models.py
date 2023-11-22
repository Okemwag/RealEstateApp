from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


from apps.common.models import TimeStampedUUIDModel

User = get_user_model()

class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")
    
class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+254780523654")
    about_me = models.TextField(verbose_name=_("About Me"), default="I am a real estate agent")
    license = models.CharField(verbose_name=_("License"), max_length=20, blank=True, null=True)
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"), default="/default.png", upload_to="profile_photos")
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices,
                              default=Gender.OTHER, max_length=10)
    country = CountryField(verbose_name=_("Country"), default="KE",null=False, blank=False)
    city = models.CharField(verbose_name=_("City"), max_length=80, default="Nairobi",
                            blank=False, null=False)
    is_buyer = models.BooleanField(verbose_name=_("Is Buyer"), default=False,
                                   help_text=_("Hey are you looking to buy a property?"))
    is_seller = models.BooleanField(verbose_name=_("Is Seller"), default=False,
                                    help_text=_("Hey are you a seller?"))
    is_agent = models.BooleanField(verbose_name=_("Is Agent"), default=False,
                                      help_text=_("Hey are you a real estate agent?"))
    top_agent = models.BooleanField(verbose_name=_("Top Agent"), default=False,
                                    help_text=_("Hey are you a top agent?"))
    rating = models.DecimalField(verbose_name=_("Rating"), default=0.0, max_digits=4, decimal_places=2,null=True, blank=True)
    
    num_reviews = models.PositiveIntegerField(verbose_name=_("Number of Reviews"), default=0, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    