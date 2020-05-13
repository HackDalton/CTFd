"""hackdalton: add fname, lname to users

Revision ID: d0dee6e2957a
Revises: 1093835a1051
Create Date: 2020-05-12 21:37:35.049896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0dee6e2957a'
down_revision = '1093835a1051'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('fname', sa.String(length=128), nullable=True))
    op.add_column('users', sa.Column('lname', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'lname')
    op.drop_column('users', 'fname')
    # ### end Alembic commands ###
