<template>
  <div class="container">

    <!-- <NewsBar :news="newsbarData"></NewsBar> -->

    <div class="header">
      <div class="logo">
        <a href="http://bel3raby.net" target="_blank">
          <img src="logo.png" alt="logo-bel3raby" />
        </a>
      </div>

      <div class="country-filter">
        <a @click="switchArea('worldwide')" href="#" :class="area == 'worldwide' ? 'active' : ''">العالم</a>
        <a @click="switchArea('egypt')" href="#" :class="area == 'egypt' ? 'active' : ''">مصر</a>
        <a @click="switchArea('africa')" href="#" :class="area == 'africa' ? 'active' : ''">أفريقيا</a>
        <a @click="switchArea('arab')" href="#" :class="area == 'arab' ? 'active' : ''">الدول العربية</a>
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
            معدل الوفيات
          </div>
          <div class="card-content">
            <chart class="chart" :series="chartsData[area].total_deaths"></chart>
          </div>
        </div>
        <div class="card">
          <div class="card-title">
            معدل الحالات
          </div>
          <div class="card-content">
            <chart class="chart" :series="chartsData[area].total_confirmed"></chart>
          </div>
        </div>

      </div>

      <div class="row">
          <div class="card">
            <div class="card-title">
              الوفيات الجديدة
            </div>
            <div class="card-content">
              <chart class="chart" :series="chartsData[area].new_deaths"></chart>
            </div>
          </div>

          <div class="card">
            <div class="card-title">
              الحالات الجديدة
            </div>
            <div class="card-content">
              <chart class="chart" :series="chartsData[area].new_confirmed"></chart>
            </div>
          </div>

      </div>
      <div class="row">

        <div class="card table">
          <div class="card-title">
            احصائيات الدول
          </div>
          <div class="card-content">
            <Grid ref="grid" :data="countriesData"></Grid>
          </div>
        </div>
      </div>

    </div>

    <div class="sidebar" v-if="stats">

      <div class="card-2">
        <div class="card-2-content">
          <h1>
            اجمالي الاصابات <br />
            <span style="color: #03a9f4;">{{ stats.total_confirmed.worldwide.toLocaleString() }}</span>
          </h1>
          <table>
            <tr>
              <th>مصر</th>
              <th>أفريقيا</th>
              <th>العرب</th>
            </tr>
            <tr>
              <td>{{ stats.total_confirmed.egypt.toLocaleString() }}</td>
              <td>{{ stats.total_confirmed.africa.toLocaleString() }}</td>
              <td>{{ stats.total_confirmed.arab.toLocaleString() }}</td>
            </tr>
          </table>
        </div>
      </div>

      <div class="card-2">
        <div class="card-2-content">
          <h1>
            اجمالي المتعافين <br />
            <span style="color: #42d885;">{{ stats.total_recovered.worldwide.toLocaleString() }}</span>
          </h1>
          <table>
            <tr>
              <th>مصر</th>
              <th>أفريقيا</th>
              <th>العرب</th>
            </tr>
            <tr>
              <td>{{ stats.total_recovered.egypt.toLocaleString() }}</td>
              <td>{{ stats.total_recovered.africa.toLocaleString() }}</td>
              <td>{{ stats.total_recovered.arab.toLocaleString() }}</td>
            </tr>
          </table>
        </div>
      </div>

      <div class="card-2">
        <div class="card-2-content">
          <h1>
            اجمالي الوفيات <br />
            <span style="color: #ff5b93;">{{ stats.total_deaths.worldwide.toLocaleString() }}</span>
          </h1>
          <table>
            <tr>
              <th>مصر</th>
              <th>أفريقيا</th>
              <th>العرب</th>
            </tr>
            <tr>
              <td>{{ stats.total_deaths.egypt.toLocaleString() }}</td>
              <td>{{ stats.total_deaths.africa.toLocaleString() }}</td>
              <td>{{ stats.total_deaths.arab.toLocaleString() }}</td>
            </tr>
          </table>
        </div>
      </div>

      <div class="card-2">
        <div class="card-2-content">
          <h1>
            الاصابات الجديدة <br />
            <span style="color: #ff5b93;">{{ stats.new_confirmed.worldwide.toLocaleString() }}</span>
          </h1>
          <table>
            <tr>
              <th>مصر</th>
              <th>أفريقيا</th>
              <th>العرب</th>
            </tr>
            <tr>
              <td>{{ stats.new_confirmed.egypt.toLocaleString() }}</td>
              <td>{{ stats.new_confirmed.africa.toLocaleString() }}</td>
              <td>{{ stats.new_confirmed.arab.toLocaleString() }}</td>
            </tr>
          </table>
        </div>
      </div>

      <div class="card-2">
        <div class="card-2-content">
          <h1>
            الوفيات الجديدة <br />
            <span style="color: #ff5b93;">{{ stats.new_deaths.worldwide.toLocaleString() }}</span>
          </h1>
          <table>
            <tr>
              <th>مصر</th>
              <th>أفريقيا</th>
              <th>العرب</th>
            </tr>
            <tr>
              <td>{{ stats.new_deaths.egypt.toLocaleString() }}</td>
              <td>{{ stats.new_deaths.africa.toLocaleString() }}</td>
              <td>{{ stats.new_deaths.arab.toLocaleString() }}</td>
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
import NewsBar from "~/components/NewsBar.vue";

export default {
  components: {
    NewsBar,
    Chart,
    Grid
  },
  data() {
    return {
      stats: null,
      trends: null,
      area: 'worldwide',
      chartsData: {
        worldwide: { total_confirmed: null, total_deaths: null, total_recovered: null, total_active: null, new_confirmed: null, new_deaths: null, new_recovered: null },
        egypt: { total_confirmed: null, total_deaths: null, total_recovered: null, total_active: null, new_confirmed: null, new_deaths: null, new_recovered: null },
        africa: { total_confirmed: null, total_deaths: null, total_recovered: null, total_active: null, new_confirmed: null, new_deaths: null, new_recovered: null },
        arab: { total_confirmed: null, total_deaths: null, total_recovered: null, total_active: null, new_confirmed: null, new_deaths: null, new_recovered: null },
      },
      countriesData: null,
      latestReport: null,
      newsbarData: null,
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      axios.get("/api/stats/").then(res => {
        this.stats = res.data;
      });

      axios.get("/api/reports/").then(res => {
        this.latestReport = res.data.filter(e => e.country_arabic);
        this.countriesData = this.latestReport;

        this.newsbarData = [];
        res.data
          .sort((a, b) => b.new_confirmed - a.new_confirmed)
          .slice(0, 50)
          .forEach(e => {
            this.newsbarData.push(`${e.emoji} ${e.country_arabic}  ${e.new_confirmed} <span class="arrow-up"></span> `);
          });
      });

      axios.get("/api/trends/").then(res => {
        this.trends = res.data;
        this.fillCharts(this.trends)
      });
    },
    fillCharts(data) {
      Object.keys(data).forEach(category => {

        Object.keys(data[category]).forEach(area => {

          let points = Object.keys(data[category][area]).map(k => {
            return {x: new Date(k), y: data[category][area][k] };
          });

          let color = "#007eff";
          let type = "line";

          if (category.includes("deaths")) {
            color = "#db4437";
          }

          if (category.includes("recovered")) {
            color = "#37db5a";
          }

          if (category.includes("new")) {
            type = "bar";
          }


          let seriesName = 'الاصابات';
          if (category.includes('deaths')) {
            seriesName = 'الوفيات';
          } else if (category.includes('recovered')) {
            seriesName = 'المتعافين';
          }

          this.chartsData[area][category] = [{
            name: seriesName,
            key: area + ' ' + category,
            data: points,
            color: color,
            type: type
          }];

        });

      });

      // merge recovered with confirmed (total & new)
      Object.keys(this.chartsData).forEach(area => {
        this.chartsData[area]['total_confirmed'].push(...this.chartsData[area]['total_recovered']);
        this.chartsData[area]['new_confirmed'].push(...this.chartsData[area]['new_recovered']);
      });

    },
    switchArea(area) {
      this.area = area;
      this.countriesData = this.latestReport.filter(e => area == "worldwide" || (area == "egypt" && e.country == "Egypt") || (area == "arab" && e.arab) || (area == "africa" && e.continent == "Africa"));
    },
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
  color: #fff;
  z-index: 999999;
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
  color: #fdab3c;
  padding: 0.7rem 1.5rem;
  border-radius: 18px;
  font-size: 1rem;
  transition: background 0.3s;
}

.country-filter a.active {
  background: #fdab3c;
  color: #202124;
  font-weight: 700;
}

.country-filter a:hover {
  background: #fdab3c;
  color: #202124;
  font-weight: 700;
}

.card {
  margin: 10px;
  border: 1px solid #909090;
  border-radius: 10px;
  text-align: right;
}

.card-title {
  position: relative;
  top: -10px;
  background: #202124;
  color: #fff;
  display: inline-block;
  padding: 0 1rem;
  right: 1rem;
}

.chart {
  margin: 0 5px;
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
    color: #fdab3c;
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
