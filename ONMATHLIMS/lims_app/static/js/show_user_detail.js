$(function(){
  pageInit();
});
function pageInit() {
  $("#billing_table").jqGrid({
    url: '/lims_app/show_billing_info',
    datatype: "json",
    colNames: ['项目', '金额', '开票','时间', '备注'],
    colModel: [
      {name: 'project_number', index: 'project_number', editable: true, width: 90},
      {name: 'expense', index: 'expense', editable: true, width: 60},
      {name: 'billing_number', index: 'billing_number', editable: true, width: 90},
      {name: 'time', index: 'time', editable: true, width: 60},
      {name: 'comment', index: 'comment', editable: true, width: 100}
    ],
    rowNum: 10,
    rowList: [10, 20, 30],
    pager: "#nav_billing_table",
    sortname: 'project_number',
    sortorder: 'desc',
    viewrecords: true,
    editurl: 'lims_app/haha',
    postData: {
      user: "{{ cust_user }}"
      },
    caption: '开票信息'
  });
  $("#billing_table").jqGrid('navGrid', '#nav_billing_table', {
    edit: false,
    add: false,
    del: false
  });
  $("#billing_table").jqGrid('inlineNav', '#nav_billing_table');
}
