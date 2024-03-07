import React, { useEffect, useState } from 'react';
// import CardRecognition from './components/CardRecognition';
import logo from './jackoscope.png';
import './App.css';

function App() {
const [detectedCards, setDetectedCards] = useState([])
  useEffect(() => {
    fetch("/api/detect").then(res => res.json()).then(setDetectedCards)
  
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo"/>
        <h1>
          JackOscope
        </h1>
        { detectedCards.map(card => {
          return <div style={{ display: 'flex',flexDirection: 'row' }}>
            {/* <span>{ card.rank}</span>
            <span>{ card.suit}</span> */}
            <img src={`Card_Imgs/${card.rank}.jpg`} style={{ marginRight: '10px' }}/>
            <img src={`Card_Imgs/${card.suit}.jpg`}/>
          </div>
        }) }
      </header>
    </div>
  );


}

export default App;