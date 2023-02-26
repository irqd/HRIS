"""empty message

Revision ID: e9704c62a653
Revises: 80a647648311
Create Date: 2023-02-26 19:32:04.006088

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e9704c62a653'
down_revision = '80a647648311'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('departments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('manager', sa.String(length=50), nullable=True))
        batch_op.drop_column('supervisor')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('departments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('supervisor', mysql.VARCHAR(length=50), nullable=True))
        batch_op.drop_column('manager')

    # ### end Alembic commands ###