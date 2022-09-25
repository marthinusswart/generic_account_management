from flask_restful import Api
from generic_account_management.api_management import ApiManagement
from generic_account_management.account_management import Accounts


def create_api(app):
    api = Api(app)
    api.add_resource(ApiManagement, '/')
    api.add_resource(Accounts, '/<tenant_key>/accounts')
    #api.add_resource(UserManagement, '/<tenant_key>/users/<int:user_id>')
    return api
