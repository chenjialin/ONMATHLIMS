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
      colNames: ['样品名称', 'OMID', '样品编号', '浓度', '体积', 'RIN值', '判定结果', '时间', '备注'],
      colModel: [
            { name: 'sample_name', index: 'sample_id', editable: true, width: 60},
            { name: 'om_id', index: 'om_id', editable: true, width: 60},
            { name: 'sample_id', index: 'sample_id', editable: true, width: 60},
            { name: 'concentration', index: 'concentration', editable: true, width: 60},
            { name: 'volume', index: 'volume', editable: true, width: 60},
            { name: 'rin', index: 'rin', editable: true, width: 60},
            { name: 'results', index: 'results', editable: true, width: 60},
            { name: 'time', index: 'time', editable: true, width: 60},
            { name: 'comment', index: 'comment', editable: true, width: 60}
          ],
      gridComplete: function() {},
      caption : "质检结果",//表格的标题名字
      width: 1000
    });
}
