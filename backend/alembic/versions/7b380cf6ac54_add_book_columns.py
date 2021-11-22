"""add book columns

Revision ID: 7b380cf6ac54
Revises: e95772655a8d
Create Date: 2021-11-22 10:23:53.724028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b380cf6ac54'
down_revision = 'e95772655a8d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('book', sa.Column('annotation', sa.String(1000)))
    op.add_column('book', sa.Column('isbn', sa.String(100)))
    op.add_column('book', sa.Column('publish_at', sa.DATE))
    op.add_column('book', sa.Column('total_sells', sa.Integer))
    op.add_column('book', sa.Column('total_views', sa.Integer))



def downgrade():
    op.drop_column('book', 'annotation')
    op.drop_column('book', 'isbn')
    op.drop_column('book', 'publish_at')
    op.drop_column('book', 'total_sells')
    op.drop_column('book', 'total_views')

