// Linkedin button / modal dialog

var linkedin_connect_modal = $('#linkedin-connect-modal');
var linkedin_connect_button = $('#linkedin-connect-button');

linkedin_connect_button
	.click(function(){
		linkedin_connect_modal.modal('show');
	});
