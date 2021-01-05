class ExampleScript:
    div_codes = None

    @classmethod
    def run_script(cls, util, request_data):
        util.switch_view_by_title('title_of_desired_page')
        util.click_by_id('html_element_id')
        util.clear_by_id('html_element_id')

        # Change to next screen
        util.switch_view_by_title('title_of_desired_page')
        util.click_by_id("html_element_id")
        util.click_by_name('html_element_name')

        # Change to next screen
        util.switch_view_by_title('title_of_desired_page')
        util.enter_text_by_name('html_element_name', "desired_value")
        util.enter_text_by_name('html_element_name', "desired_value")

        # Change to next screen
        util.click_by_name('element_name')
        util.switch_view_by_title('title_of_desired_page')

        util.enter_text_by_name('html_element_name', "desired_value")
        util.enter_text_by_name('html_element_name', "desired_value")

        util.select_drop_down_item_by_name('html_element_dropdown', "desired_value")

        appl_nbr = util.log_results()

        return appl_nbr
