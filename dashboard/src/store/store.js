import Vue from 'vue'
import Vuex from 'vuex'
import realtime from './modules/realtime'

Vue.use(Vuex)

const Store = new Vuex.Store({
  modules: {
    realtime
  }
})

export default Store
