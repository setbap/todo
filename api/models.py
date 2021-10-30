from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class Todo(models.Model):

    PriorityChoices = (
        ('h', 'high'),
        ('m', 'medium'),
        ('l', 'low'),
    )

    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"))
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("user"),
        on_delete=models.CASCADE
    )
    priority = models.CharField(
        max_length=1,
        choices=PriorityChoices,
        default=PriorityChoices[1],
    )
    last_update_at = models.DateTimeField(
        _("last update at"), auto_now=True, )
    created_at = models.DateTimeField(
        _("created at"),  auto_now_add=True)

    class Meta:
        ordering = ['last_update_at']
        verbose_name = _("todo")
        verbose_name_plural = _("todos")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Todo_detail", kwargs={"pk": self.pk})
