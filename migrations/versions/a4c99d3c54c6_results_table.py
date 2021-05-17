"""results table

Revision ID: a4c99d3c54c6
Revises: 9cb1d9d88217
Create Date: 2021-05-15 21:48:33.612575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4c99d3c54c6'
down_revision = '9cb1d9d88217'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('result', sa.Column('first_correct', sa.Boolean(), nullable=True))
    op.add_column('result', sa.Column('second_correct', sa.Boolean(), nullable=True))
    op.add_column('result', sa.Column('third_correct', sa.Boolean(), nullable=True))
    op.add_column('result', sa.Column('fourth_correct', sa.Boolean(), nullable=True))
    op.add_column('result', sa.Column('fifth_correct', sa.Boolean(), nullable=True))
    op.add_column('result', sa.Column('sixth_correct', sa.Boolean(), nullable=True))
    op.add_column('result', sa.Column('seventh_correct', sa.Boolean(), nullable=True))
    op.add_column('result', sa.Column('eigth_correct', sa.Boolean(), nullable=True))
    op.add_column('result', sa.Column('ninth_correct', sa.Boolean(), nullable=True))
    op.add_column('result', sa.Column('tenth_correct', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('result', 'tenth_correct')
    op.drop_column('result', 'ninth_correct')
    op.drop_column('result', 'eigth_correct')
    op.drop_column('result', 'seventh_correct')
    op.drop_column('result', 'sixth_correct')
    op.drop_column('result', 'fifth_correct')
    op.drop_column('result', 'fourth_correct')
    op.drop_column('result', 'third_correct')
    op.drop_column('result', 'second_correct')
    op.drop_column('result', 'first_correct')
    # ### end Alembic commands ###
