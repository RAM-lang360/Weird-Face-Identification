import boto3

# Rekognitionクライアントを作成
rekognition = boto3.client('rekognition')

# 検出したい画像のS3情報
bucket = 'your-s3-bucket'
photo = 'your-image-file.jpg'

# Rekognitionでラベルを検出
response = rekognition.detect_labels(
    Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
    MaxLabels=10,  # 検出するラベルの最大数
    MinConfidence=75  # 検出するラベルの最小信頼度（パーセント）
)

# 結果を表示
print('Detected labels for ' + photo)
for label in response['Labels']:
    print(f"Label: {label['Name']}, Confidence: {label['Confidence']:.2f}%")
