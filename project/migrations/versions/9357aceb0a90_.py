"""empty message

Revision ID: 9357aceb0a90
Revises: cf1a81fea764
Create Date: 2020-12-13 19:23:05.427607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9357aceb0a90'
down_revision = 'cf1a81fea764'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_relationship', sa.Column('Related_name', sa.String(length=100), server_default='1', nullable=True))
    op.add_column('user_relationship', sa.Column('Relating_name', sa.String(length=100), server_default='1', nullable=True))
    op.drop_constraint(None, 'user_relationship', type_='foreignkey')
    op.drop_constraint(None, 'user_relationship', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'user_relationship', 'user', ['Related'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'user_relationship', 'user', ['Relating'], ['id'], ondelete='CASCADE')
    op.drop_column('user_relationship', 'Relating_name')
    op.drop_column('user_relationship', 'Related_name')
    # ### end Alembic commands ###
