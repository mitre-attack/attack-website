const AttackIndex = require('./attack-index.js');

const attackIndex = new AttackIndex();

console.debug(`Initialized new AttackIndex.`);

/**
 * The event listener for the web worker that processes messages received from the main thread.
 * Based on the received command, it calls the appropriate methods of the AttackIndex class and
 * sends the results or errors back to the main thread using postMessage.
 *
 * @listens MessageEvent
 * @param {MessageEvent} event - The event object containing the message data.
 */
self.onmessage = async (event) => {
    const { command, ...args } = event.data;

    try {
        switch (command) {
            case 'search':
                /**
                 * Searches the AttackIndex instance and sends the results back to the main thread.
                 */
                const results = await attackIndex.search(args.query, args.fields, args.limit, args.offset);
                self.postMessage({ success: true, results });
                break;

            case 'add':
                /**
                 * Adds a single data object to the AttackIndex instance and sends a success message to the main thread.
                 */
                await attackIndex.add(args.document);
                self.postMessage({ success: true });
                break;

            case 'addBulk':
                /**
                 * Adds an array of data objects to the AttackIndex instance in bulk and sends a success message to the main thread.
                 */
                attackIndex.addBulk(args.documents);
                self.postMessage({ success: true });
                break;

            case 'import':
                /**
                 * Imports serialized data into the AttackIndex instance and sends a success message to the main thread.
                 */
                await attackIndex.import(args.key, args.data);
                self.postMessage({ success: true });
                break;

            default:
                throw new Error(`Unknown command "${command}"`);
        }
    } catch (error) {
        self.postMessage({ success: false, error: error.message });
    }
};
