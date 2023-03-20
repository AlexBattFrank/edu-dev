// Функциональность для Collapsible Block

const collapsibleTitles = document.querySelectorAll('.data-collapsible-title');
collapsibleTitles.forEach(collapsibleTitle => {
    const id = collapsibleTitle.getAttribute('data-collapsible-title');
    const contentElement = document.getElementById(id);
    const collapsibleContents = document.querySelectorAll('.collapsible-content');

    collapsibleContents.forEach(collapsibleContent => {
        const parentCollapsible = collapsibleContent.closest('.collapsible-title');
        parentCollapsible.addEventListener('click', function () {
            collapsibleContent.classList.toggle('active');
            if (collapsibleContent.style.maxHeight) {
                collapsibleContent.style.maxHeight = null;
            } else {
                collapsibleContent.style.maxHeight = collapsibleContent.scrollHeight + 'px';
            }
        });
    });
});

// Функциональность для Timeline
    const timelineItems = document.querySelectorAll('.timeline li');

    timelineItems.forEach(item => {
        const h3 = item.querySelector('h3');
        const p = item.querySelector('p');
        const date = new Date(p.textContent);
        h3.textContent = date.getFullYear();
    });

// Функциональность для Skillbar
    const skillBars = document.querySelectorAll('.skill-bar-fill');

    skillBars.forEach(skillBar => {
        const percent = skillBar.getAttribute('data-percent');
        skillBar.style.setProperty('--percent', percent);
        skillBar.classList.add('active');
    });
    
// Функционал для experience
document.querySelectorAll('.experience li').forEach(item => {
    const title = item.querySelector('h3');
    const content = item.querySelectorAll('p');

    title.addEventListener('click', function() {
        content.forEach(c => c.classList.toggle('hidden'));
    });
});
