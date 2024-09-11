
class config:
    # SwitchBot APIのトークンを設定(スマホアプリから確認)
    API_TOKEN = 'ENTERYOURAPITOKEN'
    
    HOST_URL = "https://api.switch-bot.com"
    
    headers = {
    'Authorization': API_TOKEN,
    'Content-Type': 'application/json; charset=utf8',}