"""create author table

Revision ID: 60e706efe3e1
Revises: d7cb791f8f39
Create Date: 2021-11-21 08:40:27.917059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60e706efe3e1'
down_revision = 'd7cb791f8f39'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'author',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(200), nullable=False),
        sa.Column('last_name', sa.String(200), nullable=False),
    )


def downgrade():
    op.drop_table('author')
