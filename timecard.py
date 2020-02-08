from selenium import webdriver
import config
import os


class Webdriver:
    driver = webdriver.Firefox()
    def login(self, user_id, password):
        """
        logs into westvalley using user's id and password.
        """
        user_id = os.environ.get('USER_ID') 
        password = os.environ.get('PASSWORD')
        self.driver.get("https://westvalley.fastime.com")
        self.driver.find_element_by_id("txtOrderNumber").send_keys(user_id)
        self.driver.find_element_by_name("txtSSN").send_keys(password)
        self.driver.find_element_by_id("btnSubmit").click()
        self.driver.find_element_by_id("btnAccept").click()
    def save_for_later(self):
        """
        saves after inserting times.
        """
        self.driver.find_element_by_id("btnReview").click()
        # self.driver.find_element_by_id("saveLater").click()
        # self.driver.switch_to.alert.accept()
    def day_fill(self, day, code_in, code_out, date_code, holidays):
        """
        fills the times for each work day.
        """
        date = self.driver.find_element_by_xpath('//*[@id="Table13"]/tbody/tr[{}]/td[5]/font'.format(date_code)).text.strip()
        days_off = holidays['day_off']

        if date in days_off: 
            print('{} is a holiday. skipping'.format(date))
        else:
            self.driver.find_element_by_id("TCC_txt_{}_{}_IN".format(code_in,day)).send_keys("09:00")
            self.driver.find_element_by_id("TCC_optAMPM_{}_{}_IN".format(code_in, day)).send_keys("AM")
            self.driver.find_element_by_id("TCC_txt_{}_{}_OUT".format(code_in,day)).send_keys("12:00")
            self.driver.find_element_by_id("TCC_optAMPM_{}_{}_OUT".format(code_in,day)).send_keys("PM")
            self.driver.find_element_by_id("TCC_txt_{}_{}_IN".format(code_out,day)).send_keys("12:30")
            self.driver.find_element_by_id("TCC_optAMPM_{}_{}_IN".format(code_out,day)).send_keys("PM")
            self.driver.find_element_by_id("TCC_txt_{}_{}_OUT".format(code_out,day)).send_keys("05:30")
            self.driver.find_element_by_id("TCC_optAMPM_{}_{}_OUT".format(code_out,day)).send_keys("PM")
def main():
    date_codes = {
        'MON': ['6_0', '6_1', '4'],
        'TUE': ['5_0', '5_1', '7'],
        'WED': ['4_0', '4_1', '10'],
        'THU': ['3_0', '3_1', '13'],
        'FRI': ['2_0', '2_1', '16']
    }
    holidays = {
        'day_off': [
            '1/01',
            '1/20',
            '2/17',
            '5/25',
            '7/03',
            '9/07',
            '11/26',
            '12/24',
            '12/25',
            '12/31',
            '1/30',
        ]
    }
    westvalley = Webdriver()
    westvalley.login('user_id', 'password')
    for day, value in date_codes.items():
        westvalley.day_fill(day, value[0], value[1], value[2], holidays)
            
        
    westvalley.save_for_later()
if __name__ == '__main__':
    main()
