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

    //###################################################################################

    $("ol[id=query_list]").on('click', 'input[id=query_input]', function(){
        if($(this).parent().next('li').length == 0) {
            $("ol[id=query_list]").append('<li id="query_item"><select id="query_boolean"><option value="AND">AND</option><option value="OR">OR</option><option value="NOT">NOT</option></select><select id="query_property"><option value="All">All Fields</option><option value="Affiliation">Affiliation</option><option value="Author">Author</option><option value="Author+-+Corporate">Author - Corporate</option><option value="Author+-+First">Author - First</option><option value="Author+-+Full">Author - Full</option><option value="Author+-+Identifier">Author - Identifier</option><option value="Author+-+Last">Author - Last</option><option value="Book">Book</option><option value="Date+-+Completion">Date - Completion</option><option value="Date+-+Create">Date - Create</option><option value="Date+-+Entrez">Date - Entrez</option><option value="Date+-+MeSH">Date - MeSH</option><option value="Date+-+Modification">Date - Modification</option><option value="Date+-+Publication">Date - Publication</option><option value="EC%2FRN+Number">EC/RN Number</option><option value="Editor">Editor</option><option value="Filter">Filter</option><option value="Grant+Number">Grant Number</option><option value="ISBN">ISBN</option><option value="Investigator">Investigator</option><option value="Investigator+-+Full">Investigator - Full</option><option value="Issue">Issue</option><option value="Journal">Journal</option><option value="Language">Language</option><option value="Location+ID">Location ID</option><option value="MeSH+Major+Topic">MeSH Major Topic</option><option value="MeSH+Subheading">MeSH Subheading</option><option value="MeSH+Terms">MeSH Terms</option><option value="Other+Term">Other Term</option><option value="Pagination">Pagination</option><option value="Pharmacological+Action">Pharmacological Action</option><option value="Publication+Type">Publication Type</option><option value="Publisher">Publisher</option><option value="Secondary+Source+ID">Secondary Source ID</option><option value="Subject+-+Personal+Name">Subject - Personal Name</option><option value="Supplementary+Concept">Supplementary Concept</option><option value="Text+Word">Text Word</option><option value="Title">Title</option><option value="Title%2FAbstract">Title/Abstract</option><option value="Transliterated+Title">Transliterated Title</option><option value="Volume">Volume</option></select><input id="query_input" size="90"><button id="delete">Delete</button></li>');
        }
    });

    $("ol[id=query_list]").on('click', 'button[id=delete]', function(event){
        $(this).parent().remove();
    });

    $("button[id=clear_all]").click(function(event){
        $('ol').empty();
        $("ol[id=query_list]").append('<li id="query_item"><select id="query_property"><option value="All">All Fields</option><option value="Affiliation">Affiliation</option><option value="Author">Author</option><option value="Author+-+Corporate">Author - Corporate</option><option value="Author+-+First">Author - First</option><option value="Author+-+Full">Author - Full</option><option value="Author+-+Identifier">Author - Identifier</option><option value="Author+-+Last">Author - Last</option><option value="Book">Book</option><option value="Date+-+Completion">Date - Completion</option><option value="Date+-+Create">Date - Create</option><option value="Date+-+Entrez">Date - Entrez</option><option value="Date+-+MeSH">Date - MeSH</option><option value="Date+-+Modification">Date - Modification</option><option value="Date+-+Publication">Date - Publication</option><option value="EC%2FRN+Number">EC/RN Number</option><option value="Editor">Editor</option><option value="Filter">Filter</option><option value="Grant+Number">Grant Number</option><option value="ISBN">ISBN</option><option value="Investigator">Investigator</option><option value="Investigator+-+Full">Investigator - Full</option><option value="Issue">Issue</option><option value="Journal">Journal</option><option value="Language">Language</option><option value="Location+ID">Location ID</option><option value="MeSH+Major+Topic">MeSH Major Topic</option><option value="MeSH+Subheading">MeSH Subheading</option><option value="MeSH+Terms">MeSH Terms</option><option value="Other+Term">Other Term</option><option value="Pagination">Pagination</option><option value="Pharmacological+Action">Pharmacological Action</option><option value="Publication+Type">Publication Type</option><option value="Publisher">Publisher</option><option value="Secondary+Source+ID">Secondary Source ID</option><option value="Subject+-+Personal+Name">Subject - Personal Name</option><option value="Supplementary+Concept">Supplementary Concept</option><option value="Text+Word">Text Word</option><option value="Title">Title</option><option value="Title%2FAbstract">Title/Abstract</option><option value="Transliterated+Title">Transliterated Title</option><option value="Volume">Volume</option></select><input id="query_input" size="90"></li>');
    });

    $("button[id=search]").click(function(){
        var queryData = "";

        $( "li[id=query_item]" ).each(function( index ) {
            var $qInput = $(this).find("input[id=query_input]").val();
            var $qBool = $(this).find("select[id=query_boolean]").val();
            var $qProp = $(this).find("select[id=query_property]").val();

            if($qInput != "") {
                if ($qBool != undefined) {
                    queryData += "+" + $qBool + "+" + $qInput;
                } else {
                    queryData += $qInput;
                }

                if($qProp != "All") {
                    queryData += "[" + $qProp + "]"
                }
            }
        });

        $.ajax({
             url: '/SARS/abstractevaluation/',
             type: 'POST',
             data : { the_docs : queryData, quantity: $("input[name=quantity]").val()},
             success: function() {
                 window.location = '/SARS/abstractevaluation/';
             }
         });
    });

});
