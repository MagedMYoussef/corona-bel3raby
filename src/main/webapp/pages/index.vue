<template>
  <div class="container">

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
            معدل الوفيات - {{ arabicMapping[area] }}
          </div>
          <div class="card-content">
            <chart class="chart" :series="chartsData[area].total_deaths"></chart>
          </div>
        </div>
        <div class="card">
          <div class="card-title">
            معدل الحالات - {{ arabicMapping[area] }}
          </div>
          <div class="card-content">
            <chart class="chart" :series="chartsData[area].total_confirmed"></chart>
          </div>
        </div>

      </div>


      <div class="row">

        <div style="flex: 1;">

          <div class="card">
            <div class="card-title">
              أكثر الدول إصابة - {{ arabicMapping[area] }}
            </div>
            <div class="card-content">
              <pie-chart class="chart" :series="topCountries.total_confirmed.series" :labels="topCountries.total_confirmed.labels"></pie-chart>
            </div>
          </div>

          <div class="card">
            <div class="card-title">
              أكثر الدول وفيات - {{ arabicMapping[area] }}
            </div>
            <div class="card-content">
              <pie-chart class="chart" :series="topCountries.total_deaths.series" :labels="topCountries.total_deaths.labels"></pie-chart>
            </div>
          </div>

          <div class="card">
            <div class="card-title">
              الحالات الجديدة - {{ arabicMapping[area] }}
            </div>
            <div class="card-content">
              <chart class="chart" :series="chartsData[area].new_confirmed"></chart>
            </div>
          </div>

          <div class="card">
            <div class="card-title">
              الوفيات الجديدة - {{ arabicMapping[area] }}
            </div>
            <div class="card-content">
              <chart class="chart" :series="chartsData[area].new_deaths"></chart>
            </div>
          </div>

      </div>

      <div class="card table">
        <div class="card-title">
          احصائيات الدول - {{ arabicMapping[area] }}
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
            اجمالي الإصابات <br />
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
            الإصابات الجديدة <br />
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
import PieChart from "~/components/PieChart.vue";
import Grid from "~/components/Grid.vue";

export default {
  head() {
    return {
      title: `كورونا بالعربي - متابعة حية لآخر إحصائيات فيروس كوفيد-19`
    };
  },
  components: {
    Chart,
    PieChart,
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
      arabicMapping: {
        worldwide: 'العالم',
        arab: 'الدول العربية',
        africa: 'أفريقيا',
        egypt: 'مصر',
      },
      countriesData: null,
      latestReport: null,
      topCountries: { total_confirmed: { series: null, labels: null }, total_deaths: { series: null, labels: null } }
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
        this.fillTopCountries(this.countriesData);
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
          let type = "area";

          if (category.includes("deaths")) {
            color = "#db4437";
          }

          if (category.includes("recovered")) {
            color = "#37db5a";
          }

          if (category.includes("new")) {
            type = "bar";
          }


          let seriesName = 'الإصابات';
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
    fillTopCountries(data) {

      ['total_confirmed', 'total_deaths'].forEach(e => {

        this.topCountries[e].series = [];
        this.topCountries[e].labels = [];

        data
          .sort((a, b) => b[e] - a[e])
          .slice(0, 10)
          .forEach(k => {
            this.topCountries[e].labels.push(k.country_arabic);
            this.topCountries[e].series.push(k[e]);
          });

      });

    },
    switchArea(area) {
      this.area = area;
      this.countriesData = this.latestReport.filter(e => area == "worldwide" || (area == "egypt" && e.country == "Egypt") || (area == "arab" && e.arab) || (area == "africa" && e.continent == "Africa"));
      this.fillTopCountries(this.countriesData);
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
  height: 10px;
  background-color: #202124;
}

::-webkit-scrollbar-thumb {
  background-color: #505258;
}

.container {
  font-family: "Cairo", sans-serif;
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
  font-family: "El Messiri", sans-serif;
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

a {
  text-decoration: none;
  color: #fff;
}


// responsive
@media only screen and (max-width: 1400px) {
  .apexcharts-legend {
    display: none !important;
  }
}

@media only screen and (max-width: 1200px) {
  .sidebar {
    display: none;
  }

  .main {
    width: 100vw;
  }

  .header {
    width: 100vw;
  }

  .country-filter a {
    padding: 0.5rem;
    border-radius: 10px;
  }

}

@media only screen and (max-width: 800px) {
  .row {
    display: block;
  }

  .links {
    display: none;
  }

  .apexcharts-legend {
    display: block !important;
  }
}

@media only screen and (max-width: 500px) {
  .apexcharts-legend {
    display: none !important;
  }
}

</style>
