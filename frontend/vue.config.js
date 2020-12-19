module.exports = {
  'outputDir': './dist',
  'assetsDir': 'static',
  'devServer': {
    'proxy': {
      '/api*': {
        'target': 'http://api:5000/'
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
