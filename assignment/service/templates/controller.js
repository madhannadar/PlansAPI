
var app = angular.module('myApp', []);

// angular.module('myApp').component('getPlans',{
//   templateUrl:'getPlans.html',
//   // template:'<p>hey controller</p>',
//   controller:['$scope','$http',function getPlans($scope,$http){
//       var self = this
//       var auth = window.btoa("madhan:madhan")
//       headers = {"Authorization": "Basic " + auth};
//       // console.log("submit clicket",$scope.Plans.planName)
//       $http({
//           method : "GET",
//           url : "http://127.0.0.1:8000/api/plans/",
//           headers:headers
//         }).then(function mySuccess(response) {
//           $scope.result = response.data;
//           console.log($scope.result)
//         }, function myError(response) {
//           $scope.errorResult = response.data
//           $scope.result = null  
//           console.log($scope.result)
//       });      
//     }
//   ]
// })



app.controller('getPlans',function($scope,$http) {
  $scope.getPlans = function(){
      var auth = window.btoa("madhan@gmai.com:madhan")
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
          // $scope.result = null  
          console.log("erro",response.data)
      });
  }
})

app.controller('addPlans', function($scope,$http) {
  $scope.flag = false
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
        planType:"",
        planServiceId:"",
        planGST:"",
        planOriginalPrice:"",
        planIsActive:"1"
    }
    $scope.submitPlans = function(){
        data = {
          "plan_name":$scope.Plans.planName,  
          "plan_description": $scope.Plans.planDesc,
          "plan_amount": $scope.Plans.planAmount,
          "plan_added":  new Date(),
          "plan_icon": $scope.Plans.planIcon,
          "plan_type": $scope.Plans.planType,
          "plan_service_id": $scope.Plans.planServiceId,
          "plan_gst_amount": $scope.Plans.planGST,
          "plan_video": null,
          "plan_sample_report": null,
          "plan_original_price": $scope.Plans.planOriginalPrice,
          "plan_isactive": $scope.Plans.planIsActive,
          "plan_created_by": null,
          "plan_updated_by": 1,
          "last_modified":new Date()
        }
        $scope.flag = true
        var auth = window.btoa("madhan:madhan")
        headers = {"Authorization": "Basic " + auth};
        console.log("submit clicket",data)
        $http({
            method : "POST",
            url : "http://127.0.0.1:8000/api/plans/",
            headers:headers,
            data:data
          }).then(function mySuccess(response) {
            $scope.myWelcome = response.data;
            // $window.location.href = '/Home/index.html';
            $scope.Plans = {}
          }, function myError(response) {
            console.log(response)
            // $scope.myWelcome = response.statusText;
        });
    }    
    // $scope.Plans.lastName = "Doe"
    // $scope.fullName = function() {
    //     return $scope.firstName + " " + $scope.lastName;
    // }
})

