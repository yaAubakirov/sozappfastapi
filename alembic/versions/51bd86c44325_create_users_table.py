"""create users table

Revision ID: 51bd86c44325
Revises: 42b8c51f4b77
Create Date: 2022-07-17 11:30:52.160181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51bd86c44325'
down_revision = '42b8c51f4b77'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('identification', sa.String(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('identification')
        )
    pass

def downgrade() -> None:
    op.drop_table('users')
    pass
