$(document).ready(function(){
	$("#table").jqGrid(
		{
			url: 'save',
			datatype : 'local',
			height: 500,
			// height: 'auto',
			colNames: ['样品编号', '样品名称', 'rin值','浓度(ng/uL)','体积(ul)', '判定结果', '时间', '备注'],
			colModel: [
						{ name: 'sample_id', index: 'sample_id', editable: true, width: 60},
						{ name: 'sample_name', index: 'sample_name', editable: true, width: 60},
						{ name: 'rin', index: 'rin', editable: true, width: 60},
						{ name: 'concentration', index: 'concentration', editable: true, width: 60},
						{ name: 'volume', index: 'volume', editable: true, width: 60},
						{ name: 'qualitycheck_results', index: 'qualitycheck_results', editable: true, width: 60},
						{ name: 'qualitycheck_time', index: 'qualitycheck_time', editable: true, width: 60},
						{ name: 'qualitycheck_comment', index: 'qualitycheck_comment', editable: true, width: 60}
					],
			gridComplete: function() {},
			caption : "质检结果",//表格的标题名字
			width: 1000
		});
	});

$(function(){
	//页面加载完成之后执行
	pageInit();
});
function pageInit(){
	return;
}
