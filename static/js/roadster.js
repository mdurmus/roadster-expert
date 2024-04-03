$(document).ready(function(){
    setTimeout(function(){
        $('#msg').alert('close');
    }, 6000);
});

$(document).ready(function(){
    $('#searchButton').click(function(){
        $('#staticBackdrop').modal('show');
    });

})