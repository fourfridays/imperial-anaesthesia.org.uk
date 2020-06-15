from django.db import models
from django.shortcuts import render

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import (
    StreamFieldPanel, FieldPanel, MultiFieldPanel, FieldRowPanel
)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from .blocks import ImageGridBlock, SingleColumnBlock, TwoColumnBlock, ThreeColumnBlock, FourColumnBlock
from taxonomy.models import Node


class StandardPage(Page):
    page_subtitle = models.TextField(max_length=255, blank=True)
    body = StreamField([
        ('single_column', SingleColumnBlock(group='COLUMNS')),
        ('two_columns', TwoColumnBlock(group='COLUMNS')),
        ('three_columns', ThreeColumnBlock(group='COLUMNS')),
        ('four_columns', FourColumnBlock(group='COLUMNS')),
        ('image_grid', ImageGridBlock(icon='image', min_num=2, max_num=4, help_text='Minimum 2 blocks and a maximum of 4 blocks')),
    ],default='')

    content_panels = Page.content_panels + [
        FieldPanel('page_subtitle'),
        StreamFieldPanel('body'),
    ]


@register_snippet
class Person(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    role = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    category = models.ForeignKey('taxonomy.Node', on_delete=models.PROTECT, limit_choices_to=Node.get_department_categories, default='')

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "people"

    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.role)

    panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('first_name', classname="col6"),
                FieldPanel('last_name', classname="col6"),
            ])
        ], "Name"),
        FieldPanel('role'),
        FieldPanel('bio'),
        ImageChooserPanel('image'),
        FieldPanel('category')
    ]


class PeopleIndexPage(Page):
    page_subtitle = models.TextField(max_length=255, blank=True)

    def get_context(self, request):
        context = super(PeopleIndexPage, self).get_context(request)
        context['people'] = Person.objects.all()
        return context

    content_panels = Page.content_panels + [
        FieldPanel('page_subtitle')
    ]