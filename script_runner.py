from result_handler import ResultHandler
from scripts.add_deposit_account import AddDepositAccount
from scripts.add_loan_account import AddLoanAccount
from scripts.add_misc_account import AddMiscAccount
from scripts.example_script import ExampleScript
from scripts.delete_customer import DeleteCustomer
from selenium_driver import SeleniumDriver
from selenium_wrapper_utils import Utils


class ScriptRunner:
    website = None

    def __init__(self):
        self.utils = Utils(SeleniumDriver().browser)
        # Add scripts here
        self.options = {
            'example_script': ExampleScript(),
        }

    def run_scripts(self, requests, username, password):
        results = []
        self.utils.login_and_start_session(self.website, username, password)
        self.utils.pause(5)
        #self.utils.browser.maximize_window()
        for request in requests:
            script = self.options.get(request.get('script_action').lower())
            try:
                result = script.run_script(self.utils, request)
                results.append({'SUCCESS': ResultHandler.parse_results(result)})
            except Exception as e:
                results.append({'FAILURE': 'Script failure, all previous results were successful ' + str(e)})
                break

        return results
