"""Initial migration.

Revision ID: f68dc4829373
Revises: 
Create Date: 2020-10-02 02:11:29.658673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f68dc4829373'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('convidados',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=20), nullable=True),
    sa.Column('acompanhante', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_convidados_nome'), 'convidados', ['nome'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_convidados_nome'), table_name='convidados')
    op.drop_table('convidados')
    # ### end Alembic commands ###
