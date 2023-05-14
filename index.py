import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutomationProcess:

    page_three_count = 0 # Count for page three 

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

        edit_element = self.find_element_by_xpath('//div[@role="tablist"]/div[2]/div/div/div[2]/div/div/div/div/div/button')
        edit_element.click()

        self.process_page_one()

    def process_page_one(self):

        check_box_element = self.find_element_by_xpath('//div[@class="wc-content"]/div/div/span/input')
        if(check_box_element.is_selected()):
            next_element_page_1 = self.find_element_by_xpath('//div[@class="wc-borderlayout"]/div/div[2]/button')
            next_element_page_1.click()
        else:
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
        government_choice = 2 # Yes is 1 | No is 2
        goverment_question = self.find_element_by_xpath(f'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[19]/div/div[2]/div[2]/div/div/div[1]/fieldset/div/label/input[@value={government_choice}]')
        goverment_question.click()

        next_button = self.find_element_by_xpath('//button[@type="submit" and @title="Go to next page"]')
        next_button.click()

        self.process_page_three()

    def process_page_three(self):

        # Question 1: Family name
        if self.page_three_count == 0:
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
            self.page_three_count += 1
            self.process_sub_page_three()

            #-------------------------------------------------------

        else:
            self.process_page_four()


    def process_sub_page_three(self):
        self.process_page_three()
        
    
    def process_page_four(self):
        return
    
    def process_page_five(self):
        return


    

automation_process = AutomationProcess()
automation_process.open_browser()
