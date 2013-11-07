# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Persona'
        db.create_table(u'common_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'common', ['Persona'])

        # Adding model 'Auto'
        db.create_table(u'common_auto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('duenio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Persona'])),
            ('modelo', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'common', ['Auto'])


    def backwards(self, orm):
        # Deleting model 'Persona'
        db.delete_table(u'common_persona')

        # Deleting model 'Auto'
        db.delete_table(u'common_auto')


    models = {
        u'common.auto': {
            'Meta': {'object_name': 'Auto'},
            'duenio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Persona']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'common.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['common']