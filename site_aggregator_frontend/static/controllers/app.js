// Define the `phonecatApp` module
var app = angular.module('app', []);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
  });

// Define the `PhoneListController` controller on the `phonecatApp` module
app.controller('PhoneListController', function PhoneListController($scope) {
  $scope.phones = [
    {
      name: 'Test 1',
      snippet: 'This is the snippet of Test 1'
    }, {
      name: 'Test 2',
      snippet: 'This is the snippet of Test 2'
    }, {
      name: 'Test 3',
      snippet: 'This is the snippet of Test 3'
    }
  ];
 });