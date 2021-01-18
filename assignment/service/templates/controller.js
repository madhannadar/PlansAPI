
var app = angular.module('myApp', []);
app.controller('personCtrl', function($scope,$http) {
    $scope.planTypeOption =[
        {id: '1', name: 'Option A'},
        {id: '2', name: 'Option B'},
        {id: '3', name: 'Option C'}
    ]
    $scope.Plans = {
        planName : "",
        planDesc :"",
        planAmount :"",
        planIcon:"",
        planServiceId:"",
        planGST:""
    }
    $scope.submitPlans = function(){
        var auth = window.btoa("madhan:madhan")
        headers = {"Authorization": "Basic " + auth};
        console.log("submit clicket",$scope.Plans.planName)
        $http({
            method : "GET",
            url : "http://127.0.0.1:8000/api/plans/",
            headers:headers
          }).then(function mySuccess(response) {
            $scope.myWelcome = response.data;
            console.log(response.data)
          }, function myError(response) {
            $scope.myWelcome = response.statusText;
        });
    }    
    // $scope.Plans.lastName = "Doe"
    // $scope.fullName = function() {
    //     return $scope.firstName + " " + $scope.lastName;
    // }
})

app.controller('getPlans',function($scope,$http) {
    $scope.getPlans = function(){
        var auth = window.btoa("madhan:madhan")
        headers = {"Authorization": "Basic " + auth};
        // console.log("submit clicket",$scope.Plans.planName)
        $http({
            method : "GET",
            url : "http://127.0.0.1:8000/api/plans/",
            headers:headers
          }).then(function mySuccess(response) {
            $scope.result = response.data;
            console.log($scope.result)
          }, function myError(response) {
            $scope.myWelcome = response.statusText;
        });
    }    
})