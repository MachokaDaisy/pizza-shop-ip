"""Fixed table typo

Revision ID: 83cbc2c939e5
Revises: aafd499adc00
Create Date: 2020-09-24 06:50:43.502471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83cbc2c939e5'
down_revision = 'aafd499adc00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('checkout', sa.Column('total_amount', sa.Integer(), nullable=True))
    op.drop_column('checkout', 'total_amout')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('checkout', sa.Column('total_amout', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('checkout', 'total_amount')
    # ### end Alembic commands ###