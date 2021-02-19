# Linebot_using_Flask
### Environment
-   ngrok(allow people to connect to your web server)
-   Flask(a lightweight web framework, which is our web server in this practice)
-   Line for Business(register an account to create an official line bot for the practice)
### Ngrok
run ngrok.exe and type "ngrok http <your port>", then record the URL, which you will need when you create your own official line bot.

# 1.Hands-on Practice:create a basic line bot 
### Introduction
In this practice, I create a line bot that when people send message to the robot, the robot would reply the user's name, user's ID and the message that user send. 
### Demo
You could run hands-on practice1.py to see the demo. Before you run the code, replace line_bot_api, handler and port number as yours. 

I use <code>line_bot_api.reply_message()</code> to reply message to our line users. This function takes two variables, event token and the type of message object. In this practice, I use <code>TextSendMessage()</code> to reply messages.

### Code
![image](https://user-images.githubusercontent.com/32606310/108176818-68cad880-713d-11eb-9748-4fcd36c16c64.png)
### Line demo
![InkedIMG_6977_LI](https://user-images.githubusercontent.com/32606310/108203296-447ef400-715d-11eb-8a69-dea3c3d0383f.jpg)

# 2.Hands-on practice:create a line bot that reply different types of messages
### Introduction 
In this practice, I create a line bot that reponse with different kind of messages, such as image, sticker, and location.
### Demo
You could run hands-on practice2.py to see the demo. Before you run the code, replace line_bot_api, handler and port number as yours.

I use <code>line_bot_api.reply_message()</code> again, but input different object types :<code>StickerSendMessage(), ImageSendMessage(), LocationSendMessage()</code>. If the user doesn't type in correct command, the line bot would return "wrong command! plz type again" instead.

### Code
![image](https://user-images.githubusercontent.com/32606310/108203024-e7833e00-715c-11eb-8ef1-649c09eca003.png)
### Line demo
![IMG_6978](https://user-images.githubusercontent.com/32606310/108203229-27e2bc00-715d-11eb-942d-21253123ae39.PNG)
![IMG_6979](https://user-images.githubusercontent.com/32606310/108203236-29ac7f80-715d-11eb-8155-bb94fc322b9f.PNG)

# 3.Hands-on practice:create a line bot with a database
### Introduction
In this practice, I create a line bot that connect to a SOLite3 which store users' information and messages. When the user type 'show<user's name>text history', 
the line bot show all the user's text history. 
### Demo
You could run hands-on practice3.py to see the demo. Before you run the code, replace line_bot_api, handler and port number as yours.</br>

### Code 
-   create a database and a table called log in sqlite3</br>
![image](https://user-images.githubusercontent.com/32606310/108462395-802dd100-72b7-11eb-8da7-87424fb5cb45.png)</br>
-   query sqlite the user's text history</br>
![image](https://user-images.githubusercontent.com/32606310/108462440-93d93780-72b7-11eb-9124-213c43741c0b.png)</br>
-   insert user's text into sqlite3</br>
![image](https://user-images.githubusercontent.com/32606310/108462469-9e93cc80-72b7-11eb-975b-7ec61508ab86.png)</br>
### Line demo
![image](https://user-images.githubusercontent.com/32606310/108463787-fa5f5500-72b9-11eb-9f1a-65d1f71287da.png)
