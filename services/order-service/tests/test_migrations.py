from alembic import command
from alembic.autogenerate import compare_metadata
from alembic.config import Config
from alembic.migration import MigrationContext
from sqlalchemy import create_engine, inspect

from app.database import Base


def _cfg(url: str) -> Config:
    cfg = Config("alembic.ini")
    cfg.set_main_option("sqlalchemy.url", url)
    return cfg


def test_upgrade_and_downgrade(tmp_path):
    url = f"sqlite:///{tmp_path}/m.db"
    cfg = _cfg(url)
    command.upgrade(cfg, "head")
    assert "orders" in inspect(create_engine(url)).get_table_names()
    command.downgrade(cfg, "base")
    assert "orders" not in inspect(create_engine(url)).get_table_names()


def test_models_match_migrations(tmp_path):
    """Fails if someone edits models.py but forgets to write a migration."""
    url = f"sqlite:///{tmp_path}/m.db"
    command.upgrade(_cfg(url), "head")
    with create_engine(url).connect() as conn:
        diff = compare_metadata(MigrationContext.configure(conn), Base.metadata)
    assert diff == []
