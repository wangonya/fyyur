"""empty message

Revision ID: 131853079f63
Revises: 2ea503b65873
Create Date: 2019-11-02 13:54:37.879620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '131853079f63'
down_revision = '2ea503b65873'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    # ### end Alembic commands ###