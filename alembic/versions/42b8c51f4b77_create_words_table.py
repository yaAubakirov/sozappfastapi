"""create words table

Revision ID: 42b8c51f4b77
Revises: 
Create Date: 2022-07-17 11:06:45.721435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42b8c51f4b77'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'words', 
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
        sa.Column('kazakh', sa.String(), nullable=False), 
        sa.Column('russian', sa.String(), nullable=False)
        )
    pass


def downgrade() -> None:
    op.drop_table('words')
    pass
