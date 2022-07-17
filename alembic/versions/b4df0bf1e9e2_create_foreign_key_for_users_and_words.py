"""create foreign key for users and words

Revision ID: b4df0bf1e9e2
Revises: 51bd86c44325
Create Date: 2022-07-17 11:40:48.027704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4df0bf1e9e2'
down_revision = '51bd86c44325'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('words', sa.Column('who_added', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'words_users_fk',
        source_table="words",
        referent_table="users",
        local_cols=['who_added'],
        remote_cols=['id'],
        ondelete="CASCADE"
        )
    pass


def downgrade() -> None:
    op.drop_constraint('words_users_fk', table_name="words")
    op.drop_column('words', 'who_added')
    pass
