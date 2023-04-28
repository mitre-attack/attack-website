const path = require('path');
const TerserPlugin = require('terser-webpack-plugin');
const { InjectManifest } = require('workbox-webpack-plugin');

module.exports = (env, argv) => {
    const isProduction = argv.mode === 'production';

    return {
        entry: {
            'search_bundle': './src/index.mjs',
            'search_bundle.worker': './src/search-service.worker.mjs'
        },
        output: {
            path: path.resolve(__dirname, 'dist'),
            filename: '[name].js',
            publicPath: '/',
        },
        plugins: [
            new InjectManifest({
                swSrc: './src/search-service.worker.mjs',
                swDest: 'search_bundle.worker.js',
            }),
        ],
        mode: isProduction ? 'production' : 'development',
        target: 'web',
        module: {
            rules: [
                {
                    test: /\.m?js$/,
                    use: {
                        loader: 'babel-loader',
                        options: {
                            presets: ['@babel/preset-env'],
                            comments: false
                        }
                    },
                    type: 'javascript/auto',
                },
                {
                    test: /\.cjs$/,
                    type: 'javascript/auto',
                },
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
