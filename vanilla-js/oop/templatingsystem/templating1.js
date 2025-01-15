function render(template, data) {
    return template
      .replace(/{{#each (\w+)}}([\s\S]*?){{\/each}}/g, (match, key, innerTemplate) => {
        const items = data[key];
        if (Array.isArray(items)) {
          return items.map(item => render(innerTemplate, { this: item })).join('');
        }
        return '';
      })
      .replace(/{{\s*(\w+)\s*}}/g, (match, key) => {
        return data[key] !== undefined ? data[key] : '';
      });
  }
  const template = `
  <h1>{{title}}</h1>
  <p>{{description}}</p>
  <ul>
    {{#each items}}
    <li>{{this}}</li>
    {{/each}}
  </ul>
`;

const data = {
  title: 'Hello, World!',
  description: 'This is a templating system with loops.',
  items: ['Item A', 'Item B', 'Item C']
};

const output = render(template, data);
document.getElementById('app').innerHTML = output;
  