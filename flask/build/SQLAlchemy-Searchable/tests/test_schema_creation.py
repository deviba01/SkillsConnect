import sqlalchemy as sa
from sqlalchemy_utils import TSVectorType
from tests import SchemaTestCase


class TestAutomaticallyCreatedSchemaItems(SchemaTestCase):
    should_create_indexes = [
        u'textitem_search_vector_index',
    ]
    should_create_triggers = [
        u'textitem_search_vector_trigger',
    ]


class TestSearchVectorWithoutColumns(SchemaTestCase):
    should_create_indexes = [
        u'textitem_search_vector_index',
    ]
    should_create_triggers = []

    def create_models(self):
        class TextItem(self.Base):
            __tablename__ = 'textitem'

            id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

            name = sa.Column(sa.Unicode(255))

            search_vector = sa.Column(TSVectorType())

            content = sa.Column(sa.UnicodeText)
