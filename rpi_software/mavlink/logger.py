import csv
import time 
from mav_listener import initialize_mavlink_connection, update_mavlink_data, battery_current, battery_voltage,optical_flow_vector, optical_flow_quality, wind_speed, wind_direction

#setup log files
battery_log_file = open('battery_log.csv', 'w', newline='')
battery_log_writer = csv.writer(battery_log_file) # Create file for battery data
battery_log_writer.writerow(['timestamp', 'voltage_V', 'current_A'])

optical_flow_log_file = open('optical_flow_log.csv', 'w', newline='')
optical_flow_log_writer = csv.writer(optical_flow_log_file) # Create file for optical flow data
optical_flow_log_writer.writerow(['timestamp', 'x_mps', 'y_mps', 'quality'])

wind_log_file = open('wind_log.csv', 'w', newline='')
wind_log_writer = csv.writer(wind_log_file) # Create file for wind data
wind_log_writer.writerow(['timestamp', 'speed_mps', 'direction_deg'])

if not initialize_mavlink_connection():
    print("Failed to connect. Attempting to restart connection.")
    initialize_mavlink_connection()



try: 
    while True: 
        if update_mavlink_data():
            current_time = time.time()
            
            # Log battery data
            battery_log_writer.writerow([current_time, battery_voltage, battery_current])
            battery_log_file.flush()

            # Log optical flow data
            optical_flow_log_writer.writerow([current_time, optical_flow_vector['x_mps'], optical_flow_vector['y_mps'], optical_flow_quality])
            optical_flow_log_file.flush()

            # Log wind data
            if wind_direction is not None:
                wind_log_writer.writerow([current_time, wind_speed, wind_direction])
                wind_log_file.flush()
            else: 
                wind_log_writer.writerow([current_time, wind_speed, 'N/A'])
                wind_log_file.flush()

        time.sleep(0.1) # Adjust sample rate as needed
except KeyboardInterrupt: # Will not work when running on the drone 
    print("Logging stopped by user.")

finally:
    # close log files
    battery_log_file.close()
    optical_flow_log_file.close()
    wind_log_file.close()
