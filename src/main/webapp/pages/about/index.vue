<template>
  <div class="bg container">

    <Header>
    </Header>

    <div class="content">
      <div>

        <div class="hero-image">
          <img src="http://2.gravatar.com/avatar/b60ade6a237cea8aed96af18333438ef?s=256" alt="Maged M Youssef profile picture">
        </div>
        <div class="hero-headline">
          <p class="name">Maged Youssef</p>
          <p class="description">👨‍💻 <span class="yellow">Software</span> Engineer @ <span class="blue">Mentor - Siemens</span><br /> ✅ Co-Founder of <span class="blue">bel3raby.net</span> 🎉 Founder of <span class="blue">scriple.io</span>
          </p>
        </div>
        <div class="social-btns" :class="externalStyles">
          <a href="https://twitter.com/MagedMYoussef" class="btn twitter" target="_blank">
            <img src="~assets/images/twitter-icon.svg" class="fa fa-twitter social-icon" alt="">
          </a>

          <a href="https://www.linkedin.com/in/magedmyoussef/" class="btn linkedin" target="_blank">
            <img src="~assets/images/linkedin-icon.svg" class="fa fa-linkedin social-icon" alt="">
          </a>

          <a href="https://www.facebook.com/magedmagdy07" class="btn facebook" target="_blank">
            <img src="~assets/images/facebook-icon.svg" class="fa fa-facebook social-icon" alt="">
          </a>
        </div>
      </div>

      <div>

        <div class="hero-image">
          <img src="http://0.gravatar.com/avatar/0df1e7b6269c0e5f052288b9171ddda0?s=256&d=mm&r=g" alt="Maged M Youssef profile picture">
        </div>
        <div class="hero-headline">
          <p class="name">Fady Dawood</p>
          <p class="description">👨‍💻 <span class="yellow">Software</span> Engineer @ <span class="blue">Mentor - Siemens</span><br /> ✅ Co-Founder of <span class="blue">bel3raby.net</span> 🎉 Founder of <span class="blue">scriple.io</span>
          </p>
        </div>
        <div class="social-btns" :class="externalStyles">
          <a href="https://twitter.com/MagedMYoussef" class="btn twitter" target="_blank">
            <img src="~assets/images/twitter-icon.svg" class="fa fa-twitter social-icon" alt="">
          </a>

          <a href="https://www.linkedin.com/in/magedmyoussef/" class="btn linkedin" target="_blank">
            <img src="~assets/images/linkedin-icon.svg" class="fa fa-linkedin social-icon" alt="">
          </a>

          <a href="https://www.facebook.com/magedmagdy07" class="btn facebook" target="_blank">
            <img src="~assets/images/facebook-icon.svg" class="fa fa-facebook social-icon" alt="">
          </a>
        </div>
      </div>

 <div>

        <div class="hero-image">
          <img src="https://scontent-hbe1-1.xx.fbcdn.net/v/t1.0-9/67811253_2525875867435506_7960829231548596224_o.jpg?_nc_cat=102&_nc_sid=09cbfe&_nc_oc=AQn8qFS_syoN1JUTVsMB7gIVso_zV0SESynxX6DdvTJ7zz0CHFfhxkfpb_qzAcqYgSY&_nc_ht=scontent-hbe1-1.xx&oh=a9f74bd8a2c343c31d4998247402127f&oe=5EB05DF0" alt="Maged M Youssef profile picture">
        </div>
        <div class="hero-headline">
          <p class="name">Fady Khalaf</p>
          <p class="description">👨‍💻 <span class="yellow">Software</span> Engineer @ <span class="blue">Mentor - Siemens</span>
          </p>
        </div>
        <div class="social-btns" :class="externalStyles">
          <a href="https://twitter.com/MagedMYoussef" class="btn twitter" target="_blank">
            <img src="~assets/images/twitter-icon.svg" class="fa fa-twitter social-icon" alt="">
          </a>

          <a href="https://www.linkedin.com/in/magedmyoussef/" class="btn linkedin" target="_blank">
            <img src="~assets/images/linkedin-icon.svg" class="fa fa-linkedin social-icon" alt="">
          </a>

          <a href="https://www.facebook.com/magedmagdy07" class="btn facebook" target="_blank">
            <img src="~assets/images/facebook-icon.svg" class="fa fa-facebook social-icon" alt="">
          </a>
        </div>
      </div>
    </div>
    <div class="stars">
      <div class="objects">
        <img src="~assets/images/rocket.svg" alt="" class="object_rocket" width="40px">
        <div class="earth-moon">
          <img src="~assets/images/earth.svg" alt="" class="object_earth" width="100px">
          <img src="~assets/images/moon.svg" alt="" class="object_moon" width="80px">
        </div>
        <div class="box_astronaut">
          <img src="~assets/images/astronaut.svg" alt="" class="object_astronaut" width="140px">

        </div>
      </div>
      <div class="glowing_stars">
        <div class="star"></div>
        <div class="star"></div>
        <div class="star"></div>
        <div class="star"></div>
        <div class="star"></div>
      </div>
    </div>
  </div>

</template>

<script>
import Header from "~/components/Header.vue";

export default {
    components: {
        Header
    }
};
</script>

<style>
/* Reset */

::selection {
  background: #ffd618; /* WebKit/Blink Browsers */
  color: #131313;
}
::-moz-selection {
  background: #ffd618; /* Gecko Browsers */
  color: #131313;
}


/* Animations */
@-moz-keyframes rocket-movement {
  100% {
    -moz-transform: translate(1200px, -600px);
  }
}
@-webkit-keyframes rocket-movement {
  100% {
    -webkit-transform: translate(1200px, -600px);
  }
}
@keyframes rocket-movement {
  100% {
    transform: translate(1200px, -600px);
  }
}
@-moz-keyframes spin-earth {
  100% {
    -moz-transform: rotate(-360deg);
    transition: transform 20s;
  }
}
@-webkit-keyframes spin-earth {
  100% {
    -webkit-transform: rotate(-360deg);
    transition: transform 20s;
  }
}
@keyframes spin-earth {
  100% {
    -webkit-transform: rotate(-360deg);
    transform: rotate(-360deg);
    transition: transform 20s;
  }
}

@-moz-keyframes move-astronaut {
  100% {
    -moz-transform: translate(-160px, -160px);
  }
}
@-webkit-keyframes move-astronaut {
  100% {
    -webkit-transform: translate(-160px, -160px);
  }
}
@keyframes move-astronaut {
  100% {
    -webkit-transform: translate(-160px, -160px);
    transform: translate(-160px, -160px);
  }
}
@-moz-keyframes rotate-astronaut {
  100% {
    -moz-transform: rotate(-720deg);
  }
}
@-webkit-keyframes rotate-astronaut {
  100% {
    -webkit-transform: rotate(-720deg);
  }
}
@keyframes rotate-astronaut {
  100% {
    -webkit-transform: rotate(-720deg);
    transform: rotate(-720deg);
  }
}

/* General animated styles */

.hero-headline {
  color: #fff;
}

.hero-headline .name {
  font-size: 3rem;
  margin-bottom: 1rem;
  font-weight: 400;
}

.hero-headline .description {
  z-index: 220 !important;
  font-size: 1.2rem;
  margin-bottom: 2rem;
  line-height: 2rem;
  font-weight: 400;
}

.blue {
  color: #0089ff;
  font-size: 16px;
}

.yellow {
  color: #eac510;
  font-weight: 700;
}

.hero-image img {
  width: 12rem;
  height: 12rem;
  margin-bottom: 2rem;
  border-radius: 20rem;
  border: 3px solid #c7c7c7;
}

.spin-earth-on-hover {
  transition: ease 200s !important;
  transform: rotate(-3600deg) !important;
}

.bg {
  background-repeat: repeat-x;
  background-size: cover;
  background-position: left top;
  background: #202124;
  background: linear-gradient(5deg, #0c0c0e 0%, #22242d 100%);
  height: 100vh;
  width: 100vw;
}

.btn-go-home {
  position: relative;
  z-index: 200;
  margin: 15px auto;
  width: 17rem;
  padding: 10px 15px;
  border-radius: 100px;
  font-weight: 400;
  display: block;
  background: #41415d;
  color: #ffffff;
  text-align: center;
  text-decoration: none;
  font-size: 16px;
  transition: all 0.3s ease-in;
}

.btn-go-home:hover {
  box-shadow: 0px 20px 20px rgba(0, 0, 0, 0.1);
}

.central-body {
  width: 100%;
  height: 100%;
  padding: 12% 5% 10% 5%;
  text-align: center;
}

.objects img {
  z-index: 90;
  pointer-events: none;
}

.object_rocket {
  z-index: 95;
  position: absolute;
  transform: translateX(-50px);
  top: 75%;
  pointer-events: none;
  animation: rocket-movement 200s linear infinite both running;
}

.object_earth {
  position: absolute;
  top: 10%;
  left: 8%;
  z-index: 90;
  animation: spin-earth 10s infinite linear both;
}

.object_moon {
  position: absolute;
  top: 12%;
  left: 25%;
}

.object_astronaut {
  animation: rotate-astronaut 200s infinite linear both alternate;
}

.box_astronaut {
  z-index: 110 !important;
  position: absolute;
  bottom: 0;
  right: 8%;
  will-change: transform;
  animation: move-astronaut 50s infinite linear both alternate;
}

.image-404 {
  position: relative;
  z-index: 100;
  pointer-events: none;
  display: block;
  margin: auto;
}

.stars {
  background: url(~assets/images/overlay_stars.svg);
  background-repeat: repeat;
  background-size: contain;
  background-position: left top;
}

.glowing_stars .star {
  position: absolute;
  border-radius: 100%;
  background-color: #fff;
  width: 3px;
  height: 3px;
  opacity: 0.3;
  will-change: opacity;
}

.glowing_stars .star:nth-child(1) {
  top: 80%;
  left: 25%;
  animation: glow-star 2s infinite ease-in-out alternate 1s;
}
.glowing_stars .star:nth-child(2) {
  top: 20%;
  left: 40%;
  animation: glow-star 2s infinite ease-in-out alternate 3s;
}
.glowing_stars .star:nth-child(3) {
  top: 25%;
  left: 25%;
  animation: glow-star 2s infinite ease-in-out alternate 5s;
}
.glowing_stars .star:nth-child(4) {
  top: 75%;
  left: 80%;
  animation: glow-star 2s infinite ease-in-out alternate 7s;
}
.glowing_stars .star:nth-child(5) {
  top: 90%;
  left: 50%;
  animation: glow-star 2s infinite ease-in-out alternate 9s;
}

@media only screen and (max-width: 600px) {
  .brand-logo img {
    width: 120px;
  }

  .box_astronaut {
    top: 70%;
  }

  .central-body {
    margin-top: 50%;
  }
}

/* Social styles */

.social-icon {
  width: 50%;
  height: 100%;
  margin: auto;
}

.social-btns .btn,
.social-btns .btn:before,
.social-btns .btn .fa {
  transition: all 0.35s;
  transition-timing-function: cubic-bezier(0.31, -0.105, 0.43, 1.59);
}
.social-btns .btn:before {
  top: 90%;
  left: -110%;
}
.social-btns .btn .fa {
  transform: scale(0.8);
}

.social-btns .btn:before {
  background: #d2d2d2;
}

.social-btns .btn:focus:before,
.social-btns .btn:hover:before {
  top: -10%;
  left: -10%;
}
.social-btns .btn:focus .fa,
.social-btns .btn:hover .fa {
  fill: #ffffff;
  transform: scale(1);
}
.social-btns {
  margin: auto;
  font-size: 0;
  text-align: center;
  z-index: 999;
}

.social-btns .btn {
  display: inline-block;
  background-color: #fff;
  width: 3rem;
  height: 3rem;
  line-height: 3rem;
  margin: 5px 10px;
  text-align: center;
  position: relative;
  overflow: hidden;
  border-radius: 28%;
  box-shadow: 0 5px 15px -5px rgba(0, 0, 0, 0.3);
  opacity: 0.99;
  outline: none;
}

.social-btns .btn:before {
  content: "";
  width: 120%;
  height: 120%;
  position: absolute;
  transform: rotate(45deg);
}

.content {
  text-align: center;
}

.content > div {
  text-align: center;
  display: inline-block;
  margin: 16rem 3rem;
}


.container {
  font-family: "Cairo", sans-serif;
  text-align: center;
  position: absolute;
  direction: rtl;
  overflow-x: hidden;
  background: #202124;
}

</style>