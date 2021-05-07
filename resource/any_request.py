from flask import request
from flask_restful import Resource
import app
from managers.logs import LogManager
from managers.response import ResponseManager


class AnyRequest(Resource):

    @staticmethod
    def get():
        # check if special params was in request
        invalid = request.args.get('invalid')
        notawaiting = request.args.get('notawaiting')

        if notawaiting == '1':
            # false request process as error
            logs = LogManager.process_error_log(request)
            app.app.logger.error(logs)
            return ResponseManager.error_response()

        if invalid == '1':
            # process and log as error
            logs = LogManager.process_error_log(request)
            app.app.logger.error(logs)
            return ResponseManager.success_response()

        # other cases of param give success logs and success response
        logs = LogManager.process_success_log(request)
        app.app.logger.info(logs)
        return ResponseManager.success_response()

    @staticmethod
    def post():
        logs = LogManager.process_error_log(request)
        app.app.logger.error(logs)
        return ResponseManager.success_response()

    @staticmethod
    def put():
        logs = LogManager.process_error_log(request)
        app.app.logger.error(logs)
        return ResponseManager.success_response()

    @staticmethod
    def delete():
        logs = LogManager.process_error_log(request)
        app.app.logger.error(logs)
        return ResponseManager.success_response()

    @staticmethod
    def patch():
        logs = LogManager.process_error_log(request)
        app.app.logger.error(logs)
        return ResponseManager.success_response()


