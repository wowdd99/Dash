from pages.base_page import BasePage
from pages.locatorsnew import ManageShowLocators
from pages.locatorsnew import CreateNewShowLocators
import random
import time
from selenium.webdriver.common.by import By

show_code_random = 'test' + ''.join([random.choice('ABCDEF0123456789') for i in range(4)])
hex_format = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
value_int = random.randint(1,100)
awards_est_value = random.randint(1,99999)
artist_value = random.randint(1,30)
key_artist_value = random.randint(1,30)
lead_value = random.randint(1,30)
supervisor_value = 100 - artist_value - key_artist_value - lead_value


class ManageShowPage(BasePage):

    def select_random_card(self):
        elements = self.browser.find_elements(*ManageShowLocators.CARDS_LIST)
        cards_qty = len(elements)
        print(cards_qty)
        global index
        index = str(random.randrange(1, cards_qty+1))
        print(index)

    def show_code_split(self):
        show_code_and_name = self.browser.find_element(By.XPATH, "(//div[@class='info__title'])["+index+"]").get_attribute("innerText")
        print(show_code_and_name)
        global show_code_and_name_new
        show_code_and_name_new = show_code_and_name.split("|")
        print(show_code_and_name_new)
        global show_code_after_split
        global show_name_after_split
        show_code_after_split = show_code_and_name_new[0]
        show_name_after_split = show_code_and_name_new[1]
        print("Show_code_after_split", show_code_after_split)
        print("Show_name_after_split", show_name_after_split)

    def should_be_show_code_and_show_name(self):
        self.show_code_split()
        assert show_code_after_split, "Show code isn't displayed"
        print(len(show_code_and_name_new))
        if len(show_code_and_name_new) > 1:
            assert show_name_after_split, "Show name isn't displayed"

    def should_be_status(self):
        status = self.browser.find_element(By.XPATH, "(//div[@class='status__label'])["+index+"]").get_attribute('innerText')
        assert status == "Active", f"Wrong status is displayed.Current value is {status}"

    def should_be_type(self):
        show_type = self.browser.find_element(By.XPATH, "(//div[@class='info__type type'])["+index+"]").get_attribute("innerText")
        show_new = show_type.split("\n")
        show_new_after_split = show_new[1]
        assert show_new_after_split == "Awarded" or show_new_after_split == "Blocked Potential" or show_new_after_split == "Blocked Speculative", f"Wrong status.Value is {show_new_after_split}"

    def should_be_primary_producer(self):
        primary_producer = self.browser.find_element(By.XPATH, "(//span[contains (text(), 'Primary Producer')]/following-sibling::span)["+index+"]").get_attribute("innerText")
        if len(primary_producer) == 1:
            assert primary_producer, "Primary producer isn't displayed"
        elif len(primary_producer) == 0:
            assert not primary_producer, "Primary producer is displayed, but shouldn't"

    def should_be_executive_producer(self):
        executive_producer = self.browser.find_element(By.XPATH, "(//span[contains (text(), 'Executive Producer')]/following-sibling::span)["+index+"]").get_attribute("innerText")
        if len(executive_producer) == 1:
            assert executive_producer, "Executive producer isn't displayed"
        elif len(executive_producer) == 0:
            assert not executive_producer, "Executive producer is presented, but should not be"

    def should_be_start_date(self):
        start_date = self.browser.find_element(By.XPATH, "(//span[contains (text(), 'Start Date')]/parent::div) ["+index+"]").get_attribute("innerText")
        print(start_date)
        start_date_new = start_date.split("\n")
        print(start_date_new)
        start_date_only_day = start_date_new[1]
        print(start_date_only_day)
        assert start_date_only_day, "Start date isn't displayed"

    def should_be_end_date(self):
        end_date = self.browser.find_element(By.XPATH, "(//span[contains (text(), 'End Date')]/parent::div)["+index+"]").get_attribute("innerText")
        print(end_date)
        end_date_new = end_date.split("\n")
        print(end_date_new)
        end_date_only_day = end_date_new[1]
        print(end_date_only_day)
        assert end_date_only_day, "Start date isn't displayed"

    def should_be_release_date(self):
        release_date = self.browser.find_element(By.XPATH, "(//span[contains(text(),'Release Date')]/following-sibling::span)["+index+"]").get_attribute("innerText")
        print(release_date)
        if len(release_date) == 1:
            assert release_date, "Release Date isn't displayed"
        elif len(release_date) == 0:
            assert not release_date, "Release Date is presented, but should not be"

    def should_be_supervisor_seniority_split(self):
        supervisor = self.browser.find_element(By.XPATH, "(//div[contains(text(),'Supervisor')]/span)["+index+"]").get_attribute("innerText")
        assert supervisor, "Supervisor isn't displayed"

    def should_be_lead_seniority_split(self):
        lead = self.browser.find_element(By.XPATH, "(//div[contains(text(),'Lead')]/span)["+index+"]").get_attribute("innerText")
        assert lead, "Lead isn't displayed"

    def should_be_key_artist_seniority_split(self):
        key_artist = self.browser.find_element(By.XPATH, "(//div[contains(text(),'Key Artist')]/span)["+index+"]").get_attribute("innerText")
        assert key_artist, "Key Artist isn't displayed"

    def should_be_artist_seniority_split(self):
        artist = self.browser.find_element(By.XPATH, "(//div[contains(text(),'Artist')]/span)["+index+"]").get_attribute("innerText")
        assert artist, "Artist isn't displayed"

    def should_be_manage_link(self):
        manage = self.browser.find_element(By.XPATH, "(//a[contains(text(),'Manage')])["+index+"]").get_attribute("innerText")
        assert manage, "Manage link isn't displayed"

    def should_be_show_planner_link(self):
        show_planner = self.browser.find_element(By.XPATH, "(//a[contains(text(),'Show Planner')])["+index+"]").get_attribute("innerText")
        assert show_planner, "Show Planner link isn't displayed"

    def should_be_ones_link(self):
        ones = self.browser.find_element(By.XPATH, "(//a[contains(text(),'Ones')])["+index+"]").get_attribute("innerText")
        assert ones, "Ones link isn't displayed"

    def should_be_financials_link(self):
        financials = self.browser.find_element(By.XPATH, "(//a[contains(text(),'Financials')])["+index+"]").get_attribute("innerText")
        assert financials, "Financials link isn't displayed"

    def should_be_publish_archive_link(self):
        publish_archive = self.browser.find_element(By.XPATH, "(//a[contains(text(),'Publish Archive')])["+index+"]").get_attribute("innerText")
        assert publish_archive, "Publish Archive isn't displayed"

    def entering_show_code_in_the_search_field(self):
        search_input = self.browser.find_element(*ManageShowLocators.SEARCH_FIELD_INPUT)
        search_input.send_keys(show_code_after_split)

    def should_be_correct_result_after_search(self):
        self.show_code_split()
        self.entering_show_code_in_the_search_field()
        self.clicking_on_apply_btn()
        show_cards_list = self.browser.find_elements(*ManageShowLocators.SHOW_CARDS_LIST)
        for i in range(1, len(show_cards_list)+1):
            show_card = self.browser.find_element(By.XPATH, "(//div[@class='vue-recycle-scroller__item-wrapper']/div[@style!='transform: translateY(-9999px);']/descendant::div[@class='show shows__item']/descendant::div[@class='info__title'])["+str(i)+"]").get_attribute('innerText')
            print(show_card)
            assert show_code_after_split in show_card, "Show code doesn't match"

    def clicking_on_apply_btn(self):
        apply_btn = self.browser.find_element(*ManageShowLocators.APPLY_BTN)
        apply_btn.click()
        time.sleep(10)

    def check_that_active_status_is_displayed(self):
        status = self.browser.find_elements(*ManageShowLocators.STATUS)
        for i in range(1, len(status) + 1):
            status_new = self.browser.find_element(By.XPATH, "(//div[@class='status__label'])["+str(i)+"]").get_attribute('innerText')
            assert status_new == "Active", f"Wrong status is displayed.Current value is {status_new}"

    def check_that_inactive_status_is_displayed(self):
        self.change_status_to_inactive()
        status = self.browser.find_elements(*ManageShowLocators.STATUS)
        for i in range(1, len(status) + 1):
            status_new = self.browser.find_element(By.XPATH, "(//div[@class='status__label'])["+str(i)+"]").get_attribute('innerText')
            assert status_new == "Inactive", f"Wrong status is displayed.Current value is {status_new}"

    def check_that_delivered_status_is_displayed(self):
        self.clicking_on_active_dropdown()
        self.select_inactive_checkbox()
        self.select_delivered_checkbox()
        self.clicking_on_apply_btn()
        status = self.browser.find_elements(*ManageShowLocators.STATUS)
        for i in range(1, len(status) + 1):
            status_new = self.browser.find_element(By.XPATH, "(//div[@class='status__label'])["+str(i)+"]").get_attribute('innerText')
            assert status_new == "Delivered", f"Wrong status is displayed.Current value is {status_new}"

    def should_be_edit_interface(self):
        self.clicking_on_manage_link()
        edit_show_title = self.browser.find_element(*ManageShowLocators.EDIT_SHOW_TITLE)
        assert edit_show_title, "Edit/create show UI isn't displayed"

    def clicking_on_ones_link(self):
        ones = self.browser.find_element(By.XPATH, "(//a[contains(text(),'Ones')])["+index+"]")
        ones.click()
        time.sleep(30)

    def should_be_show_ones_interface(self):
        self.clicking_on_ones_link()
        show_ones_title = self.browser.find_element(*ManageShowLocators.SHOW_ONES_TITLE)
        assert show_ones_title, "Show Ones UI isn't displayed"

    def verify_that_show_code_is_pre_selected(self):
        self.show_code_split()
        self.should_be_show_ones_interface()
        show_code_in_ones = self.browser.find_element(*ManageShowLocators.SHOW_CODE_IN_ONES).get_attribute('innerText')
        print(show_code_in_ones)
        assert show_code_after_split.find(show_code_in_ones), "Show code doesn't match"

    def clicking_on_financials_link(self):
        financials = self.browser.find_element(By.XPATH, "(//a[contains(text(),'Financials')])["+index+"]")
        financials.click()
        time.sleep(20)

    def should_be_financial_interface(self):
        self.clicking_on_financials_link()
        financials_title = self.browser.find_element(*ManageShowLocators.FINANCIALS_TITLE)
        assert financials_title, "User isn't taken to the Financials page"

    def should_be_financial_interface_for_relevant_show(self):
        self.show_code_split()
        self.should_be_financial_interface()
        url_new = self.browser.current_url
        url_new_after_split = url_new.split('/')[-1]
        print("Url_new_after_split", url_new_after_split)
        assert url_new_after_split in show_code_after_split, "Page isn't relevant"

    def verify_show_stats_tab_display(self):
        show_stats_tab = self.browser.find_element(*ManageShowLocators.SHOW_STATS_TAB)
        assert show_stats_tab, "Show Stat tab isn't displayed or not default tab"

    def verify_show_inputs_tab_display(self):
        show_input_tab = self.browser.find_element(*ManageShowLocators.SHOW_INPUT_TAB)
        assert show_input_tab, "Show Input tab isn't displayed"

    def verify_avg_artist_day_rates_tab_display(self):
        avg_artist_day_rates = self.browser.find_element(*ManageShowLocators.AVG_ARTIST_DAY_RATES)
        assert avg_artist_day_rates, "Avg Artist Day Rates tab isn't displayed"

    def verify_outsource_rates_tab_display(self):
        outsource_rates = self.browser.find_element(*ManageShowLocators.OUTSOURCE_PATES)
        assert outsource_rates, "Outsource Rates tab isn't displayed"

    def verify_bid_weeks_tab_display(self):
        global bid_weeks
        bid_weeks = self.browser.find_element(*ManageShowLocators.BID_WEEKS)
        assert bid_weeks, "Bid Weeks tab isn't displayed"

    def verify_contract_value_tab_display(self):
        contract_value = self.browser.find_element(*ManageShowLocators.CONTRACT_VALUE)
        assert contract_value, "Contract Value tab isn't displayed"

    def verify_indirect_cost_tab_display(self):
        indirect_cost = self.browser.find_element(*ManageShowLocators.INDIRECT_COSTS)
        assert indirect_cost, "Indirect tab isn't displayed"

    def verify_internal_bid_tab_display(self):
        internal_bid = self.browser.find_element(*ManageShowLocators.INTERNAL_BID)
        assert internal_bid, "Internal bid isn't displayed"

    def clicking_on_bid_weeks_tab(self):
        bid_weeks.click()
        time.sleep(10)

    def check_that_upload_functionality_is_displayed(self):
        bid_weeks_functionality = self.browser.find_element(*ManageShowLocators.BID_WEEKS_UPLOAD)
        assert bid_weeks_functionality.is_displayed, "Bid weeks functionality isn't presented"

    def check_that_upload_functionality_is_not_displayed(self):
        bid_weeks_functionality_empty = self.browser.find_element(*ManageShowLocators.BID_WEEKS_EMPTY)
        assert bid_weeks_functionality_empty, "Bid weeks functionality is presented,but shouldn't"

    def clicking_on_active_dropdown(self):
        active_dropdown = self.browser.find_element(*ManageShowLocators.ACTIVE_BTN)
        active_dropdown.click()

    def select_active_checkbox(self):
        active_checkbox = self.browser.find_element(*ManageShowLocators.ACTIVE_CHX)
        active_checkbox.click()

    def select_inactive_checkbox(self):
        inactive_checkbox = self.browser.find_element(*ManageShowLocators.INACTIVE_CHX)
        inactive_checkbox.click()

    def select_delivered_checkbox(self):
        delivered_chx = self.browser.find_element(*ManageShowLocators.DELIVERED_CHX)
        delivered_chx.click()

    def change_status_to_inactive(self):
        self.clicking_on_active_dropdown()
        self.select_active_checkbox()
        self.select_inactive_checkbox()
        self.clicking_on_apply_btn()
        time.sleep(10)

    def clicking_on_manage_link(self):
        manage = self.browser.find_element(By.XPATH, "(//a[contains(text(),'Manage')])["+index+"]")
        manage.click()
        time.sleep(35)

    def selecting_show_code_in_the_card(self):
        global show_code_field
        show_code_field = self.browser.find_element(*ManageShowLocators.SHOW_CODE_FIELD).get_attribute('innerText')
        print("Show_code_field_via selecting", show_code_field)

    def clicking_on_deleting_btn(self):
        delete_btn = self.browser.find_element(*ManageShowLocators.DELETE_BTN)
        delete_btn.click()
        time.sleep(5)
        yes_delete_btn = self.browser.find_element(*ManageShowLocators.YES_DELETE_BTN)
        yes_delete_btn.click()
        time.sleep(20)

    def clicking_on_back_btn(self):
        btn_back = self.browser.find_element(*CreateNewShowLocators.BACK_BUTTON)
        btn_back.click()
        time.sleep(10)

    def open_create_show_page(self):
        create_new_show_btn = self.browser.find_element(*ManageShowLocators.CREATE_NEW_SHOW_BTN)
        create_new_show_btn.click()
        time.sleep(25)

    def input_in_the_code_field_that_was_previous_removed(self):
        show_code_input = self.browser.find_element(*ManageShowLocators.SHOW_CODE_FIELD)
        show_code_input.click()
        show_code_input_text = self.browser.find_element(*CreateNewShowLocators.INPUT)
        show_code_input_text.send_keys(show_code_field)
        time.sleep(5)

    def input_in_the_code_field(self):
        show_code_input = self.browser.find_element(*ManageShowLocators.SHOW_CODE_FIELD)
        show_code_input.click()
        show_code_input_text = self.browser.find_element(*CreateNewShowLocators.INPUT)
        global show_code_random
        global show_code_random_str
        show_code_random_str = (str(show_code_random))
        print(str(show_code_random))
        show_code_input_text.send_keys(show_code_random)
        time.sleep(5)

    def check_message_show_code_must_be_unique_is_not_present(self):
        assert self.is_not_element_present(*CreateNewShowLocators.SHOW_CODE_MUST_BE_UNIQ_MESSAGE), \
            "Show code must be unique message is displayed, but shouldn't"

    def input_in_the_show_color_field(self):
        show_color_arrow = self.browser.find_element(*CreateNewShowLocators.SHOW_COLOR_ARROW)
        show_color_arrow.click()
        hex_input = self.browser.find_element(*CreateNewShowLocators.COLOR_INPUT)
        hex_input.clear()
        time.sleep(3)
        hex_input.send_keys(hex_format)
        time.sleep(3)
        ok_btn = self.browser.find_element(*CreateNewShowLocators.OK_BUTTON)
        ok_btn.click()
        time.sleep(5)

    def input_in_the_actual_category_field(self):
        chevron_actual_category = self.browser.find_element(*CreateNewShowLocators.ACTUAL_CATEGORY_CHEVRON)
        chevron_actual_category.click()
        time.sleep(3)
        dropdown_actual_category = self.browser.find_element(*CreateNewShowLocators.ACTUAL_CATEGORY_DROPDOWN)
        dropdown_actual_category.click()
        time.sleep(3)

    def input_in_the_planning_category_field(self):
        chevron_planning_category = self.browser.find_element(*CreateNewShowLocators.PLANNING_CATEGORY_CHEVRON)
        chevron_planning_category.click()
        time.sleep(3)
        dropdown_planning_category = self.browser.find_element(*CreateNewShowLocators.PLANNING_CATEGORY_DROPDOWN)
        dropdown_planning_category.click()
        time.sleep(3)

    def input_in_the_amount_of_assets_field(self):
        amount_of_assert = self.browser.find_element(*CreateNewShowLocators.AMOUNT_OF_ASSETS_FIELD)
        amount_of_assert.click()
        amount_of_assert_input = self.browser.find_element(*CreateNewShowLocators.INPUT)
        amount_of_assert_input.send_keys(value_int)
        time.sleep(3)

    def input_in_the_amount_of_shots_field(self):
        amount_of_shots = self.browser.find_element(*CreateNewShowLocators.AMOUNT_OF_SHOTS_FIELD)
        amount_of_shots.click()
        amount_of_shorts_input = self.browser.find_element(*CreateNewShowLocators.INPUT)
        amount_of_shorts_input.send_keys(value_int)
        time.sleep(3)

    def input_in_the_start_date_field(self):
        start_day_calendar = self.browser.find_element(*CreateNewShowLocators.START_DAY_CALENDAR)
        start_day_calendar.click()
        self.clicking_on_today_day_from_calendar()
        self.clicking_on_confirm_btn()

    def clicking_on_confirm_btn(self):
        confirm_btn = self.browser.find_element(*CreateNewShowLocators.CONFIRM_BTN)
        confirm_btn.click()

    def clicking_on_today_day_from_calendar(self):
        date = self.browser.find_element(*CreateNewShowLocators.TODAY_FROM_CALENDAR)
        date.click()

    def input_in_the_end_date_field(self):
        end_day_calendar = self.browser.find_element(*CreateNewShowLocators.END_DATE_FIELD)
        end_day_calendar.click()
        self.clicking_on_today_day_from_calendar()
        self.clicking_on_confirm_btn()

    def input_in_the_seniority_splits_section(self):
        artist = self.browser.find_element(*CreateNewShowLocators.ARTIST_FIELD)
        artist.click()
        artist_input = self.browser.find_element(*CreateNewShowLocators.INPUT)
        artist_input.send_keys(artist_value)
        time.sleep(2)
        key_artist = self.browser.find_element(*CreateNewShowLocators.KEY_ARTIST_FIELD)
        key_artist.click()
        key_artist_input = self.browser.find_element(*CreateNewShowLocators.INPUT)
        key_artist_input.send_keys(key_artist_value)
        time.sleep(2)
        lead = self.browser.find_element(*CreateNewShowLocators.LEAD_FIELD)
        lead.click()
        lead_input = self.browser.find_element(*CreateNewShowLocators.INPUT)
        lead_input.send_keys(lead_value)
        time.sleep(2)
        supervisor = self.browser.find_element(*CreateNewShowLocators.SUPERVISOR_FIELD)
        supervisor.click()
        supervisor_input = self.browser.find_element(*CreateNewShowLocators.INPUT)
        supervisor_input.send_keys(supervisor_value)
        time.sleep(2)

    def input_in_the_show_currency_field(self):
        chevron_show_currency = self.browser.find_element(*CreateNewShowLocators.SHOW_CURRENCY_CHEVRON)
        chevron_show_currency.click()
        time.sleep(3)
        dropdown_show_currency = self.browser.find_element(*CreateNewShowLocators.SHOW_CURRENCY_DROPDOWN)
        dropdown_show_currency.click()
        time.sleep(3)

    def input_in_the_awards_est_field(self):
        awards_est = self.browser.find_element(*CreateNewShowLocators.AWARDS_EST_FIELD)
        awards_est.click()
        awards_est_input = self.browser.find_element(*CreateNewShowLocators.INPUT)
        awards_est_input.send_keys(awards_est_value)
        time.sleep(3)

    def input_in_the_primary_field(self):
        chevron_primary = self.browser.find_element(*CreateNewShowLocators.PRIMARY_CHEVRON)
        chevron_primary.click()
        time.sleep(3)
        dropdown_primary = self.browser.find_element(*CreateNewShowLocators.PRIMARY_DROPDOWN)
        dropdown_primary.click()
        time.sleep(5)

    def switch_to_show_input_tab(self):
        show_inputs_tab = self.browser.find_element(*ManageShowLocators.SHOW_INPUT_TAB)
        show_inputs_tab.click()
        time.sleep(5)

    def input_in_the_adelaide_field(self):
        adelaide_calendar = self.browser.find_element(*CreateNewShowLocators.ADELAIDE_FIELD)
        adelaide_calendar.click()
        time.sleep(5)
        active_date_from_calendar = self.browser.find_element(*CreateNewShowLocators.DATE_ACTIVE)
        active_date_from_calendar.click()
        time.sleep(5)
        self.clicking_on_confirm_btn()
        time.sleep(5)

    def input_in_the_primary_producer_field(self):
        chevron_primary_producer = self.browser.find_element(*CreateNewShowLocators.PRIMARY_PRODUCER_CHEVRON)
        chevron_primary_producer.click()
        time.sleep(5)
        dropdown_primary_producer = self.browser.find_element(*CreateNewShowLocators.PRIMARY_PRODUCER_DROPDOWN)
        dropdown_primary_producer.click()

    def clicking_on_creation_show_btn(self):
        create_show_btn = self.browser.find_element(*CreateNewShowLocators.CREATE_SHOW_BTN)
        create_show_btn.click()
        time.sleep(15)

    def verify_only_one_card_displaying(self):
        show_cards_list = self.browser.find_elements(*ManageShowLocators.SHOW_CARDS_LIST)
        assert len(show_cards_list) == 1, 'Show card is more than 1'

    def check_success_cart_creation_my(self):
        search_field_input = self.browser.find_element(*ManageShowLocators.SEARCH_FIELD_INPUT)
        search_field_input.send_keys(show_code)
        self.change_status_to_inactive()
        self.verify_only_one_card_displaying()
        code = self.browser.find_element(*ManageShowLocators.SHOW_CODE_AND_NAME_AFTER_SEARCH).get_attribute("innerText")
        assert show_code in code, "Show code doesn't match"
        time.sleep(5)

    def check_success_cart_creation(self):
        global show_code
        show_code = show_code_field
        self.check_success_cart_creation_my()

    def check_success_cart_creation_new(self):
        global show_code
        show_code = show_code_random
        self.check_success_cart_creation_my()
