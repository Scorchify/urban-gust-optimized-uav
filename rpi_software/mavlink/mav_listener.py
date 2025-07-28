""" the mav_listener.py file is used to listen to mavlink messages from the drone and save sensor data from the INA219, the PMW3901, and the Rev P. """
from pymavlink import mavutil
import csv

import time 

# Initialize variables to store data 
battery_current = 0.0
battery_voltage = 0.0
optical_flow_vector = {"x_mps": 0.0, "y_mps": 0.0}
optical_flow_quality = 0
wind_speed = 0.0
wind_direction = None

# Initalize internal variables 
_connection = None 
_last_heartbeat_time = 0 

def initialize_mavlink_connection(port = '/dev/ttyUSB0', baud=57600): 
    global _connection, _last_heartbeat_time
    try: 
        _connection = mavutil.mavlink_connection(port, baud=baud)
        print(f"Waiting for heartbeat from {port}...")
        _connection.wait_heartbeat()
        print("Heartbeat received from system (system_id: %d, component_id: %d)" % \
                (_connection.target_system, _connection.target_component))
        _last_heartbeat_time = time.time()
        return True
    except Exception as e:
        print(f"Failed to initialize MAVLink connection: {e}")
        _connection = None
        return False 
    
def update_mavlink_data(wait_time=5): 
    global battery_current, battery_voltage, optical_flow_vector, optical_flow_quality, wind_speed, wind_direction
    global _connection, _last_heartbeat_time

    if _connection is None or (time.time() - _last_heartbeat_time > wait_time): # Give wait_time seconds to receive a heartbeat
        # Attempt to re-initialize connection if it was lost or not established
            print("Attempting to re-initialize MAVLink connection...")
            if not initialize_mavlink_connection():
                return False # Still no connection
    try:
        msg = _connection.recv_match(blocking=False, timeout=0.01) # Non-blocking read (block - pause) 

        if msg:
            msg_type = msg.get_type()

            if msg_type == 'HEARTBEAT':
                _last_heartbeat_time = time.time() # Keep track of last heartbeat

            elif msg_type == 'BATTERY_STATUS':
                battery_voltage = msg.voltages[0] / 1000.0
                battery_current = msg.current_battery / 100.0

            elif msg_type == 'OPTICAL_FLOW':
                if msg.quality > 0:
                    optical_flow_vector = {
                        "x_mps": msg.flow_comp_m_x,
                        "y_mps": msg.flow_comp_m_y
                    }
                    optical_flow_quality = msg.quality
                else: 
                    optical_flow_vector = {"x_mps": 0.0, "y_mps": 0.0}
                    optical_flow_quality = 0.0

            elif msg_type == 'WIND':
                wind_speed = msg.speed
                wind_direction = getattr(msg, 'direction', None)
            return True # Successfully read a message
        else:
            return True

    except Exception as e:
        print(f"Error reading MAVLink message: {e}")
        _connection = None # Mark as disconnected
        return False # No message or an error occurred

def close_mavlink_connection():
    global _connection
    if _connection:
        _connection.close()
        print("MAVLink connection closed.")
    _connection = None


