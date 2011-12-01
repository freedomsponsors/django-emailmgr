from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from utils import get_unique_random

class EmailAddress(models.Model):

    user = models.ForeignKey(User, related_name="%(class)s")
    email = models.EmailField(_("Email Address"))
    is_primary = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    identifier = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = _("email address")
        verbose_name_plural = _("email addresses")
        unique_together = (("user", "email"),)

    def __unicode__(self):
        return u"%s (%s)" % (self.email, self.user.username)

    def save(self, *args, **kwargs):
        if not self.identifier:
            self.identifier = get_unique_random(20).lower()
        super(EmailAddress, self).save(*args, **kwargs)
