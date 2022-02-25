"""add forign key relationship to posts table

Revision ID: d4b91e7545b9
Revises: 79ff5d5c1942
Create Date: 2022-02-23 15:53:05.371789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4b91e7545b9'
down_revision = '79ff5d5c1942'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fkey", source_table="posts", referent_table="users", 
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('post_users_fkey', table_name='posts')
    op.drop_column("posts", 'owner_id')
