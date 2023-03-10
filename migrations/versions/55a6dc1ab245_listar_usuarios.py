"""listar  usuarios

Revision ID: 55a6dc1ab245
Revises: 008d342c4b00
Create Date: 2023-02-25 11:30:41.059291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55a6dc1ab245'
down_revision = '008d342c4b00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
