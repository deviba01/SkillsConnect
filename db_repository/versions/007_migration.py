from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
meeting = Table('meeting', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('teacher', String(length=64)),
    Column('time', String(length=5)),
    Column('day', String(length=64)),
    Column('skill', String(length=120)),
    Column('classlocation', String(length=64)),
    Column('user_id', Integer),
    Column('user_skill', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['meeting'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['meeting'].drop()
