---
Title: "Morphing Optimization for Reliable Positional & High-Efficiency Urban Stability
"
Authors: "Ayden Yeung & Julian Givens"
Description: "MORPHEUS is a morphing drone with added control profiles to optimize energy efficiency and positional accuracy in urban wind fields."
Created_at: "2025-05-19"
---
# Journal
---
## 5/19: Set up Notion HQ databases and layout - Julian
Set up the project on Notion page, sharing permissions with Ayden, and linking important documents to the main page. Additionally, I created a work log system to easily track the tasks we're completing. <br>
  
![image](https://github.com/user-attachments/assets/bcc27273-6479-48bc-817e-c12e02824908)

**Total Time Spent: 1.5hrs**

## 5/24: Set up Notion BOM Page and Drafted BOM - Julian and Ayden
Met up in real life to create the Notion BOM page and draft a full BOM for our drone. We also used some time to fully decide on an area of focus (environmental improvement). We researched viable battery, motor, and flight controller + ESC stacks to pick the best combination of electronics for our desired design. Julian and I also did research into what computing unit we wanted to use for the autonomous functions of the drone, ultimately deciding on the Hailo 8 AI Hat + Raspberry Pi 5 over the Jetson Nano for budgetary reasons. We used websites like oscarliang.com and other FPV sites to get recommmendations for the best electronics to buy for power effeciency, companion computer features, and wiring complexity while staying within a reasonable budget. <br>
  
![image](https://github.com/user-attachments/assets/f8332c23-232a-4827-9f6f-a445b897ec04)

**Total Time Spent: 6.0hrs**

## 5/26: Set up a notion page to host our lucidchart diagrams and started wiring diagram - Ayden
I signed up for lucidchart and created a Notion page to host our lucidchart digarams with the intent that we would be using lucidchart for our software control flow diagrams in the near future. Additionally, I started working on the wiring diagram, where I mainly imported the image files of the parts I needed to include. I also set up a NoodleTools research project to centralize our research and simplify APA exporting. <br>
  
![image](https://github.com/user-attachments/assets/2b2ff783-bfac-4b30-86c8-3fb526b9dff8)

**Total Time Spent: 2.0hrs** 

## 5/27: Worked on wiring diagram and CAD - Julian and Ayden
Julian and I met today on discord to work on the wiring diagram and frame CAD. Julian has made good progress with the master sketch and drone arm CAD while I have almost finished the wiring diagram, only missing UART connections to the Receiver, Raspberry Pi 5, and M10 MicroGPS from the Flight Controller. Tomorrow we're hoping to finish the wiring diagram and continue to make CAD progress. <br> <br>
**Drone Mastersketch:** <br>
![image](https://github.com/user-attachments/assets/78a16c5b-f493-4009-92b4-9d04a8f31372)

**Arm CAD:** <br>
![image](https://github.com/user-attachments/assets/bf1c2c0f-cb86-446f-b1c6-5c3f4d4c48a6)

**Drone Assembly:** <br>
![image](https://github.com/user-attachments/assets/a1fd2f09-0d0a-4291-85b2-b7d987f49777)


**Wiring Diagram:** <br>
![image](https://github.com/user-attachments/assets/18386f03-e15f-458b-aab5-1327f84b7e1d)

**Total Time Spent: 3.0hrs**

## 5/28: Finished wiring diagram and re-designed the CAD of the drone – Julian and Ayden

After I quickly finished the wiring diagram, Julian designed the Pi Camera Mounting System, developing two different versions. Additionally, we decided that a redesign of the drone's frame was in order, as the Lipo Batteries would not fit on the bottom stage of the central hub. Julian changed the master sketch to fix the issue. I also spent a lot of time transferring our Notion worklog to a GitHub Journal. Tomorrow, we're hoping to continue progressing on the CAD and start researching what Python libraries we are going to have to learn for the project.

**Updated Mastersketch:**

![image](https://github.com/user-attachments/assets/5a09b185-13ca-4e61-a7e9-ab6396974a58)

**Pi Camera V3 and AI Cam Mount V1:**

![image](https://github.com/user-attachments/assets/b1cc1e76-17ee-436b-88e1-7b657a71e642)
![image](https://github.com/user-attachments/assets/2e0a0332-95b8-40de-b62a-8a1711e71561)

**Pi Camera V3 and AI Cam Mount V2:**

![image](https://github.com/user-attachments/assets/3329a653-6627-427b-97a8-218b63c7b37d)
![image](https://github.com/user-attachments/assets/5fe61f07-8166-4c33-b776-d956aba4d108)

**Updated Drone Assembly:**

![image](https://github.com/user-attachments/assets/1ea29ddd-511a-433b-8a9e-70f3a99f9837)

**Total Time Spent: 3.0 hrs**

## 5/30: Researched deep-learning frameworks, Pi5 to FC communication (MAVLink) - Ayden
Today I made a document that hosted all of my research regarding the pros and cons of using Tensorflow or PyTorch with the Hailo AI Hat and Raspberry Pi 5. I also looked into how MAVLink works and how to calibrate a Raspberry Pi to setup MAVLink (how the companion computer talks to the flight controller).

**Research displayed on Notion** 
![image](https://github.com/user-attachments/assets/f23a2226-5899-4b27-9c74-303a192435a4)
**Total Time Spent: 2.5 hrs**


## 6/18: Researched about an additional problem that we could tackle with the drone. Today I fully went in depth into a seperate problem that could be solved via drone that might have a greater effect than our current idea - Ayden
![image](https://github.com/user-attachments/assets/741fb3e8-d7fd-47da-b4cd-06da72ca3934)
**Total Time Spent: 2.5 hrs**

## 6/25 + 6/26: Project Development - Ayden and Julian
On 6/25 we came up with another project idea seperate from the original LitterLift idea that we previously believed was the route we would take. The project we developed involved more of a physics and control theory sided background — something that we were interested in doing. The project is about optimizing quadcopter efficiency in urban wind fields. 
On 6/26 we found and annotated 8 documents, putting all important research into a categorized summary document on notion. We also decided that this concept is what we'd pursue. 
![image](https://github.com/user-attachments/assets/489aff67-a534-4476-a4d4-038347b20c00)
![image](https://github.com/user-attachments/assets/f26ee369-59a0-4ac1-8583-4f17e7f4ba36)
![image](https://github.com/user-attachments/assets/08aec18f-4fb1-46d2-8f18-1e124b2e6b18)

**Total Time Spent: 7.0 hrs (3.5hrs each)**


## 6/27: Reviewed literature on variable hedral angle quadrotors and relevant control systems - Ayden and Julian
On 6/27 we reviewed 10+ journal articles relating to the project and began assembling a plan for both the hardware and software systems. On the software side of the equation, we discussed incorporating a nonlinear control paradigm augmented by a reinforcement learning model to determine the PID or LQR gains. Below is an image of the paper we used to plan out the hardware and software routes.

![image](https://github.com/user-attachments/assets/bb2f08d9-3b2f-4bf6-8535-09b24114bcde)
![image](https://github.com/user-attachments/assets/f16aec4e-f869-43d0-824e-5a2c856643e7)

**Total Time Spent: 6.0 hrs (3hrs each)**

## 6/30: Continued reading 2 research papers while drafting a control flow diagram - Ayden and Julian
Julian read and annotated 2 more research paperand added all relevant infromation to the categorized summary document on Notion. I (Ayden) started to mock up a sample black box model for the drone. 
<img width="1846" height="684" alt="image" src="https://github.com/user-attachments/assets/4a93be68-c0ec-4733-9905-8cea5b4a53c8" />

**Total Time Spent: 2.0 hrs (1.0hrs each) 

## 7/3: Finished a draft of the control flow diagram - Ayden 
The changes made were that I filled in the Raspberry Pi box with what I think is to be the ideal parallel-cascade controller. I made some research notes to provide some justification on the general structure of the controller. Lastly, I researched a potential servo option (Dynamixel XL330-M288T) for the differential arm system. </br<
Control Flow Diagram: 
<img width="1790" height="657" alt="image" src="https://github.com/user-attachments/assets/96772fc9-c86a-4ba4-b5a2-d35e9a70fe72" />

Research notes on Dynamixel and Electronics: 
<img width="2142" height="1130" alt="image" src="https://github.com/user-attachments/assets/91bde729-061e-4459-831b-1021042f1544" />

Research notes on control architecture:
<img width="2233" height="1111" alt="image" src="https://github.com/user-attachments/assets/115a7e6d-c3d2-434a-bcd1-fcab03f9c9a0" />

**Total Time Spent: 2.5 hrs**

## 7/12: Re-edited BOM, Wiring Schematic, and Control Flow - Ayden 
- Returned from vacation (gone since 7/3)'
I removed parts specific to the LitterDrone project idea and replaced them with parts that we would need for the gust rejection drone. The list of parts included the Dynamixel XL330-M288T, and the Pixhawk 6C Mini. Additionally, I edited the wiring schematic to match this new configuration, updating it from the previous LitterDrone oriented configuration. Finally, I made small bug fixes to the control flow diagram as there was a mistake.</br>
BOM:
<img width="1274" height="871" alt="image" src="https://github.com/user-attachments/assets/ceea40ac-f63a-4855-96a9-6a4cb1c3e53c" />

Wiring Schematic:
<img width="1559" height="928" alt="image" src="https://github.com/user-attachments/assets/551c3939-b4e3-4013-b955-84e106e913e1" />

Control Flow Diagram:
<img width="1447" height="475" alt="image" src="https://github.com/user-attachments/assets/328f19a7-4e8b-4299-92a3-df778678a261" />

**Total Time Spent: 4.0 hrs** 

## 7/13: Added the wind sensor subsystem to the BOM and wiring schematic - Ayden
I did some research on types of wind sensors and what would be better for specific tests. I considered a variety of factors including cost, effectiveness indoors with turbulent wind, outdoor resistance, durability, etc. I found that the type of sensor that matched our budget (I excluded ultrasonic anemometers) would be the hot wire anemometer. I ultimately picked this over the pitot tube due to physical constraints, effectiveness with the type of gusts we were studying, and overall testing environment. After this, I researched potential options for a hot wire anemometer, eventually coming across Modern Device's Rev P. I liked this product because it wasn't super large, and detects winds up to 150 mph with reasonable accuracy. Unfortunately since it was made to work with Arduino and needs 12V, I had to add a BEC and voltage step up converter. I also replaced the GPS with an optical flow sensor because I believe that our testing will be indoors (in GPS limited areas). </br>
Updated BOM:
<img width="1575" height="861" alt="image" src="https://github.com/user-attachments/assets/3492e350-56cf-4e5f-96e3-8adf70a0419d" />

Updated Wiring Schematic:
<img width="1244" height="845" alt="image" src="https://github.com/user-attachments/assets/c4ecdc4a-d734-4cb8-9c49-86ba786ff372" />

Research on Wind Sensors: 
<img width="1776" height="1113" alt="image" src="https://github.com/user-attachments/assets/3af0f59b-69e4-4f12-b133-6098563acb37" />

**Total Time Spent: 4.0 hrs**

## 7/18: Made a research breakdown, discussed differential arm options, and installed MATLAB - Ayden and Julian
We got together to discuss our full research question, and hypothesis. We also discussed materials and cost for prototyping our differential arm design. Finally, we obtained a MATLAB license and installed the application. We are going to order the parts needed from McMaster-Carr
- Our next steps seem to be learning MATLAB and prototyping the differential arm, which would lead into finishing the drone frame

CAD: 
<img width="1502" height="895" alt="image" src="https://github.com/user-attachments/assets/a6b962e7-76a4-4a39-8eb5-e37284f1c2e3" />
Section View: 
<img width="1335" height="547" alt="image" src="https://github.com/user-attachments/assets/4ccd7e62-b37b-44b5-9352-6da800fc5907" />
Research Breakdown:
<img width="1694" height="772" alt="image" src="https://github.com/user-attachments/assets/1f1b52f1-0815-4931-8dcf-82c834d046f9" />

**Total Time Spent: 4.0 hrs (2.0 hrs each)**

## 7/24: Matlab introduction, researched compute resource allocation with current hardware - Ayden
Our main goal, which has taken significant time away from actually working on the done is learning MATLAB (and after that learning the math for control theory). Additionally, I have been putting about 30 minutes a day into learning C++ in the event we use it when editing the Ardupilot software for our testing routines. Today, I mainly worked on doing research on how to computing power should be allocated, and how I can log certain data points. I found that the Raspberry Pi 5 (Linux) has a hard time with real-time processes (control loops) which is not ideal since I planned to use it for running the parallel-cascade controller. Thankfully, the Pixhawk 6C Mini has an STM microcontroller that can run the control loops, while the Raspberry Pi does the logging, and RL morphing. I also started doing a little bit of code for the logging and MAVLink portion of the drone. 

<img width="2108" height="721" alt="image" src="https://github.com/user-attachments/assets/db7b929c-c759-4ddf-a532-a8cb84e98cda" />
<img width="1757" height="573" alt="image" src="https://github.com/user-attachments/assets/051fc577-2b94-4a6f-8c0c-91d5296b700f" />

**Total Time Spent: 2.5 hrs** 

## 7/25 + 7/26: Learned mavlink, re-learned csv, and developed mav_listener.py and logger.py files - Ayden
Today I worked on learning and developing the logic to read sensor data from the Pixhawk (which is running ardupilot) on the Raspberry Pi via Mavlink. To do this, I created a listener file that reads the output of the Pixhawk and "listens" for messages that include the sensor data, updating the corresponding variables. I developed this structure by defining functiosn that are called in logger.py to initalize the mavlink connection, and update the data. The logger.py file saves the respective sensor outputs in seperate CSV files. 
Excerpt of mav_listener.py 
<img width="1569" height="1044" alt="image" src="https://github.com/user-attachments/assets/57fed9da-3611-4a52-8cc7-63c7d3ca8f1e" />

Excerpt of logger.py
<img width="1704" height="1153" alt="image" src="https://github.com/user-attachments/assets/0efa5469-42bc-432c-a736-157dceb67db5" />

**Total Time Spent: 3.0 hrs**








