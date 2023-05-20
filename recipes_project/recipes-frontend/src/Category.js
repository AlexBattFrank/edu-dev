import React from 'react';
import useDataApi from './useDataApi';

const Category = () => {
  const [{ data, isLoading }] = useDataApi('http://localhost:8000/api/categories');

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Categories</h2>
      {data.map(category => (
        <div key={category.id}>
          <h3>{category.name}</h3>
        </div>
      ))}
    </div>
  );
};

export default Category;
