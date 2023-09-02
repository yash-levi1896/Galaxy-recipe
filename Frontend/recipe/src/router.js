import { createRouter, createWebHistory } from 'vue-router';
import DishMenu from './components/DishMenu.vue';
import RecipeDetails from './components/RecipeDetail.vue';


const routes = [
  {
    path: '/',
    name: 'All Recipe',
    component: DishMenu, // Include DishMenu in this specific route
  },
  {
    path: '/recipe/:recipe_id',
    name: 'recipeDetails',
    component: RecipeDetails,
    props: true,
  },
  // Other routes...
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
