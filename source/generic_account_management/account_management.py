from flask import request, jsonify
from flask_restful import Resource


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
            email=new_account_json['account_number'], tenant_key=tenant_key).first()
        if account:
            return {'result': 'Account already exists', 'JSON received': new_account_json}, 409
        else:
            new_account = Account()
            new_account.id = new_account_json['id']
            new_account.account_number = new_account_json['account_number']
            new_account.name = new_account_json['name']
            new_account.description = new_account_json['description']
            new_account.tenant_key = tenant_key
            new_account.creation_date = new_account_json['creation_date']
            new_account.account_type = new_account_json['account_type']
            new_account.balance = new_account_json['balance']
            new_account.creation_date = new_account_json['creation_date']
            db.session.add(new_account)
            db.session.commit()
            return {'result': 'Account created', 'JSON received': new_account_json}


""" class AccountManagement(Resource):
    def get(self, tenant_key, user_id):
        from .models.generic_account_management_models import Account
        user = User.query.filter_by(tenant_key=tenant_key, id=user_id).first()

        if not user:
            return {'result': 'No user by that id', 'Id received': user_id}, 404

        return jsonify(user.as_json())

    def put(self, tenant_key, user_id):
        from . import db
        from .models.generic_account_management_models import Account
        user = User.query.filter_by(tenant_key=tenant_key, id=user_id).first()

        if not user:
            return {'result': 'No user by that id', 'Id received': user_id}, 404

        user_json = request.get_json()
        user.first_name = user_json['first_name']
        user.last_name = user_json['last_name']
        user.email = user_json['email']
        user.mobile = user_json['mobile']

        db.session.commit()
        return {'result': 'User updated', 'JSON received': user_json}

    def delete(self, tenant_key, user_id):
        from . import db
        from .models.generic_account_management_models import Account
        user = User.query.filter_by(tenant_key=tenant_key, id=user_id).first()

        if not user:
            return {'result': 'No user by that id', 'Id received': user_id}, 404
        db.session.delete(user)
        db.session.commit()
        return {'result': 'User deleted', 'Id received': user_id} """
