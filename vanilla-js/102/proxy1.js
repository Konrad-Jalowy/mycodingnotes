const handler = {
    get(target, prop) {
        if (prop === 'balance' && target[prop] < 0) {
            throw new Error("Value must be positive!");
        }
        return target[prop];
    },
    set(target, prop, value) {
        if (prop === 'balance' && value < 0) {
            throw new Error("Value must be positive!");
        }
        target[prop] = value;
        return true;
    }
};

const account = new Proxy({ balance: 100 }, handler);
console.log(account.balance);  // 100
account.balance = -50;         // Error: Value must be positive!