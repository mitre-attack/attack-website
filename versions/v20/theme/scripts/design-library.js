$('#v-typography-tab').click(() => {
	$('#collapseTypography').collapse('toggle');
	$('#collapseFormControls').collapse('hide');
	$('#collapseFormTemplates').collapse('hide');
	$('#collapseHeaders').collapse('hide');
});

$('#v-formcontrols-tab').click(() => {
	$('#collapseFormControls').collapse('toggle');
	$('#collapseTypography').collapse('hide');
	$('#collapseFormTemplates').collapse('hide');
	$('#collapseHeaders').collapse('hide');
});

$('#v-formtemplates-tab').click(() => {
	$('#collapseFormTemplates').collapse('toggle');
	$('#collapseFormControls').collapse('hide');
	$('#collapseTypography').collapse('hide');
	$('#collapseHeaders').collapse('hide');
});

$('#v-headers-tab').click(() => {
	$('#collapseHeaders').collapse('toggle');
	$('#collapseFormTemplates').collapse('hide');
	$('#collapseFormControls').collapse('hide');
	$('#collapseTypography').collapse('hide');
});

// $('body').on('click', 'a', () =>  {
//       $('a.active').removeClass('active');
//       $(this).addClass('active');
// });
