"""empty message

Revision ID: c97d1f8256ca
Revises: 8aca639e4a97
Create Date: 2020-12-13 19:19:52.045944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c97d1f8256ca'
down_revision = '8aca639e4a97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_relationship', sa.Column('Related_name', sa.String(length=100), nullable=False))
    op.add_column('user_relationship', sa.Column('Relating_name', sa.String(length=100), nullable=False))
    op.drop_constraint(None, 'user_relationship', type_='foreignkey')
    op.drop_constraint(None, 'user_relationship', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'user_relationship', 'user', ['Relating'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'user_relationship', 'user', ['Related'], ['id'], ondelete='CASCADE')
    op.drop_column('user_relationship', 'Relating_name')
    op.drop_column('user_relationship', 'Related_name')
    # ### end Alembic commands ###
