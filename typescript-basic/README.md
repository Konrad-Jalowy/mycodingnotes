# typescript basic
basics of typescrip

# quick start
## start project
```sh
npx tsc --init
```
## run ts file in command line
```sh
npx ts-node src/foo.ts
```
## compile files
remember to specify outDir or it will compile them in cwd
```sh
npx tsc
```
## compile watch flag
```sh
npx tsc -w
```

## ts type aliases
nice reminder how they work code from the internet
```ts
type stringOrNumber = string | number

type stringOrNumberArray = (string | number)[]

type Guitarist = {
    name?: string,
    active: boolean,
    albums: stringOrNumberArray
}

type UserId = stringOrNumber

// Literal types
let myName: 'Dave'

let userName: 'Dave' | 'John' | 'Amy'
userName = 'Amy'
```