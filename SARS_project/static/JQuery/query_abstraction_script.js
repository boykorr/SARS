$(document).ready(function(){
    //Queries array
    var queries = [];
    var count = 0;

    //When Add button is clicked, add contents of query box to list
    $('button[name=add]').click(function(){
        var toAdd = $('#id_queryBox').val();
        var Xbutton = '<button id="del" name="delete" type="button" value="">&#10006</button>';
        var Ebutton = '<button id="edit" name="edit" type="button" value="">Edit</button>';
        $('#del').val(count);
        $('#edit').val(count);
        queries.push(toAdd);
        //$('ol').append(queries[0]);
        //$('ol').append(queries[1]);
        //$('ol').append(queries[2]);
        count += 1;
        $('#list').append('<div><li>' + Xbutton + Ebutton + '<span>' + toAdd + '</span>' + '</li></div>');
        //$('ol').append($('#del').attr("value"));
        //$('#list').append($("#edit").attr("value"));
    });

    //When 'X' button is clicked, query is removed
    $(document).on('click', '#del', function(){
        //delete queries[$(this).attr("value")];
        $(this).parent().remove();
        queries.slice($(this).attr("value"));
        $('#list').append(queries);
        //delete queries[$(this).attr("value")];
    });

   
    //When Edit button is clicked, query is changed to contents of query box
    $(document).on('click', '#edit', function(){
        var newString = $('input[name=queryBox]').val();
        $(this).next().html(newString);
        queries[$(this).attr("value")] = newString;
    });

    //When Clear All button is clicked, all queries are removed
    $('button[name=clear]').click(function(){
       $('ol').empty();
       queries = [];
    });
});