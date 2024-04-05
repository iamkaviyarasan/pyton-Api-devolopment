"""add user table

Revision ID: eb82b43b497b
Revises: c8942fcb7510
Create Date: 2024-04-05 14:11:20.498838

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb82b43b497b'
down_revision: Union[str, None] = 'c8942fcb7510'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    
    # ### end Alembic commands ###
    # ### end Alembic commands ###
    
    pass


def downgrade() -> None:
    op.drop_table('users')
    # ### end Alembic commands ###
    # ### end Alembic commands ###
    pass
