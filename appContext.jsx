import { createContext, useContext, useState , useCallback , UseRef, useEffect } from "react";
import { STAGE,AGE } from '../constants';

const AppContext = createContext(null);
 export function AppProvider({ children }) {
  
    const[theme, setTheme] = useState('light');