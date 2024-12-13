from db import db


# class CarModel(db.Model):
#     __tablename__ = "cars"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#     brand = db.Column(db.String(80), nullable=False)
#     make = db.Column(db.String(80), nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     price = db.Column(db.Integer, nullable=False)
#     km = db.Column(db.Integer, nullable=True)
#     cm3 = db.Column(db.Integer, nullable=True)


    # -- Branch Model
class Branch(db.Model):
    __tablename__ = "branches"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255))
    contact = db.Column(db.String(15))

# -- Customer Model
class CustomerModel(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(255))
    phone = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    id_proof_type = db.Column(db.String(50), nullable=False)
    id_proof_number = db.Column(db.String(50), unique=True, nullable=False)

# -- Account Model
class AccountModel(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'), nullable=False)
    account_type = db.Column(db.String(10), nullable=False)
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    opening_date = db.Column(db.Date, nullable=False)
    balance = db.Column(db.Numeric(15, 2), default=0)
    status = db.Column(db.String(10), nullable=False)

# -- Saving Account Model
class SavingAccountModel(db.Model):
    __tablename__ = "saving_accounts"

    id = db.Column(db.Integer, db.ForeignKey('accounts.id'), primary_key=True)
    interest_rate = db.Column(db.Numeric(5, 2), nullable=False)
    min_balance_requirement = db.Column(db.Numeric(15, 2), nullable=False)

# -- Current Account Model
class CurrentAccountModel(db.Model):
    __tablename__ = "current_accounts"

    id = db.Column(db.Integer, db.ForeignKey('accounts.id'), primary_key=True)
    overdraft_limit = db.Column(db.Numeric(15, 2), nullable=False)

# -- Verification Log Model
class VerificationLogModel(db.Model):
    __tablename__ = "verification_logs"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    verified_by = db.Column(db.String(50), nullable=False)
    verification_date = db.Column(db.Date, nullable=False)
    verification_status = db.Column(db.String(20), nullable=False)
    remarks = db.Column(db.String(255))



