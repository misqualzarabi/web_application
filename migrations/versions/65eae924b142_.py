"""empty message

Revision ID: 65eae924b142
Revises: 
Create Date: 2020-06-07 20:47:30.452799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65eae924b142'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweet',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('tweet', sa.String(length=128), nullable=True),
    sa.Column('user_name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweet')
    # ### end Alembic commands ###