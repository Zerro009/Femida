from flask import Flask, Blueprint
from .views import *

scanner = Blueprint('scanner', __name__)

scanner.add_url_rule('/ping/', 'ping', ping)

