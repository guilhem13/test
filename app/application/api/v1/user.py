import csv
from flask import jsonify, request, send_file
from app.application.http.response import Response
from app.application.validator.user import create_user_validate, update_user_validate, auth_login_validate
from app.infrastructure.persistence.sqlalchemy.repositories.user_repository import UserSqlAlchemyRepository
from app.user.services.user_service import create_new_user, select_all_user, update_data_user, filter_role_and_email, delete_data_user, get_users
from app.user.domain.entities.user import User
from app.user.services.user_service import user_must_unique
import json
import os
from .base import api_v1


@api_v1.route("/registration", methods=["POST"])
def registration():
    try:
        data = request.json
        validate = create_user_validate(data)
        if UserSqlAlchemyRepository.checkEmailMustUnique(data["email"]) == True: 
            user1 = User(last_name=data["last_name"], first_name=data["first_name"], phone=data["phone"], address=data["address"],email=data["email"],couple=data["couple"],enfants=data["enfants"],allergies=data["allergies"],regime=data["regime"], commentaires=data["commentaires"], gphoto=data["gphoto"])
            if(validate['isError']):
                return Response().badRequest(message="Failed to create user", errorMessage=validate['message'])
            UserSqlAlchemyRepository.add(user1)
            return jsonify({"message": "Form submitted successfully!"}), 200
        else: 
            return Response().serverError(message="You have already been registered in the wedding ", errorMessage=str(e))
    except Exception as e:
         return Response().serverError(message="Failed to create user", errorMessage=str(e))

@api_v1.route("/quentin/list", methods=["GET"])
def registrationList():
    User_List = UserSqlAlchemyRepository.all()
    data = [x.toDict() for x in User_List]
    csv_file_path = os.path.expanduser('~/Application/registration_list.csv')

    if data:
        keys = data[0].keys()

        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            
            # Write the header
            writer.writeheader()
            
            # Write the rows
            writer.writerows(data)

        print(f"Data has been written to {csv_file_path}")
        return send_file(csv_file_path, as_attachment=True, download_name=csv_file_path)
    
    else: 
        return "No data available to export.", 404
    
    






