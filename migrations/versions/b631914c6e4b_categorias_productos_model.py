"""categorias productos model

Revision ID: b631914c6e4b
Revises: 986b89f6f0e8
Create Date: 2023-02-25 03:42:28.800404

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b631914c6e4b'
down_revision = '986b89f6f0e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=90), nullable=False),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('productos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=45), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('imagen', sa.Text(), nullable=False),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('categorias_productos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=True),
    sa.Column('producto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoria_id'], ['categorias.id'], ),
    sa.ForeignKeyConstraint(['producto_id'], ['productos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('productos_model', schema=None) as batch_op:
        batch_op.drop_index('nombre')

    op.drop_table('productos_model')
    with op.batch_alter_table('categorias_model', schema=None) as batch_op:
        batch_op.drop_index('id')

    op.drop_table('categorias_model')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias_model',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=90), nullable=False),
    sa.Column('estado', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('categorias_model', schema=None) as batch_op:
        batch_op.create_index('id', ['id'], unique=False)

    op.create_table('productos_model',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=45), nullable=False),
    sa.Column('precio', mysql.FLOAT(), nullable=False),
    sa.Column('imagen', mysql.TEXT(), nullable=False),
    sa.Column('estado', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('productos_model', schema=None) as batch_op:
        batch_op.create_index('nombre', ['nombre'], unique=False)

    op.drop_table('categorias_productos')
    op.drop_table('productos')
    op.drop_table('categorias')
    # ### end Alembic commands ###