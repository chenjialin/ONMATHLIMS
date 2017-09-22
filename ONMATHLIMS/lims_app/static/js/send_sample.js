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
      colNames: ['样品名称', 'OMID', '样品编号', '物种', '快递编号', '管数', '时间', '备注', '所在地'],
      colModel: [
            { name: 'sample_name', index: 'sample_name', editable: true, width: 60},
            { name: 'om_id', index: 'om_id', editable: true, width: 60},
            { name: 'sample_id', index: 'sample_id', editable: true, width: 60},
            { name: 'species', index: 'species', editable: true, width: 60},
            { name: 'express_number', index: 'express_number', editable: true, width: 60},
            { name: 'product_num', index: 'product_num', editable: true, width: 60},
            { name: 'time', index: 'time', editable: true, width: 60},
            { name: 'comment', index: 'comment', editable: true, width: 60},
            { name: 'location', index: 'location', editable: true, width: 60}
          ],
      gridComplete: function() {},
      caption : "送样结果",//表格的标题名字
      width: 1000
    });
/*
    $("#table2").jqGrid(
      {
        url: 'save',
        datatype : 'local',
        height: 250,
        // height: 'auto',
        colNames: ['样品名称', 'OMID', '物种', '快递编号', '管数', '时间', '备注'],
        colModel: [
              { name: 'sample_name', index: 'sample_name', editable: true, width: 60},
              { name: 'om_id', index: 'om_id', editable: true, width: 60},
              { name: 'species', index: 'species', editable: true, width: 60},
              { name: 'express_number', index: 'express_number', editable: true, width: 60},
              { name: 'product_num', index: 'product_num', editable: true, width: 60},
              { name: 'time', index: 'time', editable: true, width: 60},
              { name: 'comment', index: 'comment', editable: true, width: 60}
            ],
        gridComplete: function() {},
        caption : "送样结果",//表格的标题名字
        width: 800
      });
*/
}
