import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import Article from './views/Article.vue'
import Vendeur from './views/Vendeur.vue'
import Research from './views/Research.vue'
import Dashboard from './views/Dashboard.vue'
import Main from './views/Main.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'main',
      component: Main,
      children: [
        {
          path: '/',
          name: 'home',
          component: Home
        },
        {
          path: '/about',
          name: 'about',
          component: About
        },
        {
          path: '/article/:id',
          name: 'article',
          component: Article
        },
        {
          path: '/vendeur/:id',
          name: 'vendeur',
          component: Vendeur
        },
        {
          path: '/dashboard',
          name: 'dashboard',
          component: Dashboard
        }
      ]
    },
    {
      path: '/research',
      name: 'research',
      component: Research
    }
  ]
})
