from datetime import date
from app.user.domain.entities.entity import Entity
from app.user.domain.value_object.roles import Roles

class User(Entity):

    def __init__(
        self,  last_name: str, first_name: str, phone: str, address: str,email: str,couple: str,enfants: str,allergies: str,regime: str, commentaires: str, gphoto: str, id: int = None
    ) -> None:
        self.id: int = id
        self.last_name: str = last_name
        self.first_name: str = first_name
        self.phone: str = phone
        self.address: str = address
        self.email: str = email
        self.couple: str = couple
        self.enfants: str = enfants
        self.allergies: str = allergies
        self.regime: str = regime
        self.commentaires: str = commentaires
        self.gphoto: str = gphoto

    @staticmethod
    def fromObject(obj):
        return User(
            id=obj.id,
            last_name=obj.last_name,
            first_name=obj.first_name,
            phone=obj.phone,
            address=obj.address,
            email=obj.email,
            couple=obj.couple,
            enfants=obj.enfants,
            allergies=obj.allergies,
            regime=obj.regime,
            commentaires=obj.commentaires,
            gphoto=obj.gphoto,
        )

    def toDict(self):
        return {"id": self.id, "last_name": self.last_name, "first_name": self.first_name, "phone": self.phone, "address": self.address, "email": self.email, "couple": self.couple, "enfants": self.enfants, "allergies": self.allergies, "regime": self.regime, "commentaires": self.commentaires, "gphoto": self.gphoto}


    def __repr__(self):
        return f"<User {self.id}>"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)
    """def __init__(
        self,  username: str, password: str, fullname: str, email: str, role: Roles = None, id: int = None
    ) -> None:
        self.id: int = id
        self.username: str = username
        self.password: str = password
        self.fullname: str = fullname
        self.email: str = email
        self.role: Roles = Roles(role)

    @staticmethod
    def fromObject(obj):
        return User(
            id=obj.id,
            username=obj.username,
            password=obj.password,
            fullname=obj.fullname,
            email=obj.email,
            role=Roles(obj.role)
        )

    def toDict(self):
        return {"id": self.id, "fullname": self.fullname, "username": self.username, "email": self.email, "role": self.role.value }


    def __repr__(self):
        return f"<User {self.id}>"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)"""