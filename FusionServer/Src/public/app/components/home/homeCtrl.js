// app/components/home/homeCtrl.js

angular
    .module('fusionApp')
    .controller('homeCtrl', ['$scope', 'appFactory', '$window', '$state', 'userFactory', 'socketFactory', function ($scope, appFactory, $window, $state, userFactory, socketFactory) {

        // Set Page Title
        appFactory.ChangePageTitle('HOME.TITLE');

        // Disable shortcuts based on usergroup
        $scope.HomePageShortCutDisabled = function (shortcut) {            
            
            var disabled = true;

            switch (shortcut) {

                case 'build':
                    disabled = false;
                    break;
                case 'blockly':
                    disabled = false;
                    break;
                case 'editor':
                    disabled = false;
                    break;
                case 'docs':
                    disabled = false;
                    break;
                case 'server':
                    disabled = true;
                    break;
                case 'datalogger':
                    disabled = false;
                    break;
                case 'settings':
                    if (userFactory.User.usergroup == 'Admin')
                        disabled = false;
                    else
                        disabled = true;
                    break;

            }
            
            if (disabled)
                return 'f-disabled';
            else
                return '';

        }

        // Link Clicked
        $scope.LinkClicked = function (path, target) {

            $window.open(path, target);

        }

        // Launches the specifed state
        $scope.Launch = function (state, mode) {

            if (mode) {
                userFactory.User.blocklySettings.Mode = mode;
            }

            $state.go(state);

        }

        let loginData = {
            username: 'mriguest',
            password: 'mriguest',
            socketId: socketFactory.Socket.id
        };

        if (!userFactory.User.username) {
            userFactory.Login(loginData);
        }

    }]);
