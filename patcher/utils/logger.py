import logging


class Log():
    '''
    Pretty logger for patcher
    '''
    logger = None
    def __init__(self, logging_name=__name__) -> None:
        '''
        Initialise class
        '''
        self.logger = logging.getLogger(logging_name)
        self.debug = self.logger.debug
        self.info = self.logger.info
        self.warning = self.logger.warning
        self.stream_handler = logging.StreamHandler()
        self.logger.addHandler(logging.NullHandler())
    
    def set_verbosity(self, verbosity) -> None:
        '''
        Set logging level
        '''
        self.logger.setLevel(verbosity)
    
    def set_logformat(self, format) -> None:
        '''
        Set logging formating
        '''
        if not self.stream_handler in self.logger.handlers:
            self.logger.addHandler(self.stream_handler)
        self.stream_handler.setFormatter(format)

def set_debug(lg: Log):
    lg.set_verbosity(logging.DEBUG)
    lg.set_logformat("%(levelname)8s %(message)s")
    return lg