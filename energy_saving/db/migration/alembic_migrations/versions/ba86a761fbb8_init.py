"""init

Revision ID: ba86a761fbb8
Revises: 
Create Date: 2017-06-29 10:45:32.511453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba86a761fbb8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('datacenter',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=36), nullable=True),
    sa.Column('location', sa.JSON(), nullable=True),
    sa.Column('type', sa.Enum('production', 'lab'), server_default='production', nullable=True),
    sa.Column('properties', sa.JSON(), nullable=True),
    sa.Column('sensor_attributes_prediction_model', sa.String(length=36), nullable=True),
    sa.Column('controller_attributes_prediction_model', sa.String(length=36), nullable=True),
    sa.Column('pue_prediction_model', sa.String(length=36), nullable=True),
    sa.Column('best_controller_params_model', sa.String(length=36), nullable=True),
    sa.Column('decision_model', sa.String(length=36), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('controller',
    sa.Column('location', sa.JSON(), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('datacenter_id', sa.String(length=36), nullable=True),
    sa.Column('name', sa.String(length=36), nullable=True),
    sa.Column('properties', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['datacenter_id'], ['datacenter.id'], onupdate='RESTRICT', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('environment_sensor',
    sa.Column('location', sa.JSON(), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('datacenter_id', sa.String(length=36), nullable=True),
    sa.Column('name', sa.String(length=36), nullable=True),
    sa.Column('properties', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['datacenter_id'], ['datacenter.id'], onupdate='RESTRICT', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sensor',
    sa.Column('location', sa.JSON(), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('datacenter_id', sa.String(length=36), nullable=True),
    sa.Column('name', sa.String(length=36), nullable=True),
    sa.Column('properties', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['datacenter_id'], ['datacenter.id'], onupdate='RESTRICT', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('controller_attribute',
    sa.Column('type', sa.Enum('binary', 'continuous', 'integer', 'discrete'), server_default='continuous', nullable=True),
    sa.Column('unit', sa.String(length=36), nullable=True),
    sa.Column('mean', sa.Float(), nullable=True),
    sa.Column('deviation', sa.Float(), nullable=True),
    sa.Column('max', sa.Float(), nullable=True),
    sa.Column('min', sa.Float(), nullable=True),
    sa.Column('possible_values', sa.JSON(), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('controller_id', sa.String(length=36), nullable=True),
    sa.Column('name', sa.String(length=36), nullable=True),
    sa.ForeignKeyConstraint(['controller_id'], ['controller.id'], onupdate='RESTRICT', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('controller_parameter',
    sa.Column('type', sa.Enum('binary', 'continuous', 'integer', 'discrete'), server_default='continuous', nullable=True),
    sa.Column('unit', sa.String(length=36), nullable=True),
    sa.Column('max', sa.Float(), nullable=True),
    sa.Column('min', sa.Float(), nullable=True),
    sa.Column('possible_values', sa.JSON(), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('controller_id', sa.String(length=36), nullable=True),
    sa.Column('name', sa.String(length=36), nullable=True),
    sa.ForeignKeyConstraint(['controller_id'], ['controller.id'], onupdate='RESTRICT', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('environment_sensor_attribute',
    sa.Column('type', sa.Enum('binary', 'continuous', 'integer', 'discrete'), server_default='continuous', nullable=True),
    sa.Column('unit', sa.String(length=36), nullable=True),
    sa.Column('mean', sa.Float(), nullable=True),
    sa.Column('deviation', sa.Float(), nullable=True),
    sa.Column('max', sa.Float(), nullable=True),
    sa.Column('min', sa.Float(), nullable=True),
    sa.Column('possible_values', sa.JSON(), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('controller_id', sa.String(length=36), nullable=True),
    sa.Column('name', sa.String(length=36), nullable=True),
    sa.ForeignKeyConstraint(['controller_id'], ['environment_sensor.id'], onupdate='RESTRICT', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sensor_attribute',
    sa.Column('type', sa.Enum('binary', 'continuous', 'integer', 'discrete'), server_default='continuous', nullable=True),
    sa.Column('unit', sa.String(length=36), nullable=True),
    sa.Column('mean', sa.Float(), nullable=True),
    sa.Column('deviation', sa.Float(), nullable=True),
    sa.Column('max', sa.Float(), nullable=True),
    sa.Column('min', sa.Float(), nullable=True),
    sa.Column('possible_values', sa.JSON(), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('sensor_id', sa.String(length=36), nullable=True),
    sa.Column('name', sa.String(length=36), nullable=True),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensor.id'], onupdate='RESTRICT', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sensor_attribute')
    op.drop_table('environment_sensor_attribute')
    op.drop_table('controller_parameter')
    op.drop_table('controller_attribute')
    op.drop_table('sensor')
    op.drop_table('environment_sensor')
    op.drop_table('controller')
    op.drop_table('datacenter')
    # ### end Alembic commands ###
