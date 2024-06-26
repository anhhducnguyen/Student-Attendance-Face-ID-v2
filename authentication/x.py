from numpy import load, expand_dims, asarray, savez_compressed
from keras_facenet import FaceNet

# Tạo một đối tượng FaceNet
embedder = FaceNet()

# Hàm để lấy vector nhúng cho một khuôn mặt
def get_embedding(model, face_pixels):
    # Chuẩn hóa giá trị pixel
    face_pixels = face_pixels.astype('float32')
    # Chuẩn hóa giá trị pixel theo các kênh (global)
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std
    # Chuyển khuôn mặt thành một mẫu
    samples = expand_dims(face_pixels, axis=0)
    # Dự đoán để lấy vector nhúng
    yhat = model.predict(samples)
    return yhat[0]

# Hàm để tạo và lưu vector nhúng từ tập dữ liệu khuôn mặt
def create_embeddings(dataset_path, output_path):
    # Tải tập dữ liệu khuôn mặt
    data = load(dataset_path)
    trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
    print('Đã tải: ', trainX.shape, trainy.shape, testX.shape, testy.shape)

    # Lấy mô hình từ đối tượng embedder
    model = embedder.model
    print('Đã tải mô hình')

    # Chuyển đổi từng khuôn mặt trong tập huấn luyện thành vector nhúng
    newTrainX = [get_embedding(model, face_pixels) for face_pixels in trainX]
    newTrainX = asarray(newTrainX)
    print(newTrainX.shape)

    # Chuyển đổi từng khuôn mặt trong tập kiểm tra thành vector nhúng
    newTestX = [get_embedding(model, face_pixels) for face_pixels in testX]
    newTestX = asarray(newTestX)
    print(newTestX.shape)

    # Lưu mảng vào một tệp ở định dạng nén
    savez_compressed(output_path, newTrainX, trainy, newTestX, testy)
    print(f'Embeddings saved to {output_path}')

