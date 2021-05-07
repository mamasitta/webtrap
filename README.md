#Flask App
###To run locally
pull the code
move to the root directory of the project

create a virtual environment and run it using the following commands
virtualenv venv
source .env/bin/activate

intall the reqired dependencies by running the following command:
pip install -r requirements.txt

### Details
PORT set up on file .flaskenv to FLASK_RUN_PORT=8001

App is giving to all requests on 'http://127.0.0.1:8001/api' url response status_code - 200 

except GET request with param notawaiting=1, on GET request to url 'http://127.0.0.1:8001/api?notawaiting=1' server will return status_code - 400 and log it with error request

On GET request to 'http://127.0.0.1:8001/api?notawaiting=1' server response status_code - 200 and log it with error

any other GET request on 'http://127.0.0.1:8001/api' with any param will have response status_code - 200 and success logs

any request on url 'http://127.0.0.1:8001/api' except GET (DELETE, POST, PUT, PATCH), will have response status_code - 200 and log with error

###LOGs DATA example:

ERROR LOG:

2021-05-07 14:27:30,287 ERROR app MainThread : Processing error request:  GET http://localhost/api parameters: ImmutableMultiDict([('invalid', '1')])


SUCCESS LOG:

2021-05-07 14:27:30,290 INFO app MainThread : Processing success request:  GET http://localhost/api parameters: ImmutableMultiDict([('invalid', '2')])

### To run tests use the following command

python -m unittest discover .

test will give logs with url 'http://localhost/api'





