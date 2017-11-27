const realtime = {
  state: {
    socket: {
      isConnected: false,
      message: ''
    }
  },
  mutations: {
    SOCKET_ONOPEN (state, event) {
      state.socket.isConnected = true
    },
    SOCKET_ONCLOSE (state, event) {
      state.socket.isConnected = false
    },
    SOCKET_ONERROR (state, event) {
      console.error(state, event)
    },
    // default handler called for all methods
    SOCKET_ONMESSAGE (state, message) {
      console.log(message)
      state.message = message
    }
  }
}

export default realtime
