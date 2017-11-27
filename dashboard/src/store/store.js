import Vue from 'vue'
import Vuex from 'vuex'
import realtime from './modules/realtime'
import socket from './modules/socket'

Vue.use(Vuex)

const Store = new Vuex.Store({
  modules: {
    realtime,
    socket
  }
})

export default Store
