<template>
  <div class="container">

    <div class="header">
      <div class="logo">
        <a href="http://bel3raby.net" target="_blank">
          <img src="bel3raby-icon.png" alt="logo-bel3raby" />
        </a>
        كورونا بالعربي
      </div>

      <div class="country-filter">
        <a @click="fillData()" href="#" class="active">العالم</a>
        <a @click="fillData()" href="#">مصر</a>
        <a @click="fillData()" href="#">أفريقيا</a>
        <a @click="fillData()" href="#">الدول العربية</a>
      </div>

      <div class="links">
        <a href="#">أخبار</a>
        <a href="#">شائعات</a>
        <a href="#">مصادر</a>
        <a href="#">أبحاث</a>
      </div>
    </div>

    <div class="main">
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
      </div>

      <div class="row">

        <div>
          <div class="card">
            <div class="card-title">
              أكثر الدول في الحالات
            </div>
            <div class="card-content">
              <chart class="chart" :chart-data="datacollection" :options="options"></chart>
            </div>
          </div>

          <div class="card">
            <div class="card-title">
              أكثر الدول في الوفيات
            </div>
            <div class="card-content">
              <chart class="chart" :chart-data="datacollection" :options="options"></chart>
            </div>
          </div>
        </div>

        <div class="card table">
          <div class="card-title">
            احصائيات الدول
          </div>
          <div class="card-content">
            <Grid :data="countriesData"></Grid>
          </div>
        </div>
      </div>

    </div>

    <div class="sidebar" v-if="stats">

      <div class="card-2">
        <div class="card-2-content">
          <h1>
            اجمالي الحالات <br />
            <span style="color: #03a9f4;">{{ stats.total_confirmed.worldwide }}</span>
          </h1>
          <table>
            <tr>
              <th>مصر</th>
              <th>أفريقيا</th>
              <th>العرب</th>
            </tr>
            <tr>
              <td>{{ stats.total_confirmed.egypt }}</td>
              <td>{{ stats.total_confirmed.africa }}</td>
              <td>{{ stats.total_confirmed.arab }}</td>
            </tr>
          </table>
        </div>
      </div>

      <div class="card-2">
        <div class="card-2-content">
          <h1>
            اجمالي المتعافين <br />
            <span style="color: #42d885;">{{ stats.total_recovered.worldwide }}</span>
          </h1>
          <table>
            <tr>
              <th>مصر</th>
              <th>أفريقيا</th>
              <th>العرب</th>
            </tr>
            <tr>
              <td>{{ stats.total_recovered.egypt }}</td>
              <td>{{ stats.total_recovered.africa }}</td>
              <td>{{ stats.total_recovered.arab }}</td>
            </tr>
          </table>
        </div>
      </div>

      <div class="card-2">
        <div class="card-2-content">
          <h1>
            اجمالي الوفيات <br />
            <span style="color: #ff5b93;">{{ stats.total_deaths.worldwide }}</span>
          </h1>
          <table>
            <tr>
              <th>مصر</th>
              <th>أفريقيا</th>
              <th>العرب</th>
            </tr>
            <tr>
              <td>{{ stats.total_deaths.egypt }}</td>
              <td>{{ stats.total_deaths.africa }}</td>
              <td>{{ stats.total_deaths.arab }}</td>
            </tr>
          </table>
        </div>
      </div>

      <div class="card-2">
        <div class="card-2-content">
          <h1>
            الحالات الجديدة <br />
            <span style="color: #ff5b93;">{{ stats.new_confirmed.worldwide }}</span>
          </h1>
          <table>
            <tr>
              <th>مصر</th>
              <th>أفريقيا</th>
              <th>العرب</th>
            </tr>
            <tr>
              <td>{{ stats.new_confirmed.egypt }}</td>
              <td>{{ stats.new_confirmed.africa }}</td>
              <td>{{ stats.new_confirmed.arab }}</td>
            </tr>
          </table>
        </div>
      </div>

      <div class="card-2">
        <div class="card-2-content">
          <h1>
            الوفيات الجديدة <br />
            <span style="color: #ff5b93;">{{ stats.new_deaths.worldwide }}</span>
          </h1>
          <table>
            <tr>
              <th>مصر</th>
              <th>أفريقيا</th>
              <th>العرب</th>
            </tr>
            <tr>
              <td>{{ stats.new_deaths.egypt }}</td>
              <td>{{ stats.new_deaths.africa }}</td>
              <td>{{ stats.new_deaths.arab }}</td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import Chart from "~/components/Chart.vue";
import Grid from "~/components/Grid.vue";

export default {
  components: {
    Chart,
    Grid
  },
  data() {
    return {
      stats: null,
      countriesData: null,
      newsbarData: null,
      datacollection: null,
      options: {
        responsive: true,
        maintainAspectRatio: false,
        tooltips: {
          mode: "label",
          intersect: false
        },
        scales: {
          xAxes: [
            {
              display: true,
              gridLines: {
                display: true,
                color: "#58585860"
              }
            }
          ],
          yAxes: [
            {
              display: true,
              gridLines: {
                display: true,
                color: "#58585860"
              }
            }
          ]
        }
      }
    };
  },
  mounted() {
    this.fillData();
    this.getData();
  },
  methods: {
    getData() {
      axios.get("/api/stats/").then(res => {
        console.log("statssss", res);
        this.stats = res.data;
      });

      axios.get("/api/reports/latest/").then(res => {
        console.log("report latest", res);
        this.countriesData = res.data;

        // TODO: Replace it with new_confirmed
        this.newsbarData = "";
        res.data
          .sort((a, b) => b.total_confirmed - a.total_confirmed)
          .slice(0, 25)
          .forEach(e => {
            this.newsbarData += `<div class="ticker__item">${e.emoji} ${e.country_arabic} ${e.total_confirmed} (+${e.new_confirmed})</div>`;
          });
        console.log('newsbar', this.newsbarData)
      });

    },
    fillData() {
      console.log("fillData");
      this.datacollection = {
        labels: [
          this.getRandomInt(),
          this.getRandomInt(),
          this.getRandomInt(),
          this.getRandomInt()
        ],
        datasets: [
          {
            label: "Data One",
            borderColor: "#1e88e5",
            fill: false,
            pointBorderColor: "#1e88e5",
            pointBackgroundColor: "#1e88e5",
            data: [
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt()
            ]
          },
          {
            label: "Data Two",
            borderColor: "#ffc107",
            fill: false,
            pointBorderColor: "#ffc107",
            pointBackgroundColor: "#ffc107",
            data: [
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt()
            ]
          },
          {
            label: "Data Three",
            borderColor: "#db4437",
            fill: false,
            pointBorderColor: "#db4437",
            pointBackgroundColor: "#db4437",
            data: [
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt()
            ]
          }
        ]
      };
    },
    getRandomInt() {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5;
    }
  }
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Almarai|El+Messiri|Cairo|Tajawal&display=swap");

::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px #202124;
  background-color: #202124;
}

::-webkit-scrollbar {
  width: 6px;
  background-color: #202124;
}

::-webkit-scrollbar-thumb {
  background-color: #505258;
}

.container {
  font-family: "El Messiri", sans-serif;
  min-height: 100vh;
  min-width: 100vw;
  display: flex;
  text-align: center;
  background: #202124;
  color: #fff;
  position: absolute;
  direction: rtl;
  overflow-x: hidden;
}

.header {
  position: fixed;
  top: 0;
  width: 80vw;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  font-size: 1rem;
  background: #202124;
  z-index: 999999;
}

.logo {
  font-family: "Cairo", sans-serif;
  color: #ffc023;
  font-size: 1.5rem;
}

.logo img {
  width: 3rem;
  display: inline-block;
}

.links a {
  margin: 0 1rem;
  transition: color 0.3s;
}

.links a:hover {
  color: #ffc023;
  border-bottom: 2px solid #ffc023;
}

.sidebar {
  background: #2b2e37;
  width: 20vw;
  height: 100vh;
  z-index: 9999999;
  position: fixed;
  left: 0;
  overflow-y: auto;
}

.main {
  padding-top: 6rem;
  width: 80vw;
  height: 100vh;
  overflow-y: scroll;
  overflow-x: hidden;
  direction: ltr;
}

.country-filter a {
  color: #ffc023;
  padding: 0.7rem 1.5rem;
  border-radius: 18px;
  font-size: 1rem;
  transition: background 0.3s;
}

.country-filter a.active {
  background: #ffc023;
  color: #202124;
  font-weight: 700;
}

.country-filter a:hover {
  background: #ffc023;
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
  max-height: 13.5rem;
  margin: 10px;
}

.row {
  display: flex;
  justify-content: space-between;
}

.row div.card {
  flex: 1;
}

.row div.card.table {
  flex: 2;
}

.card-2-title {
  position: relative;
  display: inline-block;
  font-size: 1.5rem;
}

.card-2-content {
  margin: 1rem;
  border-radius: 10px;
  text-align: center;
  background: #22242d;
  padding: 0.5rem 0;
}

table {
  background: #13151b;
  width: 80%;
  border-radius: 6px;
  margin: 1rem auto;

  th {
    color: #ffc023;
    padding: 0.5rem;
  }
  td {
    color: rgb(131, 131, 131);
  }
}

h1 {
  font-size: 1.5rem;
  color: #9eabd4;

  span {
    font-size: 2rem;
  }
}
</style>
