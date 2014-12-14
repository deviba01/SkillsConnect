from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
    Column('location', String(length=64)),
    Column('phone', String(length=20)),
    Column('learnTeach', String(length=1)),
    Column('skill', String(length=120)),
    Column('about_me', String(length=140)),
    Column('last_seen', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['learnTeach'].create()
    post_meta.tables['user'].columns['location'].create()
    post_meta.tables['user'].columns['phone'].create()
    post_meta.tables['user'].columns['skill'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['learnTeach'].drop()
    post_meta.tables['user'].columns['location'].drop()
    post_meta.tables['user'].columns['phone'].drop()
    post_meta.tables['user'].columns['skill'].drop()
