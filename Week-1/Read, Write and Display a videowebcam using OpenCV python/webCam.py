import cv2
# Bắt Video từ WebCam
cap = cv2.VideoCapture(0)

# Chỉ định mã FourCC: fourcc.org
temp = cv2.VideoWriter_fourcc(*'XVID')

# Video lưu lại với 24fps 640x480
out = cv2.VideoWriter('output.avi', temp, 24, (640,480))

#print(cap.isOpened())
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Lưu khung ảnh đang quay
        out.write(frame)
        # Hiển thị hình ảnh đang quay Video
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Kết thúc việc quay bằng việc tắt Terminal
cap.release()
out.release()
cv2.destroyAllWindows()