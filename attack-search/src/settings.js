const baseURL = ''; // TODO migrate from base_url (generated via Pelican)
const searchCacheSchemaVersion = 2;

const searchFilePaths = [
  'campaigns.json',
  'assets.json',
  'datacomponents.json',
  'groups.json',
  'matrices.json',
  'misc.json',
  'mitigations.json',
  'resources.json',
  'software.json',
  'sub-techniques.json',
  'tactics.json',
  'techniques.json',
  'detectionstrategies.json',
  'analytics.json',
];
module.exports = {
  baseURL,
  searchCacheSchemaVersion,
  searchFilePaths,
};
