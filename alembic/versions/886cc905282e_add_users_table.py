"""add users table

Revision ID: 886cc905282e
Revises: bb961e093d7b
Create Date: 2022-07-07 17:56:56.971069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '886cc905282e'
down_revision = 'bb961e093d7b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
