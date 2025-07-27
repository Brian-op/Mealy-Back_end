import logging
from logging.config import fileConfig

from flask import current_app
from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Setup loggers
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')


# Get the db instance from current_app
def get_db():
    return current_app.extensions['migrate'].db


def get_engine():
    try:
        # Works with Flask-SQLAlchemy <3.x
        return get_db().get_engine()
    except AttributeError:
        # Works with Flask-SQLAlchemy >=3.x
        return get_db().engine


def get_metadata():
    db = get_db()
    # Support for multiple binds (if used), otherwise just main metadata
    return db.metadatas.get(None, db.metadata) if hasattr(db, "metadatas") else db.metadata


def get_engine_url():
    try:
        return get_engine().url.render_as_string(hide_password=False).replace('%', '%%')
    except AttributeError:
        return str(get_engine().url).replace('%', '%%')


# Inject the DB URI into the Alembic config
config.set_main_option('sqlalchemy.url', get_engine_url())


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=get_metadata(),
        literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""

    # Avoid empty migration scripts
    def process_revision_directives(context, revision, directives):
        if getattr(config.cmd_opts, 'autogenerate', False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info('No changes in schema detected.')

    conf_args = current_app.extensions['migrate'].configure_args
    if conf_args.get("process_revision_directives") is None:
        conf_args["process_revision_directives"] = process_revision_directives

    connectable = get_engine()

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=get_metadata(),
            **conf_args
        )

        with context.begin_transaction():
            context.run_migrations()


# Determine mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
