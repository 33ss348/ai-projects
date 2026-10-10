async function handleSend(){
    const msg= inputVal.trim();
    if(!msg|| isBotTyping) return;
    setInputVal('');
    if (stage ===   STAGE.NAME) { handleNameSubmit(msg); return; }
    if (stage !== STAGE.CHAT) return;
    if((isRestricted(msg) {addMsg('bot','Please ask me about movies only.'); }
        addMsg('user', msg); setInputActive(false);
        setIsBotTyping(true); 
            try{
                const {reply}= await callAIWith Search(msg);
                addMsg('bot', reply||'Sorry, I could not find an answer to that. Please try again.');
            } catch{addMsg('bot', 'Sorry, I could not find an answer to that. Please try again.');}
        ))
}
        finally{setIsBotTyping(false); setInputActive(true);}


const CHIPS={
        'Hiden Games': 'What are some underrated gen movies?',
        'Latest movies': 'Recomend great movies from the last 2 years.',
        'Something Different': ''
}