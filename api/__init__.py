from flask_restx import Namespace

api_namespace = Namespace('api', description='signed RESTful API')

from . import api_total_client
from . import api_client_list
from . import api_signed_range
from . import api_job_check
