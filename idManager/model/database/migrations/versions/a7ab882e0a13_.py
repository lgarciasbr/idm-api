"""empty message

Revision ID: a7ab882e0a13
Revises: c27878227c6a
Create Date: 2017-02-28 13:40:31.200916

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a7ab882e0a13'
down_revision = 'c27878227c6a'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('idm-accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.Binary(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('idm-groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('idm-token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=200), nullable=False),
    sa.Column('last_accessed_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['idm-accounts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('group')
    op.drop_table('token')
    op.drop_table('account')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('account_id_seq'::regclass)"), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='account_pkey'),
    sa.UniqueConstraint('email', name='account_email_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('token',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('account_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('token', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('last_accessed_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], name='token_account_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='token_pkey')
    )
    op.create_table('group',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='group_pkey')
    )
    op.drop_table('idm-token')
    op.drop_table('idm-groups')
    op.drop_table('idm-accounts')
    ### end Alembic commands ###
