import { BrowserRouter, Routes, Route } from "react-router-dom";
import Task from "./pages/task";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Task/>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
