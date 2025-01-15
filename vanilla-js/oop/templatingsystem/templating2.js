function render(template, data) {
    // Warunki (if/else)
    template = template.replace(/{{#if (\w+)}}([\s\S]*?){{else}}([\s\S]*?){{\/if}}/g, (match, key, ifContent, elseContent) => {
      return data[key] ? render(ifContent, data) : render(elseContent, data);
    });
  
    template = template.replace(/{{#if (\w+)}}([\s\S]*?){{\/if}}/g, (match, key, ifContent) => {
      return data[key] ? render(ifContent, data) : '';
    });
  
    // Pętle (each)
    template = template.replace(/{{#each (\w+)}}([\s\S]*?){{\/each}}/g, (match, key, innerTemplate) => {
      const items = data[key];
      if (Array.isArray(items)) {
        return items.map(item => render(innerTemplate, { ...data, this: item })).join('');
      }
      return '';
    });
  
    // Proste zmienne
    return template.replace(/{{\s*(\w+)\s*}}/g, (match, key) => {
      return data[key] !== undefined ? data[key] : '';
    });
  }
  const template = `
  <h1>{{title}}</h1>
  <p>{{description}}</p>

  {{#if showList}}
    <ul>
      {{#each items}}
        <li>{{this}}</li>
      {{/each}}
    </ul>
  {{else}}
    <p>No items to display.</p>
  {{/if}}
`;

const data = {
  title: 'Advanced Templating System',
  description: 'This template supports conditions and loops.',
  showList: true,
  items: ['Item 1', 'Item 2', 'Item 3']
};

const output = render(template, data);
document.getElementById('app').innerHTML = output;