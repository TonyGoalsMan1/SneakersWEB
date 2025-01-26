import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import Products from '../pages/Products.vue'
import Auth from '../pages/Auth.vue'

const routes = [
    { path: '/', component: Home },
    { path: '/products', component: Products },
    { path: '/auth', component: Auth }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
