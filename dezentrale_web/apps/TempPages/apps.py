from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TemppagesConfig(AppConfig):
    """Configuration for TempPages app."""

    name = 'dezentrale_web.apps.TempPages'
    verbose_name = _("Temppages")
