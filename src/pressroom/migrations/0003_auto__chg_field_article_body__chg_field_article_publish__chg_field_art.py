# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Article.body'
        db.alter_column('pressroom_article', 'body', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Article.publish'
        db.alter_column('pressroom_article', 'publish', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Article.summary'
        db.alter_column('pressroom_article', 'summary', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Article.pub_date'
        db.alter_column('pressroom_article', 'pub_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Article.slug'
        db.alter_column('pressroom_article', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

        # Changing field 'Section.slug'
        db.alter_column('pressroom_section', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

        # Changing field 'Document.file'
        db.alter_column('pressroom_document', 'file', self.gf('django.db.models.fields.files.FileField')(max_length=100))

        # Changing field 'Document.pub_date'
        db.alter_column('pressroom_document', 'pub_date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Document.slug'
        db.alter_column('pressroom_document', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

    def backwards(self, orm):

        # Changing field 'Article.body'
        db.alter_column('pressroom_article', 'body', self.gf('models.TextField')("Body text"))

        # Changing field 'Article.publish'
        db.alter_column('pressroom_article', 'publish', self.gf('models.BooleanField')("Publish on site"))

        # Changing field 'Article.summary'
        db.alter_column('pressroom_article', 'summary', self.gf('models.TextField')(default=u''))

        # Changing field 'Article.pub_date'
        db.alter_column('pressroom_article', 'pub_date', self.gf('models.DateTimeField')("Publish date"))

        # Changing field 'Article.slug'
        db.alter_column('pressroom_article', 'slug', self.gf('models.SlugField')())

        # Changing field 'Section.slug'
        db.alter_column('pressroom_section', 'slug', self.gf('models.SlugField')())

        # Changing field 'Document.file'
        db.alter_column('pressroom_document', 'file', self.gf('models.FileField')("Document"))

        # Changing field 'Document.pub_date'
        db.alter_column('pressroom_document', 'pub_date', self.gf('models.DateTimeField')("Date published"))

        # Changing field 'Document.slug'
        db.alter_column('pressroom_document', 'slug', self.gf('models.SlugField')())

    models = {
        'photologue.photo': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Photo'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_related'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.6'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'pressroom.article': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Article'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'articles'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['pressroom.Document']"}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'articles'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['photologue.Photo']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'articles'", 'symmetrical': 'False', 'to': "orm['pressroom.Section']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "u''", 'null': 'True', 'blank': 'True'})
        },
        'pressroom.document': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Document'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pressroom.section': {
            'Meta': {'ordering': "['title']", 'object_name': 'Section'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        }
    }

    complete_apps = ['pressroom']