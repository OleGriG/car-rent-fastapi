"""initial migration

Revision ID: 6a6c4fd3c2e9
Revises: 6620d4cbc458
Create Date: 2024-06-25 02:12:23.483423

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a6c4fd3c2e9'
down_revision: Union[str, None] = '6620d4cbc458'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###