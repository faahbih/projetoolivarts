# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from desenho.desenho_model import Desenho
from config.template_middleware import TemplateResponse
from mock import Mock
from routes.desenhos.new import salvar
from routes.rest import desenhos
from tekton.gae.middleware.redirect import RedirectResponse


class NewTests(GAETestCase):
    def test_sucesso(self):
        resposta = salvar(email='test@test.com', descricao='fazer desenho', arquivo='exemplo1')
        self.assertIsInstance(resposta, RedirectResponse)
        self.assertEqual('/desenhos', resposta.context)
        desenhos = Desenho.query().fetch()
        self.assertEqual(1, len(desenhos))
        des = desenhos[0]
        self.assertEqual('test@test.com', des.email)
        self.assertEqual('fazer desenho', des.descricao)
        self.assertEqual('exemplo1', des.arquivo)

    def test_erro_validacao(self):
        resposta = salvar()
        self.assertIsInstance(resposta, TemplateResponse)
        self.assert_can_render(resposta)
        self.assertIsNone(Desenho.query().get())
        self.assertDictEqual({u'desenhos': {},
                              u'erros': {'email': u'Required field','descricao': u'Required field', 'arquivo': u'Required field'}},
                             resposta.context)

    def test_salvar_desenho_erro_json(self):
        resposta_http = Mock()
        resposta = desenhos.salvar(resposta_http)
        self.assert_can_serialize_as_json(resposta)
        resposta_http.set_status.assert_called_once_with(400)


mock = Mock()

mock.bizarro(9)
mock.bizarro.assert_called_once_with(9)
