var app = angular.module('myApp', []);

app.controller('StoreController',function($scope,$http){
    console.log("controlller")
    $scope.getPlans = function(){
        var auth = window.btoa("madhan@gmail.com:madhan")
        var headers = {"Authorization": "Basic " + auth};
        // console.log("submit clicket",$scope.Plans.planName)
        $http({
            method : "GET",
            url : "http://127.0.0.1:8000/api/plans/",
            headers:headers
          }).then(function mySuccess(response) {
            $scope.plans = response.data;
            $scope.flag = true
            console.log($scope.result)
          }, function myError(response) {
            $scope.errorResult = response.data
            // $scope.result = null  
            $scope.flag = false
            console.log(response.data)
        });
    }

})