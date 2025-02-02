import logging
import os
from flask.logging import default_handler

class LoggerConfig:
    def __init__(self, app):
        self.app = app
        self.folder = 'logs'

        # Create logs folder if it doesn't exist
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        # Remove the default log handler
        app.logger.removeHandler(default_handler)
        
        # Log format
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        formatter = logging.Formatter(log_format)

        # Info handler (logs INFO and WARNING)
        info_handler = logging.FileHandler(os.path.join(self.folder, "info.log"))
        info_handler.setLevel(logging.INFO)
        info_handler.setFormatter(formatter)

        # Define a filter to exclude ERROR and above levels from info_handler
        class MaxLevelFilter(logging.Filter):
            def __init__(self, level):
                self.max_level = level

            def filter(self, record):
                return record.levelno < self.max_level
            
        class warning_filter(logging.Filter):
            def filter(self, record):
                return record.levelno == logging.WARNING

        info_handler.addFilter(MaxLevelFilter(logging.WARNING))

        warning_handler = logging.FileHandler(os.path.join(self.folder, "warning.log"))
        warning_handler.setLevel(logging.WARNING)
        warning_handler.setFormatter(formatter)

        warning_handler.addFilter(warning_filter())

        # Error handler (logs ERROR and CRITICAL)
        error_handler = logging.FileHandler(os.path.join(self.folder, "error.log"))
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(formatter)

        # Add handlers to the app logger
        app.logger.addHandler(info_handler)
        app.logger.addHandler(error_handler)    
        app.logger.addHandler(warning_handler)

        # Set the app's logger level to DEBUG (logs everything)
        app.logger.setLevel(logging.DEBUG)
