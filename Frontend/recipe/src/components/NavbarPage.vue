<template>
  <nav class="navbar">
    <ul class="nav-list">
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/recipe">Recipes</router-link></li>
      <li><router-link to="/recommendations">Personalized Recommendations</router-link></li>
      <li><router-link to="/favorite">Favorites</router-link></li>
      <li><router-link to="/shopping-list">Shopping List</router-link></li>
    </ul>
    <div class="auth-section">
      <span v-if="!isUserLoggedIn">
      <router-link to="/login">Login</router-link>
      <router-link to="/register">Signup</router-link>
      </span>
       <span v-else> <!-- User is logged in -->
        {{ username }} <!-- Render the username from local storage -->
        <p @click="logout">Logout</p> <!-- Add a logout link -->
      </span>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavbarPage',
  computed: {
    isUserLoggedIn() {
      // Check if the "username" key is present in local storage
      return !!localStorage.getItem("username");
    },
    username() {
      // Get the username from local storage
      return localStorage.getItem("username");
    },
    
  },
  methods:{
    logout(){
       localStorage.clear();
        this.$router.push("/");
    }
  },
};
</script>

<style scoped>
.navbar {
  background-color: #3498db;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  margin-top: 0px;
  margin-bottom: 50px;
}
body{
  margin: 0px;
}

.nav-list {
  list-style: none;
  padding: 0;
  display: flex;
}

.nav-list li {
  margin-right: 20px;
}

.nav-list li:last-child {
  margin-right: 0;
}

.nav-list a {
  text-decoration: none;
  color: white;
  font-weight: bold;
}

.auth-section {
  display: flex;
}

.auth-section a.router-link {
  margin-left: 10px;
  color: white;
  text-decoration: none;
  font-weight: bold;
}
</style>
