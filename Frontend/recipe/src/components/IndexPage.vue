<template>
    <div class="homepage">
          <NavbarPage></NavbarPage>
        <div id="banner">
        <img :src="currentImage" alt="">
        </div>
        <div class="divi2">
            <p>AI Powered Recipe and Ingredients from All over the world</p>
            <p>100+ Recipes</p>
            <p>400+ Review</p>
        </div>

        <div>
            <div class="divi3">
            <h2>Popular recipe collections...</h2>
            </div>
        <div class="recipe-collections">
        <div>
            <img src="https://images.immediate.co.uk/production/volatile/sites/30/2020/08/sausage-ragu-ccde614.jpg?webp=true&quality=90&resize=400%2C363" alt="">
            <p>Sausage pasta recipes</p>
        </div>
        <div>
            <img src="https://images.immediate.co.uk/production/volatile/sites/30/2013/05/BBCGFO-FamilyMealPlan-FalafelLunchBox02856preview-f45ba7f.jpg?webp=true&quality=90&resize=620%2C563" alt="">
            <p>Lunchbox recipes</p>
        </div>
        <div>
            <img src="https://images.immediate.co.uk/production/volatile/sites/30/2021/11/Chicken-thigh-recipes-f2e4c0a.jpg?webp=true&quality=90&resize=620%2C563" alt="">
            <p>Chicken thigh recipes</p>
        </div>
        <div>
            <img src="https://images.immediate.co.uk/production/volatile/sites/30/2020/08/prawn_fried_rice-2481925.jpg?webp=true&quality=90&resize=440%2C400" alt="">
            <p>Quick and healthy recipes</p>
        </div>
        </div>
        </div>
        <div>
            <div class="divi4">
                <h2>What's New...</h2>
            </div>
            <div class="recipe-grid">
            <div class="recipe-item">
                <img src="https://www.allrecipes.com/thmb/M22pX1hGvUT6v6F62ybWVc3dA1Q=/364x242/filters:no_upscale():max_bytes(150000):strip_icc():focal(1999x0:2001x2):format(webp)/16330-Stuffed-Peppers-mfs-STEP-024-812c58e78eb5489789d1d1c6dfd661ff.jpg" alt="">
                <h3>Stuffed Peppers</h3>
            </div>
            <div class="recipe-item">
                <img src="https://www.allrecipes.com/thmb/ETpwldL2BqMGcBnGzLuqrh7xaiE=/364x242/filters:no_upscale():max_bytes(150000):strip_icc():focal(499x0:501x2):format(webp)/872665-old-school-mac-n-cheese-RainbowJewels-4x3-1-980f2f32734744289c8956256206035e.jpg" alt="">
                <h3>Old School Mac n' Cheese</h3>
            </div>
            <div class="recipe-item">
                <img src="https://www.allrecipes.com/thmb/H4siKAKhE-iBtkGEuhDvLEq13tA=/364x242/filters:no_upscale():max_bytes(150000):strip_icc():focal(479x0:481x2):format(webp)/Chicken-Enchiladas-739fd129b4f3439293859ba87f263162.jpg" alt="">
                <h3>Chicken Enchiladas</h3>
            </div>
            <div class="recipe-item">
                <img src="https://www.allrecipes.com/thmb/VV_vtUy_KrNpl0M1fjTIRNEcTz0=/364x242/filters:no_upscale():max_bytes(150000):strip_icc():focal(440x517:442x519):format(webp)/3563526chef-johns-meatball-inspired-meatloaf-Chef-John-1x1-1-4444adef5cef4d0ea395f9f445bf1682.jpg" alt="">
                <h3>Chef John's Meatball-Inspired Meatloaf</h3>
            </div>
            <div class="recipe-item">
                <img src="https://www.allrecipes.com/thmb/J2GVbv_Gt2F-Je5RUGRvTNWh8r8=/364x242/filters:no_upscale():max_bytes(150000):strip_icc():focal(1613x0:1615x2):format(webp)/5336800-f8bab4e4e6af4c8aba74c196d374840a.jpg" alt="">
                <h3>Stir-Fried Ginger Broccoli Beef</h3>
            </div>
           
            <div class="recipe-item">
                <img src="https://www.allrecipes.com/thmb/RXPUcWciXgp7BILZ7GKl5iNNPkM=/364x242/filters:no_upscale():max_bytes(150000):strip_icc():focal(999x0:1001x2):format(webp)/275576-easy-air-fryer-pork-chops-DDMFS-4x3-b2d7316498cd4d25901f403958754d31.jpg" alt="">
                <h3>Easy Air Fryer Pork Chops</h3>
            </div>
             </div>
        </div>
        <!-- <div class="divi5">
            <img src="https://images.immediate.co.uk/production/volatile/sites/30/2023/09/0509-easy-familly-1502425.jpg?quality=90&resize=960,408" alt="">
        </div> -->
         
         <div class="late-summer-specialties">
               <div class="divi4">
                <h2>Late Summer Specialties ...</h2>
               </div>
            <div class="recipe-grid">
            <div class="recipe-item">
                <img src="https://www.allrecipes.com/thmb/-MgmPdKzHg5ipp4NVsQRiZ0AgkE=/248x165/filters:no_upscale():max_bytes(150000):strip_icc():focal(1259x477:1261x479):format(webp)/8963090_BakedEggplantParmesan4x3-f56f527b2f054d7082dad9def9d4fb10.jpg" alt="">
                <h3>18 Italian Eggplant Recipes You'll Love</h3>
            </div>
            <div class="recipe-item">
                <img src="https://www.allrecipes.com/thmb/wppvs_x4ZbZ3tjHpApVk3TCvu2k=/248x165/filters:no_upscale():max_bytes(150000):strip_icc():focal(999x0:1001x2):format(webp)/plum-pork-bf62a0bb41244e4596fd42c9cf557691.jpeg" alt="">
                <h3>20 Top Recipes for That Middle Ground Between <br> Summer and Fall</h3>
            </div>
            <div class="recipe-item">
                <img src="https://www.allrecipes.com/thmb/fXF9wLnLRnvVIfgrJo-R1PGDNkU=/248x165/filters:no_upscale():max_bytes(150000):strip_icc():focal(999x0:1001x2):format(webp)/275368-fig-ricotta-cake-lutzflcat-2000-5d6c03096f8040fbb0b47bba18ec5244.jpg" alt="">
                <h3>22 Fresh Fig Recipes</h3>
            </div>
            <div class="recipe-item">
                <img src="https://www.allrecipes.com/thmb/-MQU33vKawuuyhrwN4Y1oNSVA5k=/248x165/filters:no_upscale():max_bytes(150000):strip_icc():focal(324x0:326x2):format(webp)/458727-Plum-Blueberry-Upside-Down-Cake-Photo-by-CCloves2bake-650x465-242b2e351b33431aa817ad79bcca966e.jpg" alt="">
                <h3>14 Perfect Plum, Peach, and Pear Desserts for Late <br> Summer</h3>
            </div>
            <div class="recipe-item">
                <img src="https://www.allrecipes.com/thmb/LBu-C4nvldae1zKxfVw3SKUlF7w=/248x165/filters:no_upscale():max_bytes(150000):strip_icc():focal(324x0:326x2):format(webp)/5679204-726909414f514e24aa4d4f613db75f1a.jpg" alt="">
                <h3>These 17 Recipes Will Hook You on Hatch Chiles</h3>
            </div>
           
            <div class="recipe-item">
                <img src="https://www.allrecipes.com/thmb/IWMObg8eclzrVgz4SHt0BLJBFi0=/248x165/filters:no_upscale():max_bytes(150000):strip_icc():focal(299x0:301x2):format(webp)/4508324_little-lamb-meatballs-in-a-spicy-eggplant-tomato-sauce_chef-john-c95de4e135714da393c59a94837f2661.jpg" alt="">
                <h3>10 Top-Rated Main Dish Eggplant Dinners</h3>
            </div>
             </div>
        </div>


        <footer>
            <div class="footer-container">

                 <div class="footer-logo">
                   <img src="https://www.allrecipes.com/thmb/654t4XHoQIwmjRLxb1jkXyA7xOY=/300x150/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/ar_magazine-457b736e5ed6442ea95b29d69489d496.png" alt="">
                 </div>
            
            <div>
                <p>DINNERS</p>
                <p>MEALS</p>  
                <p>INGREDIENTS</p>
                <p>OCCASIONS</p>
                <p>CUISINES</p>
                <p>KITCHEN TIPS</p>
                <p>NEWS</p>
                <p>FEATURES</p>
            </div>
            <div>
               <p>About Us</p>
               <p>Editorial Process</p>
               <p>Anti-Racism Pledge</p>
               <p>Privacy Policy</p>
               <p>Product Vetting</p>
            </div>
            <div>
               <p>Terms of Service</p>
               <p>Advertise</p>
               <p>Careers</p>
               <p>Contact</p>
            </div>
            </div>
        </footer>
    </div>
</template>

<script>
import NavbarPage from './NavbarPage.vue'

export default {

  data() {
    return {
      images: [
        "https://www.dineout.co.in/blog/wp-content/uploads/2020/09/Blog-banner-01.jpg",
        "https://previews.123rf.com/images/unitonevector/unitonevector1909/unitonevector190900288/129490277-banner-is-written-natural-oatmeal-new-recipe-diet-food-no-soy-calcium-rich-lover-sodium-lactose.jpg",
        "https://d3jmn01ri1fzgl.cloudfront.net/photoadking/webp_thumbnail/6066ff8eeffaa_template_image_1617362830.webp",
        "https://d3jmn01ri1fzgl.cloudfront.net/photoadking/webp_thumbnail/6067021110aab_json_image_1617363473.webp",
        
      ],
      currentImageIndex: 0,
      intervalId: null,
      intervalDuration: 3000, // 5 seconds
    };
  },
  computed: {
    currentImage() {
         console.log(`Current Image Index: ${this.currentImageIndex}`);
    console.log(`Current Image URL: ${this.images[this.currentImageIndex]}`);
      return this.images[this.currentImageIndex];
    },
  },
   created() {
    // Delay the start of the image carousel to ensure the Vue instance is ready
    setTimeout(this.startImageCarousel, 0);
  },
  onBeforeUnmount() {
    // Clear the interval to prevent memory leaks
    clearInterval(this.intervalId);
  },
  methods: {
    startImageCarousel() {
      this.intervalId = setInterval(() => {
        // Increment the current image index, loop back to the first image if at the end
        this.currentImageIndex = (this.currentImageIndex + 1) % this.images.length;
      }, this.intervalDuration);
    },
  },  
   components: {
    NavbarPage,
  },
}
</script>


<style scoped>
#banner img{
    width: 100%;
    box-sizing: border-box;
    margin-bottom: 10px;
    height: 500px;
}
#banner{
  margin-top: 0px;
  margin-bottom: 0px;
}

.divi2{
    display: flex;
    border-radius: 15px;
    background-color: #3498db;
    color: aliceblue;
    padding-left: 70px;
    margin-bottom: 40px;
}

.divi2 :nth-child(1){
    margin-right: 60px;
    font-size: 30px;
}

.divi2 :nth-child(2){
    margin-right: 40px;
    font-size: 30px;
}

.divi2 :nth-child(3){
    font-size: 30px;
}

.recipe-collections {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  width: 70%;
  margin: auto;
  margin-bottom: 80px;
}

.recipe-collections > div {
  flex: 1;
  text-align: center;
}

.divi3{
    width: 70%;
    display: flex;
    margin: auto;
}

.recipe-collections img {
  max-width: 100%;
  height: auto;
}

.recipe-collections p {
  font-weight: bold;
}

.recipe-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  width: 75%;
  margin: auto;
  margin-bottom: 80px;
}

.recipe-item {
  text-align: center;
}

.recipe-item img {
  max-width: 100%;
  height: auto;
}
.divi4{
    width: 70%;
    display: flex;
    margin: auto;
}

.recipe-item h3 {
  margin: 0;
  padding: 10px;
  font-weight: bold;
}

.divi5{
    width: 100%;
    margin-bottom: 100px;
}

.late-summer-specialties {
  margin-top: 20px;
  text-align: center;
}

.card-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.card {
  flex: 0 0 calc(33.33% - 20px); /* 3 cards per row with some spacing */
  margin-bottom: 20px;
  background-color: #f9f9f9;
  padding: 10px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.card img {
  max-width: 100%;
  height: auto;
}

.card h3 {
  margin-top: 10px;
}

.footer-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  color: #fff;
  padding: 20px;
}

.footer-links {
  display: flex;
  flex-direction: column;
}

.footer-links p {
  margin: 5px 0;
}

.footer-logo img {
  max-width: 100%;
  height: auto;
}

</style>



