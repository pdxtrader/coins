// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from './App'
import router from './router'
import store from './store/store'
import VueNativeSock from 'vue-native-websocket'

Vue.use(BootstrapVue)
Vue.use(
  VueNativeSock,
  'ws://localhost:9999/?topic=press&consumerGroup=dashboard&offset=0',
  {
    store: store,
    reconnection: true,
    reconnectionAttempts: 5,
    reconnectionDelay: 3000
  }
)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: {
    App
  }
})
