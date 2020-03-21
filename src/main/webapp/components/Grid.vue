<template>
<div>
  <ag-grid-vue style="height: 25rem; margin: 1rem;"
        class="ag-theme-balham-dark"
        :columnDefs="columnDefs"
        :rowData="rowData"
        :gridOptions="gridOptions"
        :defaultColDef="defaultColDef">
    </ag-grid-vue>
</div>
</template>

<script>
    import {AgGridVue} from "ag-grid-vue";

    export default {
        data() {
            return {
                columnDefs: null,
                rowData: null,
                gridOptions: null,
                gridApi: null,
                defaultColDef: null
            }
        },
        components: {
            AgGridVue
        },
        beforeMount() {

            this.gridOptions = {
                enableRtl: true
            };
            this.defaultColDef = { resizable: true };
            console.log('tableeeeee')
            this.columnDefs = [
                {headerName: 'Make', field: 'make'},
                {headerName: 'Model', field: 'model'},
                {headerName: 'Price', field: 'price'}
            ];

            this.rowData = [
                {make: 'Toyota', model: 'Celica', price: 35000},
                {make: 'Ford', model: 'Mondeo', price: 32000},
                {make: 'Porsche', model: 'Boxter', price: 72000}
            ];


        },
        mounted() {
            this.gridApi = this.gridOptions.api;
            this.gridApi.sizeColumnsToFit();
        }
    }

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
</style>
