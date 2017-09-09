from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class EventsIndexPage(Page):
    intro = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class EventPage(Page):
    start = models.DateTimeField()
    intro = models.CharField(max_length=250)
    description = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('start'),
        FieldPanel('intro'),
        FieldPanel('description'),
    ]
