from selenium import webdriver
import os
from Booking.Booking_filtration import BookingFiltration
from Booking.booking_report import BookingReport
from selenium.webdriver.common.by import By
from prettytable import PrettyTable

class Booking(webdriver.Chrome):
    def __init__(self, driver_path="C:\\Users\\ASUS\\Desktop\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe",teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        super().__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val,exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get("https://www.booking.com/booking-home/index.en-gb.html?aid=304142&label=gen173bo-1DCAEoggI46AdIM1gDaGyIAQGYATG4ARfIAQzYAQPoAQH4AQOIAgGYAgKoAgO4AueIt6YGwAIB0gIkNjY3NTczOGMtMGMzNS00MGM0LTkwN2YtMWNiNDUzNzMyOTBj2AIE4AIB")
        # self.find_element(By.CSS_SELECTOR,'a[aria-label="Sign in"] span[class="e57ffa4eb5"]').click()
        # self.find_element(By.CSS_SELECTOR,'a[title="Sign in with Facebook"]').click()

    
    def change_currency(self, currency=None):
        currency_element=self.find_element(By.CSS_SELECTOR,"#currency-selector-button")
        currency_element.click()
        selected_currency_element=self.find_element(By.CSS_SELECTOR,".bui-traveller-header__currency.bui-traveller-header__currency--active")
        selected_currency_element.click()
    
    def select_place_to_go(self, place_to_go):
        search_field=self.find_element(By.CSS_SELECTOR,"#ss")
        search_field.send_keys(place_to_go)
        first_result=self.find_element(By.CSS_SELECTOR,"body > div:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > form:nth-child(1) > div:nth-child(14) > div:nth-child(1) > div:nth-child(13) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > span:nth-child(2)")
        first_result.click()
    
    def select_dates(self,check_indate,check_outdate):
        check_in_element =self.find_element(By.CSS_SELECTOR,f'span[aria-label="{check_indate}"] span[aria-hidden="true"]')
        check_in_element.click()
        check_out_element = self.find_element(By.CSS_SELECTOR,f'span[aria-label="{check_outdate}"] span[aria-hidden="true"]')
        check_out_element.click()
        
    def select_no_person(self,count=1):
        selection_item = self.find_element(By.ID,"xp__guests__toggle")
        selection_item.click()
        while True:
            decrease_adults=self.find_element(By.CSS_SELECTOR,'button[data-bui-ref="input-stepper-subtract-button"]')
            decrease_adults.click()
            adults_value_element = self.find_element(By.ID,"group_adults")
            adults_value=adults_value_element.get_attribute('value')
            if int(adults_value)==1:
                break
        increase_adults=self.find_element(By.CSS_SELECTOR,'button[data-bui-ref="input-stepper-add-button"]')
        for _ in range(count-1):
            increase_adults.click()
    
    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR,'button[type="submit"]')
        search_button.click()
        self.find_element(By.CLASS_NAME,'a1b3f50dcd ca736cec7e f7c6687c3d db7f07f643 a33c3d5e6b').click()

    
    def apply_filtration(self):
        Filtration=BookingFiltration(driver=self)
        Filtration.apply_star_rating(3,4,5)
        Filtration.sort_price_lowest_first()
        
    def report_results(self):
        hotel_boxes=self.find_element(By.ID,"hotellist_inner").find_element(By.CLASS_NAME,"sr_property_block")
        report=BookingReport(hotel_boxes)
        table=PrettyTable(["Hotel Name","Hotel Price","Hotel Score"])
        table.add_rows(report.pull_deal_boxes())
        
        

