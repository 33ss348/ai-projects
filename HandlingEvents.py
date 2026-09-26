import{useState, useEffect, useRef} from 'react';
import{UseApp} from '../context/AppContext';
import{parseAIText} from '../utils/parseAIText';
import{STAGE, AGE, CATEGORIES_BY_AGE, MOODS_BY_AGE, LANGUAGES} from 'Constants';
  function TypingDots(){
    return(
      <div className="chat-row bot-row">
        <div className="bot-avatar"><i className="bi bi-stars"></i></div>
      </div>
        <div className="bubble bot-bubble">
        <div className="typing-dots"><span></span><span></span><span></span></div>
    );
  }
function SpecialContent({content}){
  const {addMsg,SwitchAge} = UseApp();
  const{cats, setCats} = useState([]);
  const{langs, setLangs} = useState(['Any language']);
  const{type}= context;

  if(type === 'mood-greeting')return({