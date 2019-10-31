module.exports = {
  devServer: {
    proxy: {
      '^/v1': {
        target: 'http://localhost:5000',
        ws: true,
        changeOrigin: true
      }
    }
  },
  'transpileDependencies': [
    'vuetify'
  ]
}