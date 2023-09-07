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
      <router-link to="/login" style="text-decoration:none;color:white">Login</router-link>
      <router-link to="/register" style="text-decoration:none;color:white;margin-left:10px;">Signup</router-link>
      </span>
       <span v-else> 
       <span>{{ username }}</span> 
        <span @click="logout" style="margin-left:10px;cursor:pointer;">Logout</span>
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
       alert('Logout sucessful !')
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
  margin-bottom: 5px;
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
