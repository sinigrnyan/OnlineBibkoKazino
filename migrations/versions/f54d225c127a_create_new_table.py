"""create new table

Revision ID: f54d225c127a
Revises: 
Create Date: 2024-12-21 20:12:02.140726

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from website.models import User

revision: str = 'f54d225c127a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
new_table_name="Ochen vazhnaya tablica"

def upgrade() -> None:
    op.create_table(
        new_table_name,
        sa.Column("id",sa.Integer, primary_key=True),
        sa.Column("name", sa.String(150), primary_key=True)
    )


def downgrade() -> None:
    op.drop_table(new_table_name)
