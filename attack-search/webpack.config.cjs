const path = require('path');
const TerserPlugin = require('terser-webpack-plugin');

module.exports = (env, argv) => {
    const isProduction = argv.mode === 'production';

    return {
        entry: {
            'search_bundle': './src/index.js',
            'search_bundle.worker': './src/attack-index.js'
        },
        output: {
            path: path.resolve(__dirname, 'dist'),
            filename: '[name].js'
        },
        mode: isProduction ? 'production' : 'development',
        target: 'web',
        module: {
            rules: [
                {
                    test: /\.js$/,
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
        optimization: isProduction
            ? {
                minimize: true,
                minimizer: [
                    new TerserPlugin({
                        terserOptions: {
                            compress: {
                                drop_console: true, // This option removes console statements
                            },
                        },
                    }),
                ],
            }
            : {},
    };
};
