import cv2

# Haar Cascade sınıflandırıcılarını yükleme (yüz algılama için kullanacağız)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Videonun kaynağını açın
video_capture = cv2.VideoCapture('C:\\Users\\celeb\\Desktop\\opencv\\video.mp4')  # video.mp4 yerine kendi video dosyanızın yolunu belirtin

while True:
    # Videodan bir çerçeve alın
    ret, frame = video_capture.read()
    
    if not ret:
        break
    
    # Gri tona dönüştürünpip3 install opencv-python

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri algılayın
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Algılanan yüzlerin etrafına dikdörtgen çizin
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Çerçeve üzerine metin ekleyin
    cv2.putText(frame, "Yuz Bulundu", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Sonuç çerçevesini gösterin
    cv2.imshow('Video', frame)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırakın ve pencereyi kapatın
video_capture.release()
cv2.destroyAllWindows()
