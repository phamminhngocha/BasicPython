#T5.2.1.2
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
df = pd.read_csv("BangLuong.csv")

# Tính tổng lương theo từng đơn vị
TongLuongTheoDonVi = df.groupby('Đơn vị công tác')['Tổng lương'].sum()

# Vẽ biểu đồ cột
TongLuongTheoDonVi.plot(kind='bar', figsize=(10, 6))

# Đặt tiêu đề và nhãn cho biểu đồ
plt.title('Tổng thu nhập theo từng đơn vị')
plt.xlabel('Đơn vị công tác')
plt.ylabel('Tổng thu nhập')

# Hiển thị biểu đồ
plt.show()
