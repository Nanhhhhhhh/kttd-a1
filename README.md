# KTTD - Team A1: Kiểm thử tự động ứng dụng Android Swag Labs

**Học phần:** Kiểm thử phần mềm – Thực hành kiểm thử tự động  
**Lớp:** INT1401  
**Nhóm:** A1 (App Testing Team 1 / Nhóm N01)  
**Đề tài:** DT10 – Kiểm thử ứng dụng Mobile Swag Labs bằng Appium Python Client  
**Kho lưu trữ GitHub:** https://github.com/Nanhhhhhhh/kttd-a1  

---

## 👥 Danh sách thành viên Nhóm A1
1. **Đoàn Nam Anh (A46489)** – Nhóm trưởng (Quản trị repo, phân chia Issue, review PR và tổng hợp)
2. **Nguyễn Bá Tùng Bách (A45575)** – Kỹ sư kiểm thử (Phát triển ca kiểm thử sắp xếp theo Tên)
3. **Đoàn Ngọc Huy (A46445)** – Kỹ sư kiểm thử (Phân tích kịch bản kiểm thử & tài liệu Waits)
4. **Phạm Hùng (A43714)** – Kỹ sư kiểm thử (Phát triển ca kiểm thử sắp xếp theo Giá)
5. **Đặng Hoàng Nam (A45514)** – Kỹ sư kiểm thử (Thực thi kiểm thử, xuất báo cáo và chuẩn bị slide)

---

## 🎯 Chuyên đề Tuần 6: Sắp xếp sản phẩm (PRODUCTS Screen)
- **Ứng dụng kiểm thử:** Swag Labs (Android APK `com.swaglabsmobileapp`)
- **Tài khoản kiểm thử:** `standard_user` / `secret_sauce`
- **Chuyên đề lý thuyết Selenium-Python:**
  - Mục 5.1: Explicit Waits (`WebDriverWait`, `expected_conditions`)
  - Mục 5.2: Implicit Waits (`implicitly_wait`)
  - Mục 7.5: Locate elements By (`AppiumBy.ACCESSIBILITY_ID`, `By.XPATH`)
  - Mục 7.1: Exceptions (`TimeoutException`, `NoSuchElementException`)
- **Hàm/Lớp bắt buộc sử dụng:**
  - `webdriver.Remote`, `AppiumBy.ACCESSIBILITY_ID`, `WebDriverWait`, `EC.visibility_of_element_located`, `EC.element_to_be_clickable`, `implicitly_wait`, `find_elements`, `TimeoutException`.

---

## 🛠️ Cài đặt & Hướng dẫn chạy kiểm thử

1. **Cài đặt thư viện phụ thuộc:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Chạy kiểm thử với Pytest & xuất báo cáo HTML:**
   ```bash
   pytest -v tuan-06/test_sap_xep_san_pham.py --html=tuan-06/anh/report.html --self-contained-html
   ```

3. **Chạy trực tiếp với Unittest:**
   ```bash
   python3 -m unittest -v tuan-06/test_sap_xep_san_pham.py
   ```

---

## 📁 Cấu trúc thư mục kho mã nguồn
```text
kttd-a1/
├── README.md
├── requirements.txt
├── .gitignore
├── .github/
│   └── pull_request_template.md
└── tuan-06/
    ├── test_sap_xep_san_pham.py
    ├── testcases.md
    ├── slide_tuan06_a1.md
    ├── slide_tuan06_a1.html
    ├── slide_tuan06_a1.pptx
    └── anh/
        ├── report.html
        ├── tc01_sort_az.png
        ├── tc02_sort_za.png
        ├── tc03_sort_price_low_high.png
        ├── tc04_sort_price_high_low.png
        ├── tc05_explicit_wait.png
        └── tc06_timeout_exception.png
```
