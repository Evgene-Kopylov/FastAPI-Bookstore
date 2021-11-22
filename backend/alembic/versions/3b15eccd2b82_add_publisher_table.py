"""add publisher table

Revision ID: 3b15eccd2b82
Revises: 336ef488f853
Create Date: 2021-11-22 08:36:23.845063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b15eccd2b82'
down_revision = '336ef488f853'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'publisher',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(200), nullable=False),
    )

def downgrade():
    op.drop_table('publisher')