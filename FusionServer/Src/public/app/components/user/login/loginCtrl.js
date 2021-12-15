angular
    .module('fusionApp')
    .controller('loginCtrl', ['$scope', 'userFactory', 'appFactory', '$location', 'socketFactory', '$window', function ($scope, userFactory, appFactory, $location, socketFactory, $window) {

        $scope.existingUsers = [];

        $scope.socketData = socketFactory.data;

        $scope.createUser = function() {

            var dialogData = {
                title: 'Enter Username?',
                content: '',
                userInput: 'Enter Username'
            };

            appFactory.showOkCancel(dialogData).then(function(dialogInput){

                var userData = {
                    username: dialogInput,
                    password: dialogInput.toLowerCase(),
                    usergroup: 'Guest'
                };

                userFactory.Create(userData);

            });

        };

        $scope.login = function(username) {

            var loginData = {
                username: username,
                password: username,
                socketId: socketFactory.Socket.id
            };

            userFactory.Login(loginData);

        };

        $scope.deleteGuest = function(userId) {            
            userFactory.DeleteGuest(userId).then(function(){
                $scope.refreshGuestList();
            });
        };

        $scope.refreshGuestList = function() {
            userFactory.GetAllGuests().then(function(data){
                $scope.existingUsers = data;
            });
        };

        // Set Page Title
        appFactory.ChangePageTitle('LOGIN.TITLE');

        // Fetch Existing Guest Users
        $scope.refreshGuestList();


    }]);
