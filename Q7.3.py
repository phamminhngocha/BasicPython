#Q7.3
def Ham02(text):
    # ???
    text = text.lower()    
    # ???
    ws = text.split()
    # ???
    wc = {}
    # ???
    for w in ws:
        # ???
        w = w.strip(".,!?")        
        # ???
        if w in wc:
            wc[w] += 1
        else:
            wc [w] = 1
    return wc
# Nhập giá trị đầu vào
it = Input("Nhập một đoạn văn:")
# ???
result = Ham02(it)
# ???
for w1, c1 in result.items():
    print(f"{w1}: {c1}")














