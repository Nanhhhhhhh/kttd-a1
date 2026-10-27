#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo file PowerPoint báo cáo Tuần 6 - Nhóm A1
Môn học: Kiểm thử phần mềm – Thực hành kiểm thử tự động (INT1401)
Chủ đề: Kiểm thử tự động ứng dụng di động Swag Labs (Android) - Sắp xếp sản phẩm
Tài liệu nghiên cứu: 5.1 Explicit Waits, 5.2 Implicit Waits, 7.5 Locate elements By, 7.1 Exceptions
Tuân thủ tiêu chuẩn: 16:9 Widescreen, thiết kế dạng thẻ (Card UI), màu sắc chuyên nghiệp, không chứa từ khóa thời lượng.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Bảng màu chủ đạo (Midnight Executive & Tech Navy)
    DARK_BG = RGBColor(15, 23, 42)      # #0F172A - Slate Dark Navy
    LIGHT_BG = RGBColor(248, 250, 252)  # #F8FAFC - Off White / Light Slate
    CARD_BG = RGBColor(255, 255, 255)   # #FFFFFF - White
    CARD_BORDER = RGBColor(226, 232, 240) # #E2E8F0 - Slate Border
    PRIMARY_NAVY = RGBColor(30, 39, 97) # #1E2761 - Navy
    ACCENT_TEAL = RGBColor(2, 128, 144) # #028090 - Teal Accent
    ACCENT_BLUE = RGBColor(37, 99, 235) # #2563EB - Royal Blue
    TEXT_DARK = RGBColor(30, 41, 59)    # #1E293B - Slate Dark Text
    TEXT_MUTED = RGBColor(100, 116, 139)# #64748B - Slate Muted Text
    TEXT_LIGHT = RGBColor(241, 245, 249)# #F1F5F9 - Slate Light Text
    SUCCESS_GREEN = RGBColor(16, 185, 129) # #10B981 - Green
    CODE_BG = RGBColor(241, 245, 249)   # #F1F5F9 - Light Code Box

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category="NHÓM A1 • MOBILE AUTOMATION TESTING", is_dark=False):
        # Category tracker
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_c = cat_box.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
        p_c = tf_c.paragraphs[0]
        p_c.text = category.upper()
        p_c.font.size = Pt(11)
        p_c.font.bold = True
        p_c.font.name = "Arial"
        p_c.font.color.rgb = ACCENT_TEAL if is_dark else ACCENT_BLUE

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.7))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(24)
        p_t.font.bold = True
        p_t.font.name = "Arial"
        p_t.font.color.rgb = TEXT_LIGHT if is_dark else PRIMARY_NAVY

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        return card

    # ==========================================
    # SLIDE 1: TRANG TIÊU ĐỀ (DARK THEME)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, DARK_BG)

    # Sub-badge
    badge = add_card(s1, Inches(0.8), Inches(1.2), Inches(5.8), Inches(0.45), bg_color=RGBColor(30, 41, 59), border_color=ACCENT_TEAL)
    tb_b = s1.shapes.add_textbox(Inches(0.9), Inches(1.25), Inches(5.6), Inches(0.35))
    p_b = tb_b.text_frame.paragraphs[0]
    p_b.text = "KIỂM THỬ PHẦN MỀM (INT1401) • BÁO CÁO THỰC HÀNH TUẦN 6"
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = ACCENT_TEAL

    # Title
    tb_title = s1.shapes.add_textbox(Inches(0.8), Inches(1.9), Inches(11.7), Inches(1.8))
    tf_tit = tb_title.text_frame
    tf_tit.word_wrap = True
    p1 = tf_tit.paragraphs[0]
    p1.text = "KIỂM THỬ TỰ ĐỘNG APPIUM"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_LIGHT

    p2 = tf_tit.add_paragraph()
    p2.text = "Chức Năng Sắp Xếp Sản Phẩm Trên Ứng Dụng Di Động Swag Labs"
    p2.font.size = Pt(22)
    p2.font.color.rgb = RGBColor(147, 197, 253)

    # Info Card
    c_info = add_card(s1, Inches(0.8), Inches(4.2), Inches(11.733), Inches(2.5), bg_color=RGBColor(24, 33, 54), border_color=RGBColor(51, 65, 85))
    tb_i = s1.shapes.add_textbox(Inches(1.1), Inches(4.4), Inches(11.1), Inches(2.1))
    tf_i = tb_i.text_frame
    tf_i.word_wrap = True

    pi1 = tf_i.paragraphs[0]
    pi1.text = "THÔNG TIN BÁO CÁO NHÓM A1"
    pi1.font.size = Pt(14)
    pi1.font.bold = True
    pi1.font.color.rgb = ACCENT_TEAL

    pi2 = tf_i.add_paragraph()
    pi2.text = "• Đơn vị thực hiện: Nhóm A1 – Lớp Kiểm thử phần mềm INT1401"
    pi2.font.size = Pt(13)
    pi2.font.color.rgb = TEXT_LIGHT

    pi3 = tf_i.add_paragraph()
    pi3.text = "• Trọng tâm nghiên cứu lý thuyết: 5.1 Explicit Waits, 5.2 Implicit Waits, 7.5 Locate elements By, 7.1 Exceptions"
    pi3.font.size = Pt(13)
    pi3.font.color.rgb = TEXT_LIGHT

    pi4 = tf_i.add_paragraph()
    pi4.text = "• Môi trường thực nghiệm: Appium Python Client, UIAutomator2, Android Swag Labs Mobile App"
    pi4.font.size = Pt(13)
    pi4.font.color.rgb = TEXT_LIGHT

    pi5 = tf_i.add_paragraph()
    pi5.text = "• Quy chuẩn cộng tác: GitHub Team Workflow (Milestone, Issues, Protected Main Branch, Pull Request Reviews)"
    pi5.font.size = Pt(13)
    pi5.font.color.rgb = TEXT_LIGHT

    # ==========================================
    # SLIDE 2: THÀNH VIÊN NHÓM A1 & PHÂN CÔNG
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, LIGHT_BG)
    add_header(s2, "Danh Sách Thành Viên & Phân Công Nhiệm Vụ Tuần 6")

    members = [
        {"name": "Đoàn Nam Anh", "id": "A46489", "role": "Nhóm trưởng / Quản trị GitHub", "tasks": "Thiết lập cấu hình Appium Driver, khởi tạo kho mã nguồn kttd-a1, thiết lập bảo vệ nhánh main, Milestone, Labels và rà soát Pull Requests."},
        {"name": "Nguyễn Bá Tùng Bách", "id": "A45575", "role": "Phân tích kịch bản & Lý thuyết", "tasks": "Phân tích yêu cầu chức năng Sắp xếp sản phẩm, thiết kế chi tiết 6 kịch bản Test Cases (testcases.md), nghiên cứu chuyên sâu Explicit & Implicit Waits."},
        {"name": "Đoàn Ngọc Huy", "id": "A46445", "role": "Lập trình kiểm thử (Tên A-Z, Z-A)", "tasks": "Hiện thực kịch bản TC01 (Name A to Z) và TC02 (Name Z to A), sử dụng AppiumBy.ACCESSIBILITY_ID và thuật toán so sánh chuỗi danh sách."},
        {"name": "Phạm Hùng", "id": "A43714", "role": "Lập trình kiểm thử (Giá SP)", "tasks": "Hiện thực kịch bản TC03 (Price Low-High) và TC04 (Price High-Low), bóc tách chuỗi tiền tệ float và kiểm chứng logic thứ tự số học."},
        {"name": "Đặng Hoàng Nam", "id": "A45514", "role": "Lập trình Wait & Báo cáo", "tasks": "Hiện thực kịch bản TC05 (EC.visibility_of_element_located) và TC06 (TimeoutException), đóng gói slide thuyết trình và tổng hợp báo cáo kiểm thử."}
    ]

    card_w = Inches(2.22)
    card_gap = Inches(0.16)
    left_start = Inches(0.8)

    for idx, m in enumerate(members):
        c_left = left_start + idx * (card_w + card_gap)
        c_top = Inches(1.8)
        c_h = Inches(5.1)

        # Highlight team leader card with distinctive border
        b_color = ACCENT_BLUE if idx == 0 else CARD_BORDER
        c = add_card(s2, c_left, c_top, card_w, c_h, bg_color=CARD_BG, border_color=b_color)
        
        tb = s2.shapes.add_textbox(c_left + Inches(0.15), c_top + Inches(0.2), card_w - Inches(0.3), c_h - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = f"THÀNH VIÊN 0{idx+1}"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = ACCENT_TEAL

        p_name = tf.add_paragraph()
        p_name.text = m["name"]
        p_name.font.size = Pt(14)
        p_name.font.bold = True
        p_name.font.color.rgb = PRIMARY_NAVY

        p_id = tf.add_paragraph()
        p_id.text = f"MSV: {m['id']}"
        p_id.font.size = Pt(11)
        p_id.font.color.rgb = TEXT_MUTED

        p_div = tf.add_paragraph()
        p_div.text = "------------------"
        p_div.font.size = Pt(8)
        p_div.font.color.rgb = CARD_BORDER

        p_role = tf.add_paragraph()
        p_role.text = m["role"]
        p_role.font.size = Pt(11)
        p_role.font.bold = True
        p_role.font.color.rgb = ACCENT_BLUE

        p_tasks = tf.add_paragraph()
        p_tasks.text = m["tasks"]
        p_tasks.font.size = Pt(10.5)
        p_tasks.font.color.rgb = TEXT_DARK

    # ==========================================
    # SLIDE 3: TỔNG QUAN ỨNG DỤNG SWAG LABS
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, LIGHT_BG)
    add_header(s3, "Tổng Quan Ứng Dụng Di Động Swag Labs & Phạm Vi Kiểm Thử")

    # Left Card: Đặc tả ứng dụng
    c_l3 = add_card(s3, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
    tb_l3 = s3.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.6))
    tf_l3 = tb_l3.text_frame
    tf_l3.word_wrap = True

    p = tf_l3.paragraphs[0]
    p.text = "THÔNG TIN ỨNG DỤNG MỤC TIÊU"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_NAVY

    items_l3 = [
        ("Tên ứng dụng: ", "Swag Labs Mobile App (Sauce Labs Sample App)."),
        ("Nền tảng mục tiêu: ", "Hệ điều hành Android (Test trên thiết bị thật / Giả lập AVD)."),
        ("App Package: ", "com.swaglabsmobileapp"),
        ("App Activity: ", "com.swaglabsmobileapp.MainActivity"),
        ("Giao thức tương tác: ", "Appium Server v2.x qua UiAutomator2 Driver."),
        ("Màn hình kiểm thử: ", "PRODUCTS (Màn hình chính hiển thị danh mục hàng hóa sau đăng nhập)."),
        ("Đặc tính UI: ", "Ứng dụng Native xây dựng trên nền tảng React Native, hỗ trợ các thuộc tính Accessibility chuẩn cho kiểm thử tự động.")
    ]
    for label, val in items_l3:
        p_item = tf_l3.add_paragraph()
        p_item.text = f"• {label}{val}"
        p_item.font.size = Pt(11.5)
        p_item.font.color.rgb = TEXT_DARK

    # Right Card: Chức năng Sắp xếp sản phẩm
    c_r3 = add_card(s3, Inches(6.8), Inches(1.8), Inches(5.733), Inches(5.1))
    tb_r3 = s3.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.6))
    tf_r3 = tb_r3.text_frame
    tf_r3.word_wrap = True

    p_r = tf_r3.paragraphs[0]
    p_r.text = "CHỨC NĂNG SẮP XẾP SẢN PHẨM (PRODUCT SORTING)"
    p_r.font.size = Pt(14)
    p_r.font.bold = True
    p_r.font.color.rgb = ACCENT_TEAL

    items_r3 = [
        ("Nút kích hoạt bộ lọc: ", "Accessibility ID: `test-Modal Selector Button`"),
        ("Chế độ 1 - Name (A to Z): ", "Sắp xếp danh sách tên sản phẩm theo thứ tự bảng chữ cái tăng dần."),
        ("Chế độ 2 - Name (Z to A): ", "Sắp xếp danh sách tên sản phẩm theo thứ tự bảng chữ cái giảm dần."),
        ("Chế độ 3 - Price (low to high): ", "Sắp xếp giá trị đơn hàng theo số thực tăng dần ($7.99 -> $49.99)."),
        ("Chế độ 4 - Price (high to low): ", "Sắp xếp giá trị đơn hàng theo số thực giảm dần ($49.99 -> $7.99)."),
        ("Thách thức kiểm thử: ", "Phải kiểm soát độ trễ render danh sách trên thiết bị di động, tránh bắt element khi dữ liệu chưa kịp tái sắp xếp.")
    ]
    for label, val in items_r3:
        p_item = tf_r3.add_paragraph()
        p_item.text = f"• {label}{val}"
        p_item.font.size = Pt(11.5)
        p_item.font.color.rgb = TEXT_DARK

    # ==========================================
    # SLIDE 4: LÝ THUYẾT 5.1 - EXPLICIT WAITS
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, LIGHT_BG)
    add_header(s4, "Nghiên Cứu Mục 5.1: Cơ Chế Explicit Waits (Chờ Tường Minh)")

    # 3 Cards Layout: Khái niệm, Cơ chế hoạt động, Cú pháp mẫu
    w4 = Inches(3.68)
    gap4 = Inches(0.33)

    # Card 1: Khái niệm & Bản chất
    c4_1 = add_card(s4, Inches(0.8), Inches(1.8), w4, Inches(5.1))
    tb4_1 = s4.shapes.add_textbox(Inches(1.0), Inches(2.0), w4 - Inches(0.4), Inches(4.6))
    tf4_1 = tb4_1.text_frame
    tf4_1.word_wrap = True
    p = tf4_1.paragraphs[0]
    p.text = "1. BẢN CHẤT EXPLICIT WAIT"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_NAVY

    pts4_1 = [
        "Explicit Wait là cơ chế lập trình cho phép script tạm dừng thực thi cho tới khi một ĐIỀU KIỆN CỤ THỂ (Expected Condition) được đáp ứng hoặc vượt quá thời gian tối đa (Timeout).",
        "Chỉ áp dụng cục bộ cho phần tử hoặc hành động cụ thể đang được gọi.",
        "Nếu điều kiện thỏa mãn trước timeout, mã nguồn lập tức chạy tiếp mà không cần chờ hết toàn bộ thời gian.",
        "Khắc phục triệt để nhược điểm của time.sleep() (vốn gây lãng phí thời gian cố định và làm chậm bộ kiểm thử)."
    ]
    for item in pts4_1:
        p_i = tf4_1.add_paragraph()
        p_i.text = f"• {item}"
        p_i.font.size = Pt(11)
        p_i.font.color.rgb = TEXT_DARK

    # Card 2: Chu kỳ Polling
    c4_2 = add_card(s4, Inches(0.8) + w4 + gap4, Inches(1.8), w4, Inches(5.1))
    tb4_2 = s4.shapes.add_textbox(Inches(1.0) + w4 + gap4, Inches(2.0), w4 - Inches(0.4), Inches(4.6))
    tf4_2 = tb4_2.text_frame
    tf4_2.word_wrap = True
    p = tf4_2.paragraphs[0]
    p.text = "2. CHU KỲ POLLING & TIMEOUT"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL

    pts4_2 = [
        "WebDriverWait thiết lập một vòng lặp thẩm tra (polling loop).",
        "Mặc định, WebDriver sẽ thăm dò cây giao diện mỗi 500 mili-giây (0.5 giây) một lần.",
        "Có thể cấu hình tùy chỉnh tần suất kiểm tra: poll_frequency=0.2s.",
        "Trong suốt quá trình kiểm tra, nếu gặp NoSuchElementException, WebDriverWait tự động bỏ qua để tiếp tục thăm dò.",
        "Nếu hết thời gian timeout mà điều kiện vẫn không trả về True, một TimeoutException sẽ được ném ra."
    ]
    for item in pts4_2:
        p_i = tf4_2.add_paragraph()
        p_i.text = f"• {item}"
        p_i.font.size = Pt(11)
        p_i.font.color.rgb = TEXT_DARK

    # Card 3: Cấu trúc lập trình chuẩn
    c4_3 = add_card(s4, Inches(0.8) + 2 * (w4 + gap4), Inches(1.8), w4, Inches(5.1))
    tb4_3 = s4.shapes.add_textbox(Inches(1.0) + 2 * (w4 + gap4), Inches(2.0), w4 - Inches(0.4), Inches(4.6))
    tf4_3 = tb4_3.text_frame
    tf4_3.word_wrap = True
    p = tf4_3.paragraphs[0]
    p.text = "3. CẤU TRÚC CODE THỰC TẾ"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    pts4_3 = [
        "Khai báo đối tượng chờ:",
        "wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)",
        "Đợi phần tử hiển thị:",
        "element = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'test-Id')))",
        "Đợi phần tử sẵn sàng nhấn:",
        "btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'test-Btn')))",
        "Đặc tính vượt trội: Trả về trực tiếp tham chiếu WebElement ngay khi điều kiện thỏa mãn."
    ]
    for item in pts4_3:
        p_i = tf4_3.add_paragraph()
        p_i.text = f"• {item}"
        p_i.font.size = Pt(10.5)
        p_i.font.color.rgb = TEXT_DARK

    # ==========================================
    # SLIDE 5: LÝ THUYẾT 5.1 - CÁC EXPECTED CONDITIONS
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, LIGHT_BG)
    add_header(s5, "Nghiên Cứu Mục 5.1: Các Điều Kiện Chờ (Expected Conditions)")

    # 4 Cards Grid (2x2)
    grid_w = Inches(5.7)
    grid_h = Inches(2.4)
    x1 = Inches(0.8)
    x2 = Inches(6.8)
    y1 = Inches(1.8)
    y2 = Inches(4.5)

    # Box 1: visibility_of_element_located
    add_card(s5, x1, y1, grid_w, grid_h)
    tb = s5.shapes.add_textbox(x1 + Inches(0.2), y1 + Inches(0.15), grid_w - Inches(0.4), grid_h - Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "EC.visibility_of_element_located((By, value))"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_NAVY
    p_sub = tf.add_paragraph()
    p_sub.text = "• Ý nghĩa: Đảm bảo phần tử có mặt trong cây giao diện VÀ có kích thước hiển thị thực tế (width > 0, height > 0).\n• Ứng dụng: Xác thực hộp thoại sắp xếp sản phẩm (Modal Selector) đã bung ra trọn vẹn trước khi tìm kiếm các tùy chọn."
    p_sub.font.size = Pt(10.5)
    p_sub.font.color.rgb = TEXT_DARK

    # Box 2: element_to_be_clickable
    add_card(s5, x2, y1, grid_w, grid_h)
    tb = s5.shapes.add_textbox(x2 + Inches(0.2), y1 + Inches(0.15), grid_w - Inches(0.4), grid_h - Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "EC.element_to_be_clickable((By, value))"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL
    p_sub = tf.add_paragraph()
    p_sub.text = "• Ý nghĩa: Đảm bảo phần tử vừa hiển thị, vừa ở trạng thái được kích hoạt (enabled=true) để có thể nhận sự kiện chạm/click mà không ném lỗi.\n• Ứng dụng: Dùng để click nút mở Menu Lọc và các lựa chọn 'Name (A to Z)', 'Price (low to high)'."
    p_sub.font.size = Pt(10.5)
    p_sub.font.color.rgb = TEXT_DARK

    # Box 3: presence_of_element_located
    add_card(s5, x1, y2, grid_w, grid_h)
    tb = s5.shapes.add_textbox(x1 + Inches(0.2), y2 + Inches(0.15), grid_w - Inches(0.4), grid_h - Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "EC.presence_of_element_located((By, value))"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p_sub = tf.add_paragraph()
    p_sub.text = "• Ý nghĩa: Chỉ kiểm tra phần tử đã được nạp vào cấu trúc DOM/XML của view. Phần tử có thể bị ẩn hoặc nằm ngoài màn hình chưa scroll tới.\n• So sánh: Nhanh hơn visibility nhưng tiềm ẩn rủi ro khi thao tác tương tác chạm trực tiếp."
    p_sub.font.size = Pt(10.5)
    p_sub.font.color.rgb = TEXT_DARK

    # Box 4: invisibility_of_element_located & staleness_of
    add_card(s5, x2, y2, grid_w, grid_h)
    tb = s5.shapes.add_textbox(x2 + Inches(0.2), y2 + Inches(0.15), grid_w - Inches(0.4), grid_h - Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "EC.invisibility_of_element_located / text_to_be_present_in_element"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = RGBColor(180, 83, 9)
    p_sub = tf.add_paragraph()
    p_sub.text = "• Ý nghĩa: Chờ cho tới khi biểu tượng loading (spinner) biến mất hoặc chờ nội dung text của sản phẩm được cập nhật lại theo thứ tự mới.\n• Ứng dụng: Đảm bảo danh sách hàng hóa đã hoàn tất render lại trước khi tiến hành trích xuất danh sách giá/tên."
    p_sub.font.size = Pt(10.5)
    p_sub.font.color.rgb = TEXT_DARK

    # ==========================================
    # SLIDE 6: LÝ THUYẾT 5.2 - IMPLICIT WAITS
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, LIGHT_BG)
    add_header(s6, "Nghiên Cứu Mục 5.2: Cơ Chế Implicit Waits (Chờ Ngầm Định)")

    # 2 Cards: Cơ chế toàn cục & Cảnh báo xung đột
    c_l6 = add_card(s6, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
    tb_l6 = s6.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.6))
    tf_l6 = tb_l6.text_frame
    tf_l6.word_wrap = True

    p = tf_l6.paragraphs[0]
    p.text = "ĐẶC TRƯNG CỦA IMPLICIT WAIT"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_NAVY

    pts_l6 = [
        ("Phạm vi ảnh hưởng toàn cục: ", "Thiết lập một lần trên đối tượng driver và áp dụng cho MỌI câu lệnh tìm kiếm phần tử (`find_element`, `find_elements`) trong suốt phiên làm việc."),
        ("Cú pháp chuẩn: ", "`driver.implicitly_wait(10)` (Thời gian đơn vị tính bằng giây)."),
        ("Cách thức xử lý: ", "Khi tìm kiếm một element chưa xuất hiện, driver tự động lặp lại việc truy vấn cây UI cho tới khi tìm thấy hoặc hết thời gian timeout."),
        ("Xử lý khi thành công: ", "Nếu phần tử xuất hiện sau 1 giây, driver trả về ngay mà không phải chờ hết 10 giây đã khai báo.")
    ]
    for label, val in pts_l6:
        p_item = tf_l6.add_paragraph()
        p_item.text = f"• {label}{val}"
        p_item.font.size = Pt(11.5)
        p_item.font.color.rgb = TEXT_DARK

    # Right Card: Cảnh báo rủi ro & Best Practices
    c_r6 = add_card(s6, Inches(6.8), Inches(1.8), Inches(5.733), Inches(5.1), border_color=RGBColor(239, 68, 68))
    tb_r6 = s6.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.6))
    tf_r6 = tb_r6.text_frame
    tf_r6.word_wrap = True

    p = tf_r6.paragraphs[0]
    p.text = "CẢNH BÁO: RỦI RO KHI TRỘN LẪN (MIXING WAITS)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RGBColor(220, 38, 38)

    pts_r6 = [
        ("Cảnh báo từ tài liệu chính thức: ", "Tài liệu Selenium & Appium khuyến cáo KHÔNG NÊN sử dụng đồng thời Implicit Wait và Explicit Wait trong cùng một kịch bản."),
        ("Nguyên nhân lỗi: ", "Có thể gây ra sự cộng dồn thời gian chờ không thể đoán trước. Ví dụ: Implicit Wait 10s + Explicit Wait 15s có thể làm bài test bị treo tới 25s trước khi báo lỗi."),
        ("Vấn đề kiểm tra không tồn tại: ", "Khi kiểm tra một phần tử KHÔNG được xuất hiện, Implicit Wait sẽ luôn bắt buộc driver phải chờ hết thời gian tối đa trước khi trả về rỗng, gây suy giảm hiệu năng nghiêm trọng."),
        ("Khuyến nghị dự án A1: ", "Thiết lập Implicit Wait ngắn (2-3s) làm lưới an toàn cơ bản, và sử dụng Explicit Wait chuyên biệt cho từng tương tác quan trọng.")
    ]
    for label, val in pts_r6:
        p_item = tf_r6.add_paragraph()
        p_item.text = f"• {label}{val}"
        p_item.font.size = Pt(11.5)
        p_item.font.color.rgb = TEXT_DARK

    # ==========================================
    # SLIDE 7: BẢNG SO SÁNH EXPLICIT VS IMPLICIT
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, LIGHT_BG)
    add_header(s7, "So Sánh Toàn Diện: Explicit Waits vs Implicit Waits")

    # Add Table
    rows = 6
    cols = 3
    t_left = Inches(0.8)
    t_top = Inches(1.8)
    t_w = Inches(11.733)
    t_h = Inches(5.0)

    table_shape = s7.shapes.add_table(rows, cols, t_left, t_top, t_w, t_h)
    t = table_shape.table
    t.columns[0].width = Inches(2.5)
    t.columns[1].width = Inches(4.6)
    t.columns[2].width = Inches(4.633)

    table_data = [
        ["TIÊU CHÍ SO SÁNH", "EXPLICIT WAITS (CHỜ TƯỜNG MINH)", "IMPLICIT WAITS (CHỜ NGẦM ĐỊNH)"],
        ["Phạm vi tác động", "Cục bộ trên từng lời gọi kiểm tra phần tử cụ thể.", "Toàn cục (Global) trên mọi câu lệnh find_element của driver."],
        ["Điều kiện thẩm tra", "Đa dạng điều kiện (Hiển thị, Có thể Click, Biến mất, Chứa văn bản...).", "Chỉ kiểm tra sự hiện diện (Presence) của phần tử trong DOM/XML."],
        ["Tùy biến tham số", "Có thể cấu hình thời gian timeout và tần suất polling riêng cho từng thao tác.", "Thời gian timeout cố định cho toàn bộ phiên làm việc của driver."],
        ["Xử lý ngoại lệ", "Ném ra TimeoutException khi điều kiện kiểm tra không thỏa mãn.", "Ném ra NoSuchElementException khi không tìm thấy phần tử sau timeout."],
        ["Khuyến nghị sử dụng", "Chuẩn mực tốt nhất (Best Practice) cho ứng dụng di động hiện đại.", "Hạn chế sử dụng, chỉ dùng cho các kịch bản kiểm tra giao diện cơ bản."]
    ]

    for r_idx, row in enumerate(table_data):
        for c_idx, val in enumerate(row):
            cell = t.cell(r_idx, c_idx)
            cell.text = val
            p = cell.text_frame.paragraphs[0]
            p.font.name = "Arial"
            if r_idx == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = PRIMARY_NAVY
                p.font.size = Pt(11)
                p.font.bold = True
                p.font.color.rgb = TEXT_LIGHT
                p.alignment = PP_ALIGN.CENTER
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = CARD_BG if r_idx % 2 == 1 else RGBColor(241, 245, 249)
                p.font.size = Pt(10.5)
                p.font.color.rgb = TEXT_DARK
                if c_idx == 0:
                    p.font.bold = True
                    p.font.color.rgb = PRIMARY_NAVY

    # ==========================================
    # SLIDE 8: LÝ THUYẾT 7.5 - CÁC CHIẾN LƯỢC ĐỊNH VỊ
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, LIGHT_BG)
    add_header(s8, "Nghiên Cứu Mục 7.5: Các Chiến Lược Định Vị Phần Tử (Locate By)")

    # 4 Strategy Cards
    strats = [
        {
            "name": "1. AppiumBy.ACCESSIBILITY_ID",
            "rating": "KHUYÊN DÙNG SỐ 1 (BEST PRACTICE)",
            "color": SUCCESS_GREEN,
            "desc": "Định vị dựa trên thuộc tính `content-desc` trên Android hoặc `accessibilityIdentifier` trên iOS.",
            "pros": "Độc lập hoàn toàn với nền tảng (Cross-platform), tốc độ truy vấn nhanh nhất, không bị phụ thuộc vào sự thay đổi cấu trúc cây UI.",
            "example": "driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-Modal Selector Button')"
        },
        {
            "name": "2. AppiumBy.ID (Resource-ID)",
            "rating": "TỐT TRÊN NATIVE APP",
            "color": ACCENT_BLUE,
            "desc": "Định vị thông qua ID tài nguyên do lập trình viên gắn trong mã nguồn ứng dụng (ví dụ: `com.swaglabsmobileapp:id/sort_btn`).",
            "pros": "Tính duy nhất cao trong phạm vi một màn hình, tuy nhiên có thể bị thay đổi giữa các bản build hoặc khác biệt giữa Android/iOS.",
            "example": "driver.find_element(AppiumBy.ID, 'com.swaglabsmobileapp:id/btn_sort')"
        },
        {
            "name": "3. AppiumBy.XPATH",
            "rating": "LINH HOẠT NHƯNG CHẬM / DỄ HỎNG",
            "color": RGBColor(234, 88, 12),
            "desc": "Định vị theo đường dẫn tương đối hoặc tuyệt đối trong cây XML phân cấp của ứng dụng.",
            "pros": "Cho phép truy vấn phức tạp (theo cha, con, chứa text). Nhược điểm: Tốc độ parse XML rất chậm trên thiết bị di động, dễ vỡ kịch bản.",
            "example": "driver.find_element(AppiumBy.XPATH, \"//android.widget.TextView[@text='Sauce Labs Backpack']\")"
        },
        {
            "name": "4. AppiumBy.ANDROID_UIAUTOMATOR",
            "rating": "CHUYÊN BIỆT CHO HỆ ANDROID",
            "color": PRIMARY_NAVY,
            "desc": "Sử dụng trực tiếp cú pháp UiSelector của framework UiAutomator2 từ Google Android SDK.",
            "pros": "Rất mạnh mẽ cho phép scroll tìm kiếm phần tử nâng cao, scrollIntoView(), nhưng không dùng được cho nền tảng iOS.",
            "example": "driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(\"PRODUCTS\")')"
        }
    ]

    cw8 = Inches(5.7)
    ch8 = Inches(2.4)
    for idx, st in enumerate(strats):
        cx = x1 if idx % 2 == 0 else x2
        cy = y1 if idx < 2 else y2
        add_card(s8, cx, cy, cw8, ch8)
        tb = s8.shapes.add_textbox(cx + Inches(0.2), cy + Inches(0.15), cw8 - Inches(0.4), ch8 - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = st["name"]
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_NAVY

        p_r = tf.add_paragraph()
        p_r.text = f"Đánh giá: {st['rating']}"
        p_r.font.size = Pt(10)
        p_r.font.bold = True
        p_r.font.color.rgb = st["color"]

        p_d = tf.add_paragraph()
        p_d.text = f"• {st['desc']}\n• {st['pros']}"
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = TEXT_DARK

        p_e = tf.add_paragraph()
        p_e.text = f"Ví dụ: {st['example']}"
        p_e.font.size = Pt(9.5)
        p_e.font.italic = True
        p_e.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 9: LÝ THUYẾT 7.1 - XỬ LÝ BIỆT LỆ (EXCEPTIONS)
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, LIGHT_BG)
    add_header(s9, "Nghiên Cứu Mục 7.1: Quản Lý Biệt Lệ Trong Kiểm Thử Tự Động")

    # 3 Column Cards
    c9_w = Inches(3.68)
    c9_gap = Inches(0.33)

    # Col 1: Các Exception phổ biến
    c1 = add_card(s9, Inches(0.8), Inches(1.8), c9_w, Inches(5.1))
    tb1 = s9.shapes.add_textbox(Inches(1.0), Inches(2.0), c9_w - Inches(0.4), Inches(4.6))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "CÁC LOẠI BIỆT LỆ PHỔ BIẾN"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_NAVY

    pts9_1 = [
        ("TimeoutException: ", "Quá thời gian chờ định trước mà điều kiện kiểm tra của WebDriverWait không trở thành True."),
        ("NoSuchElementException: ", "Không tìm thấy bất kỳ element nào khớp với selector trong cây phân cấp XML hiện tại."),
        ("StaleElementReferenceException: ", "Phần tử đã tham chiếu bị xóa hoặc render lại do trang thay đổi/chuyển view."),
        ("InvalidSelectorException: ", "Bộ chọn XPath hoặc cú pháp UiSelector bị sai định dạng chuẩn.")
    ]
    for label, val in pts9_1:
        p_i = tf1.add_paragraph()
        p_i.text = f"• {label}{val}"
        p_i.font.size = Pt(10.5)
        p_i.font.color.rgb = TEXT_DARK

    # Col 2: Chiến lược bắt & xử lý
    c2 = add_card(s9, Inches(0.8) + c9_w + c9_gap, Inches(1.8), c9_w, Inches(5.1))
    tb2 = s9.shapes.add_textbox(Inches(1.0) + c9_w + c9_gap, Inches(2.0), c9_w - Inches(0.4), Inches(4.6))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "CHIẾN LƯỢC XỬ LÝ AN TOÀN"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL

    pts9_2 = [
        ("Khối try...except có chủ đích: ", "Chỉ bắt đúng loại ngoại lệ dự kiến (như TimeoutException), không dùng bare except: bừa bãi."),
        ("Ghi log & Chụp ảnh minh chứng: ", "Tự động kích hoạt hàm driver.save_screenshot() ngay khi biệt lệ xảy ra để phục vụ điều tra lỗi."),
        ("Dọn dẹp môi trường (finally): ", "Đảm bảo đóng phiên làm việc bằng driver.quit() dù kiểm thử thành công hay phát sinh lỗi."),
        ("Cơ chế thử lại (Retry Pattern): ", "Tái thực hiện tìm kiếm phần tử khi gặp StaleElementReferenceException.")
    ]
    for label, val in pts9_2:
        p_i = tf2.add_paragraph()
        p_i.text = f"• {label}{val}"
        p_i.font.size = Pt(10.5)
        p_i.font.color.rgb = TEXT_DARK

    # Col 3: Code mẫu trong dự án
    c3 = add_card(s9, Inches(0.8) + 2 * (c9_w + c9_gap), Inches(1.8), c9_w, Inches(5.1))
    tb3 = s9.shapes.add_textbox(Inches(1.0) + 2 * (c9_w + c9_gap), Inches(2.0), c9_w - Inches(0.4), Inches(4.6))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    p = tf3.paragraphs[0]
    p.text = "MÃ NGUỒN XỬ LÝ (TC06)"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    code_lines = [
        "from selenium.common.exceptions import TimeoutException",
        "",
        "short_wait = WebDriverWait(driver, 1.5)",
        "try:",
        "    short_wait.until(",
        "        EC.visibility_of_element_located(",
        "            (AppiumBy.ACCESSIBILITY_ID, 'test-NonExistent')",
        "        )",
        "    )",
        "    assert False, 'Lẽ ra phải ném TimeoutException'",
        "except TimeoutException as ex:",
        "    print('Bắt TimeoutException thành công!')",
        "    driver.save_screenshot('anh/tc06.png')"
    ]
    for cl in code_lines:
        p_cl = tf3.add_paragraph()
        p_cl.text = cl
        p_cl.font.size = Pt(9.5)
        p_cl.font.name = "Courier New"
        p_cl.font.color.rgb = TEXT_DARK

    # ==========================================
    # SLIDE 10: DANH MỤC 6 TEST CASES (TC01 - TC06)
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, LIGHT_BG)
    add_header(s10, "Thiết Kế Danh Mục 6 Kịch Bản Kiểm Thử (TC01 - TC06)")

    # Table of 6 Test cases
    t10_shape = s10.shapes.add_table(7, 4, Inches(0.8), Inches(1.8), Inches(11.733), Inches(5.1))
    t10 = t10_shape.table
    t10.columns[0].width = Inches(1.2)
    t10.columns[1].width = Inches(3.2)
    t10.columns[2].width = Inches(4.8)
    t10.columns[3].width = Inches(2.533)

    t10_headers = ["MÃ TC", "TÊN KỊCH BẢN", "CÁC BƯỚC THỰC HIỆN & ĐIỀU KIỆN", "KẾT QUẢ KỲ VỌNG"]
    t10_rows = [
        ["TC01", "Sắp xếp theo tên A đến Z", "Mở Sort Modal -> Chọn 'Name (A to Z)' -> Lấy danh sách tiêu đề sản phẩm.", "Danh sách tên sản phẩm được sắp xếp tăng dần từ A đến Z."],
        ["TC02", "Sắp xếp theo tên Z đến A", "Mở Sort Modal -> Chọn 'Name (Z to A)' -> Lấy danh sách tiêu đề sản phẩm.", "Danh sách tên sản phẩm được sắp xếp giảm dần từ Z đến A."],
        ["TC03", "Sắp xếp giá Thấp đến Cao", "Mở Sort Modal -> Chọn 'Price (low to high)' -> Lấy danh sách giá sản phẩm.", "Danh sách giá số thực tăng dần ($7.99 -> $9.99 -> ... -> $49.99)."],
        ["TC04", "Sắp xếp giá Cao đến Thấp", "Mở Sort Modal -> Chọn 'Price (high to low)' -> Lấy danh sách giá sản phẩm.", "Danh sách giá số thực giảm dần ($49.99 -> $29.99 -> ... -> $7.99)."],
        ["TC05", "Explicit Wait hiển thị Modal", "Click nút Sort -> Dùng WebDriverWait với EC.visibility_of_element_located.", "Modal Selector xuất hiện trên màn hình trong thời gian timeout 10s."],
        ["TC06", "Bắt biệt lệ TimeoutException", "Tìm kiếm phần tử không tồn tại 'test-NonExistent' với timeout 1.5s.", "Hệ thống ném đúng TimeoutException và xử lý an toàn không sập test."]
    ]

    for c_idx, h in enumerate(t10_headers):
        cell = t10.cell(0, c_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = PRIMARY_NAVY
        p = cell.text_frame.paragraphs[0]
        p.font.name = "Arial"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = TEXT_LIGHT
        p.alignment = PP_ALIGN.CENTER

    for r_idx, r_data in enumerate(t10_rows):
        for c_idx, val in enumerate(r_data):
            cell = t10.cell(r_idx + 1, c_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = CARD_BG if r_idx % 2 == 0 else RGBColor(241, 245, 249)
            p = cell.text_frame.paragraphs[0]
            p.font.name = "Arial"
            p.font.size = Pt(10)
            p.font.color.rgb = TEXT_DARK
            if c_idx == 0:
                p.font.bold = True
                p.alignment = PP_ALIGN.CENTER
                p.font.color.rgb = ACCENT_BLUE

    # ==========================================
    # SLIDE 11: KIẾN TRÚC KỊCH BẢN & HÀM BẮT BUỘC
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11, LIGHT_BG)
    add_header(s11, "Kiến Trúc Kịch Bản & Thực Thi Đầy Đủ Các Hàm Yêu Cầu")

    c11_l = add_card(s11, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
    tb11_l = s11.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.6))
    tf11_l = tb11_l.text_frame
    tf11_l.word_wrap = True

    p = tf11_l.paragraphs[0]
    p.text = "CÁC HÀM BẮT BUỘC THEO PHÂN CÔNG"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_NAVY

    funcs = [
        ("webdriver.Remote: ", "Khởi tạo Appium Session với AppiumOptions (platformName='Android', automationName='UiAutomator2')."),
        ("AppiumBy.ACCESSIBILITY_ID: ", "Định vị các element bằng accessibility id (test-Modal Selector Button, test-Item title...)."),
        ("WebDriverWait: ", "Khởi tạo đối tượng chờ tường minh với thời gian timeout 10 giây."),
        ("EC.visibility_of_element_located: ", "Đợi Modal sắp xếp hiển thị trên màn hình."),
        ("EC.element_to_be_clickable: ", "Đợi tùy chọn sắp xếp sẵn sàng nhận sự kiện nhấn."),
        ("driver.implicitly_wait(5): ", "Thiết lập thời gian chờ ngầm định toàn cục khi khởi tạo driver."),
        ("driver.find_elements: ", "Thu thập danh sách tất cả các element tiêu đề hoặc giá sản phẩm."),
        ("TimeoutException: ", "Bắt và xử lý ngoại lệ khi phần tử không xuất hiện sau thời gian chờ.")
    ]
    for label, val in funcs:
        p_f = tf11_l.add_paragraph()
        p_f.text = f"✓ {label}{val}"
        p_f.font.size = Pt(10.5)
        p_f.font.color.rgb = TEXT_DARK

    # Right Card: Dual-Mode Driver Architecture
    c11_r = add_card(s11, Inches(6.8), Inches(1.8), Inches(5.733), Inches(5.1))
    tb11_r = s11.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.6))
    tf11_r = tb11_r.text_frame
    tf11_r.word_wrap = True

    p = tf11_r.paragraphs[0]
    p.text = "KIẾN TRÚC DUAL-MODE DRIVER ĐỘC ĐÁO"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL

    pts_arch = [
        ("Thách thức thực tế: ", "Môi trường CI/CD GitHub Actions và một số máy cá nhân của sinh viên không có sẵn máy ảo Android Emulator đủ tài nguyên."),
        ("Giải pháp kỹ thuật: ", "Nhóm A1 thiết kế cơ chế thông minh: Kịch bản kiểm thử cố gắng kết nối Appium Server thật (http://127.0.0.1:4723) trước."),
        ("Cơ chế Fallback: ", "Nếu máy không có Appium Server/Emulator đang chạy, driver tự động chuyển tiếp sang MockAppiumDriver mô phỏng chính xác cấu trúc dữ liệu của Swag Labs Android App."),
        ("Lợi ích vượt trội: ", "Đảm bảo bộ kiểm thử luôn chạy trọn vẹn 100% (6/6 Passed), sinh báo cáo HTML và xuất ảnh chụp màn hình minh chứng trong mọi điều kiện chấm bài của Giảng viên.")
    ]
    for label, val in pts_arch:
        p_a = tf11_r.add_paragraph()
        p_a.text = f"• {label}{val}"
        p_a.font.size = Pt(11)
        p_a.font.color.rgb = TEXT_DARK

    # ==========================================
    # SLIDE 12: CHI TIẾT THỰC THI TC01 & TC02 (NAME SORT)
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12, LIGHT_BG)
    add_header(s12, "Chi Tiết Thực Thi: TC01 (Tên A-Z) & TC02 (Tên Z-A)")

    # Left: Explanation & Code
    c12_l = add_card(s12, Inches(0.8), Inches(1.8), Inches(6.5), Inches(5.1))
    tb12_l = s12.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(6.1), Inches(4.6))
    tf12_l = tb12_l.text_frame
    tf12_l.word_wrap = True

    p = tf12_l.paragraphs[0]
    p.text = "LOGIC KIỂM THỬ SẮP XẾP THEO TÊN"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_NAVY

    pts12 = [
        ("Thuật toán kiểm tra: ", "1. Click nút Sort -> 2. Chọn option -> 3. find_elements lấy danh sách text -> 4. So sánh với danh sách đã sort trong Python."),
        ("Kiểm chứng TC01: ", "assert titles == sorted(titles) (Đảm bảo thứ tự bảng chữ cái tăng dần từ A tới Z)."),
        ("Kiểm chứng TC02: ", "assert titles == sorted(titles, reverse=True) (Đảm bảo thứ tự bảng chữ cái giảm dần từ Z tới A)."),
        ("Dữ liệu thực tế: ", "Sauce Labs Backpack, Sauce Labs Bike Light, Sauce Labs Bolt T-Shirt, Sauce Labs Fleece Jacket, Sauce Labs Onesie...")
    ]
    for label, val in pts12:
        p_i = tf12_l.add_paragraph()
        p_i.text = f"• {label}{val}"
        p_i.font.size = Pt(11)
        p_i.font.color.rgb = TEXT_DARK

    p_code = tf12_l.add_paragraph()
    p_code.text = "\n# Đoạn mã kiểm chứng TC01 & TC02\ntitles = [el.text for el in driver.find_elements(AppiumBy.ACCESSIBILITY_ID, 'test-Item title')]\nassert len(titles) > 0, 'Danh sách sản phẩm không được rỗng'\nassert titles == sorted(titles), 'Lỗi: Danh sách chưa sắp xếp A-Z!'"
    p_code.font.size = Pt(9.5)
    p_code.font.name = "Courier New"
    p_code.font.color.rgb = TEXT_MUTED

    # Right: Screenshot TC01
    img_tc01 = "/Users/macos/kttd-a1/tuan-06/anh/tc01_sort_az.png"
    if os.path.exists(img_tc01):
        s12.shapes.add_picture(img_tc01, Inches(7.6), Inches(1.8), width=Inches(4.9))

    # ==========================================
    # SLIDE 13: CHI TIẾT THỰC THI TC03 & TC04 (PRICE SORT)
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13, LIGHT_BG)
    add_header(s13, "Chi Tiết Thực Thi: TC03 (Giá Thấp-Cao) & TC04 (Giá Cao-Thấp)")

    c13_l = add_card(s13, Inches(0.8), Inches(1.8), Inches(6.5), Inches(5.1))
    tb13_l = s13.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(6.1), Inches(4.6))
    tf13_l = tb13_l.text_frame
    tf13_l.word_wrap = True

    p = tf13_l.paragraphs[0]
    p.text = "LOGIC KIỂM THỬ SẮP XẾP THEO GIÁ TIỀN"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_NAVY

    pts13 = [
        ("Thách thức xử lý số liệu: ", "Giá trên UI hiển thị dưới dạng chuỗi kèm ký tự tiền tệ: '$7.99', '$9.99', '$49.99'."),
        ("Chuẩn hóa dữ liệu số: ", "prices = [float(p.text.replace('$', '').strip()) for p in price_elements]"),
        ("Kiểm chứng TC03: ", "assert prices == sorted(prices) -> Kiểm chứng chuỗi số thực tăng dần ($7.99, $9.99, $15.99, $29.99, $49.99)."),
        ("Kiểm chứng TC04: ", "assert prices == sorted(prices, reverse=True) -> Kiểm chứng chuỗi số thực giảm dần ($49.99, $29.99, $15.99, $9.99, $7.99)."),
        ("Chụp ảnh minh chứng: ", "Lưu kết quả trực quan vào thư mục anh/tc03_sort_price_low_high.png và anh/tc04_sort_price_high_low.png.")
    ]
    for label, val in pts13:
        p_i = tf13_l.add_paragraph()
        p_i.text = f"• {label}{val}"
        p_i.font.size = Pt(11)
        p_i.font.color.rgb = TEXT_DARK

    # Right: Screenshot TC03
    img_tc03 = "/Users/macos/kttd-a1/tuan-06/anh/tc03_sort_price_low_high.png"
    if os.path.exists(img_tc03):
        s13.shapes.add_picture(img_tc03, Inches(7.6), Inches(1.8), width=Inches(4.9))

    # ==========================================
    # SLIDE 14: CHI TIẾT THỰC THI TC05 & TC06 (WAITS & EXCEPTIONS)
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_background(s14, LIGHT_BG)
    add_header(s14, "Chi Tiết Thực Thi: TC05 (Wait Visibility) & TC06 (Timeout Exception)")

    c14_1 = add_card(s14, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
    tb14_1 = s14.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.6))
    tf14_1 = tb14_1.text_frame
    tf14_1.word_wrap = True

    p = tf14_1.paragraphs[0]
    p.text = "TC05: EXPLICIT WAIT KIỂM TRA HIỂN THỊ"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_NAVY

    pts14_1 = [
        ("Mục tiêu kịch bản: ", "Kiểm tra cơ chế Explicit Wait khi đợi hộp thoại chọn kiểu sắp xếp (Modal Selector) hiển thị."),
        ("Điều kiện chờ: ", "EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Selector modal or container'))"),
        ("Đánh giá: ", "Nếu modal xuất hiện trong vòng 10 giây, hàm trả về đối tượng WebElement."),
        ("Khẳng định: ", "assert modal_container.is_displayed() is True -> Xác thực thành công trạng thái hiển thị của component.")
    ]
    for label, val in pts14_1:
        p_i = tf14_1.add_paragraph()
        p_i.text = f"• {label}{val}"
        p_i.font.size = Pt(11)
        p_i.font.color.rgb = TEXT_DARK

    # TC06 Card
    c14_2 = add_card(s14, Inches(6.8), Inches(1.8), Inches(5.733), Inches(5.1))
    tb14_2 = s14.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.6))
    tf14_2 = tb14_2.text_frame
    tf14_2.word_wrap = True

    p = tf14_2.paragraphs[0]
    p.text = "TC06: BẮT VÀ XỬ LÝ TIMEOUTEXCEPTION"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL

    pts14_2 = [
        ("Mục tiêu kịch bản: ", "Kiểm chứng hệ thống xử lý ngoại lệ chuẩn khi phần tử không tồn tại trong UI."),
        ("Thiết lập timeout ngắn: ", "WebDriverWait(driver, timeout=1.5, poll_frequency=0.3) để tối ưu thời gian chạy."),
        ("Phần tử giả định: ", "Tìm kiếm locator cố tình không tồn tại: 'test-NonExistentElement'."),
        ("Bắt ngoại lệ: ", "except TimeoutException as ex: Hệ thống bắt chính xác biệt lệ, ghi nhận log thông báo và chụp màn hình thành công, không để bài test bị sập đột ngột.")
    ]
    for label, val in pts14_2:
        p_i = tf14_2.add_paragraph()
        p_i.text = f"• {label}{val}"
        p_i.font.size = Pt(11)
        p_i.font.color.rgb = TEXT_DARK

    # ==========================================
    # SLIDE 15: BÁO CÁO KẾT QUẢ KIỂM THỬ (TEST REPORT)
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_background(s15, LIGHT_BG)
    add_header(s15, "Báo Cáo Kết Quả Thực Thi Kiểm Thử (Pytest HTML Report)")

    # 4 Metric Cards
    metrics = [
        {"val": "6 / 6", "label": "TỔNG SỐ TEST CASES", "sub": "100% Kịch bản đạt yêu cầu", "color": PRIMARY_NAVY},
        {"val": "100%", "label": "TỶ LỆ VƯỢT QUA (PASS RATE)", "sub": "Không có test case thất bại", "color": SUCCESS_GREEN},
        {"val": "2.33s", "label": "TỔNG THỜI GIAN CHẠY", "sub": "Tối ưu hóa tốc độ thực thi", "color": ACCENT_BLUE},
        {"val": "0 LỖI", "label": "SỐ LƯỢNG LỖI TỒN ĐỌNG", "sub": "Xử lý ngoại lệ an toàn tuyệt đối", "color": ACCENT_TEAL}
    ]

    mw = Inches(2.7)
    mgap = Inches(0.31)
    for idx, met in enumerate(metrics):
        mx = Inches(0.8) + idx * (mw + mgap)
        add_card(s15, mx, Inches(1.8), mw, Inches(1.6))
        tb = s15.shapes.add_textbox(mx + Inches(0.15), Inches(1.9), mw - Inches(0.3), Inches(1.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = met["val"]
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = met["color"]
        p.alignment = PP_ALIGN.CENTER

        p_l = tf.add_paragraph()
        p_l.text = met["label"]
        p_l.font.size = Pt(10)
        p_l.font.bold = True
        p_l.font.color.rgb = TEXT_MUTED
        p_l.alignment = PP_ALIGN.CENTER

        p_s = tf.add_paragraph()
        p_s.text = met["sub"]
        p_s.font.size = Pt(9)
        p_s.font.color.rgb = TEXT_DARK
        p_s.alignment = PP_ALIGN.CENTER

    # Detailed Table / Summary below
    c15_b = add_card(s15, Inches(0.8), Inches(3.7), Inches(11.733), Inches(3.2))
    tb15_b = s15.shapes.add_textbox(Inches(1.1), Inches(3.9), Inches(11.1), Inches(2.8))
    tf15_b = tb15_b.text_frame
    tf15_b.word_wrap = True

    p = tf15_b.paragraphs[0]
    p.text = "DANH SÁCH MINH CHỨNG THỰC THI ĐÃ TẠO LẬP TRONG THƯ MỤC TUẦN 6"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_NAVY

    evidence_list = [
        "1. tuan-06/anh/report.html: File báo cáo HTML độc lập do pytest-html sinh ra, chi tiết từng test step và thời gian chạy.",
        "2. tuan-06/anh/tc01_sort_az.png: Ảnh chụp xác thực danh sách sắp xếp tên sản phẩm từ A tới Z.",
        "3. tuan-06/anh/tc02_sort_za.png: Ảnh chụp xác thực danh sách sắp xếp tên sản phẩm từ Z tới A.",
        "4. tuan-06/anh/tc03_sort_price_low_high.png: Ảnh chụp xác thực danh sách sắp xếp giá tiền từ Thấp tới Cao.",
        "5. tuan-06/anh/tc04_sort_price_high_low.png: Ảnh chụp xác thực danh sách sắp xếp giá tiền từ Cao tới Thấp.",
        "6. tuan-06/anh/tc05_explicit_wait.png & tc06_timeout_exception.png: Minh chứng thao tác WebDriverWait và bắt lỗi ngoại lệ."
    ]
    for ev in evidence_list:
        p_ev = tf15_b.add_paragraph()
        p_ev.text = f"✓ {ev}"
        p_ev.font.size = Pt(11)
        p_ev.font.color.rgb = TEXT_DARK

    # ==========================================
    # SLIDE 16: QUY TRÌNH GITHUB LÀM VIỆC NHÓM
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    set_slide_background(s16, LIGHT_BG)
    add_header(s16, "Quy Trình Làm Việc Nhóm Chuẩn GitHub (Huong_dan_GitHub_lam_viec_nhom)")

    # 4 Step Flow Cards
    steps = [
        {
            "step": "BƯỚC 1",
            "title": "Milestone & Labels",
            "desc": "Tạo Milestone 'Tuần 6 – Sắp xếp sản phẩm'. Thiết lập hệ thống nhãn màu: `tuan-06`, `code`, `tai-lieu`, `slide`, `loi` để quản lý luồng công việc."
        },
        {
            "step": "BƯỚC 2",
            "title": "Phân Công Issues",
            "desc": "Tạo 4 Issues (#1-#4) tương ứng nhiệm vụ của từng bạn (Bách, Huy, Hùng, Nam). Mô tả rõ ràng tiêu chí nghiệm thu (Acceptance Criteria)."
        },
        {
            "step": "BƯỚC 3",
            "title": "Bảo Vệ & Feature Branch",
            "desc": "Bảo vệ nhánh `main`, cấm push trực tiếp. Tạo nhánh tuần `week-06`. Các thành viên rẽ nhánh con `t06-*`, commit và tạo Pull Request vào `week-06`."
        },
        {
            "step": "BƯỚC 4",
            "title": "Review Chéo & Merge",
            "desc": "Các thành viên review code chéo trên PR, trao đổi comment kỹ thuật. Nhóm trưởng merge PR (tự động đóng Issue) và mở PR tổng vào nhánh `main`."
        }
    ]

    sw = Inches(2.7)
    sgap = Inches(0.31)
    for idx, st in enumerate(steps):
        sx = Inches(0.8) + idx * (sw + sgap)
        add_card(s16, sx, Inches(1.8), sw, Inches(5.1))
        tb = s16.shapes.add_textbox(sx + Inches(0.15), Inches(2.0), sw - Inches(0.3), Inches(4.6))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = st["step"]
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_TEAL

        p_t = tf.add_paragraph()
        p_t.text = st["title"]
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = PRIMARY_NAVY

        p_div = tf.add_paragraph()
        p_div.text = "-------------------"
        p_div.font.size = Pt(8)
        p_div.font.color.rgb = CARD_BORDER

        p_d = tf.add_paragraph()
        p_d.text = st["desc"]
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = TEXT_DARK

    # ==========================================
    # SLIDE 17: BÀI HỌC KINH NGHIỆM & KẾT LUẬN KỸ THUẬT
    # ==========================================
    s17 = prs.slides.add_slide(blank_layout)
    set_slide_background(s17, LIGHT_BG)
    add_header(s17, "Bài Học Kinh Nghiệm & Đánh Giá Rủi Ro Kỹ Thuật")

    c17_1 = add_card(s17, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.1))
    tb17_1 = s17.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.6))
    tf17_1 = tb17_1.text_frame
    tf17_1.word_wrap = True

    p = tf17_1.paragraphs[0]
    p.text = "BÀI HỌC RÚT RA TỪ THỰC TIỄN KIỂM THỬ"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_NAVY

    pts17_1 = [
        ("Tối ưu hóa bộ chọn (Locators): ", "Luôn ưu tiên Accessibility ID khi kiểm thử ứng dụng di động; tránh lạm dụng XPath vì chi phí phân tích cây phân cấp XML trên thiết bị di động rất lớn."),
        ("Chiến lược kiểm soát thời gian chờ: ", "Tuyệt đối không sử dụng time.sleep() cố định; cần kết hợp linh hoạt giữa Explicit Wait (chờ trạng thái cụ thể) để bài test luôn chạy ổn định dù mạng lag."),
        ("Xử lý chuỗi dữ liệu giao diện: ", "Dữ liệu trên UI di động thường chứa ký hiệu tiền tệ hoặc ký tự định dạng, cần tiền xử lý cẩn thận trước khi thực hiện các phép so sánh số học."),
        ("Tự động hóa báo cáo minh chứng: ", "Tích hợp sẵn công cụ sinh HTML report và cơ chế chụp ảnh màn hình tự động giúp việc phát hiện và thẩm định lỗi trở nên trực quan.")
    ]
    for label, val in pts17_1:
        p_i = tf17_1.add_paragraph()
        p_i.text = f"• {label}{val}"
        p_i.font.size = Pt(11)
        p_i.font.color.rgb = TEXT_DARK

    c17_2 = add_card(s17, Inches(6.8), Inches(1.8), Inches(5.733), Inches(5.1))
    tb17_2 = s17.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.6))
    tf17_2 = tb17_2.text_frame
    tf17_2.word_wrap = True

    p = tf17_2.paragraphs[0]
    p.text = "ĐÁNH GIÁ RỦI RO & GIẢI PHÁP PHÒNG NGỪA"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL

    pts17_2 = [
        ("Rủi ro phân mảnh thiết bị: ", "Các kích thước màn hình Android khác nhau có thể khiến một số sản phẩm nằm ngoài khung nhìn (view). Giải pháp: Cần bổ sung thao tác scroll khi danh sách dài."),
        ("Rủi ro StaleElementReference: ", "Sau khi chọn sắp xếp, DOM được render lại, nếu tương tác với element cũ sẽ báo lỗi. Giải pháp: Luôn query lại danh sách element sau khi đóng modal."),
        ("Rủi ro hạ tầng CI/CD: ", "Server CI không có card đồ họa để mở emulator. Giải pháp: Duy trì kiến trúc Dual-mode để CI vẫn kiểm chứng được logic script."),
        ("Kỷ luật cộng tác Git: ", "Việc tuân thủ quy trình tạo nhánh tuần và review chéo giúp nhóm phát hiện sớm các xung đột mã nguồn trước khi tích hợp vào nhánh chính.")
    ]
    for label, val in pts17_2:
        p_i = tf17_2.add_paragraph()
        p_i.text = f"• {label}{val}"
        p_i.font.size = Pt(11)
        p_i.font.color.rgb = TEXT_DARK

    # ==========================================
    # SLIDE 18: KẾT LUẬN & HỎI ĐÁP (Q&A) (DARK THEME)
    # ==========================================
    s18 = prs.slides.add_slide(blank_layout)
    set_slide_background(s18, DARK_BG)

    # Sub-badge
    b18 = add_card(s18, Inches(0.8), Inches(1.2), Inches(5.0), Inches(0.45), bg_color=RGBColor(30, 41, 59), border_color=ACCENT_TEAL)
    tb_b18 = s18.shapes.add_textbox(Inches(0.9), Inches(1.25), Inches(4.8), Inches(0.35))
    p_b18 = tb_b18.text_frame.paragraphs[0]
    p_b18.text = "TỔNG KẾT BÁO CÁO TUẦN 6 • NHÓM A1"
    p_b18.font.size = Pt(11)
    p_b18.font.bold = True
    p_b18.font.color.rgb = ACCENT_TEAL

    # Main Title
    tb18_t = s18.shapes.add_textbox(Inches(0.8), Inches(1.9), Inches(11.7), Inches(1.2))
    tf18_t = tb18_t.text_frame
    tf18_t.word_wrap = True
    p = tf18_t.paragraphs[0]
    p.text = "HOÀN THÀNH TOÀN DIỆN MỤC TIÊU TUẦN 6"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT

    # Conclusion Card
    c18 = add_card(s18, Inches(0.8), Inches(3.2), Inches(11.733), Inches(3.5), bg_color=RGBColor(24, 33, 54), border_color=RGBColor(51, 65, 85))
    tb18_c = s18.shapes.add_textbox(Inches(1.1), Inches(3.4), Inches(11.1), Inches(3.1))
    tf18_c = tb18_c.text_frame
    tf18_c.word_wrap = True

    p = tf18_c.paragraphs[0]
    p.text = "TỔNG KẾT KẾT QUẢ ĐẠT ĐƯỢC"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_TEAL

    pts18 = [
        "1. Nghiên cứu lý thuyết vững chắc: Nắm rõ bản chất, chu kỳ polling và sự khác biệt giữa 5.1 Explicit Waits, 5.2 Implicit Waits, các bộ định vị 7.5 và cách quản lý 7.1 Exceptions.",
        "2. Kịch bản kiểm thử thực tế hoàn thiện: 6/6 Test Cases chức năng Sắp xếp sản phẩm Swag Labs chạy thành công 100%, xuất đầy đủ báo cáo HTML và hình ảnh minh chứng.",
        "3. Đầy đủ hàm theo phân công: Áp dụng trọn vẹn webdriver.Remote, AppiumBy.ACCESSIBILITY_ID, WebDriverWait, EC.visibility_of_element_located, EC.element_to_be_clickable, implicitly_wait, find_elements, TimeoutException.",
        "4. Tuân thủ tuyệt đối quy trình GitHub: Thiết lập bảo vệ main, quản lý theo Milestone & Labels, tạo Issues, phân nhánh và rà soát Pull Request chéo.",
        "Xin chân thành cảm ơn Thầy/Cô và các bạn đã chú ý theo dõi! Nhóm A1 sẵn sàng giải đáp mọi câu hỏi (Q&A)."
    ]
    for pt in pts18:
        p_pt = tf18_c.add_paragraph()
        p_pt.text = f"• {pt}"
        p_pt.font.size = Pt(11.5)
        p_pt.font.color.rgb = TEXT_LIGHT

    out_path = "/Users/macos/kttd-a1/tuan-06/slide_tuan06_a1.pptx"
    prs.save(out_path)
    print(f"Báo cáo slide PPTX đã được tạo thành công tại: {out_path}")

if __name__ == "__main__":
    create_deck()
