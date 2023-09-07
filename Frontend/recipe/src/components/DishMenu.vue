// MenuPage.vue
<template>
  <div>
    <NavbarPage></NavbarPage>
    <h1 style="width:50%;margin:auto;margin-top:0px;margin-bottom:10px">Recipes</h1>
    <label for="dietPreference" style="margin-top:5px;margin-bottom:10px">Diet Preference:</label>
    <select v-model="selectedDiet" id="dietPreference" @change="fetchRecipes">
      <option value="all">All</option>
      <option value="vegan">Vegan</option>
      <option value="Non-veg">Non-Veg</option>
      <option value="vegetarian">Vegetarian</option>
    </select>
    <div class="menu-grid">  
      <DishItem
        v-for="recipe in recipes"
        :key="recipe.id"
        :recipe="recipe"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import DishItem from "./DishItem.vue";
import NavbarPage from './NavbarPage.vue'

export default {
  data() {
    return {
      recipes: [],
      selectedDiet: 'all'
    };
  },
  created() {
    axios.get("https://recipefinderone.onrender.com/recipe/api/get-recipe/")
      .then((response) => {
        this.recipes = response.data;
        // console.log(response)
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  },
     methods: {
    fetchRecipes() {
      // Check if 'All' option is selected
      if (this.selectedDiet === 'all') {
        // If 'All' is selected, make a GET request without diet preference filter
        axios.get("https://recipefinderone.onrender.com/recipe/api/get-recipe/")
          .then((response) => {
            this.recipes = response.data;
          })
          .catch((error) => {
            console.error("Error fetching data:", error);
          });
      } else {
        // If a specific diet preference is selected, include it in the query
        axios.get("https://recipefinderone.onrender.com/recipe/api/get-recipe/", {
          params: {
            diet_preference: this.selectedDiet,
          },
        })
          .then((response) => {
            this.recipes = response.data;
          })
          .catch((error) => {
            console.error("Error fetching data:", error);
          });
      }
    },
  },
  components: {
    DishItem,
     NavbarPage,
  },
   watch: {
    selectedDiet: 'fetchRecipes',
  },
};
</script>

<style scoped>
     
.menu-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

/* Add additional CSS rules for responsiveness as needed */
@media (max-width: 768px) {
  .menu-grid {
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  }
}

</style>