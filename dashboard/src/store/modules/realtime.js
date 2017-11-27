const realtime = {
  state: {
    messages: []
  },
  mutations: {
    addMessage (state, message) {
      state.messages.push(message)
    }
  }

}

export default realtime
