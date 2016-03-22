angular.module('chat', ['ngResource', ])

.run(function($rootScope){
	$rootScope.canalId = angular.element(document.querySelector('#canal-id')).val()
	$rootScope.mensajes = false

	wsUrl = angular.element(document.querySelector('#ws-url')).val()
	wsHb  = angular.element(document.querySelector('#ws-hb')).val()

	ws4redis = WS4Redis({
		uri: wsUrl,
		receive_message: receiveMessage,
		heartbeat_msg: wsHb,
	})

	function receiveMessage(data){
		if( !$rootScope.mensajes ){
			return false
		}

		$rootScope.$apply(function(){
			data = $.parseJSON(data)

			if(data.method == 'POST'){
				$rootScope.mensajes.push(data.data)
			}
		})
	}
})

.config(function($resourceProvider, $httpProvider){
	$httpProvider.defaults.xsrfCookieName           = 'csrftoken'
	$httpProvider.defaults.xsrfHeaderName           = 'X-CSRFToken'
	$resourceProvider.defaults.stripTrailingSlashes = false
})

.factory('Mensaje', function($resource){
	return $resource('/api/canales/:canalId/mensajes/')
})

.controller('CanalController', function($rootScope, $scope, Mensaje){
	Mensaje.query({canalId: $rootScope.canalId}).$promise.then(function(data){
		$rootScope.mensajes = data
	})

	$scope.mensaje = {}

	$scope.enviarMensaje = function(valid){
		if( valid ){
			Mensaje.save({canalId: $rootScope.canalId}, $scope.mensaje).$promise.then(function(){
				$('#mensajeForm')[0].reset()
			}, function(){
				window.alert('Ha ocurrido un error al enviar el mensaje, intente nuevamente.')
			})
		}
	}
})