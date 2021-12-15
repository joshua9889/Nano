var origin = String(document.location.origin).slice(7)
var index = origin.indexOf(':')
var socketAddress = "ws://" + origin.slice(0, index) + ":12345/"
var ws = new WebSocket(socketAddress);

var w = window,
    d = document,
    e = d.documentElement,
    g = d.getElementsByTagName('body')[0],
    screen_x = w.innerWidth || e.clientWidth || g.clientWidth,
    screen_y = w.innerHeight|| e.clientHeight|| g.clientHeight;

   d.addEventListener('touchmove', prevFunc, {passive:false});
   
function prevFunc(e) {
    e.preventDefault();
    console.log("moved");
}
// d.ontouchmove = function(e){
    // passive:false;
    // e.preventDefault();
// }

var outgoing_data = '';

var telemetry = document.getElementById('telemetry');
    
var joystick1 = new VirtualJoystick({
    container       : document.body,
    strokeStyle     : 'white',
    mouseSupport    : true,
    limitStickTravel: true,
    stickRadius     : 50,
    stationaryBase  : true,
    baseX           : 0, //joy1x_offset,
    baseY           : 0, //screen_y - joy1y_offset,
    useCSStransform : true
});

var joystick2 = new VirtualJoystick({
    container       : document.body,
    strokeStyle     : 'white',
    mouseSupport    : true,
    limitStickTravel: true,
    stickRadius     : 50,
    stationaryBase  : true,
    baseX           : 0, //screen_x - joy2x_offset,
    baseY           : 0, //screen_y - joy2y_offset,
    useCSStransform : true
});

joystick1.addEventListener('touchStartValidation', function(event){
    var touch = event.changedTouches[0];
    // if( touch.pageX >= window.innerWidth/2 ) return false;
    if((touch.pageX >= 160) || (touch.pageY < screen_y-160)) return false;
    return true;
});

joystick2.addEventListener('touchStartValidation', function(event){
    var touch = event.changedTouches[0];
    // if( touch.pageX < window.innerWidth/2 ) return false;
    if((touch.pageX < screen_x-160) || (touch.pageY < screen_y-160)) return false;    
    return true;
});

function controlBot() {
    outgoing_data = ''
    if(joystick1._pressed){
        outgoing_data += (Math.ceil(joystick1.deltaX()) + ' ' + Math.ceil(joystick1.deltaY()) + ' ');
    }
    else{
        outgoing_data += '0 0 ';
    }
    
    if(joystick2._pressed){
        outgoing_data += (Math.ceil(joystick2.deltaX()) + ' ' + Math.ceil(joystick2.deltaY()) + ' ');
    }
    else{
        outgoing_data += '0 0 ';
    }    
    
    if(button_A.isClicked()){
        outgoing_data += '1 ';
    }
    else{
        outgoing_data += '0 ';
    }
    
    if(button_B.isClicked()){
        outgoing_data += '1 ';
    }
    else{
        outgoing_data += '0 ';
    }
    
    if(button_X.isClicked()){
        outgoing_data += '1 ';
    }
    else{
        outgoing_data += '0 ';
    }
    
    if(button_Y.isClicked()){
        outgoing_data += '1 ';
    }
    else{
        outgoing_data += '0 ';
    }
    
    ws.send(outgoing_data);
    
};

ws.onmessage = function(e){
    //telemetry.innerHTML = '<b>Telemetry:</b> <br />' + e.data;
    telemetry.innerHTML = e.data;
    console.log(e.data);
};

w.onload = init();

var game;
var button_A, button_B, button_X, button_Y;
var button_size = 60;

function init(){
    button_Y = new GameButton("Y");    
    button_X = new GameButton("X");    
    button_A = new GameButton("A");    
    button_B = new GameButton("B");
}

setInterval(function(){    
    // Screen scaling ---------------------------------------------------------
    screen_x = w.innerWidth || e.clientWidth || g.clientWidth;
    screen_y = w.innerHeight|| e.clientHeight|| g.clientHeight;
    
    // Joystick 1 locations
    joystick1._baseX = 80;
    joystick1._baseY = screen_y - 80;
    joystick1.updateLocation();
    
    // Joystick 2 locations
    joystick2._baseX = screen_x - 80;
    joystick2._baseY = screen_y - 80;
    joystick2.updateLocation();
    
    // Update button locations if necessary    
    button_A.setPosition(screen_x-110, screen_y-220);
    button_A.setSize(button_size,button_size);
    
    button_B.setPosition(screen_x-110, screen_y-290);
    button_B.setSize(button_size,button_size);
    
    button_X.setPosition(50, screen_y-220);
    button_X.setSize(button_size,button_size);
    
    button_Y.setPosition(50, screen_y-290);
    button_Y.setSize(button_size,button_size);
    
    // Function to send updated data to robot
    controlBot();
    
    }, 50);
    
    
