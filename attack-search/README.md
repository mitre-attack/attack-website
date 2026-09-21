# ATT&CK Search

This project builds the browser search code. The Python search module generates
search JSON separately from the rendered website pages.

Use Node.js 26 to match Docker. From this directory:

```sh
npm ci
npm run build-copy
```

`npm run build` creates `dist/search_bundle.js`, and `npm run copy` copies it to
`../attack-theme/static/scripts/search_bundle.js`. The copy command creates the
destination directory if needed. It does not update `output/` or existing version
snapshots. `build-copy` runs both commands in order. Use production builds for
committed theme assets. Use `npm run build:dev` for local debugging.

Git ignores all `dist/` output and `compilation-stats.json`. After changing anything
in `attack-search/`, commit the production bundle in the theme. GitHub Pages uses
the committed bundle without rebuilding it or comparing it with the source.

The repository build interface uses [Just](../docs/DEVELOPMENT.md). Run
`just build-search` to compile and stage this package. To rebuild both asset sets
and generate the branded website with current-version snapshots, run
`just build-full-website --attack-brand --all-extras`.

The generated theme `settings.js` is ignored. The developer guide describes its
dataset- and deployment-specific contents.
