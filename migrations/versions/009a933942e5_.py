"""empty message

Revision ID: 009a933942e5
Revises: 0083d2491118
Create Date: 2024-04-15 21:45:29.895068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '009a933942e5'
down_revision = '0083d2491118'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Transactions', schema=None) as batch_op:
        batch_op.alter_column('WinCount',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('LossCount',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('PeakGlobal', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.drop_column('PeakGlobal')

    with op.batch_alter_table('Transactions', schema=None) as batch_op:
        batch_op.alter_column('LossCount',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('WinCount',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
