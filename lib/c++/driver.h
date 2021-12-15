#ifndef DRIVER_H
#define DRIVER_H

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/time.h>
#include <linux/i2c-dev.h>
#include <sys/ioctl.h>
#include <fstream>
#include <iostream>

#define delay(value) usleep(value*1000)

#define lowLevelI2Cread(buffer, length){\
    opResult = write(i2c_file, buffer, 1);\
    if(opResult != 1){\
        printf("No ACK bit...");\
        exit(2);\
    }\
    read(i2c_file, buffer, length);\
} 

#define lowLevelI2Cwrite(buffer, length){\
    write(i2c_file, buffer, length+1);\
} 

#define VERSION              0x00
#define MANUFACTURER         0x01
#define DEVICE_ID            0x02
#define COMMAND              0x03
#define A0_LOW_BYTE          0x04
#define A0_HIGH_BYTE         0x05
#define A1_LOW_BYTE          0x06
#define A1_HIGH_BYTE         0x07
#define A2_LOW_BYTE          0x08
#define A2_HIGH_BYTE         0x09
#define A3_LOW_BYTE          0x0A
#define A3_HIGH_BYTE         0x0B
#define A4_LOW_BYTE          0x0C
#define A4_HIGH_BYTE         0x0D
#define A5_LOW_BYTE          0x0E
#define A5_HIGH_BYTE         0x0F
#define A6_LOW_BYTE          0x10
#define A6_HIGH_BYTE         0x11
#define A7_LOW_BYTE          0x12
#define A7_HIGH_BYTE         0x13
#define DIGITAL_INPUT        0x14
#define DIGITAL_TRISTATE     0x15
#define DIGITAL_OUTPUT       0x16
#define SERVO_ENABLE         0x17
#define SERVO_0_TARGET       0x18
#define SERVO_1_TARGET       0x19
#define SERVO_2_TARGET       0x1A
#define SERVO_3_TARGET       0x1B
#define MOTOR_0_MODE         0x1C
#define MOTOR_0_SPEED        0x1D
#define MOTOR_1_SPEED        0x1E
#define MOTOR_1_MODE         0x1F
#define I2C_MODE             0x20
#define I2C_ADDR             0x21
#define I2C_REGISTER         0x22
#define I2C_LENGTH           0x23
#define I2C_B0               0x24
#define I2C_B1               0x25
#define I2C_B2               0x26
#define I2C_B3               0x27
#define I2C_B4               0x28
#define I2C_B5               0x29
#define I2C_B6               0x2A
#define I2C_B7               0x2B
#define I2C_B8               0x2C
#define I2C_B9               0x2D
#define I2C_B10              0x2E
#define I2C_B11              0x2F
#define I2C_B12              0x30
#define I2C_B13              0x31
#define I2C_B14              0x32
#define I2C_B15              0x33
#define I2C_B16              0x34
#define I2C_B17              0x35
#define I2C_B18              0x36
#define I2C_B19              0x37
#define I2C_B20              0x38
#define I2C_B21              0x39
#define I2C_B22              0x3A
#define I2C_B23              0x3B
#define I2C_B24              0x3C
#define I2C_B25              0x3D
#define I2C_B26              0x3E
#define I2C_FLAG             0x3F
#define BATT_LOW             0x40
#define BATT_HIGH            0x41

#define S0      0x01
#define S1      0x02
#define S2      0x04 
#define S3      0x08  

#define M0      0x01 
#define M1      0x02

#define INPUT   0
#define OUTPUT  1

#define BLUE    0 
#define YELLOW  1
#define ON      1
#define OFF     0 

enum{
    D0,
    D1,
    D2,
    D3,
    D4,
    D5,
    D6,
    D7,
    A0,
    A1,
    A2,
    A3,
    A4,
    A5,
    A6,
    A7
};

class SpartanPi_driver{
    public:
        SpartanPi_driver(void);
        ~SpartanPi_driver(void);
        void setLED(int, int);
        int analogRead(int);
        int digitalRead(int);
        void pinMode(int, int);
        void digitalWrite(int, int);
        void servoEnable(int, int);
        void servoTarget(int, int);
        void motorMode(int, int);
        void motorSpeed(int, int);
        void i2cRead(unsigned char, unsigned char, unsigned char, unsigned char*);
        void i2cWrite(unsigned char, unsigned char, unsigned char, unsigned char*);
    
    private:
        int i2c_file;
        int i2c_addr;
        unsigned char i2c_buf[32];
        int opResult;
};

#endif /* DRIVER_H */