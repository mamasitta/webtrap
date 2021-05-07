import datetime


class LogManager:

    @staticmethod
    def process_error_log(request) -> str:
        """
        Processing error request give logs with request details
        :param request:
        :return:
        """
        method = request.method
        url = request.base_url
        params = request.args
        logs_format = 'Processing error request:  {method} {url} parameters: {param}'.format(
            method=method,
            url=url,
            param=params)
        return logs_format

    @staticmethod
    def process_success_log(request) -> str:
        """
        Processing success request give logs with request details
        :param request:
        :return:
        """
        method = request.method
        url = request.base_url
        params = request.args
        logs_format = 'Processing success request:  {method} {url} parameters: {param}'.format(
            method=method,
            url=url,
            param=params)
        return logs_format
