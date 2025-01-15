const helpers = {
    uppercase: str => str.toUpperCase(),
    lowercase: str => str.toLowerCase(),
    multiply: (a, b) => a * b,
    default: (value, fallback) => (value !== undefined && value !== null ? value : fallback)
  };
  
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
  
    // Helpery
    template = template.replace(/{{\s*(\w+)\(([^)]*)\)\s*}}/g, (match, helperName, args) => {
      const params = args.split(',').map(arg => {
        arg = arg.trim();
        if (arg.startsWith('"') && arg.endsWith('"')) {
          return arg.slice(1, -1); // Usuń cudzysłowy
        }
        return data[arg] !== undefined ? data[arg] : undefined; // Klucze z danych
      });
      if (typeof helpers[helperName] === 'function') {
        return helpers[helperName](...params);
      }
      return '';
    });
  
    // Proste zmienne
    return template.replace(/{{\s*(\w+)\s*}}/g, (match, key) => {
      return data[key] !== undefined ? data[key] : '';
    });
  }
  
  // Szablon
  const template = `
    <h1>{{uppercase(title)}}</h1>
    <p>{{lowercase(description)}}</p>
    <p>2 * 3 = {{multiply(2, 3)}}</p>
    <p>{{default(undefinedKey, "Fallback value")}}</p>
    <ul>
      {{#each items}}
        <li>{{uppercase(this)}}</li>
      {{/each}}
    </ul>
  `;
  
  // Dane
  const data = {
    title: 'My Awesome App',
    description: 'HELLO WORLD!',
    items: ['Item 1', 'Item 2', 'Item 3']
  };
  
  // Renderowanie i wstawienie do DOM
  const output = render(template, data);
  document.getElementById('app').innerHTML = output;
  