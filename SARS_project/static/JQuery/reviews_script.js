$(document).ready(function(){
    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    //###########################################################
    //Variable to hide/show create review fields
    var bool = false;
    var tool = false;

    //Hide create and edit review fields
    $('#createContainer').hide();
    $('#editContainer').hide();
    $('#id_title').attr("id", "id_title1");
    $('#id_description').attr("id", "id_description1");

    //When create button is pressed, show create review fields
    $('#create').click(function(){
        bool = !bool;
        $('#createContainer').toggle(bool);
    });

    //When edit button is pressed, show edit review fields
    $('#edit').click(function(){
        tool = !tool;
        $('#editContainer').toggle(tool);
    });

    //Edit review button
    $('#editReview').click(function(){
        var title = $('#id_title').val();
        var descr = $('#id_description').val();
        $.ajax({
            url: '/SARS/reviews/',
            type: "POST",
            data: {operation : 'edit', 'title' : $(document.getElementById("hlighted")).html(), 'editTitle': title, 'description' : $(document.getElementById("hlighted")).next().html(), 'editDescription':descr}
        });
        $(document.getElementById("hlighted")).html(title);
        $(document.getElementById("hlighted")).next().html(descr);
    });

    //Delete review button
    $('#delReview').click(function(){
        $.ajax({
            url: '/SARS/reviews/',
            type: "POST",
            data: {operation : 'delete', 'title' : $(document.getElementById("hlighted")).html(), 'description' : $(document.getElementById("hlighted")).next().html()}
        });
        $(document.getElementById("hlighted")).parent().remove();
    });

    //When row in table is clicked, highlight blue
    $(document).ready(function(){
        $('table tbody tr').click(function(){
            $(this).children().attr("id", "hlighted");
            $(this).closest("tr").siblings().removeClass("highlighted");
            $(this).closest("tr").siblings().children().attr("id", "");
            $(this).toggleClass("highlighted");
        });
    });
});