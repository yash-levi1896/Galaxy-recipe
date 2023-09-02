import { createApp } from 'vue'; // Import createApp from Vue 3
import App from './App.vue';
import router from './router';

const app = createApp(App);
app.use(router); // Use the router
app.mount('#app');
