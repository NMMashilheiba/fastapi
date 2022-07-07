"""add content column to posts table

Revision ID: bb961e093d7b
Revises: f4e10f4b0684
Create Date: 2022-07-07 17:51:29.938308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb961e093d7b'
down_revision = 'f4e10f4b0684'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
