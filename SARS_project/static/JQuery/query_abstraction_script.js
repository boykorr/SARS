$(document).ready(function(){
    //When Add button is clicked, add contents of query box to list
    $('button[name=add]').click(function(){
        var toAdd = $('#id_queryBox').val();
        var Xbutton = '<button name="delete" type="button" value=&#10006>&#10006</button>';
        //var EButton = '<button name="edit" type="button" value="edit">Edit</button>';
        $('#list').append('<div><li>' + Xbutton + '<span>' + toAdd + '</span>' + '</li></div>');
    });

    //When 'X' button (or text next to it) is clicked, query is removed
    $(document).on('click', 'li', function(){
        $(this).remove;
    });

    $('button[name=edit]').click(function(){
        var newString = $('input[name=queryBox]').val();
        $('.highlighted').html(newString);
    });

    //$(document).on('click', $('span').parent(), function(){
    //   $(this).remove();
    //});

    //When Clear All button is clicked, all queries are removed
    $('button[name=clear]').click(function(){
       $('ol').empty();
    });
});