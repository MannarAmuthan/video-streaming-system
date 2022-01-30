import { createStore } from "redux";
import rootReducer from "./rootReducer";

function configureStore(state = { currentVideo:"-" }) {
  return createStore(rootReducer,state);
}
export default configureStore;