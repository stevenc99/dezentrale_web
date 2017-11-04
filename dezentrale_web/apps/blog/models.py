from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page


class BlogIndexPage(Page):
    intro = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    subpage_types = ['BlogPage']


class BlogPage(Page):
    content = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
    ])
    author = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
        FieldPanel('author', classname="full"),
    ]

    parent_page_types = ['BlogIndexPage']
    subpage_types = []
