#include "driver.h"
using namespace std;

ofstream o;

SpartanPi_driver::SpartanPi_driver(void){
    i2c_addr = 0x08;
    opResult = 0;
    i2c_file = open("/dev/i2c-1", O_RDWR);
    if(i2c_file < 0){
        printf("Failed to open the I2C bus...");
        exit(1);
    }
    
    if(ioctl(i2c_file, I2C_SLAVE, i2c_addr) < 0){
        printf("Failed to acquire bus and/or talk to slave device...");
        exit(1);
    }  
    
    o.open("/sys/class/gpio/export");
    if(o < 0) printf("error 1");        
    o << "17";
    o.close();
    
    o.open("/sys/class/gpio/export");
    if(o < 0) printf("error 2");
    o << "18";
    o.close();

    delay(50);
    
}

SpartanPi_driver::~SpartanPi_driver(void){
    o.open("/sys/class/gpio/gpio17/direction");
    if(o < 0) printf("error 11");
    o << "low";
    o.close();
    
    o.open("/sys/class/gpio/gpio18/direction");
    if(o < 0) printf("error 12");
    o << "low";
    o.close();
    
    o.open("/sys/class/gpio/unexport");
    if(o < 0) printf("error 13");
    o << "17";
    o.close();
    
    o.open("/sys/class/gpio/unexport");
    if(o < 0) printf("error 14");
    o << "18";
    o.close();
    printf("something");
}

void SpartanPi_driver::setLED(int led, int value){
    
    if(led == YELLOW){
        if(value == 1){
            o.open("/sys/class/gpio/gpio17/direction");
            if(o < 0) printf("error 21");
            o << "high";
            o.close();
        }
        else{
            o.open("/sys/class/gpio/gpio17/direction");
            if(o < 0) printf("error 22");
            o << "low";
            o.close();
        }
    }
    else{
        if(value == 1){
            o.open("/sys/class/gpio/gpio18/direction");
            if(o < 0) printf("error 23");
            o << "high";
            o.close();
        }
        else{
            o.open("/sys/class/gpio/gpio18/direction");
            if(o < 0) printf("error 24");
            o << "low";
            o.close();
        }
    }
}

int SpartanPi_driver::analogRead(int port){
    if(port >= A0 && port <= A7){
        i2c_buf[0] = ((port-8) * 2) + A0_LOW_BYTE;
        lowLevelI2Cread(i2c_buf, 2);
        return((i2c_buf[1] << 8) | i2c_buf[0]);
    }
    else{
        return 0x03FF;
    }
}

int SpartanPi_driver::digitalRead(int port){
    unsigned char port_mask;
    if(port >= D0 && port <= D7){
        port_mask = 1 << port;
        i2c_buf[0] = DIGITAL_INPUT;
        lowLevelI2Cread(i2c_buf, 1);
        if(i2c_buf[0] & port_mask) return 1;
        else return 0;
    }
}

void SpartanPi_driver::pinMode(int port, int state){
    unsigned char temp_data;
    if(port >= D0 && port <= D7){
        i2c_buf[0] = DIGITAL_TRISTATE;
        lowLevelI2Cread(i2c_buf, 1);
        temp_data = i2c_buf[0];
        if(state == 1) temp_data |= (1<<port);
        else temp_data &= ~(1<<port);
        i2c_buf[0] = DIGITAL_TRISTATE;
        i2c_buf[1] = temp_data;
        lowLevelI2Cwrite(i2c_buf, 1);
    }
    return;
}

void SpartanPi_driver::digitalWrite(int port, int state){
    unsigned char temp_data;
    if(port >= D0 && port <= D7){
        i2c_buf[0] = DIGITAL_OUTPUT;
        lowLevelI2Cread(i2c_buf, 1);
        temp_data = i2c_buf[0];
        if(state == 1) temp_data |= (1<<port);
        else temp_data &= ~(1<<port);
        i2c_buf[0] = DIGITAL_OUTPUT;
        i2c_buf[1] = temp_data;
        lowLevelI2Cwrite(i2c_buf, 1);
    }
    return;
}

void SpartanPi_driver::servoEnable(int servo, int state){
    unsigned char temp_data;
    if(servo >= S0 && servo <= S3){
        i2c_buf[0] = SERVO_ENABLE;
        lowLevelI2Cread(i2c_buf, 1);
        temp_data = i2c_buf[0];
        if(state == 1) temp_data |= (1<<servo);
        else temp_data &= ~(1<<servo);
        i2c_buf[0] = SERVO_ENABLE;
        i2c_buf[1] = temp_data;
        lowLevelI2Cwrite(i2c_buf, 1);
    }
    return;
}

void SpartanPi_driver::servoTarget(int servo, int target){
    if(servo & S0 == S0){
            i2c_buf[0] = SERVO_0_TARGET;
            i2c_buf[1] = target;
            lowLevelI2Cwrite(i2c_buf, 1);
    }
    if(servo & S1 == S1){
            i2c_buf[0] = SERVO_1_TARGET;
            i2c_buf[1] = target;
            lowLevelI2Cwrite(i2c_buf, 1);
    }
    if(servo & S2 == S2){
            i2c_buf[0] = SERVO_2_TARGET;
            i2c_buf[1] = target;
            lowLevelI2Cwrite(i2c_buf, 1);
    }
    if(servo & S3 == S3){
            i2c_buf[0] = SERVO_3_TARGET;
            i2c_buf[1] = target;
            lowLevelI2Cwrite(i2c_buf, 1);
    }
    return;
}

void SpartanPi_driver::motorMode(int motor, int mode){
    if(motor & M0 == M0){
        i2c_buf[0] = MOTOR_0_MODE;
        i2c_buf[1] = mode;
        lowLevelI2Cwrite(i2c_buf, 1);
    }
    if(motor & M1 == M1){
        i2c_buf[0] = MOTOR_1_MODE;
        i2c_buf[1] = mode;
        lowLevelI2Cwrite(i2c_buf, 1);
    }
}

void SpartanPi_driver::motorSpeed(int motor, int speed){
    if(motor & M0 == M0){
        i2c_buf[0] = MOTOR_0_SPEED;
        i2c_buf[1] = speed;
        lowLevelI2Cwrite(i2c_buf, 1);
    }
    if(motor & M1 == M1){
        i2c_buf[0] = MOTOR_1_SPEED;
        i2c_buf[1] = speed;
        lowLevelI2Cwrite(i2c_buf, 1);
    }
}

void SpartanPi_driver::i2cRead(unsigned char i2c_addr, unsigned char reg, unsigned char len, unsigned char *buffer){
    unsigned char temp_data = 0xFF;
    unsigned int i;
    while (temp_data == 0xFF){
        i2c_buf[0] = I2C_FLAG;
        lowLevelI2Cread(i2c_buf, 1);
        temp_data = i2c_buf[0];
    }
    delay(1);
    
    i2c_buf[0] = I2C_MODE;
    i2c_buf[1] = 0x80;
    i2c_buf[2] = i2c_addr;
    i2c_buf[3] = reg;
    i2c_buf[4] = len;
    lowLevelI2Cwrite(i2c_buf, 4);
    
    i2c_buf[0] = I2C_FLAG;
    i2c_buf[1] = 0xFF;
    lowLevelI2Cwrite(i2c_buf, 1);
    
    temp_data = 0xFF;
    while (temp_data == 0xFF){
        i2c_buf[0] = I2C_FLAG;
        lowLevelI2Cread(i2c_buf, 1);
        temp_data = i2c_buf[0];
    }
    delay(1);
    
    i2c_buf[0] = I2C_B0;
    lowLevelI2Cread(i2c_buf, len);
    
    for (i=0; i<len; i++){
        buffer[i] = i2c_buf[i];
    }
    return;
}

void SpartanPi_driver::i2cWrite(unsigned char i2c_addr, unsigned char reg, unsigned char len, unsigned char *buffer){
    unsigned char temp_data = 0xFF;
    unsigned int i;
        
    while (temp_data == 0xFF){
        i2c_buf[0] = I2C_FLAG;
        lowLevelI2Cread(i2c_buf, 1);
        temp_data = i2c_buf[0];
    }
    
    i2c_buf[0] = I2C_MODE;
    i2c_buf[1] = 0x00;
    i2c_buf[2] = i2c_addr;
    i2c_buf[3] = reg;
    i2c_buf[4] = len;
    
    for (i=0; i<len; i++){
        i2c_buf[i+5] = buffer[i];
    }    
    lowLevelI2Cwrite(i2c_buf, len+4);
    
    i2c_buf[0] = I2C_FLAG;
    i2c_buf[1] = 0xFF;
    lowLevelI2Cwrite(i2c_buf, 1);
    
    temp_data = 0xFF;
    while (temp_data == 0xFF){
        i2c_buf[0] = I2C_FLAG;
        lowLevelI2Cread(i2c_buf, 1);
        temp_data = i2c_buf[0];
    }
    
    return;
}