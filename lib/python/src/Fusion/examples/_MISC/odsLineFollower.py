import Fusion

# Build driver object for the Fusion controller
f = Fusion.driver()

# Build an instance of "ods" for the left and right sensors
left_ods = Fusion.ods(f, f.A0)
right_ods = Fusion.ods(f, f.A1)

# Initialize variables
left_upper_thresh = 0
left_lower_thresh = 0
right_upper_thresh = 0
right_lower_thresh = 0
upper_thresh = 0
mid_thresh  = 0 
lower_thresh = 0
left_speed = 0
right_speed = 0 
thresh_calc = 0
new_reading = 0 
mode = None 

# Adjust the forward speed and GAIN if necessary and at your own risk ---------
FORWARD_SPEED = 30      # Forward speed
GAIN = 0.25             # Rate at which turn adjustment is made based on sensor reading
NEGATIVE_OFFSET = 20    # Offset of sensor reading before adjustment occurs 

# -----------------------------------------------------------------------------
# Calculate threshold values and averages to determine color of line 

# Left ODS sensor 
left_upper_thresh = 0 
left_lower_thresh = 1023

for i in range(0, 500):
	f.motorSpeed(f.M1, -40)
	f.motorSpeed(f.M0, 0)
	new_reading = left_ods.read()
	if(new_reading > left_upper_thresh): left_upper_thresh = new_reading 
	if(new_reading < left_lower_thresh): left_lower_thresh = new_reading

for i in range(0, 500):
	f.motorSpeed(f.M1, 40)
	f.motorSpeed(f.M0, 0)
	new_reading = left_ods.read()
	if(new_reading > left_upper_thresh): left_upper_thresh = new_reading 
	if(new_reading < left_lower_thresh): left_lower_thresh = new_reading	
	
print "upper = " + str(left_upper_thresh)
print "lower = " + str(left_lower_thresh)

# Right ODS sensor ------------------------------------------------------------
right_upper_thresh = 0 
right_lower_thresh = 1023

for i in range(0, 500):
	f.motorSpeed(f.M0, -40)
	f.motorSpeed(f.M1, 0)
	new_reading = right_ods.read()
	if(new_reading > right_upper_thresh): right_upper_thresh = new_reading 
	if(new_reading < right_lower_thresh): right_lower_thresh = new_reading

for i in range(0, 500):
	f.motorSpeed(f.M0, 40)
	f.motorSpeed(f.M1, 0)
	new_reading = right_ods.read()
	if(new_reading > right_upper_thresh): right_upper_thresh = new_reading 
	if(new_reading < right_lower_thresh): right_lower_thresh = new_reading	
	
print "upper = " + str(right_upper_thresh)
print "lower = " + str(right_lower_thresh)

# Calculate averages and mid points -------------------------------------------
upper_thresh = (left_upper_thresh + right_upper_thresh) / 2 
lower_thresh = (left_lower_thresh + right_lower_thresh) / 2 
mid_thresh = (upper_thresh + lower_thresh) / 2 

# Determine if line is dark or light 
thresh_calc = (left_ods.read() + right_ods.read()) / 2 
if(thresh_calc >= mid_thresh): mode = "DARK_LINE"
else: mode = "LIGHT_LINE"

print mode 

if (mode == "DARK_LINE"):
	while True:
		right_speed = FORWARD_SPEED
		left_speed = FORWARD_SPEED 

		thresh_calc = (upper_thresh - NEGATIVE_OFFSET) - left_ods.read()
		if (thresh_calc < 0): thresh_calc = 0 
		thresh_calc = int(thresh_calc * GAIN)	
		left_speed -= thresh_calc 
		right_speed += thresh_calc 
		
		thresh_calc = (upper_thresh - NEGATIVE_OFFSET) - right_ods.read()
		if (thresh_calc < 0): thresh_calc = 0 
		thresh_calc = int(thresh_calc * GAIN)	
		left_speed += thresh_calc 
		right_speed -= thresh_calc 
        
        if(left_speed >= 100): left_speed = 100
        elif(left_speed <= -100): left_speed = -100
        
        if(right_speed >= 100): right_speed = 100 
        elif(right_speed <= -100): right_speed = -100
        
        f.motorSpeed(f.M0, -right_speed)
        f.motorSpeed(f.M1, -left_speed)
		
elif (mode == "LIGHT_LINE"):
    while True:
        right_speed = FORWARD_SPEED
        left_speed = FORWARD_SPEED 

        thresh_calc = left_ods.read() - (lower_thresh + NEGATIVE_OFFSET)
        if (thresh_calc < 0): thresh_calc = 0 
        thresh_calc = int(thresh_calc * GAIN)	
        left_speed -= thresh_calc 
        right_speed += thresh_calc 

        thresh_calc = right_ods.read() - (lower_thresh + NEGATIVE_OFFSET) 
        if (thresh_calc < 0): thresh_calc = 0 
        thresh_calc = int(thresh_calc * GAIN)	
        left_speed += thresh_calc 
        right_speed -= thresh_calc 
        
        if(left_speed >= 100): left_speed = 100
        elif(left_speed <= -100): left_speed = -100
        
        if(right_speed >= 100): right_speed = 100 
        elif(right_speed <= -100): right_speed = -100
        
        f.motorSpeed(f.M0, -right_speed)
        f.motorSpeed(f.M1, -left_speed)