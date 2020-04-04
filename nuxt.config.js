
export default {
  srcDir: 'src/main/webapp',
  buildDir: 'build',
  mode: 'spa',
  router: {
    base: '/dashboard/'
  },
  /*
  ** Headers of the page
  */
  head: {
    title: 'كورونا بالعربي',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'كورونا بالعربي' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/dashboard/favicon.ico' },
      { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/ag-grid-community@23.0.0/dist/styles/ag-grid.min.css' },
      { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/ag-grid-community@23.0.0/dist/styles/ag-theme-balham-dark.min.css' }

    ],
    script: [
      { src: 'https://cdn.jsdelivr.net/npm/apexcharts' },
      { src: 'https://cdn.jsdelivr.net/npm/vue-apexcharts' },
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },
  /*
  ** Global CSS
  */
  css: [
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [

  ],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module',
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    '@nuxtjs/google-analytics',
  ],
  /*
  ** Axios module configuration
  ** See https://axios.nuxtjs.org/options
  */
  axios: {
    proxy: true
  },

  serverMiddleware: [
    '~/middleware/logger'
  ],

  /*
  ** Google analytics module configuration
  */
 googleAnalytics: {
    id: 'UA-86800492-5',
    debug: {
      sendHitTask: process.env.NODE_ENV !== 'development'
    }
  },
  // Proxy configuration
  proxy: {
    '/api': 'http://localhost:5000'
  },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
    }
  }
}
