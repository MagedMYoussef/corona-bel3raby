<template>
  <div v-if="series">
    <apexchart height="250px" :options="options" :series="series"></apexchart>
  </div>
</template>

<script>
import Vue from 'vue';

import VueApexCharts from 'vue-apexcharts';
Vue.component('apexchart', VueApexCharts);

var max = new Date().getTime(); // Current timestamp

var min = new Date(
    new Date().getFullYear(),
    new Date().getMonth() - 1,
    new Date().getDate()
);

var range = max - min;

function kFormatter(num) {
    return Math.abs(num) > 999 ? Math.sign(num)*((Math.abs(num)/1000).toFixed(1)) + 'k' : Math.sign(num)*Math.abs(num).toFixed(1);
}

export default {
    data: function() {
    return {
      options: {
        colors: ['#1673ff', '#74fd2e', '#546E7A', '#E91E63', '#FF9800'],
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
          },
          defaultLocale: 'ar',
          locales: [
            {
              name: 'en',
              options: {
                months: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                shortMonths: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                days: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
                shortDays: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
                toolbar: {
                  download: 'Download SVG',
                  selection: 'Selection',
                  selectionZoom: 'Selection Zoom',
                  zoomIn: 'Zoom In',
                  zoomOut: 'Zoom Out',
                  pan: 'Panning',
                  reset: 'Reset Zoom',
                }
              }
            },
            {
              name: 'ar',
              options: {
                months: ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو', 'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر'],
                shortMonths: ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو', 'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر'],
                days: ['الأحد', 'الأثنين', 'الثلثاء', 'الأربعاء', 'الخميس', 'الجمعة', 'السبت'],
                shortDays: ['الأحد', 'الأثنين', 'الثلثاء', 'الأربعاء', 'الخميس', 'الجمعة', 'السبت'],
                toolbar: {
                  download: 'Download SVG',
                  selection: 'Selection',
                  selectionZoom: 'Selection Zoom',
                  zoomIn: 'Zoom In',
                  zoomOut: 'Zoom Out',
                  pan: 'Panning',
                  reset: 'Reset Zoom',
                }
              }
            }
          ]

        },
        xaxis: {
          type: 'datetime',
          range: range
        },
        yaxis: {
          labels: {
            formatter: function(val) {
              return kFormatter(val);
            },
          }
        },
        stroke: {
          width: []
        },
        dataLabels: {
          enabled: false
        },
        markers: {
          size: 0,
        },
        plotOptions: {
          bar: {
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
        },
        tooltip: {
            y: {
              formatter: function(val) {
                return val.toLocaleString();
              },
              title: {
                  formatter: (seriesName) => seriesName,
              },
          },
        }

      },
    }
  },
  props: ["series"],
  mounted() {

  },
  watch: {
    series: function(newVal, oldVal) {
      if (this.series) {
        console.log('series', this.series);
        this.series.forEach(e => {
          if (e.type === 'bar') {
            this.options.stroke.width.push(0);
          } else {
            this.options.stroke.width.push(5);
          }

          if (e.key.includes('death')) {
            this.options.colors = ['#da4437', '#fdab3c'];
          }

          if (e.xaxis && e.xaxis == "category") {
            this.options.plotOptions.bar = {
              horizontal: true,
            };

            this.options.xaxis = {
              type: 'category'
            };

          }

        });
      }
    }
  }
};
</script>

<style>
.apexcharts-text {
  fill: #cacaca;
}
.apexcharts-legend-text {
  color: #cacaca !important;
}
.apexcharts-tooltip-text {
  font-family: 'Cairo', sans-serif !important;
}
.apexcharts-legend-text {
  font-family: 'Cairo', sans-serif !important;
}
.apexcharts-legend {
  bottom: 0 !important;
}
</style>
