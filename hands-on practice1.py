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
    MessageEvent, TextMessage, TextSendMessage,
    LocationSendMessage, ImageSendMessage, StickerSendMessage
)

# create flask server
app = Flask(__name__)
# your linebot message API - Channel access token (from LINE Developer)
line_bot_api = LineBotApi('TID6M67HYlTYOEDZAtRF82nPS6qQb3eu+NKv5JWE35iq5O4cuYX3ad6+986rxEfQMDCIj2npOafm2BGITvUYB8UZWp+2dWDify7IyXoGjOsJWzJnlK69ATCGIFFe2EdVoPnUCI5ONasZ96h9QEuGHQdB04t89/1O/w1cDnyilFU=')
# your linebot message API - Channel secret
handler = WebhookHandler('e8de57a5bb8575f4440be45d44399d75')

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
    
    # get msg details
    print('msg from [', user_name, '](', user_id, ') : ', msg)
    
    line_bot_api.reply_message(event.reply_token, 
                               [TextSendMessage(text ='your user\'s name: '+ user_name),
                                TextSendMessage(text ='your user\'s ID: '+ user_id),
                                TextSendMessage(text ='your message: '+ msg)])

    

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)