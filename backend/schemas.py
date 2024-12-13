# from marshmallow import Schema,fields

# class CarSchema(Schema):
#     id = fields.Str(dump_only=True)
#     name = fields.Str(required=True)
#     brand = fields.Str(required=True)
#     make = fields.Str(required=True)
#     year = fields.Integer(required=True)
#     price = fields.Integer(required=True)
#     km = fields.Integer(required=False)
#     cm3 = fields.Integer(required=False)



from marshmallow import Schema, fields

# -- Branch Schema
class BranchSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    address = fields.Str(required=False)
    contact = fields.Str(required=False)

# -- Customer Schema
class CustomerSchema(Schema):
    id = fields.Str(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    dob = fields.Date(required=True)
    address = fields.Str(required=False)
    phone = fields.Str(required=True)
    email = fields.Str(required=True)
    id_proof_type = fields.Str(required=True)
    id_proof_number = fields.Str(required=True)

# -- Account Schema
class AccountSchema(Schema):
    id = fields.Str(dump_only=True)
    customer_id = fields.Str(required=True)
    branch_id = fields.Str(required=True)
    account_type = fields.Str(required=True)
    account_number = fields.Str(required=True)
    opening_date = fields.Date(required=True)
    balance = fields.Decimal(as_string=True, required=False)
    status = fields.Str(required=True)

# -- Saving Account Schema
class SavingAccountSchema(Schema):
    id = fields.Str(dump_only=True)
    interest_rate = fields.Decimal(as_string=True, required=True)
    min_balance_requirement = fields.Decimal(as_string=True, required=True)

# -- Current Account Schema
class CurrentAccountSchema(Schema):
    id = fields.Str(dump_only=True)
    overdraft_limit = fields.Decimal(as_string=True, required=True)

# -- Verification Log Schema
class VerificationLogSchema(Schema):
    id = fields.Str(dump_only=True)
    customer_id = fields.Str(required=True)
    verified_by = fields.Str(required=True)
    verification_date = fields.Date(required=True)
    verification_status = fields.Str(required=True)
    remarks = fields.Str(required=False)
