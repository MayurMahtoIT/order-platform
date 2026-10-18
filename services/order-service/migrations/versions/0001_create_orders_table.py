"""create orders table

Revision ID: 0001
Revises:
Create Date: 2026-10-18
"""
from alembic import op
import sqlalchemy as sa

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "orders",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("customer_id", sa.String(64), nullable=False),
        sa.Column("product_id", sa.String(64), nullable=False),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("total_amount", sa.Float, nullable=False),
        sa.Column(
            "status",
            sa.Enum("PENDING", "CONFIRMED", "CANCELLED", name="orderstatus"),
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_orders_customer_id", "orders", ["customer_id"])


def downgrade() -> None:
    op.drop_index("ix_orders_customer_id", table_name="orders")
    op.drop_table("orders")
    # Postgres keeps enum types as separate objects; drop it too (no-op on SQLite).
    sa.Enum(name="orderstatus").drop(op.get_bind(), checkfirst=True)
