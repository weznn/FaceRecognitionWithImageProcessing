

get_python().system('pip install opencv-python')
import cv2
# Haar Cascade modeliyle yüz tespiti için önceden eğitilmiş bir model yüklenir
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamerayı başlat
cap = cv2.VideoCapture(0)  # 0, varsayılan kamera anlamına gelir

if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

while True:
    # Kameradan görüntü al
    ret, frame = cap.read()
    if not ret:
        print("Görüntü alınamadı!")
        break

    # Görüntüyü gri tonlamaya çevir (Yüz tespiti gri tonlamada daha etkili çalışır)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit et
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Yüzleri işaretle
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Görüntüyü ekranda göster
    cv2.imshow('Yüz Tanıma', frame)

    # 'q' tuşuna basarak çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı ve pencereleri serbest bırak
cap.release()
cv2.destroyAllWindows()





