from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
class AutomationProcess:

    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,'')))

    is_first_apply   = False
    page_three_count = 0
    page_nine_count  = 0
    yes_choice       = 1
    no_choice        = 2

    def find_element_by_xpath(self, xpath_value):
        return driver.find_element(By.XPATH, xpath_value)
    
    def open_browser(self):
        options = Options()
        options.add_experimental_option("detach", True)
    
        global driver
        driver = webdriver.Chrome(options=options)
        driver.get('https://online.immi.gov.au/lusc/login')
        
        self.login_page()

    def login_page(self):

        username_element = driver.find_element(By.ID,'username')
        username_element.clear()
        username_element.send_keys('nghilt19411@gmail.com')

        password_element = driver.find_element(By.ID,'password')
        password_element.clear()
        password_element.send_keys('abcABC@123456789')

        login_element = driver.find_element(By.NAME, 'login')
        login_element.send_keys(Keys.ENTER)

        self.consent_page()

    def consent_page(self):

        continue_element = driver.find_element(By.NAME, 'continue')
        continue_element.click()

        self.profile_page()
    
    def profile_page(self):
        
        time.sleep(2)

        try:
            edit_element = self.find_element_by_xpath('//div[@role="tablist"]/div[2]/div/div/div[2]/div/div/div/div/div/button') 
            edit_element.click()
            self.process_page_one()
        except:
            self.is_first_apply = True
            application_element = self.find_element_by_xpath('//section/div/div/div[1]/div/div/div[1]/div/div/div/div[1]/button')    
            application_element.click()
            self.process_application()

    def process_application(self):

        time.sleep(2)

        button_holiday = self.find_element_by_xpath('//section/div/div/div[2]/div/div/div/div/div[16]/button')
        button_holiday.click()
        
        button_holiday_visa = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//section/div/div/div[2]/div/div/div/div/div[16]/div/button[2]')))
        button_holiday_visa.click()
        self.process_page_one()

    def process_page_one(self):
        # Bug
        time.sleep(2)
        check_box_element = self.find_element_by_xpath('//div[@class="wc-content"]/div/div/span/input')
        if(check_box_element.is_selected()):
            next_element_page_1 = self.find_element_by_xpath('//div[@class="wc-borderlayout"]/div/div[2]/button')
            next_element_page_1.click()
        else:
            check_box_element.click()
            next_element_page_1 = self.find_element_by_xpath('//div[@class="wc-borderlayout"]/div/div[2]/button')
            next_element_page_1.click()
        
        self.process_page_two()
    
    def process_page_two(self):

        # select = Select(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='interface' and @name='interface']"))))

        # Question 1: Current location:
        select_current_location_filed = Select(self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[2]/div/div[3]/div/div/div[2]/span/select'))
        time.sleep(3) 
        select_current_location_filed.select_by_visible_text("THAILAND")

        # Question 2: Legal status:
        legal_status_field = Select(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[2]/div/div[4]/div/div/div[2]/span/select')))) 
        legal_status_field.select_by_visible_text("Citizen")

        # Question 3: Will the applicant be accompanied by dependent children at any time during their stay in Australia on this visa?
        current_applicant_one_choice = 2 # Yes is 1 | No is 2
        current_applicant_one = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[4]/div/div[2]/div[2]/div/div/div/fieldset/div/label/input[@value={current_applicant_one_choice}]')
        current_applicant_one.click() 

        # Question 4: Has the applicant been granted and entered Australia on a Working Holiday visa (subclass 417) before?
        current_applicant_two_choice = 2 # Yes is 1 | No is 2
        current_applicant_two = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[5]/div/div[2]/div[2]/div/div/div/fieldset/div/label/input[@value={current_applicant_two_choice}]')
        current_applicant_two.click() # Yes is 1 | No is 2

        # Question 5: Select the type of work and holiday visa the applicant is applying for:
        application_type_one_choice = 4 # We have 4, 5, 6 for answer
        application_type_one = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[9]/div/div[2]/div/div/div/div/fieldset/div/label/input[@value={application_type_one_choice}]')
        application_type_one.click()

        # Question 6: Has the applicant been granted and entered Australia on a first Work and Holiday visa (subclass 462) before?
        application_type_two_choice = 2 # Yes is 1 | No is 2
        application_type_two = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[10]/div/div[2]/div/div/div/div[1]/fieldset/div/label/input[@value={application_type_two_choice}]')
        application_type_two.click()

        # Question 7: Proposed arrival date
        propose_arrival_date = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[17]/div/div/div[2]/div/div/div/div/input')
        propose_arrival_date.clear()
        propose_arrival_date.send_keys('23 Dec 2023') # Example of format: 20 Dec 2023 

        # Question 8: Does the applicant have a letter of government support to attach to this visa application?
        government_choice = 1 # Yes is 1 | No is 2
        goverment_question = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[19]/div/div[2]/div[2]/div/div/div[1]/fieldset/div/label/input[@value={government_choice}]')
        goverment_question.click()

        next_button = self.find_element_by_xpath('//button[@type="submit" and @title="Go to next page"]')
        next_button.click()

        self.process_page_three()

    def process_page_three(self):

        time.sleep(2)

        # Question 1: Family name
        if self.page_three_count != 1:
            family_name = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[6]/div/div[1]/div/div[1]/div/div/div[2]/div/div/div[1]/span/input')
            family_name.clear()
            family_name.send_keys('Le')

            # Question 2: Given names
            given_name = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[6]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/span/input')
            given_name.clear()
            given_name.send_keys('Thanh Nghi')

            # Question 3: Sex
            sex_choice = "U" #  "F" is female | "M" is male | "U" is other
            sex_question = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[6]/div/div[2]/div/div/div[2]/fieldset/div/label/input[@value="' + str(sex_choice) + '"]')
            sex_question.click()

            # Question 4: Date of birth
            date_of_birth = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[6]/div/div[3]/div/div/div[2]/div/input')
            date_of_birth.clear()
            date_of_birth.send_keys('09 May 2000') # Followed by this format: dd mm yyyy

            # Question 5: Passport Number
            passport_number = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[7]/div/div[1]/div/div/div[2]/span/input')
            passport_number.clear()
            passport_number.send_keys('S356345')

            # Question 6: Country of Passport
            country_of_passport = Select(self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[7]/div/div[2]/div/div/div[2]/span/select'))
            country_of_passport.select_by_visible_text("THAILAND - THA")
            
            # Question 7: Nationality of passport holder
            national_of_passport_holder = Select(self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[7]/div/div[3]/div/div/div[2]/span/select'))
            national_of_passport_holder.select_by_visible_text("THAILAND - THA")

            # Question 8: Date of issue
            date_of_issue = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[7]/div/div[4]/div/div/div[2]/div/input')
            date_of_issue.clear()
            date_of_issue.send_keys("01 Jul 2018")

            date_of_expiry = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[7]/div/div[5]/div/div/div[2]/div/input')
            date_of_expiry.clear()
            date_of_expiry.send_keys("01 Jul 2028")

            # Question 9: Place of Issue
            place_of_issue = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[7]/div/div[7]/div/div/div[2]/span/input')
            place_of_issue.clear()
            place_of_issue.send_keys("Thailand")

            # Question 10: Does this applicant have a national identity card?   
            national_identity_card_choice = 1 # 1 is Yes | 2 is No
            national_identity_card = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[9]/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset/div/label/input[@value={national_identity_card_choice}]')
            national_identity_card.click()

            # Question 12: Town / City
            town_question = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[10]/div/div[2]/div/div/div[2]/span/input')
            town_question.clear()
            town_question.send_keys('Ho Chi Minh')

            # Question 13: State/ Province
            state_question = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[10]/div/div[3]/div/div/div[2]/span/input')
            state_question.clear()
            state_question.send_keys('Ho Chi Minh')

            # Question 14: Country of birth
            country_of_birth = Select(self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[10]/div/div[4]/div/div/div[2]/div/div/div[1]/span/select'))
            country_of_birth.select_by_visible_text("THAILAND")

            # Question 15: Relationship status
            relationship_status = Select(self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[12]/div/div[2]/div/div/div[2]/div/div/div[1]/span/select'))
            relationship_status.select_by_visible_text('Never Married')

            # Question 16: Is this applicant currently, or have they ever been known by any other names?
            other_names_choice = 2 # 1 is Yes | 2 is No
            other_names = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[13]/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset/div/label/input[@value={other_names_choice}]')
            other_names.click()

            # Question 17: Is this applicant a citizen of the selected country of passport (VietNam)?
            time.sleep(2)
            is_country_of_passport_choice = 1 # 1 is Yes | 2 is No
            is_country_of_passport = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[14]/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset/div/label/input[@value={is_country_of_passport_choice}]')
            is_country_of_passport.click()

            # Question 18: Is this applicant a citizen of any other country?
            is_citizen_other_country_choice = 2 # 1 is Yes | 2 is No
            is_citizen_other_country = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[14]/div/div[3]/div/div[2]/div[2]/div/div/div/fieldset/div/label/input[@value={is_citizen_other_country_choice}]')
            is_citizen_other_country.click()

            # Question 19: Does this applicant have other current passports?
            is_current_passport_choice = 2 # 1 is Yes | 2 is No
            is_current_passport = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[15]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/fieldset/div/label/input[@value={is_current_passport_choice}]')
            is_current_passport.click()

            # Question 20: Does this applicant have other identity documents?
            is_other_identity_document_choice = 2 # 1 is Yes | 2 is No
            is_other_identity_document = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[16]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/fieldset/div/label/input[@value={is_other_identity_document_choice}]')
            is_other_identity_document.click()

            # Question 21: Has this applicant undertaken a health examination for an Australian visa in the last 12 months?
            is_health_examination_choice = 2
            is_health_examination = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[19]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/fieldset/div/label/input[@value={is_health_examination_choice}]')
            is_health_examination.click()

            #--------------------------------------------------------
            # We answer all questions above first then we come to this question 
            # Question 11: # Add details
            add_details_button = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[9]/div/div[7]/div/button')
            add_details_button.click()

            #-------------------------------------------------------
            self.process_sub_page_three()
        else:
            next_button = self.find_element_by_xpath('//div[@class="wc-borderlayout"]/div/div[2]/button')
            next_button.click()
            self.process_page_four()

    def process_sub_page_three(self):

        time.sleep(2)

        # Question 1: Family name
        family_name = self.find_element_by_xpath(f'//section/div[@class="wc-content"]/div/div/div[{4 if self.is_first_apply else 5}]/div/div/div[1]/div/div[3]/div/div[1]/div/div/div[2]/div/div/div[1]/span/input')
        family_name.clear()
        family_name.send_keys("LE")

        # Question 2: Given Name
        given_name = self.find_element_by_xpath(f'//section/div[@class="wc-content"]/div/div/div[{4 if self.is_first_apply else 5}]/div/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div/div[1]/span/input')
        given_name.clear()
        given_name.send_keys("THANH NGHI")

        # Question 3: Identification number
        identification_number = self.find_element_by_xpath(f'//section/div[@class="wc-content"]/div/div/div[{4 if self.is_first_apply else 5}]/div/div/div[1]/div/div[4]/div/div/div[2]/span/input')
        identification_number.clear()
        identification_number.send_keys("079200023361")

        # Question 4: Country of issue
        time.sleep(1)
        country_of_issue = Select(self.find_element_by_xpath(f'//section/div[@class="wc-content"]/div/div/div[{4 if self.is_first_apply else 5}]/div/div/div[1]/div/div[5]/div/div/div[2]/span/select'))
        country_of_issue.select_by_visible_text("VIETNAM")

        # Question 5: Date of issue
        date_of_issue = self.find_element_by_xpath(f'//section/div[@class="wc-content"]/div/div/div[{4 if self.is_first_apply else 5}]/div/div/div/div/div[7]/div/div/div[2]/div/input')
        date_of_issue.clear()
        date_of_issue.send_keys("15 April 2021")

        # Question 6:  Date of expiry
        date_of_expiry = self.find_element_by_xpath(f'//section/div[@class="wc-content"]/div/div/div[{4 if self.is_first_apply else 5}]/div/div/div/div/div[8]/div/div/div[2]/div/input')
        date_of_expiry.clear()
        date_of_expiry.send_keys("15 April 2036")

        confirm_button = self.find_element_by_xpath('//div[@class="wc-borderlayout"]/div/div[2]/button')
        confirm_button.click()

        self.page_three_count += 1
        self.process_page_three()       
    
    def process_page_four(self):

        # Question 1: Is the above information correct?
        confirm_indentification_choice = 1
        confirm_indentification = self.find_element_by_xpath(f'//section/div[@class="wc-content"]/div/div/div[{4 if self.is_first_apply else 5}]/div/div/div/div/div/div/div[10]/div/div/div[2]/div/div/div[1]/fieldset/div/label/input[@value={confirm_indentification_choice}]')
        confirm_indentification.click()

        next_button = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][{6 if self.is_first_apply else 7}]/div/div/div/div[2]/button')
        next_button.click()
        self.process_page_five()
    
    def process_page_five(self):

        # Question 1: Has this applicant previously travelled to Australia or previously applied for a visa?
        is_travel_to_au_choice = 2
        if is_travel_to_au_choice == 2:
            is_travel_to_au = self.find_element_by_xpath('//section/div[@class="wc-content"]/div/div/div[5]/div/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div[2]/fieldset/div/label/input[@value="' + str(is_travel_to_au_choice) + '"]')
            is_travel_to_au.click()

            next_button = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][7]/div/div/div/div[2]/button')
            next_button.click()
            self.process_page_six()

    def process_page_six(self):
        time.sleep(2)
        # Question 1: Usual country of residence
        
        country_field = Select(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][5]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/span/select')))) 
        country_field.select_by_visible_text('VIETNAM')

        # Question 2: Office
        office_field = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][5]/div/div/div/div/div/div/div[3]/div/div[4]/div/div/div[2]/div/div/span/input')
        office_field.clear()
        office_field.send_keys('Vietnam, Ho Chi Minh City')

        # (Residential address)
        # Question 3: Country 
        country_residental = Select(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][5]/div/div/div/div/div/div/div[4]/div/div[3]/div/div[2]/div/div/div[2]/span/select'))))
        country_residental.select_by_visible_text('VIETNAM')

        # Question 4: Address
        address_residental_one = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][5]/div/div/div/div/div/div/div[4]/div/div[3]/div/div[3]/div/div/div[2]/div/div/div[1]/span/input')
        address_residental_one.clear()
        address_residental_one.send_keys('173/45 Pham Phu Thu')

        address_residental_two = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][5]/div/div/div/div/div/div/div[4]/div/div[3]/div/div[4]/div/div/div[2]/span/input')
        address_residental_two.clear()
        address_residental_two.send_keys('Ward 11, Tan Binh district')


        # Question 5: State or Province: 
        state_residental = Select(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][5]/div/div/div/div/div/div/div[4]/div/div[3]/div/div[6]/div/div[2]/div/div[2]/div/div/div[2]/span/select')))) 
        time.sleep(3)
        state_residental.select_by_visible_text("HO CHI MINH (SAI GON)")

        # Question 6: Is the postal address the same as the residential address?
        is_postal_choice = 1
        is_postal = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][5]/div/div/div/div/div/div/div[5]/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset/div/label/input[@value={is_postal_choice}]')
        is_postal.click()

        # Question 7: Mobile / Cell phone
        mobile_field = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][5]/div/div/div/div/div/div/div[6]/div/div[5]/div/div/div[2]/span/input')
        mobile_field.clear()
        mobile_field.send_keys('0936589478')

        # Question 8: Email address
        email_field = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][5]/div/div/div/div/div/div/div[7]/div/div[2]/div/div/div[2]/div/div/div[1]/span/input')
        email_field.clear()
        email_field.send_keys('nghilt19411@gmail.com')

        next_button = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][7]/div/div/div/div[2]/button')
        next_button.click()
        self.process_page_seven()

    def process_page_seven(self):

        time.sleep(2)


        # Question 1: Does the applicant authorise another person to receive written correspondence on their behalf?
        # This authorises the department to send the authorised person all written correspondence that would otherwise be sent directly to the applicant.
        # NO
        # YES_MIGRATION_AGENT
        # YES_LEGAL_PRACTITIONER
        # YES_ANOTHER_PERSON

        is_authorise_choice = "NO"
        is_authorise = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][5]/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/fieldset/div/label/input[@value="' + str(is_authorise_choice) + '"]')
        is_authorise.click()

        next_button = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][7]/div/div/div/div[2]/button')
        next_button.click()

        # We don't have page 8 on the element
        self.process_page_nine()
     
    def process_page_nine(self):
        
        time.sleep(2)

        # Question 1: Does the applicant meet the education requirements for this visa?
        if self.page_nine_count != 1:
            is_meet_choice = 1
            is_meet = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/fieldset/div/label/input[@value={is_meet_choice}]')
            is_meet.click()

            add_button = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div/div/div/div/div/div/div/div/div/button')
            add_button.click()
            self.process_sub_page_nine()
        else:
            next_button = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][7]/div/div/div/div[2]/button')
            next_button.click()
            self.process_page_ten()
       
    def process_sub_page_nine(self):

        time.sleep(2)

        self.page_nine_count+=1
        
        # Question 1: Qualification
        qualification_field = Select(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/span/select')))) 
        qualification_field.select_by_visible_text("Bachelor Degree (Other)")

        # Question 2: Course name
        course_name = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div[3]/div/div/div[2]/span/input')
        course_name.clear()
        course_name.send_keys("Electronic Commerce")     

        # Question 3: Institution Name
        institution_name = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div[4]/div/div/div[2]/span/input')              
        institution_name.clear()
        institution_name.send_keys('University Of Economics and Laws')

        # Question 4: Country of institution
        country_of_institution = Select(self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div[5]/div/div/div[2]/span/select'))
        country_of_institution.select_by_visible_text("VIETNAM")

        # Question 5: Date From
        date_from = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div[8]/div/div/div[2]/div/input')
        date_from.send_keys('15 May 2019')

        # Question 6: Date To
        date_to = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div[9]/div/div/div[2]/div/input')
        date_to.send_keys('15 May 2023')

        # Question 7: Status
        time.sleep(3)
        status_choice = Select(self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div[10]/div/div/div[2]/span/select'))
        status_choice.select_by_visible_text('Graduated')

        confirm_button = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div/div/div/div/div/div/div[2]/button')
        confirm_button.click()
        self.process_page_nine()

    def process_page_ten(self):
        
        time.sleep(2)

        # Question 1: Usual occupation
        occupation_field = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div/div/div/div/div/div/div[1]/div[3]/div/div/div[2]/span/input')
        occupation_field.clear()
        occupation_field.send_keys("Tour Guide")

        # Question 2: Industry Type
        industry_field = Select(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="wc-content"]/div[@class="wc-panel"]/div/div/div/div/div/div/div/div[1]/div[5]/div/div/div[2]/div/div/div[1]/span/select')))) 
        time.sleep(2)
        industry_field.select_by_visible_text("Other Services")

        next_button = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][7]/div/div/div/div[2]/button')
        next_button.click()
        self.process_page_eleven()
    
    def process_page_eleven(self):
        
        # Question 1: Does the applicant hold a current passport from the USA, UK, Canada, New Zealand, or the republic of Ireland?
        is_question_one_choice = 2
        is_question_one = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/fieldset/div/label/input[@value={is_question_one_choice}]')
        is_question_one.click()


        # Question 2: Does the applicant have at least functional English language ability?
        time.sleep(2)
        is_question_two_choice = 1
        is_question_two = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div[1]/fieldset/div/label/input[@value={is_question_two_choice}]')
        is_question_two.click()


        # Question 3: Select the options which represent proof of the applicant having functional English ​
        time.sleep(2) # Bug
        is_question_three_choice = 1
        is_question_three = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"]/div/div/div/div[1]/div/div/div[5]/div/div/div[2]/fieldset/div/label/input[@value={is_question_three_choice}]')
        
        if(is_question_three.is_selected()):
            print('Is Clicked')
        else:
            is_question_three.click()

        # Question 4: Name Of Test
        time.sleep(2) # Bug
        question_four = Select(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"]/div/div/div/div[1]/div/div/div[7]/div/div[3]/div/div/div[2]/div/div/div[1]/span/select'))))
        question_four.select_by_visible_text("IELTS")

        # Question 5: Date of test
        question_five = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"]/div/div/div/div[1]/div/div/div[7]/div/div[4]/div/div/div[2]/div/input')
        question_five.clear()
        question_five.send_keys("10 Feb 2021")

        # Question 6: Test Reference Number
        question_six = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"]/div/div/div/div[1]/div/div/div[7]/div/div[5]/div/div/div[2]/div/div/div[1]/span/input')
        question_six.clear()
        question_six.send_keys("PE1567846")

        # Question 7: Country where test was undertaken
        question_seven = Select(self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"]/div/div/div/div[1]/div/div/div[7]/div/div[6]/div/div/div[2]/span/select'))
        question_seven.select_by_visible_text("VIETNAM")

        # Question 8: Language Ability
        question_eight = Select(self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"]/div/div/div/div[1]/div/div/div[7]/div/div[7]/div/div/div[2]/div/div/div[1]/span/select'))
        question_eight.select_by_visible_text("Proficient")

        # Question 9: Main Language
        question_nine = Select(self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"]/div/div/div/div[1]/div/div/div[8]/div/div[2]/div/div/div[2]/div/div/div[1]/span/select'))
        question_nine.select_by_visible_text("Vietnamese")

        next_button = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][7]/div/div/div/div[2]/button')
        next_button.click()
        self.process_page_thirteen()

    def process_page_thirteen(self): 
        
        # Question 1: In the last five years, has any applicant visited, or lived, outside their country of passport, for more than 3 consecutive months? Do not include time spent in Australia.
        question_one_choice = 2
        question_one = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_one_choice}]')
        question_one.click()

        # Question 2: Does any applicant intend to enter a hospital or a health care facility (including nursing homes) while in Australia?
        question_two_choice = 2
        question_two = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div/div/div/div/div/div/div[1]/div[4]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_two_choice}]')
        question_two.click()

        # Question 3: Does any applicant intend to work as, or study or train to be, a health care worker or work within a health care facility while in Australia?
        question_three_choice = 2
        question_three = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div/div/div/div/div/div/div[1]/div[6]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_three_choice}]')
        question_three.click()

        # Question 4: Does any applicant intend to work, study or train within aged care or disability care while in Australia?
        question_four_choice = 2
        question_four = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div/div/div/div/div/div/div[1]/div[8]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_four_choice}]')
        question_four.click()

        # Question 5: Does any applicant intend to work or be a trainee at a child care centre (including preschools and creches) while in Australia?
        question_five_choice = 2
        question_five = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div/div/div/div/div/div/div[1]/div[10]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_five_choice}]')
        question_five.click()

        # Question 6: Does any applicant intend to be in a classroom situation for more than 3 months (eg. as either a student, teacher, lecturer or observer)?
        question_six_choice = 2
        question_six = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div/div/div/div/div/div/div[1]/div[12]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_six_choice}]')
        question_six.click()

        # Question 7: Has any applicant:
            # ever had, or currently have, tuberculosis?
            # been in close contact with a family member that has active tuberculosis?
            # ever had a chest x-ray which showed an abnormality?
            # Has any applicant:
            # ever had, or currently have, tuberculosis?
            # been in close contact with a family member that has active tuberculosis?
            # ever had a chest x-ray which showed an abnormality?

        question_eleven_choice = 2
        question_eleven = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[15]/div/div/div[2]/fieldset/div/label/input[@value={question_eleven_choice}]')
        question_eleven.click()

        # Question 8: During their proposed visit to Australia, does any applicant expect to incur medical costs, or require treatment or medical follow up for:
            # blood disorder
            # cancer
            # heart disease
            # hepatitis B or C and/or liver disease
            # HIV infection, including AIDS
            # kidney disease, including dialysis
            # mental illness
            # pregnancy
            # respiratory disease that has required hospital admission or oxygen therapy
            # other?
            # During their proposed visit to Australia, does any applicant expect to incur medical costs, or require treatment or medical follow up for:
            # blood disorder
            # cancer
            # heart disease
            # hepatitis B or C and/or liver disease
            # HIV infection, including AIDS
            # kidney disease, including dialysis
            # mental illness
            # pregnancy
            # respiratory disease that has required hospital admission or oxygen therapy
            # other?
        
        question_eight_choice = 2
        question_eight = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[18]/div/div/div[2]/fieldset/div/label/input[@value={question_eight_choice}]')
        question_eight.click()


        # Question 9: Does any applicant require assistance with mobility or care due to a medical condition?
        question_nine_choice = 2
        question_nine = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[20]/div/div/div[2]/fieldset/div/label/input[@value={question_nine_choice}]')
        question_nine.click()


        next_button = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][7]/div/div/div/div[2]/button')
        next_button.click()
        self.process_page_fourteen()

    def process_page_fourteen(self):
        
        # Question 1: Has any applicant ever been charged with any offence that is currently awaiting legal action?
        question_one_choice = 2
        question_one = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[5]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_one_choice}]')
        question_one.click()

        # Question 2: Has any applicant ever been convicted of an offence in any country (including any conviction which is now removed from official records)?
        question_two_choice = 2
        question_two = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[7]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_two_choice}]')
        question_two.click()

        # Question 3: Has any applicant ever been the subject of a domestic violence or family violence order, or any other order, of a tribunal or court or other similar authority, for the personal protection of another person?
        question_three_choice = 2
        question_three = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[9]/div/div[2]/div[2]/div/div/div[1]/fieldset/div/label/input[@value={question_three_choice}]')
        question_three.click()

        # Question 4: Has any applicant ever been the subject of an arrest warrant or Interpol notice?
        question_four_choice = 2
        question_four = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[11]/div/div[1]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_four_choice}]')
        question_four.click()

        # Question 5: Has any applicant ever been found guilty of a sexually based offence involving a child (including where no conviction was recorded)?
        question_five_choice = 2
        question_five = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[12]/div/div[1]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_five_choice}]')
        question_five.click()

        # Question 6: Has any applicant ever been named on a sex offender register?
        question_six_choice = 2
        question_six = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[13]/div/div[1]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_six_choice}]')
        question_six.click()

        # Question 7: Has any applicant ever been acquitted of any offence on the grounds of unsoundness of mind or insanity?
        question_seven_choice = 2
        question_seven = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[14]/div/div[1]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_seven_choice}]')
        question_seven.click()

        # Question 8: Has any applicant ever been found by a court not fit to plead?
        question_eight_choice = 2
        question_eight = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[15]/div/div[1]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_eight_choice}]')
        question_eight.click()

        # Question 9: Has any applicant ever been directly or indirectly involved in, or associated with, activities which would represent a risk to national security in Australia or any other country?
        question_nine_choice = 2
        question_nine = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[16]/div/div[1]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_nine_choice}]')
        question_nine.click()

        # Question 10: Has any applicant ever been charged with, or indicted for: genocide, war crimes, crimes against humanity, torture, slavery, or any other crime that is otherwise of a serious international concern?
        question_ten_choice = 2
        question_ten = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[17]/div/div[1]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_ten_choice}]')
        question_ten.click()

        # Question 11: Has any applicant ever been associated with a person, group or organisation that has been or is involved in criminal conduct?
        question_eleven_choice = 2
        question_eleven = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[18]/div/div[1]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_eleven_choice}]')
        question_eleven.click()

        # Question 12: Has any applicant ever been associated with an organisation engaged in violence or engaged in acts of violence (including war, insurgency, freedom fighting, terrorism, protest) either overseas or in Australia?
        question_twelve_choice = 2
        question_twelve = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[19]/div/div[1]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_twelve_choice}]')
        question_twelve.click()

        # Question 13: Has any applicant ever served in a military force, police force, state sponsored / private militia or intelligence agency (including secret police)?
        question_thirteen_choice = 2
        question_thirteen = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[20]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_thirteen_choice}]')
        question_thirteen.click()

        # Question 14: Has any applicant ever undergone any military/paramilitary training, been trained in weapons/explosives or in the manufacture of chemical/biological products?
        question_fourteen_choice = 2
        question_fourteen = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[22]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_fourteen_choice}]')
        question_fourteen.click()

        # Question 15: Has any applicant ever been involved in people smuggling or people trafficking offences?
        question_fifteen_choice = 2
        question_fifteen = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[24]/div/div/div/div[2]/div[2]/fieldset/div/label/input[@value={question_fifteen_choice}]')
        question_fifteen.click()

        # Question 16: Has any applicant ever been removed, deported or excluded from any country (including Australia)?
        question_sixteen_choice = 2
        question_sixteen = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[25]/div/div/div/div[2]/div[2]/fieldset/div/label/input[@value={question_sixteen_choice}]')
        question_sixteen.click()

        # Question 17: Has any applicant ever overstayed a visa in any country (including Australia)?
        question_seventeen_choice = 2
        question_seventeen = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[26]/div/div/div/div[2]/div[2]/fieldset/div/label/input[@value={question_seventeen_choice}]')
        question_seventeen.click()

        # Question 18: Has any applicant ever had any outstanding debts to the Australian Government or any public authority in Australia?
        question_eighteen_choice = 2
        question_eighteen = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[27]/div/div/div/div[2]/div[2]/fieldset/div/label/input[@value={question_eighteen_choice}]')
        question_eighteen.click()


        next_button = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][7]/div/div/div/div[2]/button')
        next_button.click()
        self.process_page_fifteen()

    def process_page_fifteen(self):
        
        # Question 1: Understand that they must abide by the conditions of the visa.
        question_one_choice = 1
        question_one = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[5]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_one_choice}]')
        question_one.click()

        # Question 2: Understand that the visa they are applying for does not permit them to be employed in Australia with one employer for more than 6 months without prior permission.
        question_two_choice = 1
        question_two = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[6]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_two_choice}]')
        question_two.click()

        # Question 3: Understand that the visa they are applying for does not permit them to undertake studies or training for more than 4 months.
        question_three_choice = 1
        question_three = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[7]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_three_choice}]')
        question_three.click()

        # Question 4: Have sufficient funds for the initial period of their stay in Australia and for the fare to their intended overseas destination on leaving Australia.
        question_four_choice = 1 
        question_four = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[8]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_four_choice}]')
        question_four.click()

        # Question 5: Understand that any employment is incidental to their holiday in Australia and the purpose of working is to supplement their holiday funds.
        question_five_choice = 1
        question_five = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[9]/div/div[2]/div[2]/fieldset/div/label/input[@value={question_five_choice}]')
        question_five.click()

        next_button = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][7]/div/div/div/div[2]/button')
        next_button.click()
        self.process_page_sixteen()
  
    def process_page_sixteen(self):
        
        # Question 1: Have read and understood the information provided to them in this application.
        question_one = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[1]/div/div[5]/div/div[2]/div[2]/fieldset/div/label/input[@value={self.yes_choice}]')
        question_one.click()

        # Question 2: Have provided complete and correct information in every detail on this form, and on any attachments to it.
        question_two = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[1]/div/div[6]/div/div[2]/div[2]/fieldset/div/label/input[@value={self.yes_choice}]')
        question_two.click()

        # Question 3: Understand that if any fraudulent documents or false or misleading information has been provided with this application, or if any of the applicants fail to satisfy the Minister of their identity, the application may be refused and the applicant(s), and any member of their family unit, may become unable to be granted a visa for a specified period of time.
        question_three = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[1]/div/div[7]/div/div[2]/div[2]/fieldset/div/label/input[@value={self.yes_choice}]')
        question_three.click()

        # Question 4: Understand that if documents are found to be fraudulent or information to be incorrect after the grant of a visa, the visa may subsequently be cancelled.
        question_four = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[1]/div/div[8]/div/div[2]/div[2]/fieldset/div/label/input[@value={self.yes_choice}]')
        question_four.click()

        # Question 5: Understand that if this application is approved, any person not included in this application will not have automatic right of entry to Australia.
        question_five = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[1]/div/div[9]/div/div[2]/div[2]/fieldset/div/label/input[@value={self.yes_choice}]')
        question_five.click()

        # Question 6: Will inform the Department in writing immediately as they become aware of a change in circumstances (including change of address) or if there is any change relating to information they have provided in or with this application, while it is being considered.
        question_six = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[1]/div/div[10]/div/div[2]/div[2]/fieldset/div/label/input[@value={self.yes_choice}]')
        question_six.click()

        # Question 7: Have read the information contained in the Privacy Notice (Form 1442i).
        question_seven = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[1]/div/div[12]/div/div/div[2]/fieldset/div/label/input[@value={self.yes_choice}]')
        question_seven.click()

        # Question 8: Understand that the department may collect, use and disclose the applicant's personal information (including biometric information and other sensitive information) as outlined in the Privacy Notice (Form 1442i).
        question_eight = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[1]/div/div[14]/div/div/div[2]/fieldset/div/label/input[@value={self.yes_choice}]')
        question_eight.click()

        # Question 9: Give consent to the collection of their fingerprints and facial image if required.
        question_nine = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[2]/div[2]/fieldset/div/label/input[@value={self.yes_choice}]')
        question_nine.click()

        # Question 10: Understand that, if required to provide their fingerprints and facial image, the applicant's fingerprints and facial image and biographical information held by the Department may be given to Australian law enforcement agencies to help identify the applicant and determine eligibility for grant of the visa being applied for, and for law enforcement purposes.
        question_ten = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[2]/div/div[3]/div/div/div/div[2]/div[2]/fieldset/div/label/input[@value={self.yes_choice}]')
        question_ten.click()

        # Question 11: Give consent to Australian law enforcement agencies disclosing the applicant's biometric, biographical and criminal record information to the Department to help identify the applicant, to determine eligibility for grant of a visa and for law enforcement purposes.
        question_eleven = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div/div[2]/div[2]/fieldset/div/label/input[@value={self.yes_choice}]')
        question_eleven.click()

        # Question 12: Give consent to the Department using the applicant's biometric, biographical and criminal record information obtained for the purposes of the Migration Act 1958 or the Citizenship Act 2007.
        question_twelve = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[2]/div/div[5]/div/div/div/div[2]/div[2]/fieldset/div/label/input[@value={self.yes_choice}]')
        question_twelve.click()

        # Question 13: I understand that if my visa ceases to be in effect and I do not hold another visa to remain in Australia at that time, I will be an unlawful non-citizen under the Migration Act 1958. As such, I will be expected to depart from Australia, and be subject to removal under the Migration Act 1958.
        question_thirteen = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div[2]/fieldset/div/label/input[@value={self.yes_choice}]')
        question_thirteen.click()

        # Question 14: Each applicant who is 18 years or over has read, or had explained to them, information provided by the Australian Government on Australian society and values, and agrees to the Australian values statement.
        question_fourteen = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[5]/div/div/div/div/div/div/div[4]/div/div[2]/div/div[2]/div[2]/fieldset/div/label/input[@value={self.yes_choice}]')
        question_fourteen.click()

        next_button = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div/div[@class="wc-cell"][7]/div/div/div/div[2]/button')
        next_button.click()
        self.process_checking_page()

    def process_checking_page(self):

        next_button = self.find_element_by_xpath('//div[@class="wc-borderlayout"]/div/div[2]/button')
        next_button.click()
        self.process_attachment_page()
   
    def process_attachment_page(self):
        
        travel_document_dropout = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"][1]/div/div/div[4]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div[1]')
        travel_document_dropout.click()

        time.sleep(2)

        document_type = Select(WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"][1]/div/div/div[4]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/span/select'))))
        document_type.select_by_visible_text('Passport')

        time.sleep(3)

        # To do send an attachment to this page
        
        document_upload_file = self.find_element_by_xpath('//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"][1]/div/div/div[4]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div/fieldset/input[@type="file"]')
        document_upload_file.send_keys(os.getcwd() + '\customer_data\/travel_document.pdf')
        print('Nghi', document_upload_file)

        next_button = self.find_element_by_xpath('//div[@class="wc-borderlayout"]/div/div[2]/button')
        next_button.click()

        self.process_submit_page()

    def process_submit_page(self):
        print("Nghi")
        return
    
    def process_payment_page(self):
        return
    
    def process_last_page(self):
        return
    
automation_process = AutomationProcess()
automation_process.open_browser()
