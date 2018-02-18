from django.db import models

class Event(models.Model):
    """
    Модель событий
    """
    Event_Name = models.CharField('Name', max_length=200, blank=True, null=False)
    Event_Description = models.CharField('Description', max_length=1000, blank=True, null=True)
    Event_StartEvent = models.DateTimeField('StartEvent', auto_now_add=True)
    Event_PublicationDate = models.DateTimeField('PublicationDate', auto_now_add=True)
    TagCollection = models.ManyToManyField('Tag', verbose_name='Tag', related_name='r_EventTag')



class Tag(models.Model):
    """
    Модель тегов
    """
    Tag_Name = models.CharField('TagName', max_length=30, blank=True, null=True)

    def __str__(self):
        return self.Tag_Name

class Comments (models.Model):
    """
    Модель лайков
    """
    EventLink = models.ForeignKey('Event', verbose_name='Event',
                                related_name='r_EventComment', on_delete=models.CASCADE)

