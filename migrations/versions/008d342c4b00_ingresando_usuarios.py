"""ingresando usuarios

Revision ID: 008d342c4b00
Revises: 2783760912c9
Create Date: 2023-02-25 10:52:38.603980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '008d342c4b00'
down_revision = '2783760912c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombres', sa.String(length=200), nullable=False),
    sa.Column('correo', sa.String(length=100), nullable=False),
    sa.Column('imagen', sa.Text(), nullable=True),
    sa.Column('contrasena', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios')
    # ### end Alembic commands ###
