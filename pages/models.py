from django.db import models

from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from .blocks import ImageGridBlock, SingleColumnBlock, TwoColumnBlock, ThreeColumnBlock, FourColumnBlock


class StandardPage(Page):
    # Hero section of Page
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='2400X858px'
    )
    body = StreamField([
        ('single_column', SingleColumnBlock(group='COLUMNS')),
        ('two_columns', TwoColumnBlock(group='COLUMNS')),
        ('three_columns', ThreeColumnBlock(group='COLUMNS')),
        ('four_columns', FourColumnBlock(group='COLUMNS')),
        ('image_grid', ImageGridBlock(icon='image', min_num=2, max_num=4, help_text='Minimum 2 blocks and a maximum of 4 blocks')),
    ],default='')

    content_panels = Page.content_panels + [
        ImageChooserPanel('hero_image'),
        StreamFieldPanel('body'),
    ]