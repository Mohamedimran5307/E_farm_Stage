from Pageobjects.LanguagePage import Language_page
from Pageobjects.Farmer_registry_page import Farmer_registry
from Pageobjects.Procurement_page import Procurement
from Pageobjects.Product_page import Product


class Flow_of_test:
    def __init__(self, driver):
        self.driver = driver
        self.language_page = Language_page(self.driver)
        self.login_page = None
        self.order_page = None
        self.farmer_registry = None
        self.procurement = None
        self.product = None

    def navigate_to_language_page(self):
        # Assuming the driver is already on the correct starting URL
        self.language_page = Language_page(self.driver)
        return self

    def perform_language_selection_page_action(self):
        return self.language_page.language_selection_page()

    def login(self, usernumber, OTP_1, OTP_2, OTP_3, OTP_4, OTP_5, OTP_6):
        self.login_page = self.language_page.language_selection_page()
        self.order_page = self.login_page.user_number_page(usernumber, OTP_1, OTP_2, OTP_3, OTP_4, OTP_5, OTP_6)
        return self

    def navigate_to_farmer_registry(self):
        # Assuming there's a method in Farmer_registry_section to navigate to Farmer Registry
        # If not, you might need to implement this navigation in the Farmer_registry_section class
        self.farmer_registry = Farmer_registry(self.driver)
        return self

    def perform_farmer_registry_action(self):
        return self.farmer_registry.Farmer_registry_section()

    def navigate_to_procurement_page(self):
        # Assuming there's a method in Procurement_section to navigate to Procurement
        # If not, you might need to implement this navigation in the Procurement_section class
        self.procurement = Procurement(self.driver)
        return self

    def perform_procurement_action(self):
        return self.procurement.Procurement_section()

    def perform_procurement_action_2(self):
        return self.procurement.Procurement_Cancel()

    def navigate_to_product_page(self):
        # Assuming there's a method in Product_section to navigate to Product
        # If not, you might need to implement this navigation in the Product_section class
        self.product = Product(self.driver)
        return self

    def perform_product_action(self):
        return self.product.Product_section()
