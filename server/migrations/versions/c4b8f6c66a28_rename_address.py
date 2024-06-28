"""rename address

Revision ID: c4b8f6c66a28
Revises: 1f1edcfb702c
Create Date: 2024-06-28 08:06:41.849065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4b8f6c66a28'
down_revision = '1f1edcfb702c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
