"""empty message

Revision ID: 838baf456e4c
Revises: a4909ffd6851
Create Date: 2020-03-22 19:39:49.100123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '838baf456e4c'
down_revision = 'a4909ffd6851'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('latest_report', schema=None) as batch_op:
        batch_op.add_column(sa.Column('arab', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('continent', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('latest_report', schema=None) as batch_op:
        batch_op.drop_column('continent')
        batch_op.drop_column('arab')

    # ### end Alembic commands ###
