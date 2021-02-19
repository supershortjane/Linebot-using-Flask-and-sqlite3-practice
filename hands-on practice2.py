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
line_bot_api = LineBotApi('abc')
# your linebot message API - Channel secret
handler = WebhookHandler('123')

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
    
    #push msg
    #line_bot_api.push_message(user_id,TextSendMessage(text = 'hello ^^\nif you want robot to send a sticker, please type:\"send a sticker\"\nif you want robot to send an image, please type:\"send an image\"\nif you want robot to send a location, please tyoe \"send a location\"\n'))


    
    if msg =='send a sticker':
        line_bot_api.reply_message(event.reply_token, StickerSendMessage(package_id='4',sticker_id='626'))
    elif msg =='send an image':
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTB-tDV-rlYMdwD98TezbOsUdMMPwy670g2cw&usqp=CAU', 
                                                 preview_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTB-tDV-rlYMdwD98TezbOsUdMMPwy670g2cw&usqp=CAU'))
    elif msg =='send a location':
        line_bot_api.reply_message(event.reply_token, LocationSendMessage(title='City Location',
                            address='New York City',
                            latitude=40.730610,
                            longitude=-73.935242))
    else :
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text ='Wrong command! plz type again.'))
        

                            

    

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=12345)