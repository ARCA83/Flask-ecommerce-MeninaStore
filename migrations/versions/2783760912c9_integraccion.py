"""integraccion

Revision ID: 2783760912c9
Revises: b631914c6e4b
Create Date: 2023-02-25 09:17:06.836535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2783760912c9'
down_revision = 'b631914c6e4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categorias', schema=None) as batch_op:
        batch_op.drop_index('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categorias', schema=None) as batch_op:
        batch_op.create_index('id', ['id'], unique=False)

    # ### end Alembic commands ###