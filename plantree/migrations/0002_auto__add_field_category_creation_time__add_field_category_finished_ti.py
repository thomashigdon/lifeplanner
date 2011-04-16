# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Category.creation_time'
        db.add_column('plantree_category', 'creation_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 4, 15), auto_now_add=True, blank=True), keep_default=False)

        # Adding field 'Category.finished_time'
        db.add_column('plantree_category', 'finished_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 4, 15)), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Category.creation_time'
        db.delete_column('plantree_category', 'creation_time')

        # Deleting field 'Category.finished_time'
        db.delete_column('plantree_category', 'finished_time')


    models = {
        'plantree.category': {
            'Meta': {'object_name': 'Category'},
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'auto_now_add': 'True', 'blank': 'True'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'finished_time': ('django.db.models.fields.DateTimeField', [], {'default': 'None'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['plantree']
