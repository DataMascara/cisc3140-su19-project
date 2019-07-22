from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Post, Base, User

class Controller():

    def __init__(self, url):

        engine = create_engine(url)
        Base.metadata.bind = engine

        DBSession = sessionmaker(bind=engine)

        self.session = DBSession()

    def addUser(self, firstName, lastName, email, password):
        user = self.findUserByEmail(email)
        if user is None:
            user = User(firstName=firstName, lastName=lastName, email=email, password=password)
            self.session.add(user)
            self.session.commit()
            return True
        else:
            return False

    def deleteUser(self, email):
        user = self.findUserByEmail(email)
        if user is None:
            return False
        else:
            self.session.delete(user)
            self.session.commit()
            print(user.email)
            return True

    def findUserByEmail(self, email):
        user = self.session.query(User).filter_by(email=email).first()
        return user

    def findUserByID(self, id):
        user = self.session.query(User).filter_by(id=id).first()
        return user

    def getSession(self):
        return self.session

    def getAll(self):
        message = ''
        for user in self.session.query(User).all():
            if user is not None:
                # print(type(user.firstName))
                # print(user.firstName)
                message += str(user) + '<br>'

        return message
