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

function defaultCellRenderer(params) {
    return `<span style="font-size: 0.85rem;">${params.value}</span>`;
}

function newCasesCellRenderer(params) {
    return `<span style="background: #ffc023; color: #000; padding: 1px 10px; border-radius: 5px; font-size: 0.85rem">${params.value}+</span>`;
}

function newDeathsCellRenderer(params) {
    return `<span style="background: #db4437; color: #fff; padding: 1px 10px; border-radius: 5px; font-size: 0.85rem">${params.value}+</span>`;
}

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
        methods: {
        },
        beforeMount() {

            this.gridOptions = {
                enableRtl: true,
                floatingFilter: true
            };
            this.defaultColDef = { resizable: true, sortable: true, filter: 'agNumberColumnFilter' };
            console.log('tableeeeee')
            this.columnDefs = [
                {headerName: 'البلد', field: 'country', filter: 'agTextColumnFilter', cellRenderer: defaultCellRenderer},
                {headerName: 'اجمالي الإصابات', field: 'total_cases', cellRenderer: defaultCellRenderer},
                {headerName: 'الإصابات الجديدة', field: 'new_cases', cellRenderer: newCasesCellRenderer},
                {headerName: 'اجمالي الوفيات', field: 'total_deaths', cellRenderer: defaultCellRenderer},
                {headerName: 'الوفيات الجديدة', field: 'new_deaths', cellRenderer: newDeathsCellRenderer},
                {headerName: 'المتعافين', field: 'recovered', cellRenderer: defaultCellRenderer},
                {headerName: 'الحالات النشطة', field: 'recovered', cellRenderer: defaultCellRenderer},
            ];

            this.rowData = [
                {country: 'أيطاليا', total_cases: 120000, new_cases: 5000, total_deaths: 3000, new_deaths: 500, recovered: 10000},
                {country: 'ألمانيا', total_cases: 120000, new_cases: 5000, total_deaths: 3000, new_deaths: 500, recovered: 10000},
                {country: 'السويد', total_cases: 120000, new_cases: 5000, total_deaths: 3000, new_deaths: 500, recovered: 10000},
                {country: 'أمريكا', total_cases: 120000, new_cases: 5000, total_deaths: 3000, new_deaths: 500, recovered: 10000},
                {country: 'مصر', total_cases: 120000, new_cases: 5000, total_deaths: 3000, new_deaths: 500, recovered: 10000},
                {country: 'السودان', total_cases: 120000, new_cases: 5000, total_deaths: 3000, new_deaths: 500, recovered: 10000},
                {country: 'روسيا', total_cases: 120000, new_cases: 5000, total_deaths: 3000, new_deaths: 500, recovered: 10000},
                {country: 'البرتغال', total_cases: 120000, new_cases: 5000, total_deaths: 3000, new_deaths: 500, recovered: 10000},
                {country: 'فرنسا', total_cases: 120000, new_cases: 5000, total_deaths: 3000, new_deaths: 500, recovered: 10000},
                {country: 'السعودية', total_cases: 120000, new_cases: 5000, total_deaths: 3000, new_deaths: 500, recovered: 10000},
                {country: 'الأردن', total_cases: 120000, new_cases: 5000, total_deaths: 3000, new_deaths: 500, recovered: 10000},
                {country: 'العراق', total_cases: 120000, new_cases: 5000, total_deaths: 3000, new_deaths: 500, recovered: 10000},
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

    .ag-theme-balham-dark input[type='text'] {
        border-color: #808080;
    }
</style>
