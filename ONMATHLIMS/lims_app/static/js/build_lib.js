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
      colNames: ['样品名称', '样品编号', '文库编号', '时间', '备注'],
      colModel: [
            { name: 'sample_name', index: 'sample_name', editable: true, width: 60},
            { name: 'sample_id', index: 'sample_id', editable: true, width: 60},
            { name: 'lib_id', index: 'lib_id', editable: true, width: 60},
            { name: 'time', index: 'time', editable: true, width: 60},
            { name: 'comment', index: 'comment', editable: true, width: 60}
          ],
      gridComplete: function() {},
      caption : "建库结果",//表格的标题名字
      width: 1000
    });
}
