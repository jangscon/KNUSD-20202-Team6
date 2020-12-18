"""empty message

Revision ID: cc1d5575f134
Revises: 3a9ca2f42acb
Create Date: 2020-12-17 09:19:48.759731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc1d5575f134'
down_revision = '3a9ca2f42acb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    with op.batch_alter_table('goal', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goal', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    with op.batch_alter_table('attendance', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    # ### end Alembic commands ###