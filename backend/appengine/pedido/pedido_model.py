# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaeforms.ndb.form import ModelForm


class Pedido(ndb.Model):
    email = ndb.StringProperty(required=True)
    descricao = ndb.StringProperty(required=True)
    arquivo = ndb.StringProperty(required=True)

    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(cls.email)

class PedidoForm(ModelForm):
    _model_class = Pedido
    _include = [Pedido.email, Pedido.descricao, Pedido.arquivo]
