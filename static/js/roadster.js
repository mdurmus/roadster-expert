$(document).ready(function(){
    setTimeout(function(){
        $('#msg').alert('close');
    }, 2500);
});

$(document).ready(function(){
    $('#searchButton').click(function(){
        $('#staticBackdrop').modal('show');
    });

})