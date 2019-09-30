from app import db

# By default nullable is set as false
# Class used to create user table (users)
class User(db.Model):
    __tablename__ = "MFP_Adopt_User"

    id_user = db.Column(db.Integer, primary_key=True)
    ds_email = db.Column(db.String(256), unique=True)
    ds_password = db.Column(db.String(256))
    img_user = db.Column(db.String(256))
    id_zipcode = db.Column(db.Integer, db.ForeignKey('Zipcode.id_zipcode'))
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())

    zipcode = db.relationship('Zipcode', foreign_keys=id_zipcode)

    def __init__(self, ds_email, ds_password, img_user, id_zipcodes):
        self.ds_email = ds_email
        self.ds_password = ds_password
        self.img_user = img_user
        self.id_zipcodes = id_zipcodes

    def __repr__(self):
        return "<id_user='%i', ds_email='%s', img_user='%s', id_zipcode='%i'>" % (self.id_user, self.ds_email, self.ds_email, self.id_zipcode)


# Class used to create zipcode table (zipcodes)
class Zipcode(db.Model):
    __tablename__ = "MFP_Adopt_Zipcode"

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
    __tablename__ = "MFP_Adopt_Corporation"

    id_corporation = db.Column(db.Integer, primary_key=True)
    ds_name = db.Column(db.String(256))
    nb_cnpj = db.Column(db.String(18), unique=True)
    id_user = db.Column(db.Integer, db.ForeignKey('User.id_user'))

    user = db.relationship('User', foreign_keys=id_user)

    def __init__(self, ds_name, nb_cnpj, id_user):
        self.ds_name = ds_name
        self.nb_cnpj = nb_cnpj
        self.id_user = id_user

    def __repr__(self):
        return "<id_corporation='%i', ds_name='%s', nb_cnpj='%s', id_user='%i'>" % (self.id_corporation, self.ds_name, self.nb_cnpj, self.id_user)


# Class used to create individual table (individuals)
class Individual(db.Model):
    __tablename__ = "MFP_Adpot_Individual"

    id_individual = db.Column(db.Integer, primary_key=True)
    ds_firstname = db.Column(db.String(100))
    ds_lastname = db.Column(db.String(100))
    nb_age = db.Column(db.Integer)
    id_user = db.Column(db.Integer, db.ForeignKey('User.id_user'))

    user = db.relationship('User', foreign_keys=id_user)

    def __init__(self, ds_firstname, ds_lastname, nb_age, id_user):
        self.ds_firstname = ds_firstname
        self.ds_lastname = ds_lastname
        self.nb_age = nb_age
        self.id_user = id_user

    def __repr__(self):
        return "<id_individual='%i', ds_firstname='%s', ds_lastname='%s', nb_age='%i', id_user='%i'>" % (self.id_individual, self.ds_firstname, self.ds_lastname, self.nb_age, self.id_user)


# Class used to create contact type table (contact_types)
class ContactType(db.Model):
    __tablename__ = "MFP_Adopt_ContactType"

    id_contactType = db.Column(db.Integer, primary_key=True)
    nb_telephone = db.Column(db.String(15))
    id_user = db.Column(db.Integer, db.ForeignKey('User.id_user'))

    user = db.relationship('User', foreign_keys=id_user)

    def __init__(self, nb_telephone, id_user):
        self.nb_telephone = nb_telephone
        self.id_user = id_user

    def __repr__(self):
        return "<id_contactType='%i', nb_telephone='%s', id_user='%i'>" % (self.id_contactType, self.nb_telephone, self.id_user)


# Class used to create pet table (pets)
class Pet(db.Model):
    __tablename__ = "MFP_Adpot_Pet"

    id_pet = db.Column(db.Integer, primary_key=True)
    ds_info = db.Column(db.Text)
    nb_age = db.Column(db.Integer)
    op_sex = db.Column(db.Boolean)
    op_hairSize = db.Column(db.Integer)
    nb_weight = db.Column(db.Integer)
    st_adoption = db.Column(db.Boolean)
    id_breed = db.Column(db.Integer, db.ForeignKey('Breed.id_breed'))
    id_user = db.Column(db.Integer, db.ForeignKey('User.id_user'))
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())

    user = db.relationship('User', foreign_keys=id_user)
    breed = db.relationship('Breed', foreign_keys=id_breed)

    def __init__(self, ds_info, nb_age, op_sex, op_hairSize, nb_weight, st_adoption, id_breed, id_user):
        self.ds_info = ds_info
        self.nb_age = nb_age
        self.op_sex = op_sex
        self.op_hairSize = op_hairSize
        self.nb_weight = nb_weight
        self.st_adoption = st_adoption
        self.id_breed = id_breed
        self.id_user = id_user

    def __repr__(self):
        return "<id_pet='%i', id_user='%i', nb_age='%i', op_sex='%s', st_adoption='%s', op_hairSize='%s', nb_weight='%s', id_breed='%i'>" % (self.id_pet, self.id_user, self.nb_age, self.op_sex, self.st_adoption, self.op_hairSize, self.nb_weight, self.id_breed)


# Class used to create pet type table (pet_types)
class PetType(db.Model):
    __tablename__ = "MFP_Adopt_PetType"

    id_petType = db.Column(db.Integer, primary_key=True)
    ds_name = db.Column(db.String(256))
    id_petCategory = db.Column(db.Integer, db.ForeignKey('PetCategory.id_petCategory'))

    petCategory = db.relationship('PetCategory', foreign_keys=id_petCategory)

    def __init__(self, ds_name, id_petCategory):
        self.ds_name = ds_name
        self.id_petCategory = id_petCategory

    def __repr__(self):
        return "<id_petType='%i', ds_name='%s', id_petCategory='%i'>" % (self.id_petType, self.ds_name, self.id_petCategory)


# Class used to create pet category table (pet_categories)
class PetCategory(db.Model):
    __tablename__ = "MFP_Adopt_Category"

    id_petCategory = db.Column(db.Integer, primary_key=True)
    ds_name = db.Column(db.String(256))

    def __init__(self, ds_name):
        self.ds_name = ds_name

    def __repr__(self):
        return "<id_petCategory='%i', ds_name='%s'>" % (self.id_petCategory, self.ds_name)


# Class used to create breed table (breeds)
class Breed(db.Model):
    __tablename__ = "MFP_Adopt_Breed"

    id_breed = db.Column(db.Integer, primary_key=True)
    ds_name = db.Column(db.String(256))

    def __init__(self, ds_name):
        self.ds_name = ds_name

    def __repr__(self):
        return "<id_breed='%i', ds_name='%s'>" % (self.id_breed, self.ds_name)


# Class used to create adoption table (adoptions)
class Adoption(db.Model):
    __tablename__ = "adoptions"

    id = db.Column(db.Integer, primary_key=True)
    pets_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
    pets_users_id = db.Column(db.Integer, db.ForeignKey('pets.users_id'))
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now(), server_onupdate=db.func.now())

    pets = db.relationship('Pet', foreign_keys=pets_id)
    pets_users = db.relationship('Pet', foreign_keys=pets_users_id)
    users = db.relationship('User', foreign_keys=users_id)

    def __init__(self, pets_id, pets_users_id, users_id):
        self.pets_id = pets_id
        self.pets_users_id = pets_users_id
        self.users_id = users_id

    def __repr__(self):
        return "<Adoption %r>" % self.id
