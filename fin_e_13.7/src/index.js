import './styles.css';

const app = document.createElement('div');
app.id = 'app';

const header = document.createElement('h1');
header.textContent = 'Уважаемый разработчик, вам привет от "старых штиблет"!';

app.appendChild(header);
document.body.appendChild(app);

