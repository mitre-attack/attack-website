# ATT&CK Style

ATT&CK Style is a JavaScript package that builds the CSS styles for the ATT&CK website.
The outputs are 3 CSS files:

* `dist/style-attack.css`
* `dist/style-user.css`
* `dist/style-archive.css` (preserved-site appearance compatibility)

These files are then copied into `<ATT&CK-website-git-repo>/attack-theme/static/`.
Use `npm run build-copy` to compile and copy all three files, or use the repository's
[build commands](../docs/DEVELOPMENT.md#commands-and-generator-options) to build the complete website.
Intermediate `dist/` outputs are ignored; the three compiled CSS files in the theme
must be regenerated and committed after changing anything in `attack-style/`, just
like the compiled ATT&CK Search bundle after changes to `attack-search/`. GitHub Pages
uses the committed assets without rebuilding or comparing them against source.
The repository build interface requires [Just](../docs/DEVELOPMENT.md); use
`just build-style` to compile and stage this package or `just build-assets` for both.

## Installation

To set up the ATT&CK Style package, follow these steps:

1. **Prerequisite: Ensure Node.js is Installed**:

   Use Node.js 26 to match Docker.

2. **Navigate to the attack-style Sub-folder**:

   Clone the repository, then change your directory to the attack-style sub-folder.

    ```bash
    cd <repository-folder>/attack-style
    ```

3. **Install Dependencies**:

   Run the following command to install the necessary dependencies:

    ```bash
    npm ci
    ```

## Build

1. **Build the CSS Files**:

   Use the following command to compile the SCSS files into CSS.
   The CSS output files will be generated in the `dist/` directory.

    ```bash
    npm run build
    ```

2. **Copy CSS Files**:

   Copy `dist/style-attack.css`, `dist/style-user.css`, and `dist/style-archive.css` to `<ATT&CK-website-git-repo>/attack-theme/static/`.

    ```bash
    npm run copy
    ```

The files are now ready to be used in the process to build the ATT&CK website!

## Documentation

Style documentation is maintained as Markdown files next to the SCSS source.
Use these files as the source of truth for how each style folder is organized:

* `abstracts/README.md`
* `base/README.md`
* `layout/README.md`
* `components/README.md`
* `themes/README.md`

When adding or changing SCSS behavior, update the nearest Markdown file in the same folder.
These docs are committed source files, not generated output.
