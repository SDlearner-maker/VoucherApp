from django.db import models
import secrets
from django.db.models.signals import post_save


class UniqueCodes(models.Model):
    """
    Class to create human friendly gift/coupon codes.
    """

    # Model field for our unique code
    code = models.CharField(max_length=16, blank=True, null=True, unique=True)

    @classmethod
    def post_create(cls, sender, instance, created, *args, **kwargs):
        """
        Connected to the post_save signal of the UniqueCodes model. This is used to set the
        code once we have created the db instance and have access to the primary key (ID Field)
        """
        # If new database record
        if created:
            # We have the primary key (ID Field) now so let's grab it
            id_string = str(instance.id)
            # Define our random string alphabet (notice I've omitted I,O,etc. as they can be confused for other characters)
            upper_alpha = "ABCDEFGHJKLMNPQRSTVWXYZ"
            # Create an 8 char random string from our alphabet
            random_str = "".join(secrets.choice(upper_alpha) for i in range(16))
            # Append the ID to the end of the random string
            instance.code = (random_str + id_string)[-16:]
            # Save the class instance
            instance.save()

    def __str__(self):
        return "%s" % (self.code,)


# Connect the post_create function to the UniqueCodes post_save signal
#post_save.connect(Gift.post_create, sender=UniqueCodes)
