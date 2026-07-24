# QUY TẮC BẮT BUỘC

1. **KHÔNG thêm comments**
2. **LUÔN dùng tiếng Việt trong giao tiếp với user** - Đơn giản, dễ hiểu, không phức tạp
3. **CẤM tạo hàm hỗn hợp** - Code chức năng A phải vào hàm A, CẤM lẫn lộn
4. **Hạn chế newlines** - Theo bố cục hiện tại, CẤM dùng parameter/pattern/v index/elif phân chia
5. **CẤM đặt tên hàm và biến quá dài** - Attacker dễ tấn công
6. **Chạy auto_test ngay** - Sau mỗi chỉnh sửa phải test với 5 file, khi chạy test phải đợi cho toàn bộ 5 file test pass hết mới notify user.
7. **Sửa lỗi ngay** - CẤM rollback khi chưa thử sửa, CẤM để lần sau
8. **Tận dụng hết mọi hàm** - Không để unused functions
9. **KHÔNG tự ý rollback từ backup** - Phải báo trước vì backup chưa cập nhật
10. **Suy nghĩ CỰC KÌ cẩn thận** - Cấm phạm sai lầm khi chỉnh sửa
11. **Xóa file temp** - Khi chỉnh sửa xong phải xóa file temp
12. **KHÔNG tự ý hành động** - Mọi thứ phải qua ý user
13. **KHÔNG chạy python** - Dùng path C:/Users/XZ/AppData/Local/Python/pythoncore-3.12-64/python.exe thay vì python vì environment của user đang bị trục trặc
14. **KHÔNG thêm random/chance ở những vị trí có thể làm yếu tool** - Chất lượng của mọi file output đều phải mạnh như nhau
15. **Cách xử lý khi có unused/duplicate functions** - Nếu có unused thì hãy tận dụng triệt để tất cả hàm unused đó, chỉ được xóa khi hàm đó không thể tận dụng vào đâu khác. Nếu có hàm duplicate thì hãy gộp những hàm duplicate lại, "gộp" không phải "chọn" cái mạnh nhất hay "thay thế". Lưu ý : Dù làm gì thì mục đích tối thượng vẫn là biến tool trở nên mạnh hơn chứ không phải yếu đi.
    **LƯU Ý:** User không biết code - giải thích đơn giản!\*\*
    **Quy tắc đặt tên** - Tên hàm và biến phải vừa đặt theo phong cách minecraft và mang tính personal ( xem tsunami.py và meomeo.py để hiểu rõ hơn cách đặt tên ). Về personal, có thể đặt kiểu **_cat_** ( tên discord của user ) và **\_yep\_\_** ( biệt danh của user ), từ những từ này có thể suy ra như **_meoooooooooo_** hoặc **_yeppppppp_**. SỐ LƯỢNG GẠCH "\_" Ở 2 ĐẦU PHẢI TỪ 2 TRỞ LÊN VÀ CẤM CÓ GẠCH Ở GIỮA, ví dụ **abc_xyz** <-- sai. User là nam nên có thể đặt là **deptrai\_** hoặc **deptraivailon**. Bố cục phải đẹp mắt và tuân thủ quy tắc. Nhắc nhở : chỉ có 2 option đặt tên, 1 là tên minecraft 2 là tên personal nhưng tên personal 1 là do user cung cấp hoặc có thể tự suy nghĩ dựa vào những tên biến hiện có trong file để tạo ra 1 list tên rồi gửi cho user để duyệt, CẤM đặt tên tự tiện, lung tung, CẤM đặt tên = chức năng của nó. Valid variable : **xxx** Invalid variable : **abc_xxx\*\*. CẤM đặt tên xàm lồn như **a**, **b**, **c\*\*,.....
