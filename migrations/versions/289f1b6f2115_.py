"""empty message

Revision ID: 289f1b6f2115
Revises: 
Create Date: 2022-03-13 18:06:35.397017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '289f1b6f2115'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('passwordcifrada', sa.LargeBinary(), nullable=True),
    sa.Column('dni', sa.String(length=10), nullable=False),
    sa.Column('nombre', sa.String(length=20), nullable=False),
    sa.Column('apellidos', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('dni'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    # ### end Alembic commands ###
