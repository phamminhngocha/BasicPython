#Q6.2
# Nhập liệu các thông tin từ người dùng
ChiPhiCoDinh = float(input("Nhập chi phí cố định một tháng (đồng): "))
ChiPhiBienDoiMotCoc = float(input("Nhập chi phí biến đổi một cốc cafe (đồng): "))
GiaBanMotCoc = float(input("Nhập giá bán một cốc cafe (đồng): "))

# Tính lợi nhuận trên một cốc cafe
LoiNhuanMotCoc = GiaBanMotCoc - ChiPhiBienDoiMotCoc

# Tính điểm hòa vốn (số lượng cốc cafe cần bán)
DiemHoaVon = ChiPhiCoDinh / LoiNhuanMotCoc

# In kết quả ra màn hình
print("Điểm hòa vốn (Số cốc cafe cần bán mỗi tháng):", DiemHoaVon)
