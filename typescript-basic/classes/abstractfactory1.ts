// Interfejs elementu listy (li)
interface ListItem {
    render(): string;
}

// Konkretne elementy listy
class UnorderedListItem implements ListItem {
    constructor(private content: string) {}
    render(): string {
        return `<li style="color: blue;">${this.content}</li>`;
    }
}

class OrderedListItem implements ListItem {
    constructor(private content: string) {}
    render(): string {
        return `<li style="font-weight: bold;">${this.content}</li>`;
    }
}

// Interfejs listy (ul/ol)
interface List {
    addItem(item: ListItem): void;
    render(): string;
}

// Konkretne listy
class UnorderedList implements List {
    private items: ListItem[] = [];
    addItem(item: ListItem): void {
        this.items.push(item);
    }
    render(): string {
        return `<ul>${this.items.map(item => item.render()).join('')}</ul>`;
    }
}

class OrderedList implements List {
    private items: ListItem[] = [];
    addItem(item: ListItem): void {
        this.items.push(item);
    }
    render(): string {
        return `<ol>${this.items.map(item => item.render()).join('')}</ol>`;
    }
}

// Interfejs Abstract Factory
interface ListFactory {
    createList(): List;
    createListItem(content: string): ListItem;
}

// Konkretne fabryki
class UnorderedListFactory implements ListFactory {
    createList(): List {
        return new UnorderedList();
    }
    createListItem(content: string): ListItem {
        return new UnorderedListItem(content);
    }
}

class OrderedListFactory implements ListFactory {
    createList(): List {
        return new OrderedList();
    }
    createListItem(content: string): ListItem {
        return new OrderedListItem(content);
    }
}

// Klient
function renderComponent(factory: ListFactory, items: string[]): string {
    const list = factory.createList();
    items.forEach(item => list.addItem(factory.createListItem(item)));
    return list.render();
}

// Testowanie
const unorderedFactory = new UnorderedListFactory();
const orderedFactory = new OrderedListFactory();

const unorderedHtml = renderComponent(unorderedFactory, ["Item 1", "Item 2", "Item 3"]);
const orderedHtml = renderComponent(orderedFactory, ["First", "Second", "Third"]);

console.log("Lista nieuporządkowana:");
console.log(unorderedHtml);

console.log("\nLista uporządkowana:");
console.log(orderedHtml);

// Jeśli testujesz w przeglądarce:
// document.body.innerHTML = unorderedHtml + "<br>" + orderedHtml;
