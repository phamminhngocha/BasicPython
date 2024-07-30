#T7.2.2: Xây dựng chương trình bằng cách lấy code từ Chatgpt
from docx import Document

def count_text_statistics(docx_file):
    # Mở file .docx
    doc = Document(docx_file)
    
    # Đếm số đoạn văn bản
    paragraphs = doc.paragraphs
    num_paragraphs = len(paragraphs)
    
    # Đếm số dòng và số từ
    num_lines = 0
    num_words = 0
    
    for para in paragraphs:
        # Đếm số dòng trong đoạn văn bản
        lines = para.text.split('\n')
        num_lines += len(lines)
        
        # Đếm số từ trong đoạn văn bản
        words = para.text.split()
        num_words += len(words)
    
    return num_words, num_lines, num_paragraphs

# Đường dẫn đến tập tin QuyetDinh.docx
docx_file_path = 'QuyetDinh.docx'

# Gọi hàm để tính toán
words, lines, paragraphs = count_text_statistics(docx_file_path)

# In kết quả
print(f'Số từ: {words}')
print(f'Số dòng: {lines}')
print(f'Số đoạn văn bản: {paragraphs}')

