$(document).ready(function () {
    var $txtInput = $('#txt-input');
    var $listaDiv = $('#lista-div');
    var $inputEmail = $("input[name='email']");
    var $inputDescricao = $("input[name='descricao']");
    var $inputArquivo = $("input[name='arquivo']");
    var $ajaxImg = $('#ajax-img');
    var $pedidosLista = $('#pedidos-lista');

  function adicionarPedido(desenho) {

      var li = '<li id="li-' + desenho.id + '" ><button id="btn-apagar-' + desenho.id;
      li += '" class="btn btn-danger"><i class="glyphicon glyphicon-trash"></i></button>';
      li += desenho.email + ' - ' + desenho.descricao + ' - ' + desenho.arquivo + '</li>';
      $pedidosLista.append(li);

      $('#btn-apagar-' + desenho.id).click(function () {
          $.post('/rest/desenhos/apagar', {'desenho_id': desenho.id}, function () {
              $('#li-' + desenho.id).remove();
          });
      });
  }


    $.get('/rest/desenhos/listar', function (desenhos) {
        $.each(desenhos, function (i, desenho) {
            adicionarPedido(desenho);
        });

    });

    $ajaxImg.hide();

    var $msgUl = $('#msg-ul');
    var $selectPedido = $("select[name='pedido']");
    var $inputDescricao = $("input[name='descricao']");
    var $inputArquivo = $("input[name='arquivo']");


    function obterInputs() {
        return {
            'email': $inputEmail.val(),
            'descricao': $inputDescricao.val(),
            'arquivo': $inputArquivo.val(),
            'pedido': $selectPedido.val()
        };
    }

    var $salvarBotao = $('#salvar-pedido-btn');

    $salvarBotao.click(function () {
        $('div.has-error').removeClass('has-error');
        $('span.help-block').text('');

        $ajaxImg.fadeIn();
        $salvarBotao.attr('disabled', 'disabled');

        $.post('/rest/desenhos/salvar', obterInputs(), function (desenho) {
            adicionarPedido(desenho);
            $('input.form-control').val('');

        }).error(function (erro) {

            var errosJson = erro.responseJSON;

            for (propriedade in  errosJson) {
                $('#' + propriedade + '-div').addClass('has-error');
                $('#' + propriedade + '-span').text(errosJson[propriedade]);
            }

        }).always(function () {
            $ajaxImg.fadeOut();
            $salvarBotao.removeAttr('disabled');
        });
    });

    $('#jq').click(function fcn(evento) {
        $listaDiv.slideToggle();
    });


    $('#jq2').click(function fcn(evento) {
        $listaDiv.empty();
    });

    $('#enviar-btn').click(function () {
        var msg = $txtInput.val();
        $txtInput.val('');
        var item = '<li>' + msg + '</li>';

        $msgUl.prepend(item);
        $msgUl.fadeOut(400, function () {
            $msgUl.fadeIn(2000);
        });
    });
});
