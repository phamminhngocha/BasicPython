#Q7.10
import hashlib
def Sha256Hash(text):
  """
  Hàm tính toán giá trị băm SHA-256 của một chuỗi ký tự.
  Args:
      text: Chuỗi ký tự cần tính toán giá trị băm.
  Returns:
      Giá trị băm SHA-256 dưới dạng chuỗi hex.
  """
  hash_object = hashlib.sha256()
  hash_object.update(text.encode('utf-8'))  # Mã hóa chuỗi thành bytes trước khi cập nhật
  return hash_object.hexdigest()

VanBanGoc =input("Nhập văn bản cần mã hóa:")
VanBanMaHoa = Sha256Hash(VanBanGoc)

print("Văn bản gốc:", VanBanGoc)
print("Giá trị băm SHA-256:", VanBanMaHoa)
print("""Về mặt kỹ thuật, không thể giải mã trực tiếp một văn bản đã được mã hóa bằng SHA-256.
Tuy nhiên, ta có thể sử dụng những kỹ thuật tấn công như: brute-force hoặc rainbow table
để giải mã nếu như văn bản mã hóa là yếu hoặc ngắn!!!""")
