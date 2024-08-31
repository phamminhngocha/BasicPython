#Q7.5
from googletrans import Translator

def Main():
    translator = Translator()
    while True:
        print("\nChọn hướng dịch:")
        print("1. Tiếng Anh sang Tiếng Việt")
        print("2. Tiếng Việt sang Tiếng Anh")
        print("3. Thoát")

        Chon = input("Nhập lựa chọn của bạn (1/2/3): ")
        if Chon == '1':
            text = input("Nhập văn bản tiếng Anh: ")
            translation = translator.translate(text, dest='vi')
            print("Bản dịch tiếng Việt:", translation.text)
        elif Chon == '2':
            text = input("Nhập văn bản tiếng Việt: ")
            translation = translator.translate(text, dest='en')
            print("Bản dịch tiếng Anh:", translation.text)
        elif Chon == '3':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại!")

if __name__ == "__main__":
    Main()













