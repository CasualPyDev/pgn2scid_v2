import platform
import ui_init
import sys
import config
from fbs_runtime.application_context.PyQt5 import ApplicationContext


appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
appctxt.app.setStyle('Fusion')

OP_SYS = platform.system()
config.write(OP_SYS)
if __name__ == '__main__':
    main_window = ui_init.MainUi()
    main_window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
