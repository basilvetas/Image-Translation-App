"use strict";

var app = angular.module('image-translation', []);			

app.controller('ImageTranslationCtrl', ['$scope', '$http', '$httpParamSerializerJQLike', 
function ImageTranslationCtrl($scope, $http, $httpParamSerializerJQLike) {			  

	var loadLanguages = function() {
		$http.get("languages.json").then(function(success) {		
			$scope.langList = success.data;
			console.log($scope.langList);
	  }, function(failure) {});	
	}

	loadLanguages();

  $scope.predict = function(url, source, target) {

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
					source: source, 
					target: target
				},
			};

	  	$http(req).then(function(success) {

	  		console.log(success.data);

	  		var source = []			  		
	  		_.each(success.data.source.data.translations, function(value, key) {
					source.push(Object.values(value)[0]);
				});

				var target = []			  		
	  		_.each(success.data.target.data.translations, function(value, key) {
					target.push(Object.values(value)[0]);
				});
	  		
	  		$scope.concepts = _.zip(source, target, vals);
			}, function(failure) {});

		}, function(failure) {});
	}	 
}]);