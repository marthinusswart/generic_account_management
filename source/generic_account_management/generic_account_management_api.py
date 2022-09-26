from flask_restful import Api
from generic_account_management.api_management import ApiManagement
from generic_account_management.account_management import Accounts, AccountManagement


def create_api(app):
    api = Api(app)
    api.add_resource(ApiManagement, '/api/v1')
    api.add_resource(Accounts, '/api/v1/<tenant_key>/accounts')
    api.add_resource(AccountManagement,
                     '/api/v1/<tenant_key>/accounts/<int:account_id>')
    return api
