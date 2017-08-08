# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaeforms.base import Form, StringField, IntegerField
from gaeforms.ndb.form import ModelForm
from gaeforms.ndb.property import SimpleCurrency


class Categoria(ndb.Model):
    nome = ndb.StringProperty(required=True)

    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(cls.nome)


class CategoriaForm(ModelForm):
    _model_class = Categoria
    _include = [Categoria.nome]
