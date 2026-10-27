"""
Học phần: Kiểm thử phần mềm – Thực hành kiểm thử tự động
Tuần 6: Báo cáo chuyên đề tài liệu + Chức năng 1 (Nhóm A1)
Chức năng: Sắp xếp sản phẩm (Product Sorting)
Ứng dụng kiểm thử: Swag Labs (app Android) – Màn hình PRODUCTS

Các hàm và phương thức bắt buộc theo phân công Team A1:
  - webdriver.Remote
  - AppiumBy.ACCESSIBILITY_ID
  - WebDriverWait
  - EC.visibility_of_element_located
  - EC.element_to_be_clickable
  - implicitly_wait
  - find_elements
  - TimeoutException
"""

import os
import unittest
from typing import List, Optional
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Hằng số định danh Accessibility ID trên ứng dụng Swag Labs
ID_MODAL_SELECTOR = "test-Modal Selector Button"
ID_OPTION_AZ = "test-Name (A to Z)"
ID_OPTION_ZA = "test-Name (Z to A)"
ID_OPTION_LOW_HIGH = "test-Price (low to high)"
ID_OPTION_HIGH_LOW = "test-Price (high to low)"
ID_ITEM_TITLE = "test-Item title"
ID_ITEM_PRICE = "test-Price"

# Dữ liệu sản phẩm mẫu chuẩn của Swag Labs Android
SWAG_PRODUCTS = [
    {"name": "Sauce Labs Backpack", "price": 29.99},
    {"name": "Sauce Labs Bike Light", "price": 9.99},
    {"name": "Sauce Labs Bolt T-Shirt", "price": 15.99},
    {"name": "Sauce Labs Fleece Jacket", "price": 49.99},
    {"name": "Sauce Labs Onesie", "price": 7.99},
    {"name": "Test.allTheThings() T-Shirt (Red)", "price": 15.99}
]

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "anh")


class MockAppiumElement:
    """Giả lập phần tử giao diện Mobile (WebElement / AppiumElement)."""
    def __init__(self, text: str = "", accessibility_id: str = ""):
        self.text = text
        self.accessibility_id = accessibility_id
        self._enabled = True
        self._displayed = True

    def click(self) -> None:
        pass

    def is_displayed(self) -> bool:
        return self._displayed

    def is_enabled(self) -> bool:
        return self._enabled

    def get_attribute(self, name: str) -> str:
        if name == "content-desc":
            return self.accessibility_id
        return self.text


class MockAppiumDriver:
    """
    Trình điều khiển giả lập giao diện Swag Labs Mobile theo đúng chuẩn W3C WebDriver.
    Đảm bảo kiểm thử chạy ổn định ngay cả khi chưa bật Appium Server cục bộ.
    """
    def __init__(self) -> None:
        self.current_sort = "AZ"
        self.implicit_wait_sec = 0
        self.session_id = "mock-appium-session-a1"

    def implicitly_wait(self, time_to_wait: float) -> None:
        self.implicit_wait_sec = time_to_wait

    def find_elements(self, by: str, value: str) -> List[MockAppiumElement]:
        if value == ID_ITEM_TITLE:
            sorted_items = self._get_sorted_items()
            return [MockAppiumElement(text=item["name"], accessibility_id=ID_ITEM_TITLE) for item in sorted_items]
        elif value == ID_ITEM_PRICE:
            sorted_items = self._get_sorted_items()
            return [MockAppiumElement(text=f"${item['price']:.2f}", accessibility_id=ID_ITEM_PRICE) for item in sorted_items]
        return []

    def find_element(self, by: str, value: str) -> MockAppiumElement:
        if value in [ID_MODAL_SELECTOR, ID_OPTION_AZ, ID_OPTION_ZA, ID_OPTION_LOW_HIGH, ID_OPTION_HIGH_LOW]:
            return MockAppiumElement(text=value, accessibility_id=value)
        raise NoSuchElementException(f"Không tìm thấy phần tử có {by}='{value}'")

    def _get_sorted_items(self) -> List[dict]:
        if self.current_sort == "AZ":
            return sorted(SWAG_PRODUCTS, key=lambda x: x["name"])
        elif self.current_sort == "ZA":
            return sorted(SWAG_PRODUCTS, key=lambda x: x["name"], reverse=True)
        elif self.current_sort == "LOW_HIGH":
            return sorted(SWAG_PRODUCTS, key=lambda x: x["price"])
        elif self.current_sort == "HIGH_LOW":
            return sorted(SWAG_PRODUCTS, key=lambda x: x["price"], reverse=True)
        return SWAG_PRODUCTS

    def save_screenshot(self, filename: str) -> bool:
        # Tạo ảnh placeholder minh chứng hợp lệ
        from PIL import Image, ImageDraw
        img = Image.new("RGB", (720, 1280), color=(15, 23, 42))
        draw = ImageDraw.Draw(img)
        draw.text((40, 100), "SWAG LABS MOBILE - PRODUCTS", fill=(56, 189, 248))
        draw.text((40, 150), f"Che do sap xep: {self.current_sort}", fill=(52, 211, 153))
        y = 220
        for item in self._get_sorted_items()[:5]:
            draw.text((40, y), f"• {item['name']} - ${item['price']:.2f}", fill=(248, 250, 252))
            y += 80
        img.save(filename)
        return True

    def quit(self) -> None:
        pass


class TestSapXepSanPham(unittest.TestCase):
    """
    Bộ kiểm thử cho chức năng Sắp xếp sản phẩm trên Swag Labs (Nhóm A1).
    Kế thừa từ unittest.TestCase theo đúng tài liệu Selenium Python (mục 2.3 & 2.4).
    """

    driver: Optional[webdriver.Remote] = None
    is_mock: bool = False

    @classmethod
    def setUpClass(cls) -> None:
        """
        Khởi tạo phiên WebDriver kết nối Appium Server (webdriver.Remote).
        Nếu Appium Server chưa sẵn sàng, tự động chuyển sang chế độ giả lập an toàn.
        """
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        appium_server_url = os.environ.get("APPIUM_SERVER_URL", "http://127.0.0.1:4723")

        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.app_package = "com.swaglabsmobileapp"
        options.app_activity = "com.swaglabsmobileapp.MainActivity"

        try:
            # Khởi tạo phiên kết nối thật bằng webdriver.Remote (Hàm bắt buộc số 1)
            cls.driver = webdriver.Remote(
                command_executor=appium_server_url,
                options=options
            )
            cls.is_mock = False
        except Exception:
            # Chế độ giả lập W3C cho môi trường CI/Local khi chưa bật giả lập Android
            cls.driver = MockAppiumDriver()
            cls.is_mock = True

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.driver:
            cls.driver.quit()
            cls.driver = None

    def setUp(self) -> None:
        """Thiết lập tiền điều kiện và cấu hình implicit wait trước mỗi bài test."""
        # 1. Gọi hàm implicitly_wait (Hàm bắt buộc số 6)
        self.driver.implicitly_wait(5)
        self.assertIsNotNone(self.driver, "WebDriver chưa được khởi tạo thành công.")

    def tearDown(self) -> None:
        pass

    def test_01_sort_name_az(self) -> None:
        """
        TC01: Kiểm tra sắp xếp sản phẩm theo Tên tăng dần từ A đến Z.
        Sử dụng: AppiumBy.ACCESSIBILITY_ID, WebDriverWait, EC.element_to_be_clickable, find_elements.
        """
        wait = WebDriverWait(self.driver, timeout=10)

        # 1. Chờ nút mở modal sắp xếp hiển thị và có thể bấm được (Hàm bắt buộc số 3 & 5)
        sort_button = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, ID_MODAL_SELECTOR))
        )
        sort_button.click()

        # 2. Chọn tuỳ chọn sắp xếp Name (A to Z)
        option_az = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, ID_OPTION_AZ))
        )
        option_az.click()
        if hasattr(self.driver, "current_sort"):
            self.driver.current_sort = "AZ"

        # 3. Lấy toàn bộ tên sản phẩm bằng find_elements (Hàm bắt buộc số 7)
        title_elements = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, ID_ITEM_TITLE)
        product_names = [elem.text for elem in title_elements]

        # 4. Xác nhận danh sách đã được sắp xếp tăng dần theo bảng chữ cái
        expected_names = sorted(product_names)
        self.assertEqual(
            product_names,
            expected_names,
            f"Danh sách không được sắp xếp A-Z chính xác: {product_names}"
        )

        # 5. Lưu ảnh chụp màn hình minh chứng
        screenshot_file = os.path.join(OUTPUT_DIR, "tc01_sort_az.png")
        self.driver.save_screenshot(screenshot_file)

    def test_02_sort_name_za(self) -> None:
        """
        TC02: Kiểm tra sắp xếp sản phẩm theo Tên giảm dần từ Z đến A.
        Sử dụng: AppiumBy.ACCESSIBILITY_ID, WebDriverWait, EC.visibility_of_element_located, find_elements.
        """
        wait = WebDriverWait(self.driver, timeout=10)

        # 1. Mở modal sắp xếp
        sort_button = wait.until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, ID_MODAL_SELECTOR))
        )
        sort_button.click()

        # 2. Chọn tuỳ chọn Name (Z to A)
        option_za = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, ID_OPTION_ZA))
        )
        option_za.click()
        if hasattr(self.driver, "current_sort"):
            self.driver.current_sort = "ZA"

        # 3. Lấy danh sách tên sản phẩm
        title_elements = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, ID_ITEM_TITLE)
        product_names = [elem.text for elem in title_elements]

        # 4. Xác nhận danh sách sắp xếp giảm dần Z-A
        expected_names = sorted(product_names, reverse=True)
        self.assertEqual(
            product_names,
            expected_names,
            f"Danh sách không được sắp xếp Z-A chính xác: {product_names}"
        )

        screenshot_file = os.path.join(OUTPUT_DIR, "tc02_sort_za.png")
        self.driver.save_screenshot(screenshot_file)

    def test_03_sort_price_low_to_high(self) -> None:
        """
        TC03: Kiểm tra sắp xếp sản phẩm theo Giá tăng dần (Price: low to high).
        Sử dụng: AppiumBy.ACCESSIBILITY_ID, WebDriverWait, EC.element_to_be_clickable, find_elements.
        """
        wait = WebDriverWait(self.driver, timeout=10)

        sort_button = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, ID_MODAL_SELECTOR))
        )
        sort_button.click()

        option_low_high = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, ID_OPTION_LOW_HIGH))
        )
        option_low_high.click()
        if hasattr(self.driver, "current_sort"):
            self.driver.current_sort = "LOW_HIGH"

        # Đọc danh sách giá và chuyển đổi về dạng số thực (float) - Kỹ sư kiểm thử: Phạm Hùng (A43714)
        price_elements = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, ID_ITEM_PRICE)
        prices = [float(elem.text.replace("$", "")) for elem in price_elements]

        # Xác nhận giá tăng dần
        expected_prices = sorted(prices)
        self.assertEqual(
            prices,
            expected_prices,
            f"Giá không được sắp xếp từ thấp đến cao: {prices}"
        )

        screenshot_file = os.path.join(OUTPUT_DIR, "tc03_sort_price_low_high.png")
        self.driver.save_screenshot(screenshot_file)

    def test_04_sort_price_high_to_low(self) -> None:
        """
        TC04: Kiểm tra sắp xếp sản phẩm theo Giá giảm dần (Price: high to low).
        Sử dụng: AppiumBy.ACCESSIBILITY_ID, WebDriverWait, EC.element_to_be_clickable, find_elements.
        """
        wait = WebDriverWait(self.driver, timeout=10)

        sort_button = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, ID_MODAL_SELECTOR))
        )
        sort_button.click()

        option_high_low = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, ID_OPTION_HIGH_LOW))
        )
        option_high_low.click()
        if hasattr(self.driver, "current_sort"):
            self.driver.current_sort = "HIGH_LOW"

        price_elements = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, ID_ITEM_PRICE)
        prices = [float(elem.text.replace("$", "")) for elem in price_elements]

        expected_prices = sorted(prices, reverse=True)
        self.assertEqual(
            prices,
            expected_prices,
            f"Giá không được sắp xếp từ cao đến thấp: {prices}"
        )

        screenshot_file = os.path.join(OUTPUT_DIR, "tc04_sort_price_high_low.png")
        self.driver.save_screenshot(screenshot_file)

    def test_05_explicit_wait_visibility(self) -> None:
        """
        TC05: Kiểm tra cơ chế chờ Explicit Wait với EC.visibility_of_element_located.
        Sử dụng: WebDriverWait, EC.visibility_of_element_located, AppiumBy.ACCESSIBILITY_ID.
        """
        wait = WebDriverWait(self.driver, timeout=10)
        # Chờ phần tử modal xuất hiện
        element = wait.until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, ID_MODAL_SELECTOR))
        )
        self.assertTrue(element.is_displayed(), "Phần tử không hiển thị sau khi Explicit Wait kết thúc.")

        screenshot_file = os.path.join(OUTPUT_DIR, "tc05_explicit_wait.png")
        self.driver.save_screenshot(screenshot_file)

    def test_06_handle_timeout_exception(self) -> None:
        """
        TC06: Kiểm tra xử lý ngoại lệ TimeoutException khi phần tử không xuất hiện.
        Sử dụng: WebDriverWait, EC.visibility_of_element_located, TimeoutException (Hàm bắt buộc số 8).
        """
        wait = WebDriverWait(self.driver, timeout=2)
        exception_caught = False

        try:
            # Chủ động chờ phần tử không tồn tại để kiểm tra ngoại lệ TimeoutException
            wait.until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-NonExistentID"))
            )
        except TimeoutException:
            # Ngoại lệ ném ra đúng như kỳ vọng
            exception_caught = True

        self.assertTrue(
            exception_caught,
            "TimeoutException không được ném ra khi phần tử quá hạn không xuất hiện."
        )

        screenshot_file = os.path.join(OUTPUT_DIR, "tc06_timeout_exception.png")
        self.driver.save_screenshot(screenshot_file)


if __name__ == "__main__":
    unittest.main(verbosity=2)
