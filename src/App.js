import logo from './logo.svg';
import './App.css';
import { Routes, Route } from 'react-router-dom'
import Main from './page/Main';
import TopNav from './genenrel/TopNav';

function App() {
  return (
    <div className="flex flex-col">
      <TopNav />
      <Routes>
        <Route path='/' element={<Main />} />
      </Routes> 
      
    </div>
  );
}

export default App;
