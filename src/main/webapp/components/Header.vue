<template>
  <div class="header">

      <div class="logo">
        <router-link to="/">
          <img src="logo.png" alt="logo-bel3raby" />
        </router-link>
      </div>

      <slot></slot>

      <div class="links">
        <router-link to="/">الرئيسية</router-link>
        <a href="http://corona.bel3raby.net/ar/vaccinecure" target="_blank">اللقاح</a>
        <a href="http://corona.bel3raby.net/ar/covid-faqs/" target="_blank">س و ج</a>
        <a href="https://covid.bel3raby.net/blog/" target="_blank">أخبار</a>
        <router-link to="about">من نحن</router-link>
      </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>

.header {
  position: fixed;
  top: 0;
  width: 100vw;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  font-size: 1rem;
  background: #202124;
  color: #fff;
  z-index: 99999999;
}

.logo {
  font-family: "Cairo", sans-serif;
  color: #fdab3c;
  font-size: 1.5rem;
}

.logo img {
  width: 8rem;
  display: inline-block;
}

.links a {
  margin: 0 1rem;
  transition: color 0.3s;
}

.links a:hover {
  color: #fdab3c;
  border-bottom: 2px solid #fdab3c;
}

.links a.nuxt-link-exact-active {
  color: #fdab3c;
  border-bottom: 2px solid #fdab3c;
}

a {
  text-decoration: none;
  color: #fff;
}


@media only screen and (max-width: 1200px) {

  .header {
    width: 100vw;
  }

}

@media only screen and (max-width: 800px) {

  .links a {
    margin: 0 3px;
  }
}


</style>