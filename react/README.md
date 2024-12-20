# React
React notes here

## How to start react project
You should probably use vite but for demo projects you can get away with
```sh
npx create-react-app my-app
```
And if you need react in current directory you use command
```sh
npx create-react-app .
```
Its good to create local projects, like one has backend in node, another has frontned in react. You create client directory and then use above command there.  
  
Now main app (having client and server directories) should have gitignore for node and react client app will have react gitignore created automatically.

Important thing: now you need to install this:
```sh
npm install --save-dev web-vitals
```
And of course you run thins command to start react:
```sh
npm start
```
And of course skeleton typescript-react app you create like this:
```sh
npx create-react-app my-app --template typescript
```
But seriously, switch to vite. Create-react-app for demo projects only.