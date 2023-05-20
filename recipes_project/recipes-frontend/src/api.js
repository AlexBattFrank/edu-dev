import axios from 'axios';

export default axios.create({
  baseURL: 'http://localhost:8000/api/',  // My URL Django API
});
