# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('plantree_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('depth', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('numchild', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('task', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('finished', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('plantree', ['Category'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('plantree_category')


    models = {
        'plantree.category': {
            'Meta': {'object_name': 'Category'},
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['plantree']
