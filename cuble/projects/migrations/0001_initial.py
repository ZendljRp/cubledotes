# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('projects_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.User'])),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 6, 28, 0, 0))),
            ('scheduled_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('outstanding_image', self.gf('django.db.models.fields.files.ImageField')(blank=True, null=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('thumbnail_image', self.gf('django.db.models.fields.files.ImageField')(blank=True, null=True, max_length=100)),
        ))
        db.send_create_signal('projects', ['Project'])

        # Adding M2M table for field tags on 'Project'
        m2m_table_name = db.shorten_name('projects_project_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('tag', models.ForeignKey(orm['tags.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'tag_id'])

        # Adding model 'Budget'
        db.create_table('projects_budget', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('company', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=128)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('stage', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('other_type', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=128)),
            ('about', self.gf('django.db.models.fields.TextField')()),
            ('hosting', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hosting_assistance', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hosting_type', self.gf('django.db.models.fields.IntegerField')(blank=True, default=3)),
            ('hosting_quotes', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=128)),
            ('branding_design', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('branding_design_about', self.gf('django.db.models.fields.TextField')(blank=True, default='')),
            ('web_design', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('web_design_stage', self.gf('django.db.models.fields.IntegerField')(blank=True, default=0)),
            ('responsive_web_design', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('badget', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('badget_file', self.gf('django.db.models.fields.files.FileField')(blank=True, null=True, max_length=100)),
        ))
        db.send_create_signal('projects', ['Budget'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('projects_project')

        # Removing M2M table for field tags on 'Project'
        db.delete_table(db.shorten_name('projects_project_tags'))

        # Deleting model 'Budget'
        db.delete_table('projects_budget')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profiles.user': {
            'Meta': {'object_name': 'User'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'charisma': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'constitution': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'dexterity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'strength': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'wisdom': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'projects.budget': {
            'Meta': {'object_name': 'Budget'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'badget': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'badget_file': ('django.db.models.fields.files.FileField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'branding_design': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'branding_design_about': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'company': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '128'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'hosting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hosting_assistance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hosting_quotes': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '128'}),
            'hosting_type': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'default': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'other_type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '128'}),
            'responsive_web_design': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'stage': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'web_design': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'web_design_stage': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'default': '0'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.User']"}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 6, 28, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'outstanding_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'scheduled_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.Tag']", 'related_name': "'projects'"}),
            'thumbnail_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        'tags.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']