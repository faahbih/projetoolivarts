from config.template_middleware import TemplateResponse
from drawing.drawing_model import Drawing
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path


@login_not_required
@no_csrf
def index(pedido_id):
    pedido = Drawing.get_by_id(int(pedido_id))
    ctx = {'pedido': pedido,
           'salvar_path': to_path(salvar)}
    return TemplateResponse(ctx, 'pedido/pedidoForm.html')


@login_not_required
def salvar(pedido_id, email, descricao, arquivo):
    pedido = Drawing.get_by_id(int(pedido_id))
    pedido.email = email
    pedido.descricao = descricao
    pedido.arquivo = arquivo
    pedido.put()
    return RedirectResponse(pedido)
