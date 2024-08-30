import json_log_formatter

class CustomJSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message, extra, record):
        log_obj = {
            'asctime': self.formatTime(record, self.datefmt),
            'name': record.name,
            'levelname': record.levelname,
            'message': message
        }
        return log_obj