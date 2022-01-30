import './App.css';
import { Provider } from "react-redux";
import VideoApp from './components/VideoApp';
import configureStore from './redux/store';

function App() {
  return (
    <div className="App">
      <Provider store={configureStore()}>
      <VideoApp></VideoApp>
      </Provider>
    </div>
  );
}

export default App;
