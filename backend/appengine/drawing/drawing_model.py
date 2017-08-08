# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaeforms.ndb.form import ModelForm


class Drawing(ndb.Model):
    email = ndb.StringProperty(required=True)
    descricao = ndb.StringProperty(required=True)
    arquivo = ndb.StringProperty(required=True)

    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(cls.email)


class DrawingForm(ModelForm):
    _model_class = Drawing
    _include = [Drawing.email, Drawing.descricao, Drawing.arquivo]