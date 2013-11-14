# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Mascota.nombre'
        db.add_column(u'common_mascota', 'nombre',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Mascota.nombre'
        db.delete_column(u'common_mascota', 'nombre')


    models = {
        u'common.especie': {
            'Meta': {'object_name': 'Especie'},
            'domesticable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'common.mascota': {
            'Meta': {'object_name': 'Mascota'},
            'duenio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Persona']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'raza': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Especie']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'common.persona': {
            'Meta': {'object_name': 'Persona'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'common.raza': {
            'Meta': {'object_name': 'Raza'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Especie']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['common']