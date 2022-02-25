"""Create Post table

Revision ID: 96183462c285
Revises: 
Create Date: 2022-02-23 13:58:36.006942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96183462c285'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
    sa.Column("title", sa.String(), nullable=False))


def downgrade():
    op.drop_table("posts")
