from app import db

#By default nullable is set as false
# Class used to create user table (users)
class User(db.Model):
    __tablename__ = "MFP_Users"

    id_user = db.Column(db.Integer, primary_key=True)
    ds_email = db.Column(db.String(256), unique=True)
    ds_password = db.Column(db.String(256))
    img_user = db.Column(db.String(256))
    id_zipcode = db.Column(db.Integer, db.ForeignKey('id_zipcode'))
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())

    zipcode = db.relationship('ZipCode', foreign_keys=id_zipcode)

    def __init__(self, ds_email, ds_password, img_user, id_zipcodes):
        self.ds_email = ds_email
        self.ds_password = ds_password
        self.img_user = img_user
        self.id_zipcodes = id_zipcodes

    def __repr__(self):
        return "<id_user='%i', ds_email='%s', img_user='%s', id_zipcode='%i'>" % (self.id_user, self.ds_email, self.ds_email, self.id_zipcode)


# Class used to create zipcode table (zipcodes)
class ZipCode(db.Model):
    __tablename__ = "MFP_Zipcode"

    id_zipcode = db.Column(db.Integer, primary_key=True)
    cd_zipcode = db.Column(db.String(8))
    ds_address = db.Column(db.String(200))
    ds_complement = db.Column(db.String(50))
    ds_neighborhood = db.Column(db.String(100))
    ds_city = db.Column(db.String(50))
    ds_state = db.Column(db.String(2))
    ds_country = db.Column(db.String(3))

    def __init__(self, cd_zipcode, ds_address, ds_neighborhood, ds_city, ds_state, ds_country):
        self.cd_zipcode = cd_zipcode
        self.ds_address = ds_address
        self.ds_neighborhood = ds_neighborhood
        self.ds_city = ds_city
        self.ds_state = ds_state
        self.ds_country = ds_country

    def __repr__(self):
        return "<id_zipcode='%i', cd_zipcode='%i', ds_address='%s', ds_complement='%s', ds_city='%s', ds_state='%s', ds_country='%s'>" % (self.id_zipcode, self.cd_zipcode, self.ds_address, self.ds_complement, self.ds_city, self.ds_state, self.ds_country)


# Class used to create corporation table (corporations)
class Corporation(db.Model):
    __tablename__ = "MFP_Corporations"

    id_corporation = db.Column(db.Integer, primary_key=True)
    ds_name = db.Column(db.String(256))
    nb_cnpj = db.Column(db.String(18), unique=True)
    id_user = db.Column(db.Integer, db.ForeignKey('Users.id_user'))

    users = db.relationship('User', foreign_keys=id_user)

    def __init__(self, ds_name, nb_cnpj, id_user):
        self.ds_name = ds_name
        self.nb_cnpj = nb_cnpj
        self.id_user = id_user

    def __repr__(self):
        return "<id_corporation='%i', ds_name='%s', nb_cnpj='%s', id_user='%i'>" % (self.id_corporation, self.ds_name, self.nb_cnpj, self.id_user)


# Class used to create individual table (individuals)
class Individual(db.Model):
    __tablename__ = "individuals"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    sex = db.Column(db.Boolean)
    age = db.Column(db.Integer)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    users = db.relationship('User', foreign_keys=users_id)

    def __init__(self, first_name, last_name, sex, users_id):
        self.first_name = first_name
        self.last_name - last_name
        self.sex = sex
        self.users_id = users_id

    def __repr__(self):
        return "<Individual %r>" % self.first_name


# Class used to create contact type table (contact_types)
class ContactType(db.Model):
    __tablename__ = "contact_types"

    id = db.Column(db.Integer, primary_key=True)
    telephone = db.Column(db.String(12))
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    users = db.relationship('User', foreign_keys=users_id)

    def __init__(self, users_id):
        self.users_id = users_id

    def __repr__(self):
        return "<ContactType %r>" % self.telephone


# Class used to create pet table (pets)
class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    pet_types_id = db.Column(db.Integer, db.ForeignKey('pet_types.id'))
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    age = db.Column(db.Integer)
    info = db.Column(db.String(400))
    sex = db.Column(db.Boolean)
    status = db.Column(db.Boolean)
    hair_size = db.Column(db.Boolean)
    weight = db.Column(db.Integer)
    breeds_id = db.Column(db.Integer, db.ForeignKey('breeds.id'))

    pet_types = db.relationship('PetType', foreign_keys=pet_types_id)
    users = db.relationship('User', foreign_keys=users_id)
    breeds = db.relationship('Breed', foreign_keys=breeds_id)

    def __init__(self, pet_types_id, users_id, age, sex, status, breeds_id):
        self.pet_types_id = pet_types_id
        self.users_id = users_id
        self.age = age
        self.sex = sex
        self.status = status
        self.breeds_id = breeds_id

    def __repr__(self):
        return "<Pet %r>" % self.pet_types_id


# Class used to create pet type table (pet_types)
class PetType(db.Model):
    __tablename__ = "pet_types"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    pet_categories_id = db.Column(db.Integer, db.ForeignKey('pet_categories.id'))

    pet_categories = db.relationship('PetCategory', foreign_keys=pet_categories_id)

    def __init__(self, type, pet_categories_id):
        self.type = type
        self.pet_categories_id = pet_categories_id

    def __repr__(self):
        return "<PetType %r>" % self.type


# Class used to create pet category table (pet_categories)
class PetCategory(db.Model):
    __tablename__ = "pet_categories"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))

    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return "<PetCategory %r>" % self.category


# Class used to create breed table (breeds)
class Breed(db.Model):
    __tablename__ = "breeds"

    id = db.Column(db.Integer, primary_key=True)
    ds_breed = db.Column(db.String(45))

    def __init__(self, ds_breed):
        self.ds_breed = ds_breed

    def __repr__(self):
        return "<Breed %r>" % self.ds_breed


# Class used to create adoption table (adoptions)
class Adoption(db.Model):
    __tablename__ = "adoptions"

    id = db.Column(db.Integer, primary_key=True)
    pets_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
    pets_users_id = db.Column(db.Integer, db.ForeignKey('pets.users_id'))
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    pets = db.relationship('Pet', foreign_keys=pets_id)
    pets_users = db.relationship('Pet', foreign_keys=pets_users_id)
    users = db.relationship('User', foreign_keys=users_id)

    def __init__(self, pets_id, pets_users_id, users_id):
        self.pets_id = pets_id
        self.pets_users_id = pets_users_id
        self.users_id = users_id

    def __repr__(self):
        return "<Adoption %r>" % self.id
