"""empty message

Revision ID: 0bf9607cc4c9
Revises: 838baf456e4c
Create Date: 2020-03-22 22:03:58.161412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bf9607cc4c9'
down_revision = '838baf456e4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('latest_report', schema=None) as batch_op:
        batch_op.drop_column('province')
        batch_op.drop_column('arab')
        batch_op.drop_column('continent')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('latest_report', schema=None) as batch_op:
        batch_op.add_column(sa.Column('continent', sa.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('arab', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('province', sa.VARCHAR(length=100), nullable=True))

    # ### end Alembic commands ###
