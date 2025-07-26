"""This script listens for specific MAVLink messages from a Pixhawk 6C Mini and will log the data"""

from pymavlink import mavutil
import time

connection = mavutil.mavlink_connection('/dev/ttyUSB0', baud=57600)
connection.wait_heartbeat()
print("Heartbeat received from system (system_id: %d, component_id: %d)" % (connection.target_system, connection.target_component))

while True: 
    msg = connection.recv_match(blocking=True)
    if not msg:
        continue
    msg_type = msg.get_type()

    if msg_type == 'BATTERY_STATUS':
        voltage = msg.voltages[0] / 1000.0  # Convert from mV to V
        current = msg.current_battery / 100.0  # Convert from mA to A
        print(f"Battery Voltage: {voltage} V, Current: {current} A")
    
    if msg_type ==  'OPTICAL_FLOW':
        quality = msg.quality 
        if quality > 0: 
            optical_flow_vector = {
            "x_mps": msg.flow_comp_m_x,
            "y_mps": msg.flow_comp_m_y,   
        }
            print(f"Optical Flow: {optical_flow_vector} (quality={quality})")
        else: 
            print(f"Omitting optical flow data due to low quality (quality={quality})")

    if msg_type == 'WIND':
        wind_speed = msg.speed # from the wind sensor
        direction = getattr(msg, 'direction', None)
        if direction is None or direction == 0.0:
            print(f"Wind Speed: {wind_speed:.3f} m/s  (direction not reported)")
        else:
            print(f"Wind Speed: {wind_speed:.3f} m/s, Wind Direction: {direction:.1f}°")

