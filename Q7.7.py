#Q7.7
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Link
Url = 'https://raw.githubusercontent.com/phamminhngocha/BigData/main/TyGiaVND2022-2023.csv'
# Đọc dữ liệu vào DataFrame
dfTyGia = pd.read_csv(Url)
# Chọn ngoại tệ X và năm y (thay thế X và y bằng giá trị thực tế)
NgoaiTeXem = input('Tên ngoại tệ cần xem dự báo:') 
NamXem = int(input('Năm xem dự báo(2022 hoặc 2023)?'))
# Lọc dữ liệu theo ngoại tệ và năm
dfLoc = dfTyGia[(dfTyGia['NgoaiTe'] == NgoaiTeXem) & (dfTyGia['Nam'] == NamXem)]
# Trực quan hóa dữ liệu (tùy chọn)
plt.plot(dfLoc['Thang'], dfLoc['TyGiaNgoaiTe-VND'])
plt.xlabel('Tháng')
plt.ylabel('Tỷ giá Ngoại tệ-VNĐ')
plt.title(f'Biểu đồ tỷ giá {NgoaiTeXem} năm {NamXem}')
plt.show()
# Chuẩn bị dữ liệu cho mô hình
X = dfLoc['Thang'].values.reshape(-1, 1)  # Tính năng: tháng
y = dfLoc['TyGiaNgoaiTe-VND'].values
# Xây dựng mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X, y)
# Dự báo tỷ giá cho tháng cuối cùng của năm
ThangCuoi = dfLoc['Thang'].max()
TyGiaDuBao = model.predict([[ThangCuoi + 1]])[0]
# Đánh giá xu hướng
if TyGiaDuBao > int(y[-1]):
    print(f"Xu hướng của ngoại tệ {NgoaiTeXem} trong năm {NamXem} là tăng.")
else:
    print(f"Xu hướng của ngoại tệ {NgoaiTeXem} trong năm {NamXem} là giảm.")













