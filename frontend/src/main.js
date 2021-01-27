import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import infiniteScroll from 'vue-infinite-scroll'

import './filters'
import vuetify from './plugins/vuetify'
import InstantSearch from 'vue-instantsearch'

Vue.config.productionTip = false

Vue.use(infiniteScroll)
Vue.use(InstantSearch)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
