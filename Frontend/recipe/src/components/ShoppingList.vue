// ShoppingList.vue

<template>
  <div>
    <NavbarPage></NavbarPage>
  <div class="shopping-list">
    <h2>Shopping List</h2>
    <div v-if="isLoading">
      <h3>Loading...</h3>
    </div>
    <div v-else>
      <div v-if="ingredients.length===0">
        <h3>shopping List is empty</h3>
      </div>
      <div v-else>
    <div v-for="(item, index) in ingredients" :key="index">
      <h3>Item {{ index + 1 }}</h3>
      <ul>
        <li v-for="(ingredient, i) in item.ingredients" :key="i">
          {{ ingredient }}
        </li>
      </ul>
      <!-- <button @click="deleteIngredient(index)">Delete</button> -->
      </div>
    </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import NavbarPage from './NavbarPage.vue'

export default {
  data() {
    return {
      ingredients: [],
      isLoading:true
    };
  },
  methods: {
    
    deleteIngredient(index) {
       const itemToRemove = this.ingredients[index];
      let token = localStorage.getItem("token") || "";

      // Make an Axios DELETE request to remove the item
      axios
        .delete(`http://localhost:8000/recipe/api/del-shoping/${itemToRemove.id}/`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((response) => {
          // Handle the successful deletion
          alert(response.data.msg);

          // Remove the item from the local ingredients array
          this.ingredients.splice(index, 1);
        })
        .catch((error) => {
          // Handle errors, e.g., show an error message
          console.error("Error removing item", error);
        });
    },
    async fetchIngredients() {
        let token=localStorage.getItem('token')
        token?token:''
      try {
        const response = await axios.get("http://localhost:8000/recipe/api/get-shoping/",{
            headers: {
             Authorization: `Bearer ${token}`,
           },
        });

        // Assuming your API returns ingredients as an array of objects
        this.ingredients = response.data.msg;
        this.isLoading=false
        
      } catch (error) {
        this.isLoading=false
        console.error("Error fetching ingredients:", error);
      }
    },
  },
  mounted() {
    // Fetch ingredients when the component is mounted
    this.fetchIngredients();
  },
  components:{
    NavbarPage
  }
};
</script>

<style scoped>
/* Container for the shopping list */
.shopping-list {
  font-size: 16px;
  margin-top: 20px;
  padding: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

/* Heading for each shopping list item */
h3 {
  margin-top: 10px;
  font-size: 18px;
  color: #333;
}

/* List of ingredients */
ul {
  list-style-type: none;
  padding: 0;
  margin-top: 5px;
}

/* Individual ingredient */
li {
  margin-bottom: 5px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Delete button */
button {
  background-color: #3498db;
  color: white;
  border: none;
  cursor: pointer;
  padding: 5px 10px;
  border-radius: 3px;
  transition: background-color 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Hover effect on the delete button */
button:hover {
  background-color: #2980b9;
}

/* User-friendly spacing */
.button-container {
  margin-top: 10px;
   text-align: left;
}
</style>

