function isMissingSearchIndexError(error) {
  return error?.status === 404 || error?.status === 0;
}

async function loadSearchDocuments(baseUrl, searchFilePaths, getJSON) {
  const settled = await Promise.all(searchFilePaths.map(async (filename) => {
    const url = `${baseUrl}${filename}`;

    try {
      return {
        documents: await getJSON(url),
        filename,
        loaded: true,
      };
    } catch (error) {
      if (isMissingSearchIndexError(error)) {
        console.debug(`Skipping missing search index file: ${filename}`);
        return { documents: [], filename, loaded: false };
      }
      throw error;
    }
  }));

  const loadedFiles = settled.filter((result) => result.loaded);
  if (loadedFiles.length === 0) {
    throw new Error('No search index files loaded.');
  }

  return loadedFiles.reduce((acc, result) => acc.concat(result.documents), []);
}

module.exports = {
  loadSearchDocuments,
};
