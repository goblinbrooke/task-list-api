"""empty message

Revision ID: 36001725f420
Revises: 80e834b1f896
Create Date: 2021-11-02 10:28:13.930129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36001725f420'
down_revision = '80e834b1f896'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(length=200), nullable=False))
    op.drop_column('goal', 'goal_title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('goal_title', sa.VARCHAR(length=200), autoincrement=False, nullable=False))
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###
