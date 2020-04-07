<template>
  <div class="header">

      <div class="logo">
        <router-link to="/">
          <img src="logo.png" alt="logo-bel3raby" />
        </router-link>
      </div>

      <slot></slot>

      <div class="links">
        <a href="http://corona.bel3raby.net/ar/vaccinecure" target="_blank">اللقاح</a>
        <a href="http://corona.bel3raby.net/ar/covid-faqs/" target="_blank">س و ج</a>
        <a href="http://corona.bel3raby.net/ar/blog/" target="_blank">أخبار</a>
        <router-link to="about">من نحن</router-link>
      </div>
    </div>
</template>

<script>

const description = `كورونا بالعربي - متابعة حية لآخر إحصائيات فيروس كوفيد-19`;
const title = `كورونا بالعربي`;


export default {
  head() {
    return {
      title: title,
      meta: [
        {
          name: 'description',
          hid: 'description',
          content: description
        },
        // Open Graph
        {
          hid: 'og:description',
          property: 'og:description',
          content: description
        },
        {
          hid: 'og:title',
          property: 'og:title',
          content: title
        },
        {
          hid: 'og:site_name',
          property: 'og:site_name',
          content: 'بالعربي.نت'
        },
        { name: 'og:type', content: 'website' },
        { name: 'og:url', content: 'http://bel3raby.net/' },
        { name: 'og:image', content: 'http://corona.bel3raby.net/ar/wp-content/uploads/2020/03/Featured-image-02-1.png' },
        { name: 'og:image:alt', content: 'بالعربي.نت' },

        // Twitter Card
        { name: 'twitter:card', content: 'summary' },
        { name: 'twitter:site', content: 'بالعربي.نت' },
        {
          name: 'twitter:title',
          content: title
        },
        {
          name: 'twitter:description',
          content: description
        },
        { name: 'twitter:image', content: 'http://corona.bel3raby.net/ar/wp-content/uploads/2020/03/Featured-image-02-1.png' },
        { name: 'twitter:image:alt', content: 'بالعربي.نت' }
      ]
    };
  },
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

  .logo img {
    width: 6rem;
    display: inline-block;
  }


  html {
    font-size: 14px;
  }

}


</style>