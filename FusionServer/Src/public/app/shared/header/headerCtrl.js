angular
    .module('fusionApp')
    .controller('headerCtrl', ['$scope', '$mdSidenav', '$mdDialog', 'appFactory', 'userFactory', '$location', 'socketFactory', '$state', '$translate', 'settingsFactory', function ($scope, $mdSidenav, $mdDialog, appFactory, userFactory, $location, socketFactory, $state, $translate, settingsFactory) {

        // Controller Variables =======================================

        // Gets User
        $scope.user = userFactory.User;

        $scope.wirelessSettings = {}
        $scope.availableWifiConnections = [];
        $scope.SelectedWirelessConnectionPassword = null;

        //Get Page Title from appFactory
        $scope.appData = appFactory.data;

        // Language
        $scope.selectedLanguage = function() {
            return $translate.use();
        }

        // Get supported languages
        $scope.supportedLanguages = appFactory.getLanguages();

        // Header symbols click =======================================

        // Opens Fusion sidebar menu
        $scope.openFusionMenu = function () {
            $mdSidenav('fusionMenu').toggle();
        }

        // Navigate to home
        $scope.navigateHome = function () {

            $state.go('home');

        }

        // Show battery details
        $scope.showBatteryDetails = function (ev) {

            var title = "Battery Details"
            var content;

            if (socketFactory.data.BatteryLevel == -1 || socketFactory.data.BatteryLevel == "") {

                content = "Battery Level: No Battery Connected";

            } else {

                content = "Battery Level: " + socketFactory.data.BatteryLevel + " %";

            }

            appFactory.showAlert(ev, title, content);

        }

        // Shows Internet connection details
        $scope.showInternetDetails = function (ev) {

            var text = '';

            if (socketFactory.data.InternetAccess)
                text = 'Available';
            else
                text = 'Not Available';

            var title = "Internet Details"

            var content = "Access: " + text;

            appFactory.showAlert(ev, title, content);

        }

        // Shows Wifi connection details
        $scope.showWifiDetails = function (ev) {

            var title = "Wireless Details"

            var content = "Connection: " + socketFactory.data.WifiConnection.ssid;
            content += "<br>";
            content += "IP: " + socketFactory.data.WifiConnection.ip;

            appFactory.showAlert(ev, title, content);

        }

        // Shows running program details
        $scope.showProgramDetails = function (ev) {

            if (socketFactory.data.ProgramRunning.running == undefined)
                socketFactory.data.ProgramRunning.running = false;

            if (socketFactory.data.ProgramRunning.user == undefined)
                socketFactory.data.ProgramRunning.user = 'None';

            var title = "Program Details"

            var content = "Program Running: " + socketFactory.data.ProgramRunning.running;
            content += '<br>';
            content += 'User: ' + socketFactory.data.ProgramRunning.user;

            appFactory.showAlert(ev, title, content);

        }

        // Opens power options
        $scope.openPowerMenu = function ($mdOpenMenu, ev) {
            var originatorEv = ev;
            $mdOpenMenu(ev);
        }

        // Opens the wifi menu
        $scope.openWifiMenu = function ($mdMenu, ev) {

            $scope.refreshWirelessConnections().then(function(){
                var originatorEv = ev;
                $mdMenu.open(ev);
            });
            
        };

        // Opens language options
        $scope.openLanguageMenu = function ($mdOpenMenu, ev) {
            var originatorEv = ev;
            $mdOpenMenu(ev);
        };

        // Change language
        $scope.changeLanguage = function(languageCode) {
            appFactory.changeLanguage(languageCode);
        };

        // Power off menu actions =====================================

        // Poweroff
        $scope.powerOff = function () {
            
            var data = {
                socketId: socketFactory.Socket.id
            }
            
            userFactory.Logout(data).then(function (response) {
                appFactory.PowerOff();
            });
        }

        // Restart function
        $scope.restart = function () {
            
            var data = {
                socketId: socketFactory.Socket.id
            }
            
            userFactory.Logout(data).then(function (response) {
                appFactory.Restart();
            });
        }

        // Poweroff
        $scope.logout = function () {

            var data = {
                socketId: socketFactory.Socket.id
            }

            userFactory.Logout(data);
        }

        // Fetches Wireless Connections
        $scope.refreshWirelessConnections = function () {

            return new Promise(function(resolve, reject) {

                settingsFactory.GetWirelessConnections().then(function (data) {

                    if (data) {
    
                        for (var i = data.length - 1; i >= 0; i--) {
    
                            if (data[i].ssid == $scope.wirelessSettings.SSID) {
                                data.splice(data.indexOf(data[i]), 1);
                            } else if (data[i].ssid == socketFactory.data.WifiConnection.ssid && data[i].address == socketFactory.data.WifiConnection.bssid) {
                                data[i].Connected = true;
                            }
    
                        }
    
                        $scope.availableWifiConnections = data;
    
                    }
    
                    return resolve();
    
                });

            });

        }

        // Makes update button clickable when update available
        $scope.allowUpdate = function () {

            if (socketFactory.data.UpdateAvailable && socketFactory.data.InternetAccess)
                return false;
            else
                return true;

        }

        // Hides the wireless setting content menu if there ore no available connections
        $scope.hasAvailableWifiConnections = function() {
            if ($scope.availableWifiConnections > 0) 
                return true;
            else
                return false;            
        };

        // Connects to the desired connection
        $scope.connectToNetwork = function (connection) {

            if (connection.Connected) {

                appFactory.showOkCancel({
                    title: $translate.instant('SETTINGS.DISCONNECT_FROM_NETWORK.TITLE'),
                    warning: true
                }).then(function (answer) {

                    // Action accepted

                    settingsFactory.DisconnectWirelessConnection().then(function (response) {

                        $scope.refreshWirelessConnections();

                    });


                }, function () {

                    // Action canceled

                });

            } else if (connection.security != 'open') {

                $scope.SelectedWirelessConnectionSSID = connection.ssid;

                $mdDialog.show({
                    contentElement: '#settingsConnectNetworkDialog',
                    parent: angular.element(document.body),
                    clickOutsideToClose: true
                });

            } else {

                var data = {
                    ssid: connection.ssid,
                    password: null
                }

                settingsFactory.SetWirelessConnection(data).then(function (response) {

                    $scope.refreshWirelessConnections();

                });

            }

        }

        $scope.connectToNetworkPassword = function () {

            var data = {
                ssid: $scope.SelectedWirelessConnectionSSID,
                password: $scope.SelectedWirelessConnectionPassword,
            }

            $scope.closeDialog();

            settingsFactory.SetWirelessConnection(data).then(function (response) {
                $scope.SelectedWirelessConnectionSSID = null;
                $scope.SelectedWirelessConnectionPassword = null;

                $scope.refreshWirelessConnections();

            });

        };

        $scope.togglePasswordShowing = function () {

            $scope.ShowPasswordToConnect = !$scope.ShowPasswordToConnect;

            var input = $('#selectedWirelessConnectionPasswordInput')[0];

            if ($scope.ShowPasswordToConnect)
                input.type = 'text';
            else
                input.type = 'password';

        };

        $scope.closeDialog = function () {
            $mdDialog.hide();
        };

        $scope.cancelDialog = function () {
            $mdDialog.cancel();
        };

        $scope.showUpdateDialog = function(){

            $mdDialog.show({
                contentElement: '#updateDialog',
                parent: angular.element(document.body),
                clickOutsideToClose: true
            });

        };

        $scope.updateFUsion = function(){

            // Action accepted
            appFactory.updateFusion().then(function (data) {

            });

        };

        // Socket Communication for console =========================        
        socketFactory.Socket.on('update-output', function (msg) {

            var console = document.getElementById("update-console");
            var incomingText = msg.output;

            if (!incomingText.includes("Update Finished!")) {

                var incomingText = msg.output;

                //Only keeps the last 500 characters displayed to avoid lag over time
                //                $scope.updateConsole = $scope.updateConsole.slice(-(500 - incomingText.length)) + incomingText;
                $scope.updateConsole += incomingText;
                $scope.$apply();

                //Scrolls output textbox down automattically
                console.scrollTop = console.scrollHeight

            } else {

                var incomingText = msg.output;

                $scope.updateConsole += incomingText;
                $scope.$apply();

            }

        });


        // Helper Methods =============================================

        // Returns if user is logged in
        $scope.userLoggedIn = function () {

            var userLoggedIn = null;

            if ($scope.user.username)
                userLoggedIn = true;
            else
                userLoggedIn = false;

            return userLoggedIn;

        }

    }]);
