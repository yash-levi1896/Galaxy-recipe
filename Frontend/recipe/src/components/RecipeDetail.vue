<template>
  <div class="recipe-detail" v-if="recipe">
    <div class="image-container">
      <img :src="recipe.image_url" :alt="recipe.title" class="recipe-image" />
    </div>
    <div class="info-container">
      <h2 class="recipe-title">{{ recipe.title }}</h2>
      <p class="description">{{ recipe.description }}</p>
      <h3>Ingredients</h3>
      <!-- Render ingredients only if recipe.ingredients is defined -->
      <ul v-if="recipe.ingredients" class="ingredients-list">
        <li v-for="(ingredient, index) in recipe.ingredients" :key="index" class="ingredient">
          {{ ingredient }}
        </li>
      </ul>
      <p class="cooking-time">Cooking Time (in min): {{ recipe.cooking_time }}</p>
      <p class="servings">Servings: {{ recipe.servings }}</p>
      <button class="favorite-button">Add to Favorite</button> <!-- Added button class -->
    </div>
  </div>
</template>

<script>
import axios from "axios";


export default {
  props: {
    recipeData: Object, // The recipe data object passed as a prop
  },
  data() {
    return {
      recipe: Object, // Local data property to hold the modified recipe data
    };
  },
  created() {
    // Fetch the recipe data
    axios.get(`http://localhost:8000/recipe/api/recipe-detail/${this.$route.params.recipe_id}/`)
      .then((response) => {
        this.recipe = response.data;
        console.log(response)
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
</script>

<style scoped>
.recipe-detail {
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 20px;
  display: flex;
  width:60%;
  margin: auto;
  flex-direction: row; /* Changed to horizontal flex direction */
  align-items: center;
  justify-content: space-around; /* Added to separate image and info */
}

.title {
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #333;
}

.image-container {
  text-align: center;
  border: 5px solid #fff;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
  padding-top: 0px ;
}

.recipe-image {
  width: 200px; /* Increased image width */
  height: auto;
  border-radius: 10px;
  display: block;
  box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2); /* Added box shadow */
}

.info-container {
  margin-left: 20px; /* Adjusted margin to separate image and info */
  text-align: left;
  max-width: 600px;
}

.recipe-title {
  font-size: 24px;
  font-weight: bold;
  margin-top: 20px;
  color: #333;
}

.description {
  margin-top: 10px;
  color: #666;
}

.ingredients-list {
  margin-top: 20px;
  list-style-type: disc;
  padding-left: 20px;
}

.ingredient {
  margin-bottom: 8px;
  color: #444;
}

.cooking-time,
.servings {
  margin-top: 20px;
  font-weight: bold;
  color: #333;
}

.favorite-button {
  background-color: #f60;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s; /* Added transition for smooth hover effect */
}

.favorite-button:hover {
  background-color: #f90; /* Change background color on hover */
}

</style>
