# Generated by Django 2.2.10 on 2020-03-07 19:43

from django.db import migrations, models
import django.db.models.deletion
import pages.blocks
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('single_column', wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('background_color', pages.blocks.BackgroundColorBlock())], group='COLUMNS')), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('background_color', pages.blocks.BackgroundColorBlock())], group='COLUMNS')), ('three_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('middle_column', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('background_color', pages.blocks.BackgroundColorBlock())], group='COLUMNS')), ('four_columns', wagtail.core.blocks.StructBlock([('left_column_1', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('left_column_2', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column_1', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column_2', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('background_color', pages.blocks.BackgroundColorBlock())], group='COLUMNS')), ('image_grid', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))], help_text='Minimum 2 blocks and a maximum of 4 blocks', icon='image', max_num=4, min_num=2))], default='')),
                ('hero_image', models.ForeignKey(blank=True, help_text='2400X858px', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
