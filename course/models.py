from django.db import models
from django.template.response import TemplateResponse

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class CourseIndexPage(RoutablePageMixin, Page):
    @route(r'^submit-course/$')
    def submit_course(self, request):
        from .views import submit_course
        return submit_course(request)


class Course(models.Model):
    title = models.CharField(max_length=140)
    summary = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    external_url = models.URLField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    flyer = models.FileField(upload_to='documents/', null=True, blank=True)
    application_form = models.FileField(upload_to='documents/', null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)