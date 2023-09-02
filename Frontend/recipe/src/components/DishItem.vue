<!-- DishItem.vue -->
<template>
  <!-- DishItem.vue -->
  <router-link :to="{ name: 'recipeDetails', params: { recipe_id: recipe.id } }">
    <div class="dish">
      <img :src="recipe.image_url" :alt="recipe.title" />
      <h3>{{ recipe.title }}</h3>
    </div>
  </router-link>
</template>

<script>
export default {
  props: {
    recipe: Object,
  },
};
</script>

<style scoped>
/* Add CSS styling for the DishItem component */
.dish {
  border: 1px solid #ddd;
  padding: 20px;
  text-align: center;
  transition: transform 0.2s ease; /* Add a smooth hover effect */
}

.dish img {
  max-width: 100%;
  height: auto;
}

.dish h3 {
  font-size: 18px;
  margin-top: 10px;
  text-decoration: none;
}

/* Hover effect */
.dish:hover {
  transform: scale(1.05);
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
