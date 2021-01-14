module.exports = {
  'outputDir': './dist',
  'assetsDir': 'static',
  'devServer': {
    'proxy': {
      '/api*': {
        'target': `${process.env.API_PROXY_TARGET}`
      }
    }
  },
  'css': {
    'loaderOptions': {
      'sass': {
        'sassOptions': {

        }
      }
    }
  },
  'transpileDependencies': [
    'vuetify'
  ]
}
