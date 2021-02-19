# import flask related
from flask import Flask, request, abort
# import linebot related
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

# import for database
import sqlite3

# create flask server
app = Flask(__name__)
# your linebot message API - Channel access token (from LINE Developer)
line_bot_api = LineBotApi('TID6M67HYlTYOEDZAtRF82nPS6qQb3eu+NKv5JWE35iq5O4cuYX3ad6+986rxEfQMDCIj2npOafm2BGITvUYB8UZWp+2dWDify7IyXoGjOsJWzJnlK69ATCGIFFe2EdVoPnUCI5ONasZ96h9QEuGHQdB04t89/1O/w1cDnyilFU=')
# your linebot message API - Channel secret
handler = WebhookHandler('e8de57a5bb8575f4440be45d44399d75')

# connect to database
connect = sqlite3.connect('user_msg_history.db', check_same_thread=False)
cursor = connect.cursor()

cursor.execute("CREATE TABLE log \
               (id integer primary key, \
                name varchar(20), \
                user_id text,\
                msg text)")
connect.commit()

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        print('receive msg')
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# handle msg
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user info & message
    user_id = event.source.user_id
    msg = event.message.text
    user_name = line_bot_api.get_profile(user_id).display_name
    
    # fetch log & save to text
    if msg == 'show'+user_name+'text history':
        logs = cursor.execute("SELECT * FROM log")
        log_text = ''
        for log in logs:
            log_text = log_text + '\n' + str(log)
        line_bot_api.reply_message(event.reply_token, 
                                   TextSendMessage(text = log_text))
    else:
        # save into database
        cursor.execute("INSERT INTO log (name, user_id, msg) \
                           VALUES (?, ?, ?)", (user_name, user_id, msg))
        connect.commit()
        line_bot_api.reply_message(event.reply_token, 
                                   TextSendMessage(text = 'message received！'))

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)