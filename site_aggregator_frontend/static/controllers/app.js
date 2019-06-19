var app = angular.module('app', []);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
  });

app.controller('MainController', function MainController($scope, $http) {
  $http.get('http://127.0.0.1:8000/api/tags/').
        then(function(response) {
            $scope.tags = response.data.results;
        });
 });