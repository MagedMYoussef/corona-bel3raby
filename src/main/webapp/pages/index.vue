<template>
  <div class="container">

    <div class="header">
      <div class="logo">
        <a href="http://bel3raby.net" target="_blank">
          <img src="bel3raby-icon.png" alt="logo-bel3raby">
        </a>
        كورونا بالعربي
      </div>
      <div class="links">
        <a href="#">أخبار</a>
        <a href="#">شائعات</a>
        <a href="#">مصادر</a>
        <a href="#">أبحاث</a>
      </div>
    </div>

    <div class="main">

      <div class="country-filter">
        <a @click="fillData()" href="#" class="active">العالم</a>
        <a @click="fillData()" href="#">مصر</a>
        <a @click="fillData()" href="#">أفريقيا</a>
        <a @click="fillData()" href="#">الدول العربية</a>
      </div>

      <div class="card">
        <div class="card-title">
          معدل الحالات
        </div>
        <div class="card-content">
            <chart class="chart" :chart-data="datacollection" :options="options"></chart>
        </div>
      </div>

      <div class="card">
        <div class="card-title">
          معدل الوفيات
        </div>
        <div class="card-content">
            <chart class="chart" :chart-data="datacollection" :options="options"></chart>
        </div>
      </div>

      <div class="row">
              <div class="card">
        <div class="card-title">
          معدل الحالات
        </div>
        <div class="card-content">
            <chart class="chart" :chart-data="datacollection" :options="options"></chart>
        </div>
      </div>

      <div class="card">
        <div class="card-title">
          معدل الوفيات
        </div>
        <div class="card-content">
            <chart class="chart" :chart-data="datacollection" :options="options"></chart>
        </div>
      </div>
       <div class="card">
        <div class="card-title">
          معدل الوفيات
        </div>
        <div class="card-content">
            <chart class="chart" :chart-data="datacollection" :options="options"></chart>
        </div>
      </div>
      </div>

        <div class="card">
        <div class="card-title">
          احصائيات الدول
        </div>
        <div class="card-content">
            <Grid></Grid>
        </div>
      </div>
    </div>

    <div class="sidebar">
      Hello
    </div>

  </div>
</template>

<script>
import Logo from '~/components/Logo.vue'
import Chart from '~/components/Chart.vue'
import Grid from '~/components/Grid.vue'

export default {
  components: {
    Logo,
    Chart,
    Grid
  },
  data () {
    return {
      datacollection: null,
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  mounted () {
    this.fillData()
  },
  methods: {
    fillData () {
      console.log('fillData');
      this.datacollection = {
        labels: [this.getRandomInt(), this.getRandomInt()],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [this.getRandomInt(), this.getRandomInt()]
          }, {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [this.getRandomInt(), this.getRandomInt()]
          }
        ]
      }
    },
    getRandomInt () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    }
  }

}
</script>

<style c>

@import url('https://fonts.googleapis.com/css?family=Almarai|El+Messiri|Tajawal&display=swap');

.container {
  font-family: 'El Messiri', sans-serif;
  min-height: 100vh;
  min-width: 100vw;
  display: flex;
  text-align: center;
  background: #202124;
  color: #fff;
  position: absolute;
  direction: rtl;
}

.header {
    position: fixed;
    top: 0;
    width: 80vw;
    display: flex;
    justify-content: space-between;
    padding: 1rem;
    font-size: 1rem;
    background: #202124;
    z-index: 999999;
}

.logo {
  color: #FFC023;
  font-size: 1.5rem;
}

.logo img {
  width: 3rem;
  display: inline-block;
}

.links {
  margin-top: 1rem;
}

.links a {
  margin: 0 1rem;
  transition: color 0.3s;
}

.links a:hover {
  color: #FFC023;
  border-bottom: 2px solid #FFC023;
}

.sidebar {
  background: #2B2E37;
  width: 20vw;
  z-index: 9999;
}

.main {
  padding-top: 6rem;
  width: 80vw;
}

.country-filter {
  margin-bottom: 2rem;
}

.country-filter a {
  color: #FFC023;
  padding: 0.7rem 1.5rem;
  border-radius: 18px;
  font-size: 1rem;
  transition: background 0.3s;
}

.country-filter a.active {
  background: #FFC023;
  color: #202124;
  font-weight: 700;
}

.country-filter a:hover {
  background: #FFC023;
  color: #202124;
  font-weight: 700;
}

.card {
  margin: 1em;
  border: 1px solid #909090;
  border-radius: 10px;
  text-align: right;
}

.card-title {
  position: relative;
  top: -10px;
  background: #202124;
  display: inline-block;
  padding: 0 1rem;
  right: 1rem;
}

.chart {
  position: relative;
  max-height: 15rem;
  margin: 10px;
}

.row {
  display: flex;
  justify-content: space-between;
}

.row div {
  flex: 1;
}

</style>
