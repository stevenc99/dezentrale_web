from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class home(Page):
    devMessage = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('devMessage', classname="full")
    ]
