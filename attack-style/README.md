# ATT&CK Style

ATT&CK Style is a JavaScript package that builds the CSS styles for the ATT&CK website.
The outputs are simply 2 CSS files:

* `dist/style-attack.css`
* `dist/style-user.css`

These files are then copied into `<ATT&CK-website-git-repo>/attack-theme/static/`.
Currently this is done manually - no automation.
But also, the CSS is not updated very often.

## Installation

To set up the ATT&CK Style package, follow these steps:

1. **Prerequisite: Ensure Node.js is Installed**:

   Make sure you have the latest Node.js LTS version installed.

2. **Navigate to the attack-style Sub-folder**:

   Clone the repository, then change your directory to the attack-style sub-folder.

    ```bash
    cd <repository-folder>/attack-style
    ```

3. **Install Dependencies**:

   Run the following command to install the necessary dependencies:

    ```bash
    npm install
    ```

## Build

1. **Build the CSS Files**:

   Use the following command to compile the SCSS files into CSS.
   The CSS output files will be generated in the `dist/` directory.

    ```bash
    npm run build
    ```

2. **Copy CSS Files**:

   Copy both `dist/style-attack.css` and `dist/style-user.css` to `<ATT&CK-website-git-repo>/attack-theme/static/`.

    ```bash
    npm run copy
    ```

The files are now ready to be used in the process to build the ATT&CK website!
