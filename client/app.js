"use strict";

var app = angular.module('image-translation', []);			

app.controller('ImageTranslationCtrl', ['$scope', '$http', '$httpParamSerializerJQLike', 
function ImageTranslationCtrl($scope, $http, $httpParamSerializerJQLike) {			  
	$scope.count = 0;
	$scope.myFunction = function() {
		$scope.count^=1;
	}
	var loadLanguages = function() {
		$http.get("languages.json").then(function(success) {		
			$scope.langList = success.data;

			$scope.language1 = $scope.langList[20];
			$scope.language2 = $scope.langList[20];
	  }, function(failure) {});	
	}

	loadLanguages();

  $scope.predict = function(url, source, target) {

  	$scope.imageUrl = url;
  	
  	var req = {
		 method: 'POST',
		 url: 'http://localhost:7777/predict/',
		 headers: {
      	'Content-Type': 'application/x-www-form-urlencoded', 
      	'Accept': 'application/json' 
    	},
		 data: $httpParamSerializerJQLike({url: url, count: $scope.count}),
		};

  	$http(req).then(function(success) {			  				  					  		
  		var words = Object.keys(success.data);
  		var vals = Object.values(success.data);			  		
  		
  		$scope.lang1 = source.lang;
  		$scope.lang2 = target.lang;

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

	  	var req_audio = {
	  	     method: 'POST',
	  	     url: 'http://localhost:5002/',
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

	  	$http(req_audio).then(function(success) {
	  	    
	  	    var source = new Audio('source.wav')
	  	    var target = new Audio('target.wav')
	  	    source.play()
	  	    target.play()

	  	}, function(failure) {});

		}, function(failure) {});
	}	 
}]);
