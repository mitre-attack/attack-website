import { IndexedDbWrapper } from './indexed-db-wrapper.cjs';

class DatabaseManager {
    constructor(buildId) {
        if (!DatabaseManager.instance) {
            this.dbName = buildId ? `AttackWebsite-${buildId}` : 'AttackWebsite';

            /**
             * The following schemas will initialize three IndexedDB tables. Each schema corresponds to one
             * table. The TableWrapper class obfuscates the CRUD logic for interfacing with IndexedDB tables.
             *
             * 1. content_table: handles all objects loaded from index.json
             *
             * 2. flexsearch_table: handles the FlexSearch document instance (so we don't have to re-index index.json every time
             *    FlexSearch is cleared from browser memory!).
             *
             * 3. uuids: stores the build_uuid to distinguish the current running application (e.g., ATT&CK Website +
             *    ATT&CK v13) from a version of the application that was previously loaded (e.g., ATT&CK Website +
             *    ATT&CK v12).
             */
            this.schemas = {
                content_table: '&id, title, path, content',
                searchindex_table: '++id, title, content',
                uuids: 'build_uuid',
            };

            /**
             * A quick note on the schemas passed in the above 👆 IndexedDBWrapper initializations:
             *
             * The &id syntax means that the id field is the primary key of the table, but it will not be auto-incremented.
             * In this case, you must provide a unique value for the id field when inserting a new record, and the
             * IndexedDB will enforce uniqueness on the id field.
             *
             * The ++id syntax means that the id field is the primary key of the table and it will be auto-incremented. In
             * other words, when you insert a new record without providing a value for the id field, the IndexedDB will
             * automatically assign a unique, incremental value to the id field.
             */

            // Initialize the database
            this.db = new IndexedDbWrapper(this.dbName, this.schemas);

            // Create references to the tables
            this.contentDb = this.db.getTableWrapper('content_table');
            this.searchIndexDb = this.db.getTableWrapper('searchindex_table');
            this.uuidDb = this.db.getTableWrapper('uuids');

            // Make the class a singleton
            DatabaseManager.instance = this;
        }

        return DatabaseManager.instance;
    }
}

// Initialize the DatabaseManager and lock it down
const databaseManager = new DatabaseManager();
Object.freeze(databaseManager);

export default databaseManager;
