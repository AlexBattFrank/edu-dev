import React from 'react';
import useDataApi from './useDataApi';

const Recipes = () => {
  const [ { data, isLoading } ] = useDataApi('http://localhost:8000/api/recipes');

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Recipes</h2>
      {data.map(recipe => (
        <div key={recipe.id}>
          <h3>{recipe.name}</h3>
          <p>{recipe.description}</p>
        </div>
      ))}
    </div>
  );
};

export default Recipes;
