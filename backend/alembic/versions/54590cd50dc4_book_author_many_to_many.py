"""book author Many-to-Many

Revision ID: 54590cd50dc4
Revises: d199d9c8b73f
Create Date: 2021-11-21 19:18:31.563190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54590cd50dc4'
down_revision = 'd199d9c8b73f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'book_author',
        sa.Column('book_id', sa.Integer, primary_key=True),
        sa.Column('author_id', sa.Integer, primary_key=True)
    )    


def downgrade():
    op.drop_table('book_author')
