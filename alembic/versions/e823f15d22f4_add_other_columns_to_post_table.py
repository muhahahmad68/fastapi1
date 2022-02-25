"""add other columns to post table:

Revision ID: e823f15d22f4
Revises: d4b91e7545b9
Create Date: 2022-02-23 16:13:41.168892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e823f15d22f4'
down_revision = 'd4b91e7545b9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",
                sa.Column("published", sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column("posts",
                sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text('now()'))
                )


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
