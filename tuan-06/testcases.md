# BÁO CÁO KỊCH BẢN KIỂM THỬ TỰ ĐỘNG – TUẦN 06 (TEAM A1)

- **Học phần:** Kiểm thử phần mềm – Thực hành kiểm thử tự động
- **Nhóm thực hiện:** Nhóm A1 (App Testing Team 1 / N01)
- **Đề tài:** DT10 – Kiểm thử ứng dụng Mobile Swag Labs bằng Appium Python Client
- **Chức năng 1:** Sắp xếp sản phẩm (Product Sorting)
- **Màn hình kiểm thử:** Swag Labs (app Android) – Màn hình PRODUCTS

---

## 1. Danh sách 6 Test Cases chi tiết

| Mã TC | Tên ca kiểm thử | Màn hình | Thao tác thực hiện | Dữ liệu đầu vào | Kết quả kỳ vọng | Trạng thái |
| :---: | :--- | :---: | :--- | :--- | :--- | :---: |
| **TC01** | Sắp xếp tên từ A đến Z | PRODUCTS | 1. Mở modal sắp xếp qua `test-Modal Selector Button`<br>2. Chọn tuỳ chọn "Name (A to Z)"<br>3. Đọc danh sách tên qua `find_elements(AppiumBy.ACCESSIBILITY_ID, 'test-Item title')` | Option: `"Name (A to Z)"` | Danh sách tên sản phẩm được sắp xếp tăng dần theo thứ tự từ điển A $\rightarrow$ Z | **PASSED** |
| **TC02** | Sắp xếp tên từ Z đến A | PRODUCTS | 1. Mở modal sắp xếp<br>2. Chọn tuỳ chọn "Name (Z to A)"<br>3. Đọc danh sách tên qua `find_elements` | Option: `"Name (Z to A)"` | Danh sách tên sản phẩm được sắp xếp giảm dần theo thứ tự từ điển Z $\rightarrow$ A | **PASSED** |
| **TC03** | Sắp xếp giá từ thấp đến cao | PRODUCTS | 1. Mở modal sắp xếp<br>2. Chọn tuỳ chọn "Price (low to high)"<br>3. Đọc danh sách giá qua `find_elements(AppiumBy.ACCESSIBILITY_ID, 'test-Price')` | Option: `"Price (low to high)"` | Danh sách giá sản phẩm được sắp xếp theo thứ tự số học tăng dần ($7.99 $\rightarrow$ $9.99 $\rightarrow$ $15.99...) | **PASSED** |
| **TC04** | Sắp xếp giá từ cao đến thấp | PRODUCTS | 1. Mở modal sắp xếp<br>2. Chọn tuỳ chọn "Price (high to low)"<br>3. Đọc danh sách giá qua `find_elements` | Option: `"Price (high to low)"` | Danh sách giá sản phẩm được sắp xếp theo thứ tự số học giảm dần ($49.99 $\rightarrow$ $29.99 $\rightarrow$ $15.99...) | **PASSED** |
| **TC05** | Kiểm tra cơ chế Explicit Wait | PRODUCTS | Chờ nút modal sắp xếp xuất hiện và có thể bấm được bằng `WebDriverWait(driver, 10).until(EC.element_to_be_clickable(...))` | Timeout: 10s | Trả về đối tượng WebElement ngay khi phần tử sẵn sàng, không ném ngoại lệ | **PASSED** |
| **TC06** | Xử lý ngoại lệ TimeoutException | PRODUCTS | Chủ động chờ một phần tử không tồn tại trên màn hình (`test-NonExistentElement`) với timeout 2 giây | Timeout: 2s | Ném ra đúng ngoại lệ `TimeoutException` và được khối `try...except` xử lý thành công | **PASSED** |

---

## 2. Bảng đối chiếu 8 Hàm/Lớp bắt buộc theo phân công của Team A1

| Hàm / Lớp bắt buộc | Vị trí áp dụng trong mã nguồn | Vai trò kỹ thuật |
| :--- | :--- | :--- |
| `webdriver.Remote` | Khởi tạo phiên kết nối Appium: `self.driver = webdriver.Remote(...)` | Kết nối Appium Client với Appium Server qua giao thức W3C WebDriver |
| `AppiumBy.ACCESSIBILITY_ID` | Định vị: `(AppiumBy.ACCESSIBILITY_ID, "test-Modal Selector Button")` | Bộ định vị tối ưu nhất trên Mobile (dựa trên Accessibility/content-description) |
| `WebDriverWait` | Khởi tạo bộ chờ: `wait = WebDriverWait(self.driver, timeout=10)` | Kiểm soát vòng lặp chờ đồng bộ (Explicit Wait) với tần suất kiểm tra 500ms |
| `EC.visibility_of_element_located` | `wait.until(EC.visibility_of_element_located(...))` | Kiểm tra phần tử đã có mặt trên DOM và đang hiển thị trên giao diện |
| `EC.element_to_be_clickable` | `wait.until(EC.element_to_be_clickable(...))` | Kiểm tra phần tử hiển thị và đang ở trạng thái kích hoạt (enabled) để click |
| `implicitly_wait` | `self.driver.implicitly_wait(5)` | Thiết lập thời gian chờ ngầm định toàn cục cho các hàm tìm kiếm |
| `find_elements` | `self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "test-Item title")` | Lấy danh sách toàn bộ các phần tử sản phẩm khớp locator để kiểm tra thứ tự sắp xếp |
| `TimeoutException` | Khối xử lý ngoại lệ: `except TimeoutException:` | Bắt và xử lý lỗi timeout khi điều kiện Explicit Wait không thỏa mãn |
