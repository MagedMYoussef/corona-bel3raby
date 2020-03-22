<template>
<div>
  <ag-grid-vue style="height: 30rem; margin: 1rem;"
        class="ag-theme-balham-dark"
        :columnDefs="columnDefs"
        :rowData="data"
        :gridOptions="gridOptions"
        :defaultColDef="defaultColDef">
    </ag-grid-vue>
</div>
</template>

<script>

import { AgGridVue } from 'ag-grid-vue';

function defaultCellRenderer(params) {
  return `<span style="font-size: 0.85rem;">${params.value}</span>`;
}

function newCasesCellRenderer(params) {
  return `<span style="background: #ffc023; color: #000; padding: 1px 10px; border-radius: 5px; font-size: 0.85rem">${params.value}+</span>`;
}

function newDeathsCellRenderer(params) {
  return `<span style="background: #db4437; color: #fff; padding: 1px 10px; border-radius: 5px; font-size: 0.85rem">${params.value}+</span>`;
}

function countryCellRenderer(params) {

    if (params.data.emoji) {
        return `<span style="font-size: 0.85rem">${params.data.emoji} ${params.value}</span>`;
    }

    return defaultCellRenderer(params);
}


export default {
  props: {
    data: {
      type: Array,
      required: true,
    }
  },
  data() {
    return {
      columnDefs: null,
      rowData: null,
      gridOptions: null,
      gridApi: null,
      defaultColDef: null,
    }
  },
  components: {
    AgGridVue,
  },
  methods: {
  },
  beforeMount() {
    this.gridOptions = {
      enableRtl: true,
      floatingFilter: true,
    };

    this.defaultColDef = { resizable: true, sortable: true, filter: 'agNumberColumnFilter' };
    this.columnDefs = [
      {
        headerName: 'البلد', field: 'country_arabic', filter: 'agTextColumnFilter', cellRenderer: countryCellRenderer,
      },
      { headerName: 'اجمالي الإصابات', field: 'total_confirmed', cellRenderer: defaultCellRenderer },
      { headerName: 'الإصابات الجديدة', field: 'new_confirmed', cellRenderer: newCasesCellRenderer },
      { headerName: 'معدل الزيادة', field: 'increase_rate', cellRenderer: defaultCellRenderer },
      { headerName: 'اجمالي الوفيات', field: 'total_deaths', cellRenderer: defaultCellRenderer },
      { headerName: 'الوفيات الجديدة', field: 'new_deaths', cellRenderer: newDeathsCellRenderer },
      { headerName: 'معدل الوفاة', field: 'death_rate', cellRenderer: defaultCellRenderer },
      { headerName: 'المتعافين', field: 'total_recovered', cellRenderer: defaultCellRenderer },
      { headerName: 'الحالات النشطة', field: 'active', cellRenderer: defaultCellRenderer },
    ];

  },
  mounted() {
    this.gridApi = this.gridOptions.api;
    this.gridApi.sizeColumnsToFit();
  },
};

</script>

<style lang="scss">
  @import "../../../../node_modules/ag-grid-community/dist/styles/ag-grid.css";
  @import "../../../../node_modules/ag-grid-community/dist/styles/ag-theme-balham-dark.css";

    .ag-theme-balham-dark .ag-root-wrapper {
        background-color: unset;
    }

    .ag-theme-balham-dark .ag-row.ag-row-even {
        background-color: unset;
    }

    .ag-theme-balham-dark .ag-row.ag-row-hover {
        background-color: #3d474d;
    }

    .ag-theme-balham-dark .ag-header {
        background-color: #2b2d37;
    }

    .ag-theme-balham-dark input[type='text'] {
        border-color: #808080;
    }
</style>
