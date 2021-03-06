"""empty message

Revision ID: 8bc8b265edaf
Revises: a7ab882e0a13
Create Date: 2017-02-28 14:28:46.964792

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8bc8b265edaf'
down_revision = 'a7ab882e0a13'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('idm_accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.Binary(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('idm_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('idm_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=200), nullable=False),
    sa.Column('last_accessed_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['idm_accounts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('idm-token')
    op.drop_table('idm-groups')
    op.drop_table('idm-accounts')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('idm-accounts',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"idm-accounts_id_seq"\'::regclass)'), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='idm-accounts_pkey'),
    sa.UniqueConstraint('email', name='idm-accounts_email_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('idm-groups',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"idm-groups_id_seq"\'::regclass)'), nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='idm-groups_pkey')
    )
    op.create_table('idm-token',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"idm-token_id_seq"\'::regclass)'), nullable=False),
    sa.Column('account_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('token', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('last_accessed_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['idm-accounts.id'], name='idm-token_account_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='idm-token_pkey')
    )
    op.drop_table('idm_token')
    op.drop_table('idm_groups')
    op.drop_table('idm_accounts')
    ### end Alembic commands ###
