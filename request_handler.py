import json

from error_handler import RequiredParamsNotPresent, UnSupportedScriptAction, BadAddAccountParam, BadRequestParam, \
    BadDeleteCustomerParam, TooManyRequests
from script_runner import ScriptRunner


class RequestHandler:
    required_params = None

    @classmethod
    def process_request(cls, request):
        script_data = cls.parse_arguments(request)
        script_runner = ScriptRunner()
        results = script_runner.run_scripts(script_data.get('requests'), script_data.get('username', 'username_here'),
                                            script_data.get('password', 'password_here'))
        script_runner.utils.logout()
        return results

    @classmethod
    def parse_arguments(cls, request):
        """Extract params from request and validate required params are present"""
        parameters = json.loads(request.data.decode())
        reqs = parameters.get('requests')
        for req in reqs:
            cls.validate_params(req)
        return parameters

    @classmethod
    def validate_params(cls, parameters):
        """Validate params for given script action"""

        # reqs = parameters.get('requests')
        # if not reqs or len(reqs) > 20 or len(reqs) == 0:
        #   raise TooManyRequests("Invalid requests attempted, min=1, max=20")

        action = parameters.get('script_action', 'NONE PROVIDED').lower()

        if action not in RequestHandler.required_params.keys():
            raise UnSupportedScriptAction(
                "invalid scriptAction name " + action + "... valid options: " + str(
                    RequestHandler.required_params.keys()))

        req_params = set(RequestHandler.required_params.get(action))
        if not req_params.issubset(set(parameters.keys())):
            raise RequiredParamsNotPresent("Required Params Not Found for,", action, str(req_params))

        # Add param validations here
        if action == 'example_script':
            if parameters.get('example') not in ['N', 'A', 'Z']:
                raise BadRequestParam("invalid example value, valid options: A, N, or Z")
