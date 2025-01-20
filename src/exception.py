import sys
from src.logger import Logging

def error_message_detail(error, error_message: sys):
    _, _, exc_tb = sys.exc_info()  # Fixed: sys.exc_info() instead of error_detail.error_info()
    file_name = exc_tb.tb_frame.f_code.co_filename  # Fixed: Correct traceback structure
    error_message = "Error occurred in python script name[{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_message=error_detail)  # Fixed function name

    def __str__(self):
        return self.error_message
