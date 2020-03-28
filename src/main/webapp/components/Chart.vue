<template>
  <div v-if="series">
    <apexchart height="200px" :options="options" :series="series"></apexchart>
  </div>
</template>

<script>
import Vue from 'vue';

import VueApexCharts from 'vue-apexcharts';
Vue.component('apexchart', VueApexCharts);

var max = new Date().getTime(); // Current timestamp

var min = new Date(
    new Date().getFullYear(),
    new Date().getMonth() - 2,
    new Date().getDate()
);

var range = max - min;

export default {
    data: function() {
    return {
      options: {
        colors: ['#2E93fA', '#66DA26', '#546E7A', '#E91E63', '#FF9800'],
        chart: {
          width: "100%",
          height: "100%",
          zoom: {
            type: 'x',
            enabled: true,
            autoScaleYaxis: true
          },
          events: {
            beforeZoom: function(ctx) {
              // we need to clear the range as we only need it on the iniital load.
              ctx.w.config.xaxis.range = undefined
            }
          }
        },
        xaxis: {
          type: 'datetime',
          range: range
        },
        dataLabels: {
          enabled: false
        },
        markers: {
          size: 0,
        },
        plotOptions: {
          bar: {
            distributed: true,
          }
        },
        sfill: {
          type: 'gradient',
          gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.5,
            opacityTo: 0,
            stops: [0, 90, 100]
          },
        },
        grid: {
          show: true,
          borderColor: '#717171',
          strokeDashArray: 0,
          position: 'back',
          xaxis: {
              lines: {
                  show: true
              }
          },
          yaxis: {
              lines: {
                  show: true
              }
          },
          row: {
              colors: undefined,
              opacity: 0.5
          },
          column: {
              colors: undefined,
              opacity: 0.5
          },
          padding: {
              top: 0,
              right: 0,
              bottom: 0,
              left: 0
          },
      }

      },
    }
  },
  props: ["series"],
  mounted() {
  }
};
</script>

<style>
</style>
