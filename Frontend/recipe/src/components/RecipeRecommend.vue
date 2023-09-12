<template>
  <div>
    <NavbarPage></NavbarPage>
  <div class="recipe-recommendation">
    <h2>Recipe Recommendation</h2>
    <form @submit.prevent="findRecipe">
      <label for="dietType">Diet Type:</label>
      <select v-model="dietType" id="dietType">
        <option value="vegan">Vegan</option>
        <option value="vegetarian">Vegetarian</option>
        <option value="non-veg">Non-Veg</option>
        <option value="dairy-free">Dairy-Free</option>
      </select>

      <label for="includedIngredients">Included Ingredients(seperated by comma):</label>
      <input v-model="includedIngredients" type="text" id="includedIngredients" placeholder="Enter ingredients to include">

      <label for="excludedIngredients">Excluded Ingredients(seperated by comma):</label>
      <input v-model="excludedIngredients" type="text" id="excludedIngredients" placeholder="Enter ingredients to exclude">

      <button type="submit">Find Recipe</button>
    </form>

    <div v-if="showResults">
      <h3>Recommended Recipe:</h3>
      <!-- Display recommended recipe here -->
            <p>{{ recommendedRecipe[recommendedRecipe.length-1] }}</p>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import NavbarPage from './NavbarPage.vue'

export default {
    name:'PerRec',
  data() {
    return {
      dietType: 'vegan',
      includedIngredients: '',
      excludedIngredients: '',
      showResults: false,
      recommendedRecipe: [],
    };
  },
  watch: {
    dietType: 'findRecipe',
    includedIngredients: 'findRecipe',
    excludedIngredients: 'findRecipe',
  },

  methods: {
    findRecipe() {
      // Send a POST request to your backend API with the selected options
      const requestData = {
        diet: this.dietType,
        ingredients_list: this.includedIngredients,
        not_ingredients_list: this.excludedIngredients,
      };

      // Make an Axios POST request to your backend
      // Replace 'your-backend-api-url' with the actual API endpoint
      axios.post('https://recipefinderone.onrender.com/recipe/api/recipe-recommend/', requestData)
        .then((response) => {
          // Handle the response and set the recommended recipe
        //    console.log(response.data.msg)
          this.recommendedRecipe.push(response.data.msg);
          this.showResults = true;
        })
        .catch((error) => {
          console.error('Error finding recipe:', error);
        });
    },
  },
  components:{
    NavbarPage
  },
};
</script>

<style scoped>
.recipe-recommendation {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
  background-color: #f9f9f9;
  border-radius: 5px;
}

h2 {
  font-size: 24px;
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  font-weight: bold;
  margin-bottom: 6px;
}

select,
input {
  width: 100%;
  padding: 10px;
  margin: 6px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background-color: #2980b9;
}

div[if] {
  margin-top: 20px;
}

h3 {
  font-size: 20px;
  margin-bottom: 10px;
}
</style>

