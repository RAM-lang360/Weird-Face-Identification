import sqlite3
import json

def create_connection(db_file):
    """ SQLite データベースに接続する """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def insert_face_details(conn, face_details):
    """ データを FaceDetails テーブルに挿入する """
    sql = '''
    INSERT INTO FaceDetails (
        BoundingBoxWidth, BoundingBoxHeight, BoundingBoxLeft, BoundingBoxTop,
        AgeRangeLow, AgeRangeHigh, SmileValue, SmileConfidence,
        EyeglassesValue, EyeglassesConfidence, SunglassesValue, SunglassesConfidence,
        GenderValue, GenderConfidence, BeardValue, BeardConfidence,
        MustacheValue, MustacheConfidence, EyesOpenValue, EyesOpenConfidence,
        MouthOpenValue, MouthOpenConfidence, FaceOccludedValue, FaceOccludedConfidence,
        EyeDirectionYaw, EyeDirectionPitch, EyeDirectionConfidence,
        PoseRoll, PoseYaw, PosePitch,
        QualityBrightness, QualitySharpness, Confidence,
        EmotionType, EmotionConfidence,
        LandmarkType, LandmarkX, LandmarkY
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    try:
        cur = conn.cursor()
        cur.execute(sql, face_details)
        conn.commit()
        print("データが正常に挿入されました。")
    except sqlite3.Error as e:
        print(f"エラーが発生しました: {e}")

def process_json_file(json_file):
    """ JSON ファイルを処理し、データベースに挿入する """
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # JSON データから FaceDetails を取得
    face_details_list = data.get("FaceDetails", [])
    
    # データベース接続
    database = "your_database.db"
    conn = create_connection(database)
    
    if conn:
        for face in face_details_list:
            # FaceDetails データを抽出
            bounding_box = face.get("BoundingBox", {})
            age_range = face.get("AgeRange", {})
            smile = face.get("Smile", {})
            eyeglasses = face.get("Eyeglasses", {})
            sunglasses = face.get("Sunglasses", {})
            gender = face.get("Gender", {})
            beard = face.get("Beard", {})
            mustache = face.get("Mustache", {})
            eyes_open = face.get("EyesOpen", {})
            mouth_open = face.get("MouthOpen", {})
            emotions = face.get("Emotions", [])
            landmarks = face.get("Landmarks", [])
            pose = face.get("Pose", {})
            quality = face.get("Quality", {})
            face_occluded = face.get("FaceOccluded", {})
            eye_direction = face.get("EyeDirection", {})
            
            # 統合データを作成
            face_details = (
                bounding_box.get("Width", None),
                bounding_box.get("Height", None),
                bounding_box.get("Left", None),
                bounding_box.get("Top", None),
                age_range.get("Low", None),
                age_range.get("High", None),
                smile.get("Value", None),
                smile.get("Confidence", None),
                eyeglasses.get("Value", None),
                eyeglasses.get("Confidence", None),
                sunglasses.get("Value", None),
                sunglasses.get("Confidence", None),
                gender.get("Value", None),
                gender.get("Confidence", None),
                beard.get("Value", None),
                beard.get("Confidence", None),
                mustache.get("Value", None),
                mustache.get("Confidence", None),
                eyes_open.get("Value", None),
                eyes_open.get("Confidence", None),
                mouth_open.get("Value", None),
                mouth_open.get("Confidence", None),
                face_occluded.get("Value", None),
                face_occluded.get("Confidence", None),
                eye_direction.get("Yaw", None),
                eye_direction.get("Pitch", None),
                eye_direction.get("Confidence", None),
                pose.get("Roll", None),
                pose.get("Yaw", None),
                pose.get("Pitch", None),
                quality.get("Brightness", None),
                quality.get("Sharpness", None),
                face.get("Confidence", None),
                # Emotions と Landmarks の処理
                *(e.get("Type", None) + e.get("Confidence", None) for e in emotions),
                *(l.get("Type", None) + l.get("X", None) + l.get("Y", None) for l in landmarks)
            )
            
            # データを挿入
            insert_face_details(conn, face_details)
        
        conn.close()

if __name__ == '__main__':
    process_json_file('data.json')
