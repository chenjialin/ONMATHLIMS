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
      colNames: ['样品名称', '物种','快递编号','管数', '时间', '备注'],
      colModel: [
            { name: 'sample_name', index: 'sample_name', editable: true, width: 60},
            { name: 'species', index: 'species', editable: true, width: 60},
            { name: 'express_number', index: 'express_number', editable: true, width: 60},
            { name: 'product_num', index: 'product_num', editable: true, width: 60},
            { name: 'time', index: 'time', editable: true, width: 60},
            { name: 'comment', index: 'comment', editable: true, width: 60}
          ],
      gridComplete: function() {},
      caption : "送样结果",//表格的标题名字
      width: 1000
    });
}
