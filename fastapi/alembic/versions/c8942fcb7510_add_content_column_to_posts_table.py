"""add content column to posts table

Revision ID: c8942fcb7510
Revises: b5db5a047a92
Create Date: 2024-04-05 12:49:35.523653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8942fcb7510'
down_revision: Union[str, None] = 'b5db5a047a92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False ))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
