// Abstrakcyjna fabryka
class ListFactory {
    createList(items) {
        throw new Error("Method 'createList()' must be implemented.");
    }
}

// Konkretne fabryki
class UnorderedListFactory extends ListFactory {
    createList(items) {
        const ul = document.createElement("ul");
        items.forEach(item => {
            const li = document.createElement("li");
            li.textContent = item;
            ul.appendChild(li);
        });
        return ul;
    }
}

class OrderedListFactory extends ListFactory {
    createList(items) {
        const ol = document.createElement("ol");
        items.forEach(item => {
            const li = document.createElement("li");
            li.textContent = item;
            ol.appendChild(li);
        });
        return ol;
    }
}

// Klient
function renderList(factory, items, containerId) {
    const container = document.getElementById(containerId);
    if (!container) {
        throw new Error(`Container with id '${containerId}' not found.`);
    }

    const list = factory.createList(items);
    container.appendChild(list);
}

// Testowanie
const items = ["Item 1", "Item 2", "Item 3"];

const ulFactory = new UnorderedListFactory();
const olFactory = new OrderedListFactory();

document.body.innerHTML = "<div id='container'></div>";

console.log("Dodawanie listy nieuporządkowanej:");
renderList(ulFactory, items, "container");

console.log("Dodawanie listy uporządkowanej:");
renderList(olFactory, items, "container");
