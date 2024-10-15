from flask import Flask
import os
from google.cloud import vision
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# Google Cloud Visionの認証情報を設定
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your-service-account-key.json"

# データベース接続の設定
DATABASE_URI = 'mysql+pymysql://username:password@host/database_name'
engine = create_engine(DATABASE_URI)
metadata = MetaData()

# 顔認識の結果を格納するテーブルを定義
faces_table = Table('faces', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('joy_likelihood', String(50)),
                    Column('sorrow_likelihood', String(50)),
                    Column('anger_likelihood', String(50)),
                    Column('surprise_likelihood', String(50)),
                    Column('detection_confidence', String(50)))

# テーブルが存在しない場合は作成
metadata.create_all(engine)

# Google Cloud Vision APIクライアントを作成
client = vision.ImageAnnotatorClient()

# 画像ファイルを指定（ローカルパスまたはURL）
image_path = "path_to_image.jpg"

def detect_faces(image_path):
    """Vision APIを使用して画像から顔を検出する"""
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.face_detection(image=image)
    faces = response.face_annotations

    if response.error.message:
        raise Exception(f'{response.error.message}')

    return faces

def insert_face_data(face_data):
    """SQLに顔認識データを挿入する"""
    with engine.connect() as conn:
        for face in face_data:
            conn.execute(faces_table.insert().values(
                joy_likelihood=face.joy_likelihood.name,
                sorrow_likelihood=face.sorrow_likelihood.name,
                anger_likelihood=face.anger_likelihood.name,
                surprise_likelihood=face.surprise_likelihood.name,
                detection_confidence=str(face.detection_confidence)
            ))

@app.route('/src')
def main():
    """Flaskのルートエンドポイント"""
    try:
        # 顔認識を実行
        faces = detect_faces(image_path)
        
        # SQLデータベースに顔認識結果を保存
        if faces:
            insert_face_data(faces)
            return f"{len(faces)} faces inserted into the database."
        else:
            return "No faces detected."
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    # アプリケーションを起動
    app.run(debug=True, host='0.0.0.0', port=5000)
