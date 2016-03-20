$(document).ready(function(){
    //Queries array
    var queries = [];

    //When Add button is clicked, add contents of query box to list
    $('button[name=add]').click(function(){
        var toAdd = $('#id_queryBox').val();
        var Xbutton = '<button id="del" name="delete" type="button" value="">&#10006</button>';
        var Ebutton = '<button id="edit" name="edit" type="button" value="">Edit</button>';
        queries.push(toAdd);
        $('#list').append('<div><li>' + Xbutton + Ebutton + '<span>' + toAdd + '</span>' + '</li></div>');
    });

    //When 'X' button is clicked, query is removed from page and array
    $(document).on('click', '#del', function(){
        $(this).parent().remove();
        var indexOfElementToRemove = queries.indexOf($(this).next().next().clone().html());
        queries.splice(indexOfElementToRemove,1);
    });

   
    //When Edit button is clicked, query is changed to contents of query box
    $(document).on('click', '#edit', function() {
        //If new query (changed query) is not in queries array then change it
        if (!(queries.contains($('input[name=queryBox]')))) {
            var newString = $('input[name=queryBox]').val();
            var indexOfElementToBeChanged = queries.indexOf($(this).next().clone().html());
            queries[indexOfElementToBeChanged] = newString;
            $(this).next().html(newString);
            $('#list').append(queries.toString());
        }
    });

    //When Clear All button is clicked, all queries are removed
    $('button[name=clear]').click(function(){
       $('ol').empty();
       queries = [];
    });

    //Passing queries array to python abstract evaluation
    $('button[name=search]').click(function(){
        var new_data = ['a','b','c','d','e'];
        $.get('/SARS/abstractevaluation/', {'data': queries},function(data){});
    });
});
