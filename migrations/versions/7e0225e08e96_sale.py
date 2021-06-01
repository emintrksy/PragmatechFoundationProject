"""Sale

Revision ID: 7e0225e08e96
Revises: d8fe976af0bc
Create Date: 2021-06-01 16:59:51.160122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e0225e08e96'
down_revision = 'd8fe976af0bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_status', sa.String(length=50), nullable=True))
        batch_op.drop_column('product_sale_name')
        batch_op.drop_column('product_sale')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_sale', sa.VARCHAR(length=50), nullable=True))
        batch_op.add_column(sa.Column('product_sale_name', sa.VARCHAR(length=20), nullable=True))
        batch_op.drop_column('product_status')

    # ### end Alembic commands ###
