#Q7.6
import openai
import requests

# Cấu hình API keys (phải thay thế bằng keys của bạn trong ChtGPT và trong Bing)
openai.api_key = 'YOUR_OPENAI_API_KEY'
bing_subscription_key = 'YOUR_BING_SUBSCRIPTION_KEY'
bing_search_url = 'https://api.bing.microsoft.com/v7.0/search'

def TraCuuChatGPT(TruyVan):
    KetQua = openai.Completion.create(
        engine="text-davinci-003", # Hoặc engine phù hợp khác
        prompt=TruyVan,
        max_tokens=150, # Điều chỉnh theo nhu cầu
        temperature=0.7, # Điều chỉnh độ "sáng tạo" của câu trả lời
    )
    return KetQua.choices[0].text.strip()

def TraCuuBing(query):
    headers = {'Ocp-Apim-Subscription-Key': bing_subscription_key}
    params = {'q': query, 'textDecorations': True, 'textFormat': 'HTML'}
    response = requests.get(bing_search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()   

    # Trích xuất kết quả tìm kiếm (có thể tùy chỉnh theo nhu cầu)
    if 'webPages' in search_results and 'value' in search_results['webPages']:
        return search_results['webPages']['value'][0]['snippet']
    else:
        return "Không tìm thấy kết quả trên Bing."

def Main():
    while True:
        print("\nChọn công cụ tra cứu:")
        print("1. ChatGPT")
        print("2. Bing")
        print("3. Thoát")
        Chon = input("Nhập lựa chọn của bạn (1/2/3): ")

        if Chon == '1':
            query = input("Nhập câu hỏi cho ChatGPT: ")
            result = search_chatgpt(query)
            print("ChatGPT trả lời:", result)
        elif Chon == '2':
            query = input("Nhập từ khóa tìm kiếm trên Bing: ")
            result = search_bing(query)
            print("Kết quả từ Bing:", result)
        elif Chon == '3':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    Main()
