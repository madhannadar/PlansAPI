var app = angular.module('myApp', []);

app.controller('StoreController',function($scope,$http){
    $scope.getPlans = function(){
        var auth = window.btoa("madhan:madhan")
        headers = {"Authorization": "Basic " + auth};
        // console.log("submit clicket",$scope.Plans.planName)
        $scope.temp = "madnhan"
        $http({
            method : "GET",
            url : "http://127.0.0.1:8000/api/plans/",
            headers:headers
          }).then(function mySuccess(response) {
            $scope.result = response.data;
            console.log($scope.result)
          }, function myError(response) {
            $scope.errorResult = response.data
            $scope.result = null  
            console.log($scope.result)
        });
    }

})