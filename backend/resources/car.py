from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.car import Branch
from models.car import SavingAccountModel, CurrentAccountModel
from models.car import CustomerModel
from models.car import VerificationLogModel

from schemas import BranchSchema
from schemas import SavingAccountSchema
from schemas import CurrentAccountSchema
from schemas import CustomerSchema
from schemas import VerificationLogSchema

blp = Blueprint("BankOperations", __name__, description="Operations on bank entities")

@blp.route("/branch/<string:branch_id>")
class Branch(MethodView):
    @blp.response(200, BranchSchema)
    def get(self, branch_id):
        branch = BranchModel.query.get_or_404(branch_id)
        return branch

    def delete(self, branch_id):
        branch = BranchModel.query.get_or_404(branch_id)
        db.session.delete(branch)
        db.session.commit()
        return {"message": "Branch deleted"}, 200

@blp.route("/branch")
class BranchList(MethodView):
    @blp.response(200, BranchSchema(many=True))
    def get(self):
        branches = BranchModel.query.all()
        return branches

    @blp.arguments(BranchSchema)
    @blp.response(201, BranchSchema)
    def post(self, branch_data):
        branch = BranchModel(**branch_data)
        try:
            db.session.add(branch)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A branch with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the branch.")
        return branch

@blp.route("/customer/<string:customer_id>")
class Customer(MethodView):
    @blp.response(200, CustomerSchema)
    def get(self, customer_id):
        customer = CustomerModel.query.get_or_404(customer_id)
        return customer

    def delete(self, customer_id):
        customer = CustomerModel.query.get_or_404(customer_id)
        db.session.delete(customer)
        db.session.commit()
        return {"message": "Customer deleted"}, 200

@blp.route("/customer")
class CustomerList(MethodView):
    @blp.response(200, CustomerSchema(many=True))
    def get(self):
        customers = CustomerModel.query.all()
        return customers

    @blp.arguments(CustomerSchema)
    @blp.response(201, CustomerSchema)
    def post(self, customer_data):
        customer = CustomerModel(**customer_data)
        try:
            db.session.add(customer)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A customer with that ID proof number already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the customer.")
        return customer
