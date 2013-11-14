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
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'common', ['Persona'])

        # Adding model 'Mascota'
        db.create_table(u'common_mascota', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('duenio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Persona'], null=True, blank=True)),
            ('raza', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Especie'])),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'common', ['Mascota'])

        # Adding model 'Especie'
        db.create_table(u'common_especie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('domesticable', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'common', ['Especie'])

        # Adding model 'Raza'
        db.create_table(u'common_raza', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('especie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Especie'])),
        ))
        db.send_create_signal(u'common', ['Raza'])


    def backwards(self, orm):
        # Deleting model 'Persona'
        db.delete_table(u'common_persona')

        # Deleting model 'Mascota'
        db.delete_table(u'common_mascota')

        # Deleting model 'Especie'
        db.delete_table(u'common_especie')

        # Deleting model 'Raza'
        db.delete_table(u'common_raza')


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