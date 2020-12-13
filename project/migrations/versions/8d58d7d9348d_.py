"""empty message

Revision ID: 8d58d7d9348d
Revises: 2249e5c0348b
Create Date: 2020-12-13 18:41:17.805552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d58d7d9348d'
down_revision = '2249e5c0348b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_relationship', 'Related',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user_relationship', 'Relating',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_relationship', 'Relating',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('user_relationship', 'Related',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###