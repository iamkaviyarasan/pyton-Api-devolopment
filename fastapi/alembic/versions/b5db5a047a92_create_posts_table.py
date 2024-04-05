"""create posts table

Revision ID: b5db5a047a92
Revises: 
Create Date: 2024-04-05 11:34:26.807064

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5db5a047a92'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    # op.drop_table('users')
    # op.drop_table('votes')
    # op.drop_table('posts')
    # op.drop_table('posts')
    # op.drop_table('posts')
    pass
