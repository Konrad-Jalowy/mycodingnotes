interface HasID {
    id: number
}

const withoutId = <T extends HasID>(user: T): Omit<T, "id"> => {
    let partial: Partial<T> = {...user};
    delete partial.id;
    return partial as Omit<T, "id">
}

console.log(withoutId({ id: 1, name: 'Jane Doe' }))