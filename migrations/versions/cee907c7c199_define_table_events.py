"""define table events

Revision ID: cee907c7c199
Revises: 
Create Date: 2023-01-17 15:42:02.296717

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'cee907c7c199'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), server_default=sa.text('1'), nullable=False),
    sa.Column('sensor_type', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('temperature', sa.Float(), nullable=True),
    sa.Column('humidity', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_events_id'), 'events', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_events_id'), table_name='events')
    op.drop_table('events')
    # ### end Alembic commands ###