// MenuPage.vue
<template>
  <div>
    <h1 style="width:50%;margin:auto;margin-top:0px;margin-bottom:10px">Recipes</h1>
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

export default {
  data() {
    return {
      recipes: [],
    };
  },
  created() {
    axios.get("http://127.0.0.1:8000/recipe/api/get-recipe/")
      .then((response) => {
        this.recipes = response.data;
        // console.log(response)
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  },
  components: {
    DishItem,
  },
};
</script>
<style scoped>
     
.menu-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

/* Add additional CSS rules for responsiveness as needed */
@media (max-width: 768px) {
  .menu-grid {
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  }
}

</style>