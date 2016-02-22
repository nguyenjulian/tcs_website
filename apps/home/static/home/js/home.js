// set up project tag dropdown
var project_tag_dropdown = $('#project-tag-dropdown');

project_tag_dropdown
	.dropdown();

// filter projects functionality 
function get_selected_tags_from_dropdown() {
	return $('.item.active.filtered').map(function(){
		return $(this).data('value');
	}).get().join(',');
}

var filter_projects_btn = $('#filter-projects-btn');
filter_projects_btn.click(function(){
	$.get(
		'/projects/?tags='+get_selected_tags_from_dropdown(), 
		function(data) {
			alert(this.url);
		}
	);
});
