from peewee import *

database = SqliteDatabase(None)

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class ViewModel(BaseModel):
    def save():
        raise RuntimeError("Attempted to insert into an SQL View")

class User(BaseModel):
    discord = TextField(null=True)
    display_name = TextField(null=True)
    nickname = TextField(unique=True)
    password = BlobField(null=True)
    temp_pw = BooleanField(default=True, null=True)
    wikidot = TextField(unique=True)

    class Meta:
        table_name = 'User'

class Article(BaseModel):
    added = TimestampField()
    bonus = IntegerField()
    corrected = TimestampField(null=True)
    author = ForeignKeyField(column_name='idauthor', field='id', model=User)
    corrector = ForeignKeyField(backref='User_idcorrector_set', column_name='idcorrector', field='id', model=User, null=True)
    is_original = BooleanField(default=False)
    link = TextField(null=True)
    name = TextField()
    words = IntegerField()

    class Meta:
        table_name = 'Article'

class Backup(BaseModel):
    articles = IntegerField()
    date = TimestampField()
    fingerprint = BlobField()
    author = ForeignKeyField(column_name='idauthor', field='id', model=User)
    sha1 = BlobField()

    class Meta:
        table_name = 'Backup'

class Note(BaseModel):
    content = TextField()
    author = ForeignKeyField(column_name='idauthor', field='id', model=User)
    title = TextField()

    class Meta:
        table_name = 'Note'

class Translation(BaseModel):
    added = TimestampField()
    bonus = IntegerField()
    author = ForeignKeyField(column_name='idauthor', field='id', model=User)
    link = TextField(null=True)
    name = TextField()
    words = IntegerField()

    class Meta:
        table_name = 'Translation'

class UserType(BaseModel):
    name = TextField(unique=True)

    class Meta:
        table_name = 'UserType'

class UserHasType(BaseModel):
    user_type = ForeignKeyField(column_name='idtype', field='id', model=UserType)
    user = ForeignKeyField(column_name='iduser', field='id', model=User)

    class Meta:
        table_name = 'UserHasType'

class Frontpage(ViewModel):
    ...
