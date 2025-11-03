from networksecurity.logging import logger
import sys

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message
        _, _, exc_tb = error_detail.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.lineno = exc_tb.tb_lineno

    def __str__(self):
        return (
            f"Error occurred in python script [{self.file_name}] "
            f"line number [{self.lineno}] "
            f"error message [{self.error_message}]"
        )


if __name__ == '__main__':
    try:
        logger.logging.info('Entering the block')
        a = 1 / 0
    except Exception as e:
        raise NetworkSecurityException(e, sys)

     
        