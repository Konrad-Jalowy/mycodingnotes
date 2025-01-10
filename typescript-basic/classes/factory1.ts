// Interfejs fabryki
interface ListFactory {
    createList(items: string[]): HTMLElement;
}

// Konkretne fabryki
class UnorderedListFactory implements ListFactory {
    createList(items: string[]): HTMLElement {
        const ul = document.createElement("ul");
        items.forEach(item => {
            const li = document.createElement("li");
            li.textContent = item;
            ul.appendChild(li);
        });
        return ul;
    }
}

class OrderedListFactory implements ListFactory {
    createList(items: string[]): HTMLElement {
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
function renderList(factory: ListFactory, items: string[], containerId: string): void {
    const container = document.getElementById(containerId);
    if (!container) {
        throw new Error(`Container with id '${containerId}' not found.`);
    }

    const list = factory.createList(items);
    container.appendChild(list);
}

// Testowanie
const items: string[] = ["Item A", "Item B", "Item C"];

const ulFactory: ListFactory = new UnorderedListFactory();
const olFactory: ListFactory = new OrderedListFactory();

document.body.innerHTML = "<div id='container'></div>";

console.log("Dodawanie listy nieuporządkowanej:");
renderList(ulFactory, items, "container");

console.log("Dodawanie listy uporządkowanej:");
renderList(olFactory, items, "container");
