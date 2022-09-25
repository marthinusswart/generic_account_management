from generic_account_management import db


class Account(db.Model):
    __tablename__ = 'generic_account'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    creation_date = db.Column(db.DateTime)
    description = db.Column(db.String(150))
    tenant_key = db.Column(db.String(150))
    account_type = db.Column(db.String(20))
    balance = db.Column(db.Float)
    account_number = db.Column(db.String(150))

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'account_type': self.account_type,
            'balance': self.balance,
            'creation_date': self.creation_date,
            'account_number': self.account_number,
            'tenant_key': self.tenant_key
        }


class TransactionClassification(db.Model):
    __tablename__ = 'generic_transaction_classification'
    id = db.Column(db.Integer, primary_key=True)
    classification = db.Column(db.String(150))
    description = db.Column(db.String(150))
    tenant_key = db.Column(db.String(150))

    def as_json(self):
        return {
            'id': self.id,
            'classification': self.classification,
            'description': self.description,
            'tenant_key': self.tenant_key
        }


class TransactionDetail(db.Model):
    __tablename__ = 'generic_transaction_detail'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    amount = db.Column(db.Float)
    description = db.Column(db.String(150))
    vendor_id = db.Column(db.Integer)
    tenant_key = db.Column(db.String(150))
    classification_id = db.Column(db.Integer)

    def as_json(self):
        return {
            'id': self.id,
            'account_id': self.account_id,
            'description': self.description,
            'date': self.date,
            'amount': self.amount,
            'vendor_id': self.vendor_id,
            'classification_id': self.classification_id,
            'tenant_key': self.tenant_key
        }
