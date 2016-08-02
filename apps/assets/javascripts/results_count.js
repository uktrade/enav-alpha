(function () {
    $('#results-count').each(function(){
        var $count = $('em', this),
            $form = $('#results-form'),
            action = $form.data('count-action');

        $('input', $form).on('change', function() {
            $.ajax({
                    url: action,
                    type: 'GET',
                    data: $form.serialize(),
                    success:function(result){
                        $count.text(result['count']);
                    }
            });
        });
    });
})();
