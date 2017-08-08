var resti=angular.module('resti',[]);
    resti.factory('PedidoApi',function($rootScope){
       return{
           salvar: function(pedido){
              var obj={};
               obj.success=function(fcnSucesso){
                   obj.fcnSucesso=fcnSucesso;
               };
               obj.error=function(fcnError){
                   obj.fcnError=fcnError;
               };
               setTimeout(function(){
                   pedido.id=1;
                   obj.fcnSucesso(pedido);
                   $rootScope.$digest();
               },1000);
               return obj;
           }
       };
    });
