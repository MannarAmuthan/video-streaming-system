const reducerRoot = (state,action)=>{
  switch (action.type) {
    case "setVideo":
      return {
        ...state,
        currentVideo: action.payload
      };
    default:
      return state;
  }
};


export default reducerRoot;