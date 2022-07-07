"""add foreign_key to posts table

Revision ID: fe78a80f0f49
Revises: 886cc905282e
Create Date: 2022-07-07 18:18:01.447487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe78a80f0f49'
down_revision = '886cc905282e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fkey', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fkey', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
