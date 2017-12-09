"use strict";

var app = angular.module('image-translation', []);			

app.controller('ImageTranslationCtrl', ['$scope', '$http', '$httpParamSerializerJQLike', 
function ImageTranslationCtrl($scope, $http, $httpParamSerializerJQLike) {			  

	var loadLanguages = function() {
		$http.get("languages.json").then(function(success) {		
			$scope.langList = success.data;
	  }, function(failure) {});	
	}

	loadLanguages();

  $scope.predict = function(url, source, target) {

  	$scope.url = url;
  	$scope.lang1 = source.lang;
  	$scope.lang2 = target.lang;

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
					lang1: source.code, 
					lang2: target.code
				},
			};

	  	$http(req).then(function(success) {
	  		
	  		var source = []			  		
	  		_.each(success.data.lang1, function(value, key) {
					source.push(value);
				});

				var target = []			  		
	  		_.each(success.data.lang2, function(value, key) {
					target.push(value);
				});
	  		
	  		$scope.concepts = _.zip(source, target, vals);
			}, function(failure) {});

		}, function(failure) {});
	}	 
}]);