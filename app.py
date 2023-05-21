# 統合版  鸚鵡機器人
#################################### line-bot-sdk 
#載入flask模Fsk,eques,abort
from flask import Flask, request, abort     # Flask, request, abort
                                            #

#載入linebot模組中的LineBotApi(Linee),Wbookderiece
from linebot import (
    LineBotApi,WebhookHandler
)

#載入1inebot.exceptis模中的Invalidigatureerror(錯偵錯)
from linebot.exceptions import (
    InvalidSignatureError
)

# 載入1inebot.models模組中的essageEventTextesageTextSeessage
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
#################################### line-bot-sdk ///////

#################################### python 環境 
# 載入jso模組(格式化輸出結果)
import json

#################################### python 環境 /////////


#建立application物件
app = Flask(__name__)

#放入自己的LINEBOTChanel AccessToken
#line_bot_api = LineBotApi("CHANNEL_ACCESS_TOKEN" )
line_bot_api = LineBotApi("S2b3Gs/ThNvATsC8wLD/k8Gh+fDmLqwwXsIMoUgKcB8fipzb+I/Uasnj3L5K9m58g5kCQvNSeWEXU1NZWEEV44tmhe1vAj5Dl5Tn83g2gOLXKpv6h5PtWgU+J5bjGwUW7vR2HmXK8xll/xJ9EcqbPAdB04t89/1O/w1cDnyilFU=" )

#放入自己的LINEBTCelSecret
#handler = WebhookHandler("CHANNEL_SECRET" )
handler = WebhookHandler("b9ec8063810d87c112557bfcf5007455" )


#Webhook 入口  ，監聽所有來自/calbackstRqs
@app.route("/callback", methods=['POST'])  #https://b40e-2001-288-5630-0-5d12-7854-57cb-ef81.ngrok-free.app + /callback
def callback():
    signature = request.headers['X-Line-Signature']  #Get X-Line-Signature header value ，檢測是否從LINE傳過來的資料
    body = request.get_data(as_text=True)            #將接收到的請求轉換為文字
    json_data = json.loads(body)                     #將接收到的資訊轉為JSON格式
    json_str = json.dumps(json_data, indent=4)       #格式化jsn_dat讓輸儲果
    print(json_str)                                  #印出來檢視一下
    
    #Handle Webhook body
    try:
        #如果Channel Access Token或Channel Secret發生錯誤
        #會進入到exceptInvalidSignatureError:區塊。
        handler.handle(body, signature)
    except InvalidSignatureError:
        #如果有錯誤代表ChaelAccskeSecet
        #可能輸入錯誤或無效。
        # 處理錯誤,abort400。
        abort(400)
    #返回OKLINEDevelopers收到K後代表ok
    return 'OK'

#################################### line-bot-訊息接收處
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    json_data=json.loads(str(event))  #將接收到的資訊轉為 JSON 格式
    json_str = json.dumps(json_data,indent=4)  #格式化 json_data 讓輸出結果增加可讀性
    print(json_str)
    
    get_msg =event.message.text #將
    
    line_bot_api.reply_message(event.reply_token,TextSendMessage(get_msg))  #回傳文字訊息，將字串強制轉型成 TextSendMessage

    
#################################### line-bot-訊息接收處 /////    

    
# 主程式 MAIN
if __name__ == "__main__":  # 用來判斷是否為該檔案的主程式
    # 啟用服務
    app.run(port=2023)
