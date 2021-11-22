"""book publisher One-to-Many

Revision ID: 336ef488f853
Revises: 54590cd50dc4
Create Date: 2021-11-22 08:33:34.665180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '336ef488f853'
down_revision = '54590cd50dc4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('book', sa.Column('publisher_id', sa.Integer))


def downgrade():
    op.drop_column('book', 'publisher')
