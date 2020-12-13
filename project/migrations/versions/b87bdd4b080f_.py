"""empty message

Revision ID: b87bdd4b080f
Revises: 031bd2da7fd2
Create Date: 2020-12-13 18:27:49.414456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b87bdd4b080f'
down_revision = '031bd2da7fd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_username'), ['username'])

    with op.batch_alter_table('user_relationship', schema=None) as batch_op:
        batch_op.alter_column('Related',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('Relating',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.create_foreign_key(batch_op.f('fk_user_relationship_Related_user'), 'user', ['Related'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(batch_op.f('fk_user_relationship_Relating_user'), 'user', ['Relating'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_relationship', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_user_relationship_Relating_user'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_user_relationship_Related_user'), type_='foreignkey')
        batch_op.alter_column('Relating',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('Related',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_email'), type_='unique')

    # ### end Alembic commands ###
