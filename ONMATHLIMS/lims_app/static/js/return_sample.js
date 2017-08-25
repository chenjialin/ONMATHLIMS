$(function(){
  pageInit();
});
function pageInit(){
  $("#table").jqGrid(
    {
      url: 'save',
      datatype : 'local',
      height: 450,
      // height: 'auto',
      colNames: ['样品名称', '样品编号', '所在地', '时间', '备注'],
      colModel: [
            { name: 'sample_name', index: 'sample_name', editable: true, width: 60},
            { name: 'sample_id', index: 'sample_id', editable: true, width: 60},
            { name: 'location', index: 'location', editable: true, width:90},
            { name: 'time', index: 'time', editable: true, width: 60},
            { name: 'comment', index: 'comment', editable: true, width: 60}
          ],
      gridComplete: function() {},
      caption : "返样结果",//表格的标题名字
      width: 1000
    });
  }
