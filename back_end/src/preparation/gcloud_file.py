from google.cloud import vision
import io
import os

# 認証情報の設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/app/src/daring-cache-438622-k2-82f5a6510dc5.json'

def detect_text(image_path):
    # Vision APIのクライアントを作成
    client = vision.ImageAnnotatorClient()

    # 画像を読み込む
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    # 画像オブジェクトを作成
    image = vision.Image(content=content)

    # テキスト検出を実行
    response = client.face_detection(image=image)
    faces = response.face_annotations

    # 結果を表示
    print('Detected text:')
    for face in faces:
        print(f'顔の感情: {face.joy_likelihood}, {face.sorrow_likelihood}, {face.anger_likelihood}, {face.surprise_likelihood}')
    if response.error.message:
        raise Exception(f'{response.error.message}')
# 画像ファイルのパスを指定
detect_text('/app/src/preparation/test.jpg')
