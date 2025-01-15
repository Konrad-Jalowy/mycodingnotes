// Model (Reaktywność)
class Model {
    constructor(data = {}) {
      this.data = new Proxy(data, {
        set: (target, key, value) => {
          target[key] = value;
          this.notify();
          return true;
        }
      });
      this.listeners = [];
    }
  
    onChange(callback) {
      this.listeners.push(callback);
    }
  
    notify() {
      this.listeners.forEach(callback => callback(this.data));
    }
  }
  
  // Komponenty
  class Component {
    constructor(selector, model, template) {
      this.element = document.querySelector(selector);
      this.model = model;
      this.template = template;
  
      // Aktualizuj widok, gdy dane w modelu się zmienią
      this.model.onChange(data => this.render(data));
    }
  
    render(data) {
      this.element.innerHTML = this.template(data);
    }
  }
  
  // Router
  class Router {
    constructor() {
      this.routes = [];
    }
  
    add(path, callback) {
      this.routes.push({ path, callback });
    }
  
    navigate(path) {
      history.pushState({}, '', path);
      this.handleRoute();
    }
  
    handleRoute() {
      const currentPath = window.location.pathname;
      const route = this.routes.find(r => r.path === currentPath);
      if (route) route.callback();
    }
  
    start() {
      window.addEventListener('popstate', () => this.handleRoute());
      this.handleRoute();
    }
  }
  
  // Przykład użycia frameworka
  document.addEventListener('DOMContentLoaded', () => {
    // Tworzymy model
    const model = new Model({
      title: 'Welcome to the App',
      content: 'This is the home page.'
    });
  
    // Tworzymy komponent
    const appComponent = new Component('#app', model, data => `
      <h1>${data.title}</h1>
      <p>${data.content}</p>
    `);
  
    // Tworzymy router
    const router = new Router();
  
    router.add('/home', () => {
      model.data.title = 'Home Page';
      model.data.content = 'This is the home page.';
    });
  
    router.add('/about', () => {
      model.data.title = 'About Page';
      model.data.content = 'This is the about page.';
    });
  
    router.start();
  
    // Obsługa przycisków nawigacyjnych
    document.querySelectorAll('[data-route]').forEach(button => {
      button.addEventListener('click', () => {
        const path = button.getAttribute('data-route');
        router.navigate(path);
      });
    });
  });
  