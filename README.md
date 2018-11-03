# Example of embedding nodejs app in uliweb project

## Why?

1. Can debug and deploy with same style
2. No cross-domain needed

## How to embed?

1. Create a uliweb app for nodejs app like [node_example](apps/node_example)
2. Configure publicPath under static directory, [example: publicPath: '/static/node/'](apps/node_example/webpack.prod.config.js#L11)
3. Configure npm scripts to watch source code and build, [example](apps/node_example/package.json#L6)
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
5. Access http://localhost:8000 to view the dev web server
6. Try to modify nodejs source code( for example app.vue )
7. Try to refresh browser with Ctrl+Shift+R or disable the browser cache to see the result after modification

## Known issue

1. When nodejs source code changed and built, in browser need to use 'Ctrl+Shift+R' to refresh, so that browser won't use old version in cache.
