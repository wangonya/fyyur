"""empty message

Revision ID: 2ea503b65873
Revises: 9e6d45f3dffe
Create Date: 2019-10-27 15:23:21.539231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ea503b65873'
down_revision = '9e6d45f3dffe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Show', 'venue_name')
    op.drop_column('Show', 'artist_name')
    op.drop_column('Show', 'artist_image_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('artist_image_link', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('Show', sa.Column('artist_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('Show', sa.Column('venue_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
