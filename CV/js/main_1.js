// Функциональность для Collapsible Block
// let i;
// const coll = document.getElementsByClassName("collapsible");
//
// for (i = 0; i < coll.length; i++) {
//     console.log(i)
//     const header = coll[i].previousElementSibling;
//     console.log(header)
//     header.addEventListener('click', function () {
//       this.classList.toggle('active');
//       const content = header.nextElementSibling;
//       if (content.style.maxHeight){
//         content.style.maxHeight = null;
//       } else {
//         content.style.maxHeight = content.scrollHeight + "px";
//         }
//     });
// }



const collapsibleTitles = document.querySelectorAll('.collapsible-title');
collapsibleTitles.forEach(collapsibleTitle => {
  const id = collapsibleTitle.getAttribute('data-collapsible');
  const contentElement = document.getElementById(id);
  const collapsibleContents = document.querySelectorAll('.collapsible-content');

  collapsibleContents.forEach(collapsibleContent => {
    const parentCollapsible = collapsibleContent.closest('.collapsible');
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