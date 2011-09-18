from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _

class ContactType(models.Model):
    name = models.CharField(_('Type'), max_length=100)
    title = models.CharField(_('Title'), max_length=100)
    icon = models.ImageField(_('Icon'), upload_to='icons',
        blank=True, null=True
    )
    
    def __unicode__(self):
        return self.title

class Contact(models.Model):
    contact_type = models.ForeignKey(ContactType, verbose_name=_('Contact Type'))
    value = models.CharField(_('Number'), max_length=100)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    
    def __unicode__(self):
        return u'%s: %s' % (unicode(self.contact_type), self.value)
