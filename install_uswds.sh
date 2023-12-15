#!/bin/bash

CUSTOM_ATTR=(
    '$theme-checkbox-border-radius: "md",'
    '$theme-button-font-family: "body",'
    '$theme-link-color: "red-warm"',
    ''
)

# setup styles.scss
create_styles () {
cat << EOF > styles.scss
// 1. Load your project's USWDS settings configuration
@forward "uswds-theme.scss";
// 2. Load USWDS source code
@forward "./node_modules/@uswds/uswds/packages/uswds/_index.scss";

@use "uswds-core" with (
    \$theme-button-border-radius : "0px",
    \$theme-button-stroke-width : "42424242px",
    \$theme-show-notifications: false
)

EOF
}

get_npm (){
    # install uswds 
    npm install @uswds/uswds --save-exact
    # install compiler
    npm install @uswds/compile --save-dev
}

create_gulpfile (){
# setup styles.scss
cat << EOF > gulpfile.js
/* gulpfile.js */

/**
* Import uswds-compile
*/
const uswds = require("@uswds/compile");

/**
* USWDS version
* Set the major version of USWDS you're using
* (Current options are the numbers 2 or 3)
*/
uswds.settings.version = 3;

/**
* Path settings
* Set as many as you need
*/
uswds.paths.dist.css = './assets/css';
uswds.paths.dist.theme = './sass/uswds';

/**
* Exports
* Add as many as you need
*/
exports.init = uswds.init;
exports.compile = uswds.compile;
exports.watch = uswds.watch;
exports.css = uswds.copyTheme;
EOF
}

customize() {
    THE_PATH="sass/uswds/_uswds-theme.scss"

    npx gulp init

    echo "@use \"uswds-core\" with (" | tee -a $THE_PATH

    for line in "${CUSTOM_ATTR[@]}"
    do 
        printf "\t$line\n" | tee -a $THE_PATH;
    done 
    echo ");" | tee -a $THE_PATH;
}

execute() {
    npx gulp compile
    ls assets/css/
    yes | cp -rf assets/css/styles.css ../attack-theme/static/style/uswds.scss
}


main(){
    # create and move
    mkdir -p uswds
    pushd uswds
    # create resources
    npm init -y
    # execute functions
    get_npm
    create_gulpfile
    create_styles
    # generate css and move it to necessary place
    customize
    execute
    popd
    # I `rm -rf` the directory because the NPM dir is gross
    # rm -rf uswds

    # TODO 
    # TO GET THIS TO WORK WITH THE update-attack.py 
    # style.scss NEEDS TO BE UPDATED TO INCLUDE uswds.scss
    # Should look like
    # `@import "_colors.scss", "_matrix.scss", "_misc.scss", "_nav.scss", "_footer.scss", "_fonts.scss", "_layouts.scss", "_search.scss", "_versioning.scss", "_tour.scss", "uswds.scss";`
}

main
