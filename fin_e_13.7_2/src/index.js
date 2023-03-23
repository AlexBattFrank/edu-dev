import './styles.css';

const app = document.createElement('div');
app.id = 'app';

const header = document.createElement('h1');
header.textContent = 'В Ипатьевской слободе,\n' +
  'По улицам водят коня,\n' +
  'На улицах пьяный бардак,\n' +
  'На улицах полный "привет"....';

app.appendChild(header);
document.body.appendChild(app);

