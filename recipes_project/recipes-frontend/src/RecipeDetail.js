import React from 'react';
import { useParams } from 'react-router-dom';
import useDataApi from './useDataApi';

const RecipeDetail = () => {
  const { id } = useParams();
  const [ { data, isLoading } ] = useDataApi(`http://localhost:8000/api/recipes/${id}`);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>{data.name}</h2>
      <p>{data.description}</p>
    </div>
  );
};

export default RecipeDetail;
