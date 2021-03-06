"""add proto type settings for dial vpn.

Revision ID: 45c7c3141a21
Revises: 313c830f061c
Create Date: 2014-10-10 10:22:23.395475

"""

# revision identifiers, used by Alembic.
revision = '45c7c3141a21'
down_revision = '313c830f061c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dial_settings', sa.Column('proto', sa.String(length=80), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dial_settings', 'proto')
    ### end Alembic commands ###
