#Dựa vào tuổi, xác định Giai đoạn tương ứng của con người.
Tuoi=int(input('Nhập tuổi='))
if Tuoi<=0:
    GiaiDoan="Không hợp lệ!"
elif 0<Tuoi<6:
    GiaiDoan="Trẻ em"
elif 6<=Tuoi<10:
    GiaiDoan="Nhi đồng"
elif 10<=Tuoi<18:
    GiaiDoan="Thiếu nhi"
elif 18<=Tuoi<40:
    GiaiDoan="Thanh niên"
elif 40<=Tuoi<65:
    GiaiDoan="Trung niên"
elif 65<=Tuoi:
    GiaiDoan="Người cao tuổi"    
print(f"Người {Tuoi} tuổi thuộc giai đoạn: {GiaiDoan}")
