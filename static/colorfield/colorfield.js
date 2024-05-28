/** global: django */

window.addEventListener('load', function (event) {
    if (typeof django !== 'undefined' && typeof django.jQuery !== 'undefined') {
        (function ($) {
            console.log('Django and jQuery are defined.');

            // Check if jscolor is loaded
            if (typeof jscolor === 'undefined') {
                console.error('jscolor is not defined. Ensure the jscolor library is loaded.');
                return;
            }

            // Add color picker to inlines added dynamically
            $(document).on('formset:added', function onFormsetAdded(event, row) {
                console.log('Formset added:', row);
                jscolor.install();
            });
        })(django.jQuery);
    } else {
        console.error('Django or jQuery is not defined.');
    }
});
