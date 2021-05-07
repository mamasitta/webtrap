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
        time = datetime.datetime.now().timestamp()
        logs = 'Processing error request:\nmethod: {method}\nurl: {url}\nparameters: {param}\ntime: {time}'.format(
            method=method,
            url=url,
            param=params,
            time=time)
        return logs

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
        time = datetime.datetime.now().timestamp()
        logs = 'Processing success request:\nmethod: {method}\nurl: {url}\nparameters: {param}\ntime: {time}'.format(
            method=method,
            url=url,
            param=params,
            time=time)
        return logs
