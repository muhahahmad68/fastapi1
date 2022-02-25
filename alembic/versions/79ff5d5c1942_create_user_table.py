"""create user table

Revision ID: 79ff5d5c1942
Revises: 74e03cc9e616
Create Date: 2022-02-23 15:26:27.246767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79ff5d5c1942'
down_revision = '74e03cc9e616'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                     sa.Column('id', sa.Integer(), nullable=False),
                     sa.Column('email', sa.String(), nullable=False),
                     sa.Column('password', sa.String(), nullable=False),
                     sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                     server_default=sa.text('now()'), nullable=False),
                     sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email')
                     )


def downgrade():
    op.drop_table("users")