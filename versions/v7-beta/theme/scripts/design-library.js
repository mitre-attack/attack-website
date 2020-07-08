$('#v-typography-tab').click(function(e){
	$('#collapseTypography').collapse('toggle');
	$('#collapseFormControls').collapse('hide');
	$('#collapseFormTemplates').collapse('hide');
	$('#collapseHeaders').collapse('hide');
});

$('#v-formcontrols-tab').click(function(e){
	$('#collapseFormControls').collapse('toggle');
	$('#collapseTypography').collapse('hide');
	$('#collapseFormTemplates').collapse('hide');
	$('#collapseHeaders').collapse('hide');
});

$('#v-formtemplates-tab').click(function(e){
	$('#collapseFormTemplates').collapse('toggle');
	$('#collapseFormControls').collapse('hide');
	$('#collapseTypography').collapse('hide');
	$('#collapseHeaders').collapse('hide');
});

$('#v-headers-tab').click(function(e){
	$('#collapseHeaders').collapse('toggle');
	$('#collapseFormTemplates').collapse('hide');
	$('#collapseFormControls').collapse('hide');
	$('#collapseTypography').collapse('hide');
});

// $('body').on('click', 'a', function() {
//       $('a.active').removeClass('active');
//       $(this).addClass('active');
// });
