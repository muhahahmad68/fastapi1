"""create a content column in post table

Revision ID: 74e03cc9e616
Revises: 96183462c285
Create Date: 2022-02-23 15:03:50.168586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74e03cc9e616'
down_revision = '96183462c285'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column("content", sa.String(), nullable= False))


def downgrade():
    op.drop_column("posts", "content")
