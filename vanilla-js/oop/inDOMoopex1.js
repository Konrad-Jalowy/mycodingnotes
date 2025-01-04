class Shop {
    constructor() {
      this.render();
    }
  
    render() {
      this.cart = new ShoppingCart('app');
      new ProductList('app');
    }
  }
  
  class App {
    static cart;
  
    static init() {
      const shop = new Shop();
      this.cart = shop.cart;
    }
  
    static addProductToCart(product) {
      this.cart.addProduct(product);
    }
  }
  
  App.init();
  