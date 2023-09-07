<template>
  <div>
    <NavbarPage></NavbarPage>
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
      <button class="favorite-button" @click="addToFavorite">Add to Favorite</button>
       <button class="review-button" @click="openReviewModal" v-if="isAuthenticated">Review</button>
    </div>
  </div>
   
   <div v-if="isReviewModalOpen" class="review-modal">
      <div class="modal-content">
        <h3>Submit Review</h3>
        <div class="form-group">
          <label for="userRating">Rating:</label>
          <input v-model="userRating" type="number" id="userRating" min="1" max="5" step="1" />
        </div>
        <div class="form-group">
          <label for="userReview">Review:</label>
          <textarea v-model="userReview" id="userReview" rows="4"></textarea>
        </div>
        <button @click="submitReview">Submit</button>
        <button @click="closeReviewModal">Cancel</button>
      </div>
    </div>

    <h2 style="margin-top:40px;text-align:left;margin-left:360px;">Reviews</h2>
    <div v-if="isLoading">
      <h3>Loading...</h3>
    </div>
    <div v-else>
      <div v-if="reviews.length === 0">
      <h3>No reviews yet.Be the first one to review by logining in </h3>
      </div>
    <div v-else>
    <div class="review-cards">
      <!-- Loop through reviews and render each as a card -->
      <div v-for="(review, index) in reviews" :key="index" class="review-card">
        <!-- Dummy user image (you can replace with actual images) -->
        <div style="margin-right:30px">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfyjVSuZl6mHFDbODbb1PKoSs3sz-f2k6qeQ&usqp=CAU" alt="User Image" class="user-image" />
        <!-- User name -->
          <p class="user-name">{{ review.username }}</p>
        </div>
        <div class="review-content">
          <!-- User rating -->
          <p class="user-rating">Rating: {{ review.rating }}/5</p>
          <!-- User review -->
          <p class="user-review">{{ review.review }}</p>
        </div>
      </div>
    </div>
    </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavbarPage from './NavbarPage.vue'

export default {
  props: {
    recipeData: Object, // The recipe data object passed as a prop
  },
  data() {
    return {
      recipe: Object,
      isReviewModalOpen: false, // Add this property
      userRating: 0, // Add this property to store the user's rating
      userReview: '', // Add this property to store the user's review
      reviews: [],
      isLoading:true
    };
  },
   computed: {
    isAuthenticated() {
      // Check if the user is authenticated (e.g., by verifying the presence of a valid token)
      const authToken = localStorage.getItem('token')
      return !!authToken; // Convert to boolean
    },
  },
  mounted() {
    // Fetch the recipe data
    axios.get(`https://recipefinderone.onrender.com/recipe/api/recipe-detail/${this.$route.params.recipe_id}/`)
      .then((response) => {
        this.recipe = response.data;
        console.log(response)
      })
      .catch((error) => {
        console.error(error);
      });
      this.fetchReviews()
  },
    methods: {
    addToFavorite() {
      // Assuming this.recipe.id contains the recipe ID
      const recipe_id = this.recipe.id; // Replace with the appropriate field from your recipe object
      //const favoriteData = { recipeId: recipe_id }; // Create the payload
      let token=localStorage.getItem('token')
      token?token:''

      axios
        .post(`https://recipefinderone.onrender.com/recipe/api/add-favorite/${recipe_id}/`,null,{
          headers: {
             Authorization: `Bearer ${token}`,
           },
        })
        .then((response) => {
          // Handle the response as needed
          alert(response.data.msg)
          // You can update your UI or show a success message here
        })
        .catch((error) => {
          // Handle errors, e.g., show an error message
          alert(error.response.data.msg)
          console.log('Error adding to favorites:', error);
        });
    },
     submitReview() {
      const recipeID = this.recipe.id; // Get the recipe ID
      
      let token=localStorage.getItem('token')
      token?token:''
  
      // Prepare the review data to be sent to the backend
      
      const reviewData = {
        rating: this.userRating,
        review: this.userReview,
      };

      // Make a POST request to save the review
      if (reviewData.rating!=undefined && reviewData.review!=undefined){
          axios
        .post(`https://recipefinderone.onrender.com/recipe/api/rating/${recipeID}/`, reviewData,{
          headers: {
             Authorization: `Bearer ${token}`,
           },
        })
        .then((response) => {
          // Handle the response, e.g., show a success message
          alert(response.data.msg)
          // After submitting, close the modal
         this.closeReviewModal();
        })
        .catch((error) => {
          // Handle errors, e.g., show an error message
          console.error("Error submitting review", error);
        });
      }else{
        alert("Fill both review and rating")
      }
      
      
    },
   openReviewModal() {
      if (this.isAuthenticated) {
        this.isReviewModalOpen = true;
      } else {
        alert('Please Login !')
      }
    },
    closeReviewModal() {
      this.isReviewModalOpen = false;
      this.userRating = 0;
      this.userReview = '';
    },
    fetchReviews() {
      // Make a GET request to fetch reviews
      axios
        .get(`https://recipefinderone.onrender.com/recipe/api/get-rating/${this.$route.params.recipe_id}/`)
        .then((response) => {
          // Assign the response data to the reviews array
          this.reviews = response.data.msg;
          this.isLoading=false
        })
        .catch((error) => {
          this.isLoading=false
          console.error("Error fetching reviews:", error);
          
        });
    },
  
  },
  components:{
    NavbarPage
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
  background-color: #3498db;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s; /* Added transition for smooth hover effect */
}

.favorite-button:hover {
  background-color: #2980b9; /* Change background color on hover */
}

.review-button{
  margin-left: 10px;
  background-color: #3498db;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.review-button:hover {
  background-color: #2980b9;
}

.modal-content {
  /* Modal styles */
  /* Make it centered on the screen */
  position: fixed;
  top: 250px;
  left: 700px;
  width: 30%;
  /* height: 100%; */
  background-color: rgba(0, 0, 0, 0.7);
}

.modal-content {
  /* Modal content styles */
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
}

.close {
  /* Close button styles */
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
}

.form-group {
  margin-bottom: 10px;
}

label {
  font-weight: bold;
}

input[type="number"],
textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

textarea {
  resize: vertical;
}

button {
  background-color: #3498db;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 10px;
}

button:hover {
  background-color: #2980b9;
}

button.cancel-button {
  background-color: #ccc;
  color: #333;
}

button.cancel-button:hover {
  background-color: #999;
}

.review-cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 20px; /* Adjust the gap between cards as needed */
}

.review-card {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  width: calc(33.33% - 20px); /* Adjust card width based on your layout */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  display: flex;
  margin-left: 350px;
}

.user-image {
  max-width: 100px; /* Adjust the maximum width of the user image */
  border-radius: 50%;
  margin-right: 10px; /* Spacing between image and content */
}

.user-content {
  flex-grow: 1; /* Expand content to fill remaining space */
}

.user-name {
  font-weight: bold;
  margin-bottom: 5px;
}

.user-rating {
  font-weight: bold;
  color: #007bff; /* Adjust the color based on your design */
  margin-bottom: 5px;
  text-align: left;
}

.user-review{
  text-align: left;
  flex-grow: 1;
}


</style>
