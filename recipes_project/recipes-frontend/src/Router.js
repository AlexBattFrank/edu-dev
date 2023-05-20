import React from 'react';
import {Routes, Route, BrowserRouter, Link} from "react-router-dom";
import Category from './Category';
import Recipes from './Recipe';
import RecipeDetail from './RecipeDetail';

const TestComponent = () => <div>Test</div>;

const HomePage = () => (
  <div>
    <h1>Welcome to our cooking site!</h1>
    <Link to="/category/" style={{ display: 'block', marginBottom: '10px' }}>Categories</Link>
    <Link to="/recipes" style={{ display: 'block', marginBottom: '10px' }}>Recipes</Link>
  </div>
);

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={ <HomePage /> } />
        <Route path="/category/" element={ <Category /> } />
        <Route path="/recipes" element={ <Recipes /> } />
        <Route path="/recipes/:id" element={ <RecipeDetail /> } />
        <Route path="/about" element={ <TestComponent /> } />
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
