"""
Class for todos models
"""


from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

done_status = (('done', 'done'), ('in process', 'in process'))


class Todo(models.Model):
    """Todo models for db"""
    user = models.ForeignKey(User(username=settings.AUTH_USER_MODEL),
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=255, null=False)
    done = models.BooleanField(_("Done"), default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Serialized atibutes for api json"""
        verbose_name = _("Todo")
        verbose_name_plural = _("Todos")

    def __str__(self):
        """Todo str representation"""
        return self.title

    def __unicode__(self):
        """Todo str representation"""
        return smart_unicode(self.title)
