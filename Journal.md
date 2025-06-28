---
Title: "MORPHEUS: Morphing Optimization for Reliable Positional & High-Efficiency Urban Stability
"
Authors: "Ayden Yeung & Julian Givens"
Description: "MORPHEUS is a morphing drone with added control profiles to optmimize energy efficiency and positional accuracy in urban wind fields."
Created_at: "2024-05-19"
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

##5/30: Researched deep-learning frameworks, Pi5 to FC communication (MAVLink) - Ayden
Today I made a document that hosted all of my research regarding the pros and cons of using Tensorflow or PyTorch with the Hailo AI Hat and Raspberry Pi 5. I also looked into how MAVLink works and how to calibrate a Raspberry Pi to setup MAVLink (how the companion computer talks to the flight controller).

**Research displayed on Notion** 
![image](https://github.com/user-attachments/assets/f23a2226-5899-4b27-9c74-303a192435a4)
**Total Time Spent: 2.5 hrs**


##6/18: Researched about an additional problem that we could tackle with the drone. Today I fully went in depth into a seperate problem that could be solved via drone that might have a greater effect than our current idea - Ayden
![image](https://github.com/user-attachments/assets/741fb3e8-d7fd-47da-b4cd-06da72ca3934)
**Total Time Spent: 2.5 hrs**

##6/25 + 6/26: Project Development - Ayden and Julian
On 6/25 we came up with another project idea seperate from the original LitterLift idea that we previously believed was the route we would take. The project we developed involved more of a physics and control theory sided background — something that we were interested in doing. The project is about optimizing quadcopter efficiency in urban wind fields. 
On 6/26 we found and annotated 8 documents, putting all important research into a categorized summary document on notion. We also decided that this concept is what we'd pursue. 
![image](https://github.com/user-attachments/assets/489aff67-a534-4476-a4d4-038347b20c00)
![image](https://github.com/user-attachments/assets/f26ee369-59a0-4ac1-8583-4f17e7f4ba36)
![image](https://github.com/user-attachments/assets/08aec18f-4fb1-46d2-8f18-1e124b2e6b18)

**Total Time Spent: 6.0 hrs (3hrs each)**


##6/27: Reviewed literature on variable hedral angle quadrotors and relevant control systems - Ayden and Julian
On 6/27 we reviewed 10+ journal articles relating to the project and began assembling a plan for both the hardware and software systems. On the software side of the equation, we want to incorporate a nonlinear control paradigm augmented by a reinforcement learning model to determine the PID or LQR gains. Below is an image of the paper we used to plan out the hardware and software routes.

![image](https://github.com/user-attachments/assets/bb2f08d9-3b2f-4bf6-8535-09b24114bcde)
![image](https://github.com/user-attachments/assets/f16aec4e-f869-43d0-824e-5a2c856643e7)

**Total Time Spent: 8.0 hrs (4hrs each)**







