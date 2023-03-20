// Функциональность для Collapsible Block
const collapsibleTitles = document.querySelectorAll('.collapsible');
collapsibleTitles.forEach(collapsibleTitle => {
    const id = collapsibleTitle.getAttribute('data-collapsible-header');
    const collapsibleContent = document.querySelector(`[data-collapsible-content="${id}"]`);
    collapsibleTitle.addEventListener('click', function () {
        if (collapsibleContent.style.maxHeight) {
            collapsibleContent.style.maxHeight = null;
        } else {
            collapsibleContent.style.maxHeight = collapsibleContent.scrollHeight + 'px';
        }
    });
});

// Функциональность для Timeline
const timelineItems = document.querySelectorAll('.timeline li');
timelineItems.forEach(item => {
    const h3 = item.querySelector('h3');
    const p = item.querySelector('p');
    const date = new Date(p.textContent);
    if (!isNaN(date.getFullYear())) {
        h3.textContent = date.getFullYear();
    }
});

// Функциональность для Skillbar
const skillBars = document.querySelectorAll('.skill-bar-fill');
skillBars.forEach(skillBar => {
    const percent = skillBar.getAttribute('data-percent');
    if (percent) {
        skillBar.style.setProperty('--percent', percent);
        skillBar.classList.add('active');
    }
});

// Функционал для experience
document.querySelectorAll('.experience-item').forEach(item => {
    const title = item.querySelector('.experience-item-title');
    const content = item.querySelector('.experience-item-content');
    title.addEventListener('click', function () {
        content.classList.toggle('active');
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + 'px';
        }
    });
});
