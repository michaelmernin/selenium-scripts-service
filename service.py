import win32serviceutil
import win32service
import win32event
import servicemanager
import win32process
import win32con
import win32security
from multiprocessing import Process

from app import app

class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = "Selenium2"
    _svc_display_name_ = "Test Service"
    _svc_description_ = "Tests Python service framework by receiving and echoing messages over a named pipe"

    def __init__(self, *args):
        super().__init__(*args)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.process.terminate()
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def SvcDoRun(self):
        self.process = Process(target=self.main)
        self.process.start()
        self.process.run()

    def main(self):
        app.debug = True
    # Product WSGI server "waitress"
    #serve(app, host='127.0.0.1', port='5000')
        #serve(app, host='0.0.0.0', port='5000')
        app.run()

if __name__ == '__main__':
    # First create a token. We're pretending this user actually exists on your local computer or Active Directory domain.
    user = "username"
    pword = "password"
    domain = "." # means current domain
    logontype = win32con.LOGON32_LOGON_INTERACTIVE
    #logontype = win32con.LOGON32_LOGON_NEW_CREDENTIALS
    #provider = win32con.LOGON32_PROVIDER_WINNT50
    provider = 0
    #provider = win32con.LOGON32_LOGON_NEW_CREDENTIALS
    token = win32security.LogonUser(user, domain, pword , logontype, provider)

    # Now let's create the STARTUPINFO structure. Read the link above for more info on what these can do.
    startup = win32process.STARTUPINFO()

    # Finally, create a cmd.exe process using the "ltorvalds" token.
    appname = "c:\\windows\\system32\\cmd.exe"
    priority = win32con.NORMAL_PRIORITY_CLASS
    win32process.CreateProcessAsUser(token, appname, None, None, None, True, priority, None, None, startup)
    win32serviceutil.HandleCommandLine(Service)