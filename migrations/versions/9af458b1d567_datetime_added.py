"""datetime added

Revision ID: 9af458b1d567
Revises: a4c99d3c54c6
Create Date: 2021-05-16 17:16:58.625070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9af458b1d567'
down_revision = 'a4c99d3c54c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('result', sa.Column('date_created', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('day_joined', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'day_joined')
    op.drop_column('result', 'date_created')
    # ### end Alembic commands ###
