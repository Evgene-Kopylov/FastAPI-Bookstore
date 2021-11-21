"""Add a column to author table

Revision ID: d199d9c8b73f
Revises: 60e706efe3e1
Create Date: 2021-11-21 08:43:17.271259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd199d9c8b73f'
down_revision = '60e706efe3e1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('author', sa.Column('middle_name', sa.String(200)))


def downgrade():
    op.drop_column('author', 'middle_name')
