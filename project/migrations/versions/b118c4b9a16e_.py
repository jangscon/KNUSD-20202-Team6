"""empty message

Revision ID: b118c4b9a16e
Revises: 34b7720999b7
Create Date: 2020-12-13 19:14:57.113069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b118c4b9a16e'
down_revision = '34b7720999b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_relationship', type_='foreignkey')
    op.drop_constraint(None, 'user_relationship', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'user_relationship', 'user', ['Related'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'user_relationship', 'user', ['Relating'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###