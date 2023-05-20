import { useState, useEffect } from 'react';
import api from './api';

const useDataApi = (initialUrl) => {
  const [data, setData] = useState([]);
  const [url, setUrl] = useState(initialUrl);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await api.get(url);
        setData(result.data);
      } catch (error) {
        console.log('Error loading data', error);
      }
      setIsLoading(false);
    };

    fetchData();
  }, [url]);

  return [{ data, isLoading }, setUrl];
};

export default useDataApi;
