module.exports = {
  'outputDir': './dist',
  'assetsDir': 'static',
  'devServer': {
    'proxy': {
      '/api*': {
        'target': 'http://localhost:5000/'
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
