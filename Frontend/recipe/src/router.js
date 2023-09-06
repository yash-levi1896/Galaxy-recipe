import { createRouter, createWebHistory } from 'vue-router';
import DishMenu from './components/DishMenu.vue';
import RecipeDetails from './components/RecipeDetail.vue';
import Register from './components/SignUp.vue'
import Login from './components/LoginPage.vue'
import Index from './components/IndexPage.vue'
import FavPage from './components/favorite.vue'
import PerRec from './components/RecipeRecommend.vue'
import ShoppingList from './components/ShoppingList.vue'

const routes = [
  {
    path: '/',
    name: 'Indexpage',
    component: Index, // Include DishMenu in this specific route
  },
  {
    path: '/recipe',
    name: 'All Recipe',
    component: DishMenu, // Include DishMenu in this specific route
  },
  {
    path: '/recipe/:recipe_id',
    name: 'recipeDetails',
    component: RecipeDetails,
    props: true,
  },
  {
    path: '/register',
    name: 'Signup',
    component: Register,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/favorite',
    name: 'fav',
    component: FavPage,
  },
  {
    path: '/recommendations',
    name: 'recpage',
    component: PerRec,
  },
  {
    path: '/shopping-list',
    name: 'shopping',
    component: ShoppingList,
  },
  // Other routes...
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
