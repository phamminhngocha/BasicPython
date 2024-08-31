#Q7.9
import pyttsx3
from langdetect import detect
from gtts import gTTS
import os

VanBan = input("Nhập đoạn văn bản bạn muốn nghe: ")
try:
    NgonNgu = detect(VanBan)
    print("Ngôn ngữ sẽ áp dụng đọc văn bản của bạn là: ", NgonNgu)        
except:
    print("Không thể xác định được ngôn ngữ. Mặc định sử dụng tiếng Anh.")
    NgonNgu = "en"
if NgonNgu == "vi":
    tts = gTTS(text=VanBan, lang='vi')
    filename = "vietnamese.mp3"
    tts.save(filename)
else:
    engine = pyttsx3.init()
    engine.say(VanBan)
    filename = "english.mp3"
    engine.save_to_file(VanBan, "english.mp3")
    engine.runAndWait()

os.system("start " + filename)
