from app.user.domain.entities.user import User
from app.user.services.user_service import  create_new_user, filter_role_and_email


user_dummy = User(last_name="test", first_name="test", phone="test", address="test",email="test",couple="test",enfants="test",allergies="test",regime="test", commentaires="test", gphoto="test")
create_new_user(
        user=user_dummy, 
        last_name="test",
        first_name="test",
        phone="test",
        address="test",
        email="test",
        couple="test",
        enfants="test",
        allergies="test",
        regime="test",
        commentaires="test",
        gphoto="test"
    )
