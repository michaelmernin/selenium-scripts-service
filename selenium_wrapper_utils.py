import time
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


class Utils:
    def __init__(self, browser):
        self.browser = browser
        self.wait_time = 60

    def maximize_window(self):
        self.browser.maximize_window()

    def close_workflow(self):
        try:
            # self.switch_view_by_title('501 launch')
            self.pause(2)

            self.switch_view_by_title('enter_title_of_desired_page')
            self.browser.close()
            # self.browser.maximize_window()
        except:
            # print('stuck on switch to Add New Workflow')
            try:
                # print('attempting focus on workflow window, will pause for 5 seconds')
                self.pause(5)
                self.browser.maximize_window()
                self.switch_view_by_title('enter_title_of_desired_page')
                self.browser.close()
                # self.browser.maximize_window()

            except:
                print('script ending, final close step not initiated')
                pass

    def logout(self):
        """Attempts to logout, if unable will disconnect driver session"""
        try:
            self.switch_view_by_title('enter_title_of_logout_page')
            self.click_by_id('enter_logout_button_element')
            self.browser.quit()
        except:
            self.browser.quit()

    def log_results(self):
        result = set()
        try:
            elements = WebDriverWait(self.browser, self.wait_time).until(
                cond.presence_of_all_elements_located((By.CLASS_NAME, 'text_standard')))
            conf = self.browser.find_element_by_class_name('text_color_bold')
            for elem in elements:
                try:
                    result.add(str(elem.text))
                except:
                    pass
            result.add(str(conf.text))

        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

        return result

    def switch_views(self, window=1):
        try:
            WebDriverWait(self.browser, self.wait_time).until(cond.new_window_is_opened)
            winds = self.browser.window_handles
            # WebDriverWait(self.browser, self.wait_time).until(cond.frame_to_be_available_and_switch_to_it)
            self.browser.switch_to.window(winds[window])
            self.browser.maximize_window()
        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def switch_view_by_title(self, title):
        try:
            WebDriverWait(self.browser, self.wait_time).until(cond.new_window_is_opened)
            winds = self.browser.window_handles
            # WebDriverWait(self.browser, self.wait_time).until(cond.frame_to_be_available_and_switch_to_it)
            for win in winds:
                self.browser.switch_to.window(win)
                if title in self.browser.title.lower():
                    self.browser.maximize_window()
                    break
            # self.browser.switch_to.window(winds[window])
        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def select_step2_option(self, id, name):
        try:
            elements = WebDriverWait(self.browser, self.wait_time).until(
                cond.presence_of_all_elements_located((By.NAME, id)))
            for elem in elements:
                if elem.tag_name == 'select':
                    select = Select(elem)

            select.select_by_value(name)

        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def enter_step2_text(self, name, value):
        try:
            elements = WebDriverWait(self.browser, self.wait_time).until(
                cond.presence_of_all_elements_located((By.NAME, name)))
            for elem in elements:
                try:
                    elem.send_keys(value)
                except:
                    pass
        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def select_step_two(self, id):
        try:
            elements = WebDriverWait(self.browser, self.wait_time).until(
                cond.presence_of_all_elements_located((By.ID, id)))
            for elem in elements:
                try:
                    elem.click()
                except:
                    pass
        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def enter_text_by_name(self, name, txt_entered):
        try:
            elem = WebDriverWait(self.browser, self.wait_time).until(cond.presence_of_element_located((By.NAME, name)))
            elem.send_keys(txt_entered)
        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def enter_text_by_id(self, id, txt_entered):
        try:
            elem = WebDriverWait(self.browser, self.wait_time).until(cond.presence_of_element_located((By.ID, id)))
            elem.send_keys(txt_entered)
        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def click_by_name(self, name):
        try:
            # button = WebDriverWait(self.browser, self.wait_time).until(cond.presence_of_element_located((By.NAME, name)))
            button = WebDriverWait(self.browser, self.wait_time).until(cond.element_to_be_clickable((By.NAME, name)))
            button.click()
            # button.send_keys(Keys.ENTER)
        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def click_by_id(self, id):
        try:
            # button = WebDriverWait(self.browser, self.wait_time).until(cond.presence_of_element_located((By.ID, id)))
            button = WebDriverWait(self.browser, self.wait_time).until(cond.element_to_be_clickable((By.ID, id)))
            button.click()
            # button.send_keys(Keys.ENTER)

        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def click_by_class(self, class_name):
        try:
            # button = WebDriverWait(self.browser, self.wait_time).until(cond.presence_of_element_located((By.CLASS_NAME, class_name)))
            button = WebDriverWait(self.browser, self.wait_time).until(
                cond.element_to_be_clickable((By.CLASS_NAME, class_name)))
            button.click()
        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def clear_by_id(self, id):
        try:
            elem = WebDriverWait(self.browser, self.wait_time).until(cond.presence_of_element_located((By.ID, id)))
            elem.clear()
        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def clear_by_name(self, name):
        try:
            elem = WebDriverWait(self.browser, self.wait_time).until(cond.presence_of_element_located((By.NAME, name)))
            elem.clear()
        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def select_drop_down_item_by_name(self, name, option):
        try:
            elem = WebDriverWait(self.browser, self.wait_time).until(cond.presence_of_element_located((By.NAME, name)))
            select = Select(elem)
            select.select_by_value(option)
        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def enter_boxed_info_by_name(self, name, value):
        try:
            elem = WebDriverWait(self.browser, self.wait_time).until(cond.presence_of_element_located((By.NAME, name)))
            elem.clear()
            elem.send_keys(value)
        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def enter_boxed_info_by_id(self, id, value):
        try:
            elem = WebDriverWait(self.browser, self.wait_time).until(cond.presence_of_element_located((By.ID, id)))
            elem.clear()
            elem.send_keys(value)
        except (ElementNotVisibleException, TimeoutException) as py_ex:
            raise py_ex

    def focus(self):
        self.browser.focus()

    def enter_login_creds(self, username, password):
        self.enter_text_by_name('enter_username_element', username)
        self.enter_text_by_name('enter_password_element', password)

    def login_and_start_session(self, website, username, password):
        try:
            self.browser.get(website)
            # self.bypass_security_screen()
            self.enter_login_creds(username, password)
            self.click_by_id('enter_html_element')
        except Exception as e:
            return {"Error": "Error logging in and starting session... " + str(e)}

    # Using in when testing, migrating over to WebDriverWait
    def pause(self, secs):
        time.sleep(secs)

    # def bypass_security_screen(self):
    #     self.pause(10)
    #     # For debugging purposes
    #     all_elems = self.browser.find_elements_by_xpath("//*[@id]")
    #     tries = 0
    #     #self.click_by_id('enter_id_of_element')
    #     self.pause(5)
    #     self.click_by_id('enter_id_of_element')
    #
    #     while tries < 5:
    #         try:
    #             x = self.browser.window_handles
    #             y = self.browser.find_elements_by_id('//[@id]')
    #             # self.click_by_id('enter_id_of_element')
    #             # self.click_by_id('moreInfoContainer')
    #             if self.browser.find_element_by_id('enter_id_of_element'):
    #                 self.pause(1)
    #                 self.click_by_id('enter_id_of_element')
    #                 time.sleep(2)
    #                 self.click_by_id('enter_id_of_element')
    #                 time.sleep(5)
    #                 break
    #             else:
    #                 break
    #         except Exception as e:
    #             tries = tries + 1
    #             print(e)
    #             self.pause(5)
