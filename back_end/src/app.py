from flask import Flask

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# ルートエンドポイントの設定
@app.route('/src')
def hello_world():
    return 'Flask is running!'

if __name__ == '__main__':
    # アプリケーションを起動
    app.run(debug=True, host='0.0.0.0', port=5000)
