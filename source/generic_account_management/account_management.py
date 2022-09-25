from flask import request, jsonify
from flask_restful import Resource
from datetime import datetime


class Accounts(Resource):
    def get(self, tenant_key):
        from .models.generic_account_management_models import Account
        accounts = Account.query.filter_by(tenant_key=tenant_key)
        result = [a.as_json() for a in accounts]
        print(tenant_key)
        return jsonify(result)

    def post(self, tenant_key):
        from . import db
        from .models.generic_account_management_models import Account

        new_account_json = request.get_json()

        account = Account.query.filter_by(
            account_number=new_account_json['account_number'], tenant_key=tenant_key).first()
        if account:
            return {'result': 'Account already exists', 'JSON received': new_account_json}, 409
        else:
            new_account = Account()
            cdate = datetime.strptime(
                new_account_json['creation_date'], '%Y-%m-%d %H:%M:%S')

            new_account.account_number = new_account_json['account_number']
            new_account.name = new_account_json['name']
            new_account.description = new_account_json['description']
            new_account.tenant_key = tenant_key
            new_account.creation_date = cdate
            new_account.account_type = new_account_json['account_type']
            new_account.balance = new_account_json['balance']
            new_account.credit_limit = new_account_json['credit_limit']
            db.session.add(new_account)
            db.session.commit()
            return {'result': 'Account created', 'JSON received': new_account_json}


class AccountManagement(Resource):
    def get(self, tenant_key, account_id):
        from .models.generic_account_management_models import Account
        account = Account.query.filter_by(
            tenant_key=tenant_key, id=account_id).first()

        if not account:
            return {'result': 'No account by that id', 'Id received': account_id}, 404

        return jsonify(account.as_json())

    def put(self, tenant_key, account_id):
        from . import db
        from .models.generic_account_management_models import Account
        account = Account.query.filter_by(
            tenant_key=tenant_key, id=account_id).first()

        if not account:
            return {'result': 'No account by that id', 'Id received': account_id}, 404

        account_json = request.get_json()
        cdate = datetime.strptime(
            account_json['creation_date'], '%Y-%m-%d %H:%M:%S')
        account.account_number = account_json['account_number']
        account.name = account_json['name']
        account.description = account_json['description']
        account.tenant_key = tenant_key
        account.account_type = account_json['account_type']
        account.balance = account_json['balance']
        account.credit_limit = account_json['credit_limit']
        account.creation_date = cdate

        db.session.commit()
        return {'result': 'Account updated', 'JSON received': account_json}

    def delete(self, tenant_key, account_id):
        from . import db
        from .models.generic_account_management_models import Account
        account = Account.query.filter_by(
            tenant_key=tenant_key, id=account_id).first()

        if not account:
            return {'result': 'No account by that id', 'Id received': account_id}, 404
        db.session.delete(account)
        db.session.commit()
        return {'result': 'Account deleted', 'Id received': account_id}
