#T4.2.1: Tập tin setings.ini
import configparser
# Đọc file settings.ini
config = configparser.ConfigParser()
config.read('settings.ini')
# Thay đổi giá trị
config['Graphics']['resolution'] = '1280 x 1024'
config['Audio']['masterVolume'] = '50'
# Ghi lại các thay đổi vào file
with open('settings.ini', 'w') as configfile:
    config.write(configfile)
print("Đã thay đổi giá trị trong file settings.ini")
