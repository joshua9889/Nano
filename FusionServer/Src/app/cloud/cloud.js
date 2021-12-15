


// Attempt connecting to secret network



//     network={
//         ssid="FusionAP_41cff4"
//         scan_ssid=1
//         psk="mrifusion"
//         key_mgmt=WPA-PSK
// }

// ignore_broadcast_ssid=1

// Required libraries
// var wpa_cli = require('wireless-tools/wpa_cli');
// var scp = require('scp2');
// var os = require('os');
// var fs = require('fs');
// var request = require('request');
// var mac = require('getmac');

// module.exports = function (FusionSettings, io) {

//     // Variables
//     var FusionServerConnectionConfig = null;
//     var cloudHost = '';
//     var fusionMacAddress = '';


//     // Skip windows machines
//     if (os.platform() != 'win32') {

//         console.log('getting mac address');

//         // Fetch the computer's mac address
//         mac.getMac({
//             iface: FusionSettings.Storage.primaryInterface
//         }, function (macReadError, macAddress) {

//             // Error reading mac address
//             if (macReadError)
//                 console.log('Error reading mac: ' + macReadError);

//             else {

//                 // Set mac address
//                 fusionMacAddress = macAddress;

//                 // Check wireless status
//                 wpa_cli.status(FusionSettings.Storage.primaryInterface, function (wirelessStatusError, status) {

//                     // Error reading wireless status
//                     if (wirelessStatusError)
//                         console.log('Error reading wireless status : ' + wirelessStatusError);

//                     else {  

//                         // Verify connection to secret wifi
//                         if (status.wpa_state == 'COMPLETED' && status.ssid == FusionSettings.Cloud[0].hiddenSSID) {

//                             // Set host to AP ip address
//                             cloudHost = status.ip;

//                             // Retrieve config file       
//                             scp.scp({
//                                 host: cloudHost,
//                                 username: FusionSettings.Cloud[0].ssh_user,
//                                 password: FusionSettings.Cloud[0].ssh_pass,
//                                 path: FusionSettings.Cloud[0].configFilePath
//                             }, FusionSettings.Storage.configLocation, function (retrieveError) {

//                                 // Error getting file
//                                 if (retrieveError)
//                                     console.log('Error retrieving config file : ' + retrieveError);

//                                 // Got file successfully
//                                 else {

//                                     // Read config file
//                                     fs.readFile(FusionSettings.Storage.configLocation + FusionSettings.Cloud[0].configFileName, 'utf8', function (readConfigError, contents) {

//                                         // Error reading file
//                                         if (readConfigError)
//                                             console.log('Error reading config file : ' + readConfigError);

//                                         // Read file
//                                         else {

//                                             // Parse contents into json object
//                                             FusionServerConnectionConfig = JSON.parse(contents);

//                                             var inList = false;

//                                             // Loop through approved controllers
//                                             for (var i = 0; i < FusionServerConnectionConfig.ApprovedFusionControllers.length; i++) {

//                                                 // Check for this controller
//                                                 if (FusionServerConnectionConfig.ApprovedFusionControllers[i].mac == fusionMacAddress) {
//                                                     inList = true;
//                                                     break;
//                                                 }

//                                             }

//                                             // Fusion Controller approved
//                                             if (inList) {

//                                                 // Set wireless connection to retrieved SSID
//                                                 request({
//                                                     url: 'http://localhost:8080/api/admin/wirelessConnections',
//                                                     method: 'POST',
//                                                     json: {
//                                                         ssid: FusionServerConnectionConfig.Settings.ssid,
//                                                         password: FusionServerConnectionConfig.Settings.password
//                                                     }
//                                                 }, function (setWirelessConnectionError, response, body) {

//                                                     // Error setting wireless connection
//                                                     if (setWirelessConnectionError)
//                                                         console.log('Error setting wireless connection : ' + setWirelessConnectionError);

//                                                     else {

//                                                         // Connected successfully
//                                                         if (response.statusCode == 200) {

//                                                             FusionSettings.Storage.type = FusionSettings.Cloud[0].type;
//                                                             FusionSettings.Storage.address = FusionSettings.Cloud[0].ip;

//                                                         }

//                                                     }

//                                                     // Emit storage type
//                                                     io.sockets.emit('wifi-fusion_storage_type', FusionSettings.Storage.type);

//                                                 });
//                                             }
//                                         }
//                                     });
//                                 }
//                             });
//                         }
//                     }
//                 });
//             }
//         });
//     }
// };



// Dependencies ===========================
var os = require('os');
var rp = require('request-promise');
var mac = require('getmac');
var target = '172.16.0.1';
var pingSession = require('net-ping').createSession();
const logger = require('../utils/logger');

process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';

module.exports = function (FusionSettings, io, storage) {


    // Establishes storage check ====================================

    pingSession.pingHost (target, function (error, target) {
        
        if (error){
            storage.type = 'local';
            logger.info('Storage Type: local');
        }
        else{
            storage.type = 'classroom';
            FusionSettings.Storage.type = FusionSettings.Cloud[0].type;
            FusionSettings.Storage.address = FusionSettings.Cloud[0].ip;
            logger.info('Storage Type: classroom');
        }

        // Emit storage type
        io.sockets.emit('wifi-fusion_storage_type', FusionSettings.Storage.type);
    });


    // Skip windows machines
    // if (os.platform() != 'win32') {

    //     // Try to connect to secret network

    //     var requestOptions = {
    //         uri: 'http://localhost:8080/api/admin/wirelessConnections',
    //         method: 'POST',
    //         body: {
    //             ssid: 'c3edu.online',
    //             password: 'mydemokey'
    //         },
    //         json: true
    //     };

    //     rp(requestOptions).then(function(connected){

    //         console.log('connected to c3 network;');

    //         setTimeout(function(){

    //             // Get mac address
    //             mac.getMac({
    //                 iface: FusionSettings.Storage.primaryInterface
    //             }, function (macReadError, macAddress) {
        
    //                 // Error reading mac address
    //                 if (macReadError)
    //                     console.log('Error reading mac: ' + macReadError);
        
    //                 else {
        
    //                     // Check if a part of network
    //                     var requestOptions = {
    //                         uri: 'https://172.16.0.1:8443/api/v1/connect/123456',
    //                         method: 'GET',
    //                         rejectUnauthorized: false,
    //                         insecure: true
    //                     };

    //                     rp(requestOptions).then(function(response){

    //                         console.log('response from community check');
    //                         console.log(response);


    //                     }, function(failedCommunityCheck){
    //                         console.log('failed checking community');
    //                         console.log(failedCommunityCheck);
    //                     });

    //                 }

    //             });

    //         }, 5000);
            

    //     }, function(connectionFailed){
    //         console.log('connection to c3 network failed');
    //         console.log(connectionFailed);
    //     });

    // }

};
