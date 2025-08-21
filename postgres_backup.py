import os
import datetime
import subprocess
from loguru import logger
from pathlib import Path


def backup_postgres_table(
        host: str,
        port: int,
        database: str,
        username: str,
        password: str,
        table_name: str,
        schema_name: str,
        backup_directory: str,
        pg_dump_path: str = None
):
    """
    Backup a PostgreSQL table using pg_dump.

    Args:
        host (str): PostgreSQL host.
        port (int): PostgreSQL port.
        database (str): Database name.
        username (str): Database user.
        password (str): Database password.
        table_name (str): Table to back up.
        schema_name (str): Schema of the table.
        backup_directory (str): Directory to store backup.
        pg_dump_path (str, optional): Path to pg_dump executable. Defaults to system PATH.

    Returns:
        str: Full path to back up file if successful, None otherwise.
    """
    backup_directory = Path(backup_directory)
    if not backup_directory.exists():
        logger.error(f"Backup directory does not exist: {backup_directory}")
        return None

    # Default pg_dump path
    if pg_dump_path is None:
        pg_dump_path = "pg_dump"  # assumes pg_dump is in PATH

    if not Path(pg_dump_path).exists() and pg_dump_path != "pg_dump":
        logger.error(f"pg_dump executable not found at: {pg_dump_path}")
        return None

    # Set the environment variable for password securely
    env = os.environ.copy()
    env["PGPASSWORD"] = password

    # Create backup file with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = backup_directory / f"{table_name}_backup_{timestamp}.sql"

    # Build pg_dump command
    pg_dump_cmd = [
        pg_dump_path,
        "-h", host,
        "-p", str(port),
        "-U", username,
        "-d", database,
        "-t", f"{schema_name}.{table_name}",
        "--inserts",
        "--file", str(backup_file)
    ]

    logger.info(f"Starting backup for table {schema_name}.{table_name}...")

    try:
        subprocess.run(pg_dump_cmd, env=env, check=True, capture_output=True, text=True)
        logger.info(f"Backup completed successfully: {backup_file}")
        return str(backup_file)

    except subprocess.CalledProcessError as e:
        logger.error("Backup failed with error:")
        logger.error(e.stderr)
        return None

    except Exception as e:
        logger.exception(f"Unexpected error during backup: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    host_name = "localhost"
    port_number = 5432
    database_name = "cisco_ingestion_pipeline"
    username_data = "postgres"
    password_data = "postgres"
    table_name_data = "course_embeddings"
    schema_name_data = "model_embeddings_old"
    backup_directory_path = r"C:\Users\Supreeth\Downloads"

    result = backup_postgres_table(
        host=host_name,
        port=port_number,
        database=database_name,
        username=username_data,
        password=password_data,
        table_name=table_name_data,
        schema_name=schema_name_data,
        backup_directory=backup_directory_path,
        pg_dump_path=r"C:\Program Files\PostgreSQL\15\bin\pg_dump.exe"  # optional
    )

    if result:
        logger.info(f"Backup file ready at: {result}")
    else:
        logger.error("Backup process failed.")
