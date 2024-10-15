# Python 3.9をベースにする
FROM python:3.9-slim

# set working directory
WORKDIR /app

# install the neededpackages 
COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y sqlite3 libsqlite3-dev && \
    rm -rf /var/lib/apt/lists/* &&\
    #r install the pakages google CLI authotixzation need 
    sudo apt-get update &&\


# アプリケーションのコードをコピー
COPY src/ src/

# ポートを設定
EXPOSE 5000

# サーバーを起動
CMD ["python"]

# curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-477.0.0-linux-x86_64.tar.gz
# tar -xf google-cloud-cli-477.0.0-linux-x86_64.tar.gz
# rm -d google-cloud-cli-477.0.0-linux-x86_64.tar.gz
# pip install google-cloud-vision
# googleでの認証のためにコンテナ内にアクセスし以下のコマンドを実行
#  ./google-cloud-sdk/install.sh
# export PATH="$PATH:/app/google-cloud-sdk/bin"
# source ~/.bashrc
# gcloud init 
#   ここでURLにアクセスし認証情報をゲット

