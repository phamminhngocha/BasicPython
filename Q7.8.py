#Q7.8
import os

def LogOff():
    os.system("shutdown /l")
def Shutdown():
    os.system("shutdown /s /t 0")
def Restart():
    os.system("shutdown /r /t 0")
def Main():
    while True:
        print("\nChọn thao tác:")
        print("1. Đăng xuất (Logoff)")
        print("2. Tắt máy (Shutdown)")
        print("3. Khởi động lại (Restart)")
        print("4. Thoát")
        Chon = input("Nhập lựa chọn của bạn (1/2/3/4): ")
        if Chon == '1':
            LogOff()
        elif Chon == '2':
            Shutdown()
        elif Chon == '3':
            Restart()
        elif Chon == '4':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    Main()














