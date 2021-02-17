# Linebot_using_Flask
### Environment
-   ngrok(allow people to connect to your web server)
-   Flask(a lightweight web framework, which is our web server in this practice)
-   Line for Business(register an account to create an official line bot for the practice)
### Ngrok
run ngrok.exe and type "ngrok http <your port>", then record the URL, which people could access.

# 1.Hands-on Practice:create a basic line bot 
### Introduction
In this practice, I want to create a line bot that when people send message to the robot, the robot would reply the user's name, user's ID and the message that user send. 
### Demo
You could run hands-on practice1.py to see the demo. Before you run the code, replace line_bot_api, handler and port number as yours. 

I use line_bot_api.reply_message to reply message to our line users. This function takes two variables, event token and the type of message object. In this practice, I use TextSendMessage() to reply messages.

### Code
![image](https://user-images.githubusercontent.com/32606310/108176818-68cad880-713d-11eb-9748-4fcd36c16c64.png)
### Line 
![InkedIMG_6977_LI](https://user-images.githubusercontent.com/32606310/108177181-db3bb880-713d-11eb-86a4-519d27dedfbd.jpg= 100x20)

# 2.Hands-on practice:create a line bot that reply different types of messages
### Introduction 

