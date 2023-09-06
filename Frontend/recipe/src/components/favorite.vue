<template>
  <div>
    <NavbarPage></NavbarPage>
    <div v-for="(item, index) in items" :key="index" class="item">
      <img :src="item.image_url" alt="Item Image" class="item-image" />
      <h3 class="item-title">{{ item.title }}</h3>
      <button @click="addToMealPlanner(index)" class="action-button">Add to Meal Planner</button>
      <button @click="deleteItem(index)" class="action-button">Delete</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import NavbarPage from './NavbarPage.vue'
export default {
    name:'FavPage',
  data() {
    return {
      items: [], // Array to store data from the API
    };
  },
  mounted() {
    // Fetch data from your API here
    this.fetchData();
  },
  methods: {
    fetchData() {
      // Use Axios or another HTTP library to fetch data from your API
      // Example using Axios:

      let token=localStorage.getItem('token')
      token?token:''

      axios
        .get('http://localhost:8000/recipe/api/get-favorite/',{
            headers: {
             Authorization: `Bearer ${token}`,
           },
        })
        .then((response) => {
            console.log(response.data.msg)
          this.items = response.data.msg; // Assuming the API response is an array of items
        })
        .catch((error) => {
          console.error('Error fetching data:', error);
        });
    },
    addToMealPlanner(index) {
        const itemToAdd = this.items[index]
        let token=localStorage.getItem('token')
        token?token:''

        axios
        .post(`http://localhost:8000/recipe/api/add-shoping/${itemToAdd.id}/`,null,{
            headers: {
             Authorization: `Bearer ${token}`,
           },
        })
        .then((response) => {
            alert(response.data.msg)
        })
        .catch((error) => {
          console.error('Error fetching data:', error);
        });

    },
      

      deleteItem(index) {
      const itemToDelete = this.items[index]; // Assuming you have an array of items
      let token=localStorage.getItem('token')
      token?token:''
    // Make an HTTP DELETE request to your API
    axios
      .delete(`http://localhost:8000/recipe/api/del-favorite/${itemToDelete.id}/`,{
        headers: {
             Authorization: `Bearer ${token}`,
           },
      })
      .then((response) => {
        // Handle a successful deletion on the frontend
        alert(response.data.msg)

        // Remove the item from your local data
        this.items.splice(index, 1);
      })
      .catch((error) => {
        // Handle errors, e.g., show an error message
        console.error('Error deleting item:', error);
      });
  },
    },
components: {
     NavbarPage,
  },    
};
</script>

<style scoped>
.item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px;
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

.item-image {
  width: 100%;
  max-width: 200px;
  height: auto;
  margin-bottom: 10px;
}

.item-title {
  font-size: 1.2rem;
  margin: 5px 0;
}

.action-button {
  background-color: #3498db;
  color: #fff;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  margin-top: 10px;
  transition: background-color 0.3s;
}

.action-button:hover {
  background-color: #2980b9;
}
</style>