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

function isFloat(n){
  return Number(n) === n && n % 1 !== 0;
}

function defaultCellRenderer(params) {

  let value = params.value;
  value = parseFloat(value);

  if (!value) {
    return `<span style="font-size: 0.95rem;">${params.value}</span>`;
  }

  if (isFloat(value)) {
    value = value.toFixed(1);
  }

  return `<span style="font-size: 0.95rem;">${value.toLocaleString()}</span>`;
}

function newCasesCellRenderer(params) {
  if (params.value == 0) {
    return params.value;
  }
  return `<span style="background: #ffeec3; color: #000; padding: 1px 10px; font-size: 0.95rem; width: 5rem; display: inline-block">${params.value.toLocaleString()}+</span>`;
}

function newDeathsCellRenderer(params) {
  if (params.value == 0) {
    return params.value;
  }
  return `<span style="background: #db4437; color: #fff; padding: 1px 10px; font-size: 0.95rem; width: 5rem; display: inline-block">${params.value.toLocaleString()}+</span>`;
}

function countryCellRenderer(params) {

    if (params.data.emoji) {
        return `<span style="font-size: 0.95rem">${params.data.emoji} ${params.value}</span>`;
    }

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
        headerName: 'البلد', field: 'country_arabic', filter: 'agTextColumnFilter', cellRenderer: countryCellRenderer, minWidth: 200
      },
      { headerName: 'الإصابات', field: 'total_confirmed', cellRenderer: defaultCellRenderer },
      { headerName: 'الإصابات الجديدة', field: 'new_confirmed', cellRenderer: newCasesCellRenderer },
      { headerName: 'معدل الزيادة', field: 'increase_rate', cellRenderer: rateCellRenderer },
      { headerName: 'الوفيات', field: 'total_deaths', cellRenderer: defaultCellRenderer },
      { headerName: 'الوفيات الجديدة', field: 'new_deaths', cellRenderer: newDeathsCellRenderer },
      { headerName: 'معدل الوفاة', field: 'death_rate', cellRenderer: rateCellRenderer },
      { headerName: 'المتعافين', field: 'total_recovered', cellRenderer: defaultCellRenderer },
      { headerName: 'الحالات النشطة', field: 'total_active', cellRenderer: defaultCellRenderer },
    ];

  },
  mounted() {
    this.gridApi = this.gridOptions.api;
    this.columnApi = this.gridOptions.columnApi;

    var allColIds = this.columnApi.getAllColumns()
        .map(column => column.colId);

    this.columnApi.autoSizeColumns(allColIds);
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
