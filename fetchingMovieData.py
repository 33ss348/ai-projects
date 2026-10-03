import {useState, useEffect, useRef, useCallback} from 'react';
import{omdbSearch, omdbDetails} from '../utils/api';
import{useApp} from '../context/AppContext';

export default function searchModel({ onClose }) {
  const {openMovie} = useApp();

  const[query, setQuery] = useState('');
  const[results, setResults] = useState([]);
  const[searching, setSearching] = useState(false);
  const[searched, setSearched] = useState(false);
  const[clickingId, setClickingId] = useState(false);

  const inputRef = useRef(null);
  const detailsCache = useRef({});

  useEffect(() => { setTimeout(() => { inputRef.current?.focus(); }, 80); }, []); }

  useEffect(() => {
    results.forEach(movie => {
      if (movie.imdbID && !detailsCache.current[movie.imdbID]) {
        detailsCache.current[movie.imdbID] = omdbDetails(movie.imdbID).catch(() => null);
      }
    });
  }, [results]);

  const handleSearch = useCallback(async (q=query) => {
    const term = q.trim();
    if (!term) return;
    setSearching(true); setSearched(false); setResults([]);
    try {
      setResults(await omdbSearch(term)).slice(0, 12);
    }