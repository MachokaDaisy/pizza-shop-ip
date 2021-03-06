"""Add flavour, size and topping tables

Revision ID: aafd499adc00
Revises: 322b836574cb
Create Date: 2020-09-24 06:17:57.938234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aafd499adc00'
down_revision = '322b836574cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flavours',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pizza_flavour', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pizza_flavour')
    )
    op.create_table('sizes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pizza_size', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pizza_size')
    )
    op.create_table('toppings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pizza_topping', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pizza_topping')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flavour_id', sa.Integer(), nullable=True),
    sa.Column('size_id', sa.Integer(), nullable=True),
    sa.Column('topping_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['flavour_id'], ['flavours.id'], ),
    sa.ForeignKeyConstraint(['size_id'], ['sizes.id'], ),
    sa.ForeignKeyConstraint(['topping_id'], ['toppings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('checkout',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('total_amout', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('checkout')
    op.drop_table('orders')
    op.drop_table('toppings')
    op.drop_table('sizes')
    op.drop_table('flavours')
    # ### end Alembic commands ###
