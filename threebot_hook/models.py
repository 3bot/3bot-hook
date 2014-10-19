from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django import dispatch


from organizations.models import Organization
from threebot.models import Workflow
from threebot.models import Worker
from threebot.models import ParameterList



@python_2_unicode_compatible
class Hook(models.Model):
    owner = models.ForeignKey(Organization, blank=True, null=True)
    slug = models.SlugField(max_length=255)
    user = models.CharField(max_length=255, blank=True, null=True)
    repo = models.CharField(max_length=255, blank=True, null=True)
    secret = models.CharField(max_length=255, blank=True, null=True)
    workflow = models.ForeignKey(Workflow)
    worker = models.ForeignKey(Worker)
    param_list = models.ForeignKey(ParameterList)
 
 
    unique_together = ("workflow", "worker", "param_list")

    def get_hook_url(self):
        return "%d-%d-%d-%s" % (self.workflow.id, self.worker.id, self.param_list.id, self.slug)
    
    def __str__(self):
        return "%s (%s)" % (self.get_hook_url(), self.owner)
        
    class Meta():
        verbose_name = _("Hook")
        verbose_name_plural = _("Hooks")
        db_table = 'threebot_hook'


class HookSignal(dispatch.Signal):
    pass

hook_signal = HookSignal()


"""
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

an_user = User.objects.get(username="phi")
token = Token.objects.create(user=an_user)
print token.key
"""