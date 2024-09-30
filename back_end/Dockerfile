# Python 3.9をベースにする
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# SQLite3をインストール
RUN apt-get update && \
    apt-get install -y sqlite3 libsqlite3-dev && \
    rm -rf /var/lib/apt/lists/*

# アプリケーションのコードをコピー
COPY src/ src/

# ポートを設定
EXPOSE 5000

# サーバーを起動
CMD ["python", "src/app.py"]
#ssh -i rekognition.pem ec2-user@コンテナのIPアドレス
