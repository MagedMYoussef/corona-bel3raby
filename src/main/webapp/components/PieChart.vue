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
                chart: {
                    type: 'pie'
                },
                labels: null,
                stroke: {
                    width: 0
                }
            },
            labels: null
        }
    },
    props: ["series", "labels"],
    mounted() {
        console.log('piechart', this.series)
    },
    watch: {
        series: function(newVal, oldVal) {
            console.log('watchhhhh', newVal)
        },
        labels: function(newVal, oldVal) {
            this.options.labels = newVal;
            this.options = {...this.options}
        }
    }
}
</script>

<style>

</style>