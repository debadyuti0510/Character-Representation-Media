const CracoEsbuildPlugin = require('craco-esbuild');
const CracoBabelLoader = require('craco-babel-loader');

module.exports = {
  plugins: [
    { plugin: CracoEsbuildPlugin,
   },
   { plugin: CracoBabelLoader, options: { babelLoaderOptions: { presets: ['@babel/preset-env'], }, }, },
  ],
};