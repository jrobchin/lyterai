// Close property panes when clicked
$(document).on('click','.dropdown-pane',function(){
    $(".dropdown-pane.is-open").foundation('close');
});

// Submit demos with ajax and population solutions
$("#demo-form").submit(function(event) {


    /* stop form from submitting normally */
    event.preventDefault();

    $.ajax({
        type:$(this).attr('method'),
        url:$(this).attr('action'),
        data:$(this).serialize(),
        success: function(data){
            $("#demo-prediction").empty().append(data['prediction']);
            $("#demo-confidence").empty().append(data['confidence']);
        }
    });
    
});