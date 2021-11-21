"""create book table

Revision ID: d7cb791f8f39
Revises: 
Create Date: 2021-11-21 07:46:45.703671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7cb791f8f39'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'book',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(200), nullable=False),
    )


def downgrade():
    op.drop_table('book')
