const path = require('path');

module.exports = {
    entry: './src/search.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'search_bundle.js'
    },
    mode: 'production',
    target: 'web',
    module: {
        rules: [
            {
                test: /\.js$/,
                // exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                        comments: false
                    }
                }
            }
        ]
    },
};
