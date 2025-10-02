# Notif-US

## Giới thiệu

Phần mềm này có công dụng tự động kiểm tra các thông báo mới từ các trang web được chỉ định và gửi thông báo lên Notification Center của Windows. Điều này giúp người dùng không bỏ lỡ các thông báo quan trọng từ các website mà mình quan tâm.

## Cách hoạt động

- **`tray_icon.pyw` là file kích hoạt chính của chương trình.** Khi chạy file này, một biểu tượng (tray icon) sẽ xuất hiện ở taskbar hệ thống. Đồng thời, chương trình sẽ tự động kích hoạt file `main.py`.

- **`main.py` sử dụng Playwright để kiểm tra thông báo mới từ các website.** Danh sách website được lấy từ file `history_visited.txt`, mỗi dòng gồm 3 phần:  
  1. Link website  
  2. XPath dẫn tới thẻ `<a>` của phần tử thông báo (trong đó `<i>` là chỉ số thứ tự thông báo)  
  3. Link thông báo cuối cùng mà người dùng từng xem trong web.

- **Quy trình kiểm tra:**  
  - Với mỗi website, chương trình sẽ lấy các thông báo mới dựa trên xpath.  
  - Nếu phát hiện thông báo chưa từng được truy cập, chương trình sẽ gửi thông báo lên Notification Center của Windows.
  - Các thông báo đã quét nhưng người dùng chưa truy cập sẽ được lưu vào `omission.txt`.

- **Kiểm tra truy cập:**  
  - Việc kiểm tra xem người dùng đã truy cập thông báo hay chưa được thực hiện thông qua file database lịch sử (`history`) của trình duyệt.  
  - Đường dẫn tới file này cần được cung cấp trong `history_path.txt`.
> [!NOTE]
> - Edge: `C:\Users\<Tên_người_dùng>\AppData\Local\Microsoft\Edge\User Data\<Default/Profile 1/Profile 2/...>\History`
> - Chrome: `C:\Users\<Tên_người_dùng>\AppData\Local\Google\Chrome\User Data\<Default/Profile 1/Profile 2/...>\History`

- **Cách sử dụng tray icon:**  
  - Do tray icon của file exe không thể kiểm tra định kỳ, bạn có thể thêm shortcut vào thư mục Startup để hệ thống tự động chạy chương trình mỗi khi khởi động máy.
  - Ngoài ra, bạn có thể kích hoạt kiểm tra thủ công bằng cách click chuột trái vào icon trên taskbar.
  - Click chuột phải vào icon để mở menu tùy chọn (ví dụ: mở file cấu hình website theo dõi).

  - Bạn có thể thay đổi các file ico để đổi icon của tray icon (16px × 16px).

