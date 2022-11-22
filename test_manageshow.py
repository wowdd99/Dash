from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.manageshow_page import ManageShowPage
from pages.createnewshow_page import CreateShowPage
import pytest

link = "http://10.94.6.100:50000/"


class TestManageShows:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        username = "global"
        password = "global"
        page = LoginPage(browser, link)
        page.open()
        page.login_user(username, password)
        page = MainPage(browser, link)
        page.should_be_logout_button()
        page.close_banner()

    @pytest.mark.repeat(1)
    def test_ms_0001(self, browser):
        self.url = link + "/Home/Homepage"
        page = MainPage(browser, self.url)
        page.open()
        page.should_open_manage_show_page()
        manage_page = ManageShowPage(browser, browser.current_url)
        manage_page.select_random_card()
        manage_page.should_be_show_code_and_show_name()
        manage_page.should_be_status()
        manage_page.should_be_type()
        manage_page.should_be_primary_producer()
        manage_page.should_be_executive_producer()
        manage_page.should_be_start_date()
        manage_page.should_be_end_date()
        manage_page.should_be_release_date()
        manage_page.should_be_supervisor_seniority_split()
        manage_page.should_be_lead_seniority_split()
        manage_page.should_be_key_artist_seniority_split()
        manage_page.should_be_artist_seniority_split()
        manage_page.should_be_manage_link()
        manage_page.should_be_show_planner_link()
        manage_page.should_be_ones_link()
        manage_page.should_be_financials_link()
        manage_page.should_be_publish_archive_link()

    def test_ms_0004(self, browser):
        self.url = link + "/Home/Homepage"
        page = MainPage(browser, self.url)
        page.open()
        page.should_open_manage_show_page()
        manage_page = ManageShowPage(browser, browser.current_url)
        manage_page.select_random_card()
        manage_page.should_be_correct_result_after_search()

    def test_ms_0008(self, browser):
        self.url = link + "/Home/Homepage"
        page = MainPage(browser, self.url)
        page.open()
        page.should_open_manage_show_page()
        manage_page = ManageShowPage(browser, browser.current_url)
        manage_page.check_that_active_status_is_displayed()
        manage_page.check_that_inactive_status_is_displayed()
        manage_page.check_that_delivered_status_is_displayed()

    def test_ms_0015(self, browser):
        self.url = link + "/Home/Homepage"
        page = MainPage(browser, self.url)
        page.open()
        page.should_open_manage_show_page()
        manage_page = ManageShowPage(browser, browser.current_url)
        manage_page.select_random_card()
        manage_page.should_be_edit_interface()
        manage_page.verify_show_stats_tab_display()

    def test_ms_0017(self, browser):
        self.url = link + "/Home/Homepage"
        page = MainPage(browser, self.url)
        page.open()
        page.should_open_manage_show_page()
        manage_page = ManageShowPage(browser, browser.current_url)
        manage_page.select_random_card()
        manage_page.verify_that_show_code_is_pre_selected()

    def test_ms_0018(self, browser):
        self.url = link + "/Home/Homepage"
        page = MainPage(browser, self.url)
        page.open()
        page.should_open_manage_show_page()
        manage_page = ManageShowPage(browser, browser.current_url)
        manage_page.select_random_card()
        manage_page.should_be_financial_interface_for_relevant_show()

    def test_ms_0020(self, browser):
        self.url = link + "/Home/Homepage"
        page = MainPage(browser, self.url)
        page.open()
        page.should_open_create_new_show_page()
        create_page = CreateShowPage(browser, browser.current_url)
        create_page.should_be_show_status()

    def test_ms_0024_1(self, browser):
        # проверяем нажатие на "Create New Show" и отсутствие "Upload"
        self.url = link + "/Home/Homepage"
        page = MainPage(browser, self.url)
        page.open()
        page.should_open_manage_show_page()
        manage_page = ManageShowPage(browser, browser.current_url)
        manage_page.open_create_show_page()
        manage_page.verify_show_stats_tab_display()
        manage_page.verify_show_inputs_tab_display()
        manage_page.verify_avg_artist_day_rates_tab_display()
        manage_page.verify_outsource_rates_tab_display()
        manage_page.verify_bid_weeks_tab_display()
        manage_page.verify_contract_value_tab_display()
        manage_page.verify_indirect_cost_tab_display()
        manage_page.verify_internal_bid_tab_display()
        manage_page.clicking_on_bid_weeks_tab()
        manage_page.check_that_upload_functionality_is_not_displayed()

    def test_ms_0024_2(self, browser):
        # проверяем нажатие на "Manage и отображение "Upload"
        self.url = link + "/Home/Homepage"
        page = MainPage(browser, self.url)
        page.open()
        page.should_open_manage_show_page()
        manage_page = ManageShowPage(browser, browser.current_url)
        manage_page.select_random_card()
        manage_page.clicking_on_manage_link()
        manage_page.verify_show_stats_tab_display()
        manage_page.verify_show_inputs_tab_display()
        manage_page.verify_avg_artist_day_rates_tab_display()
        manage_page.verify_outsource_rates_tab_display()
        manage_page.verify_bid_weeks_tab_display()
        manage_page.verify_contract_value_tab_display()
        manage_page.verify_indirect_cost_tab_display()
        manage_page.verify_internal_bid_tab_display()
        manage_page.clicking_on_bid_weeks_tab()
        manage_page.check_that_upload_functionality_is_displayed()

    def test_ms_0026(self, browser):
        self.url = link + "/Home/Homepage"
        page = MainPage(browser, self.url)
        page.open()
        page.should_open_manage_show_page()
        manage_page = ManageShowPage(browser, browser.current_url)
        manage_page.select_random_card()
        manage_page.change_status_to_inactive()
        manage_page.clicking_on_manage_link()
        manage_page.selecting_show_code_in_the_card()
        manage_page.clicking_on_deleting_btn()
        manage_page.open_create_show_page()
        manage_page.input_in_the_code_field_that_was_previous_removed()
        manage_page.input_in_the_show_color_field()
        manage_page.input_in_the_actual_category_field()
        manage_page.input_in_the_planning_category_field()
        manage_page.input_in_the_amount_of_assets_field()
        manage_page.input_in_the_amount_of_shots_field()
        manage_page.input_in_the_start_date_field()
        manage_page.input_in_the_end_date_field()
        manage_page.input_in_the_seniority_splits_section()
        manage_page.input_in_the_show_currency_field()
        manage_page.input_in_the_awards_est_field()
        manage_page.input_in_the_primary_field()
        manage_page.switch_to_show_input_tab()
        manage_page.input_in_the_adelaide_field()
        manage_page.input_in_the_primary_producer_field()
        manage_page.clicking_on_creation_show_btn()
        manage_page.check_message_show_code_must_be_unique_is_not_present()
        manage_page.check_success_cart_creation()

    def test_ms_0029(self, browser):
        self.url = link + "/Home/Homepage"
        page = MainPage(browser, self.url)
        page.open()
        page.should_open_manage_show_page()
        manage_page = ManageShowPage(browser, browser.current_url)
        manage_page.select_random_card()
        manage_page.open_create_show_page()
        manage_page.input_in_the_code_field()
        manage_page.input_in_the_show_color_field()
        manage_page.input_in_the_actual_category_field()
        manage_page.input_in_the_planning_category_field()
        manage_page.input_in_the_amount_of_assets_field()
        manage_page.input_in_the_amount_of_shots_field()
        manage_page.input_in_the_start_date_field()
        manage_page.input_in_the_end_date_field()
        manage_page.input_in_the_seniority_splits_section()
        manage_page.input_in_the_show_currency_field()
        manage_page.input_in_the_awards_est_field()
        manage_page.input_in_the_primary_field()
        manage_page.switch_to_show_input_tab()
        manage_page.input_in_the_adelaide_field()
        manage_page.input_in_the_primary_producer_field()
        manage_page.clicking_on_creation_show_btn()
        manage_page.check_success_cart_creation_new()
