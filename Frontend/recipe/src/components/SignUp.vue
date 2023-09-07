<template>
  <div>
    <h1>Signup</h1>
    <div class="container">
      <form @submit.prevent="signup">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="data.username" required />
        </div>
        <div>
          <label for="email" id="em">Email:</label>
          <input type="email" id="email" v-model="data.email" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="data.password" required />
        </div>
        <button type="submit">Signup</button>
        <p>Already registered <router-link to="/login" style="text-decoration:none;color:#3498db">Login</router-link></p>
        <router-link to="/" style="text-decoration:none;color:#3498db">Home Page</router-link>
      </form>
    </div>
  </div>
</template>


<script>
import axios from 'axios'; 

export default {
  data() {
    return {
      data: {
        username: '',
        email: '',
        password: '',
      },
    };
  },
  methods: {
    async signup() {
      // Handle form submission here
       try {
        const response = await axios.post('http://localhost:8000/recipe/api/register/', this.data);
        // Handle successful signup (e.g., show a success message, redirect the user)
            alert(response.data.msg)
        
      } catch (error) {
        // Handle signup errors (e.g., show an error message)
        alert(error.response.data.username[0])
      }
    },
  },
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

#em{
  margin-right: 30px;
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
