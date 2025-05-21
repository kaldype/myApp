from config import db

# Database model represented as a python class via ORM
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Max length is 80 chars
    first_name = db.Column(db.String(80), unique = False, nullable = False)
    last_name = db.Column(db.String(80), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

    # API will receive and send JSON contact info
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }
        


