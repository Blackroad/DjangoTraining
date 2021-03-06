from django.db import models


class Group(models.Model):
    """Student Model"""
    class Meta(object):
        verbose_name = u"Група"
        verbose_name_plural = u"Групи"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва")

    leader = models.OneToOneField(
        'Student',
        max_length=246,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=u"Староста")

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    def __str__(self):
        if self.leader:
            return u"%s %s %s" % (self.title, self.leader.first_name, self.leader.last_name)
        else:
            return u"%s" % (self.title,)
