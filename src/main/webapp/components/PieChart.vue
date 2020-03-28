<template>
  <div v-if="series">
    <apexchart height="250px" :options="options" :series="series"></apexchart>
  </div>
</template>

<script>
import Vue from 'vue';

import VueApexCharts from 'vue-apexcharts';
Vue.component('apexchart', VueApexCharts);


export default {
    data: function() {
        return {
            options: {
                theme: {
                    palette: 'palette2'
                },
                chart: {
                    type: 'pie'
                },
                labels: null,
                stroke: {
                    width: 0
                },
                legend: {
                    position: 'right'
                },
                dataLabels: null
            },
            labels: null
        }
    },
    props: ["series", "labels"],
    watch: {
        labels: function(newVal, oldVal) {
            this.options.labels = newVal;
            this.options.dataLabels = {
                formatter: function(val, opt) {
                    let v = val.toFixed(1) + '%';
                    return v;
                },
                style: {
                    fontSize: '12px',
                    fontFamily: 'Cairo, sans-serif',
                },
                dropShadow: {
                    enabled: true,
                    top: 1,
                    left: 1,
                    blur: 1,
                    color: '#000',
                    opacity: 0.8
                }
            };
            this.options = {...this.options}
        }
    }
}
</script>

<style>

</style>