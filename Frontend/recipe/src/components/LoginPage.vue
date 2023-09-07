<template>
  <div>
    <h1>Login</h1>
    <div class="container">
      <form @submit.prevent="login">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="formData.username" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="formData.password" required />
        </div>
        <button type="submit">Login</button>
        <p>If not registered<router-link to="/register" style="text-decoration:none;color:#3498db;margin-left:10px;">Signup</router-link></p>
        <router-link to="/" style="text-decoration:none;color:#3498db;">Home Page</router-link>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      formData: {
        username: '',
        password: '',
      },
    };
  },
  methods: {
     async login() {
      try {
        const response = await axios.post('http://localhost:8000/recipe/api/login/', this.formData);

        // Check if login was successful (you can define your response structure)
        if (response.data.msg === 'Login succesfull') {
          // Set username and token in localStorage
          localStorage.setItem('username', this.formData.username);
          localStorage.setItem('token', response.data.token); // Replace with the actual token from your backend

          // Redirect to the dashboard or perform other actions upon successful login
          alert('Login successful');
          this.$router.push("/");
        } else {
          // Handle login failure
          alert(response.data.msg);
        }
      } catch (error) {
        // Handle errors, e.g., network issues or server errors
       // console.error('Error during login:', error);
        alert(error.response.data.msg)
      }
  },
  }
};
</script>

<style scoped>
/* ... (previous styles) */

/* Container styles */
.container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f8f8f8;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Form styles */
form {
  display: flex;
  flex-direction: column;
}

/* Label styles */
label {
  margin-bottom: 5px;
}

/* Input field styles */
input[type="text"],
input[type="email"],
input[type="password"] {
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

button[type="submit"] {
  background-color: #3498db;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #2980b9;
}

/* Center the form on the page */
html, body {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f4f4f4;
}

/* Heading styles */
h1 {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}
</style>

