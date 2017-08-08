var pedidoModulo = angular.module('pedidoModulo',['resti']);

pedidoModulo.directive('pedidoform',function(){
    return{
        restrict:'E',
        replace:true,
        templateUrl:'/static/pedido/html/pedidoForm.html',
        scope:{
            ped:'=',
            emailLabel:'@',
            descricaoLabel: '@',
            arquivoLabel:'@',
            saveComplete: '&'
        },
        controller:function($scope, PedidoApi){
            $scope.salvandoFlag=false;
            $scope.salvar = function(){
                $scope.salvandoFlag=true;
                $scope.errors={};
                var promessa = PedidoApi.salvar($scope.ped);
                promessa.success(function(ped){
                    console.log(ped);
                    $scope.ped.email='';
                    $scope.ped.descricao='';
                    $scope.ped.arquivo='';
                    $scope.salvandoFlag=false;
                    if($scope.saveComplete != undefined){
                        $scope.saveComplete({'pedido':ped});
                    }
                });
                    promessa.error(function(erros){
                    $scope.errors=erros;
                    console.log(erros);
                    $scope.salvandoFlag=false;
                });
            }
        }
    };
});


pedidoModulo.directive('pedidolinha',function(){
    return{
        restrict: 'A',
        replace:true,
        templateUrl:'/static/pedido/html/pedido_linha_tabela.html',
        scope:{
            ped:'=',
            deleteComplete:'&'
        },
        controller:function($scope, PedidoApi){
            $scope.ajaxFlag=false;
            $scope.editingFlag=false;
            $scope.pedidoEdicao={};
            $scope.deletar=function(){
                $scope.ajaxFlag=true;
                PedidoApi.deletar($scope.ped.id).success(function(){
                    $scope.deleteComplete({'pedido':$scope.ped});
                }).error(function(erro){
                    console.log(erro);
                });
            };
            $scope.editar=function(){
                $scope.editingFlag=true;
                $scope.pedidoEdicao.id=$scope.ped.id;
                $scope.pedidoEdicao.email=$scope.ped.email;
                $scope.pedidoEdicao.descricao=$scope.ped.descricao;
                $scope.pedidoEdicao.arquivo=$scope.ped.arquivo;

            };
            $scope.cancel=function(){
                $scope.editingFlag=false;
            };

            $cope.completarEdicao=function(){
                PedidoApi.editar()($scope.pedidoEdicao).success(function(pedido){
                    $scope.ped = pedido;
                    $scope.editingFlag = false;
                });
            };
       }
    };
});

