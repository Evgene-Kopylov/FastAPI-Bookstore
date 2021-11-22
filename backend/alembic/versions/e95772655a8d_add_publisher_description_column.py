"""add publisher description column

Revision ID: e95772655a8d
Revises: 3b15eccd2b82
Create Date: 2021-11-22 10:05:47.541753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e95772655a8d'
down_revision = '3b15eccd2b82'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('publisher', sa.Column('description', sa.String(600)))


def downgrade():
    op.drop_column('publisher', 'description')
