const baseURL = ''; // TODO migrate from base_url (generated via Pelican)

const searchFilePaths = [
    "campaigns.json",
    "datasources.json",
    "groups.json",
    "matrices.json",
    "misc.json",
    "mitigations.json",
    "software.json",
    "tactics.json",
    "techniques.json"
]

const MessageType = {
    SEARCH: 'search',
    SEARCH_RESULTS: 'search-results',
    ERROR: 'error'
}

export {
    baseURL,
    searchFilePaths,
    MessageType
}
