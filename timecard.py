from selenium import webdriver
import config
import os


class Webdriver:
    driver = webdriver.Firefox()
    def login(self, user_id, password):
        """
        logs into westvalley using user's id and password.
        """
        # with open ('./main.json') as main_file:
        #     data = main_file.read()
        #     obj = json.loads(data)
        # print(str(obj['user_id']))
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
        self.driver.switch_to.alert.accept()
    def day_fill(self, day, code_in, code_out):
        """
        fills the times for each work day.
        """
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
        'MON': ['6_0', '6_1'],
        'TUE': ['5_0', '5_1'],
        'WED': ['4_0', '4_1'],
        'THU': ['3_0', '3_1'],
        'FRI': ['2_0', '2_1']
    }
    westvalley = Webdriver()
    westvalley.login('user_id', 'password')
    for day, value in date_codes.items():
        westvalley.day_fill(day, value[0], value[1])
    westvalley.save_for_later()
if __name__ == '__main__':
    main()

