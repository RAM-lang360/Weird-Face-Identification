import requests
import json
import base64  
# APIキーを設定
API_KEY = 'AIzaSyDWWxchX2ef3EcjQ2UBoIRcCgK38XBHYAM'

# リクエストのURL
url = f'https://vision.googleapis.com/v1/images:annotate?key={API_KEY}'

# 解析する画像のbase64エンコードデータ
with open('/app/src/preparation/test.jpg', 'rb') as image_file:
    image_content = image_file.read()
image_base64 = base64.b64encode(image_content).decode('UTF-8')

# リクエストデータ
data = {
    "requests": [
        {
            "image": {
                "content": image_base64
            },
            "features": [
                {
                    "type": "LABEL_DETECTION",
                    "maxResults": 10
                }
            ]
        }
    ]
}

# POSTリクエストを送信
response = requests.post(url, json=data)
result = response.json()

# 結果を表示
print(json.dumps(result, indent=2))
