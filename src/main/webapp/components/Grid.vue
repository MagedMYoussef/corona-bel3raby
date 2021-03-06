<template>
<div>
  <ag-grid-vue style="height: 70rem; margin: 1rem;"
        class="ag-theme-balham-dark"
        :columnDefs="columnDefs"
        :rowData="data"
        :gridOptions="gridOptions"
        :modules="modules"
        :defaultColDef="defaultColDef">
    </ag-grid-vue>
</div>
</template>


<script>
import Vue from 'vue';

import { ModuleRegistry } from '@ag-grid-community/core';     // @ag-grid-community/core will always be implicitly available
import { ClientSideRowModelModule } from "@ag-grid-community/client-side-row-model";

ModuleRegistry.registerModules([
    ClientSideRowModelModule,
]);

import { AgGridVue } from '@ag-grid-community/vue';

function isFloat(n){
  return Number(n) === n && n % 1 !== 0;
}

function defaultCellRenderer(params) {

  let value = params.value;
  value = parseFloat(value);

  if (!value) {
    return `<span style="font-size: 0.95rem; font-family: 'Cairo', sans-serif;">${params.value.toLocaleString()}</span>`;
  }

  let percent = '';
  if (isFloat(value)) {
    percent = '%';
  }
  return `<span style="font-size: 0.95rem; font-family: 'Cairo', sans-serif;">${value.toLocaleString(undefined, {maximumFractionDigits: 1}) + percent}</span>`;
}

function newCasesCellRenderer(params) {
  if (params.value == 0) {
    return;
  }
  return `<span style="background: #ffeec3; color: #000; padding: 1px 5px; font-size: 0.95rem; font-family: 'Cairo', sans-serif; width: 6rem; text-align: center; display: inline-block">${params.value.toLocaleString()}+</span>`;
}

function newDeathsCellRenderer(params) {
  if (params.value == 0) {
    return;
  }
  return `<span style="background: #db4437; color: #fff; padding: 1px 5px; font-size: 0.95rem; font-family: 'Cairo', sans-serif; width: 6rem; text-align: center; display: inline-block">${params.value.toLocaleString()}+</span>`;
}

function countryCellRenderer(params) {
    return defaultCellRenderer(params);
}

function rateCellRenderer(params) {
  params.value = params.value * 100;
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
      columnApi: null,
      defaultColDef: null,
      modules: [ClientSideRowModelModule]
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
      pagination: true,
      paginationAutoPageSize: true
    };

    this.defaultColDef = { resizable: true, sortable: true, filter: 'agNumberColumnFilter' };
    this.columnDefs = [
      {
        headerName: 'البلد', field: 'country_arabic', filter: 'agTextColumnFilter', cellRenderer: countryCellRenderer, minWidth: 150
      },
      { headerName: 'الإصابات', field: 'total_confirmed', cellRenderer: defaultCellRenderer },
      { headerName: 'الإصابات الجديدة', field: 'new_confirmed', cellRenderer: newCasesCellRenderer },
      { headerName: 'الوفيات الجديدة', field: 'new_deaths', cellRenderer: newDeathsCellRenderer },
      { headerName: 'معدل الزيادة', field: 'increase_rate', cellRenderer: rateCellRenderer },
      { headerName: 'الوفيات', field: 'total_deaths', cellRenderer: defaultCellRenderer },
      { headerName: 'معدل الوفاة', field: 'death_rate', cellRenderer: rateCellRenderer },
      { headerName: 'المتعافين', field: 'total_recovered', cellRenderer: defaultCellRenderer },
      { headerName: 'الحالات النشطة', field: 'total_active', cellRenderer: defaultCellRenderer }
    ];

  },
  mounted() {
    this.gridApi = this.gridOptions.api;
    this.columnApi = this.gridOptions.columnApi;

    var allColIds = this.columnApi.getAllColumns()
        .map(column => column.colId);

    this.columnApi.autoSizeColumns(allColIds);
    // this.gridApi.sizeColumnsToFit();

    // sort by total_confirmed
    this.gridApi.setSortModel([{ colId: 'total_confirmed', sort: 'desc'}]);
  },
};

</script>

<style lang="scss">

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

    .ag-theme-balham-dark .ag-paging-panel {
      direction: ltr;
    }
</style>
