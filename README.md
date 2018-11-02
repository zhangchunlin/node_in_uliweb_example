# Example of embedding nodejs app in uliweb project

## How to embedding?

1. Create a uliweb app for nodejs app like [node_example](apps/node_example)
2. Configure publicPath under static directory, [example: publicPath: '/static/node/'](apps/node_example/webpack.prod.config.js)
3. Configure npm scripts to watch source code and build, [example](apps/node_example/package.json)
4. Run uliweb debug server: uliweb runserver
5. Run npm script to watch and build

## How to use this source code?

1. Install python dependency, in uliweb project root directory run:
   1. pip install -r requirements.txt
2. In nodejs source code root ( apps/node_example/ ) install nodejs dependency:
   1. npm install
3. In uliweb project root directory run the debug server:
   1. uliweb runserver
4. In nodejs source code root run watch and build command:
   1. npm run build:watch

