$(function(){
  pageInit();
});
function pageInit(){
  $("#table").jqGrid(
    {
      url: 'save',
      datatype : 'local',
      height: 500,
      // height: 'auto',
      colNames: ['样品名称', 'OMID', '样品编号', '数据量', 'q20', 'q30', '时间', '备注'],
      colModel: [
            { name: 'sample_name', index: 'sample_name', editable: true, width: 60},
            { name: 'om_id', index: 'om_id', editable: true, width: 60},
            { name: 'sample_id', index: 'sample_id', editable: true, width: 60},
            { name: 'data_count', index: 'data_count', editable: true, width: 60},
            { name: 'q20', index: 'q20', editable: true, width: 60},
            { name: 'q30', index: 'q30', editable: true, width: 60},
            { name: 'time', index: 'time', editable: true, width: 60},
            { name: 'comment', index: 'comment', editable: true, width: 60}
          ],
      gridComplete: function() {},
      caption : "上机结果",//表格的标题名字
      width: 1000
    });
}
