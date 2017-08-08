from google.appengine.ext import ndb
from drawing.drawing_model import DrawingForm, Drawing
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse


def index():
    form = DrawingForm()
    peds = Drawing.query_ordenada_por_nome().fetch()
    peds = [form.fill_with_model(p) for p in peds]
    return JsonUnsecureResponse(peds)


@login_not_required
@no_csrf
def apagar(pedido_id):
    key = ndb.Key(Drawing, int(pedido_id))
    key.delete()
    return JsonUnsecureResponse('')


@login_not_required
@no_csrf
def listar():
    form = DrawingForm()
    draws = Drawing.query_ordenada_por_nome().fetch()
    draws = [form.fill_with_model(p) for p in draws]
    return JsonUnsecureResponse(draws)


@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = DrawingForm(**propriedades)
    erros = form.validate()

    if not erros:
        drawing = form.fill_model()
        drawing.put()
        dct = form.fill_with_model(drawing)
        return JsonUnsecureResponse(dct)
    _resp.set_status(400)
    return JsonUnsecureResponse(erros)