const realtime = {
  state: {
    messages: [],
    sockets: {}
  },
  mutations: {
    SOCKET_ONOPEN (state, event) {
      console.log(event)
      state.sockets[event.currentTarget.url] = state.sockets[event.currentTarget.url] || {}
      state.sockets[event.currentTarget.url].isConnected = true
    },
    SOCKET_ONCLOSE (state, event) {
      state.sockets[event.currentTarget.url] = state.sockets[event.currentTarget.url] || {}
      state.sockets[event.currentTarget.url].isConnected = false
    },
    SOCKET_ONERROR (state, event) {
      console.error(state, event)
    },
    SOCKET_ONMESSAGE (state, message) {
      console.log(message.data)
      console.log(JSON.parse(message.data))
      JSON.parse(message.data).forEach(msg => {
        state.messages.push(JSON.parse(msg.message))
      })
    }
  }

}

export default realtime
