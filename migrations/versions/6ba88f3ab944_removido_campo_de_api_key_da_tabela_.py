"""removido campo de api key da tabela para o desenvolvimento da segunda versao do projeto

Revision ID: 6ba88f3ab944
Revises: 7fa91526be28
Create Date: 2022-04-20 18:16:07.045547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ba88f3ab944'
down_revision = '7fa91526be28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuarios', 'api_key')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuarios', sa.Column('api_key', sa.VARCHAR(length=511), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
