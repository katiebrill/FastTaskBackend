from flask import *
from extensions import db
import pdb

pic = Blueprint('pic', __name__, template_folder='templates')

@pic.route('/push', methods=['GET', 'POST'])
def get_classes():


