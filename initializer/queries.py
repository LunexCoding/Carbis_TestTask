from database.tables import DatabaseTables


class SqlQueries:
    createTableSettings = f"""
        CREATE TABLE IF NOT EXISTS {DatabaseTables.SETTINGS} (
            `ServiceURL` VARCHAR(255),
            `API` VARCHAR(255),
            `Language` VARCHAR(2) NOT NULL CHECK (Language IN ('ru', 'en')),
            `HelpStringVisibility` BOOLEAN NOT NULL CHECK (HelpStringVisibility IN (0, 1))
        );
    """
