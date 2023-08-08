from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import  By



class BookingReport:
    def __init__(self,boxes_section_element: WebDriver):
        self.boxes_section_element = boxes_section_element

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_element(By.CLASS_NAME,'sr_property_block')
    
    def pull_titles(self):
        for deal_box in self.dealboxes:
            collection = []
            hotel_name=deal_box.find_element(By.CLASS_NAME,'sr-hotel__name').get_attribute('innerHTML').strip()
            hotel_price = deal_box.find_element(By.CLASS_NAME,'bui-price-display__value').get_attribute('innerHTML').strip()
            hotel_score = deal_box.get_attribute('data-score').strip()
            collection.append([hotel_name,hotel_price,hotel_score])
        return collection