var app = angular.module('image-translation', []);			

app.controller('ImageTranslationCtrl', ['$scope', '$http', '$httpParamSerializerJQLike', 
function ImageTranslationCtrl($scope, $http, $httpParamSerializerJQLike) {			  

	var loadLanguages = function() {
		$http.get("languages.json").then(function(success) {		
			$scope.validLanguages = success.data;			
	  }, function(failure) {});	
	}

	loadLanguages();

  $scope.predict = function(url, language) {

  	$scope.url = url;

  	var req = {
		 method: 'POST',
		 url: 'http://localhost:7777/predict/',
		 headers: {
      	'Content-Type': 'application/x-www-form-urlencoded', 
      	'Accept': 'application/json' 
    	},
		 data: $httpParamSerializerJQLike({url: url}),
		};

  	$http(req).then(function(success) {			  				  					  		
  		var words = Object.keys(success.data);
  		var vals = Object.values(success.data);			  		

  		var req = {
				method: 'POST',
				url: 'http://localhost:5001/',
				headers: {
		      	'Content-Type': 'application/x-www-form-urlencoded', 
		      	'Accept': 'application/json' 
				},
				data: {
					words: words, 
					source: 'en', 
					target: language
				},
			};

	  	$http(req).then(function(success) {

				var translations = []			  		
	  		_.each(success.data.data.translations, function(value, key) {
					translations.push(Object.values(value)[0]);
				});
	  		
	  		$scope.concepts = _.zip(words, translations, vals);
			}, function(failure) {});

		}, function(failure) {});
	}	 
}]);