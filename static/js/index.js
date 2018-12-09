function myFunction(args) {
   location.href = "edit_contact";
}

$(document).ready(function(){


$(".edit_button" ).click(function(e) {
  var $item = $(this).closest("tr")   // Finds the closest row <tr> 
                       .find(".email_class")     // Gets a descendent with class="nr"
                       .text();
var url = "http://127.0.0.1:5000/edit_contact_page?add=" + $item
window.location = url;

});

$(".delete_button" ).click(function(e) {
  var $item = $(this).closest("tr")   // Finds the closest row <tr> 
                       .find(".email_class")     // Gets a descendent with class="nr"
                       .text();

    var r = confirm("Are you sure you want to delete the record,Press yes to continue or cancel");
    if (r == true) {
    var $item = $(this).closest("tr")   // Finds the closest row <tr> 
                       .find(".email_class")     // Gets a descendent with class="nr"
                       .text();

 
    $.ajax({ url: 'http://127.0.0.1:5000/delete_contact', success: function(){},data: {'val1':$item}, type: 'POST' ,success:function(response){
     alert(response);}  });

    var url = "http://127.0.0.1:5000/" 
    window.location = url;
  
   }   

     

});



});



function fun1(arg)
{
    $.ajax({ url: 'http://127.0.0.1:5000/change_page_contact', success: function(){},data: {'val1':arg}, type: 'POST' ,success:function(response){var myDiv = $('#super-div-1'); 
        myDiv.html(response);
       }  });
    
}


function fun2(arg)
{
    $.ajax({ url: 'http://127.0.0.1:5000/change_page_search', success: function(){},data: {'val1':arg}, type: 'POST' ,success:function(response){var myDiv = $('#super-div-2'); 
        myDiv.html(response);
       }  });
    
}
/*
function required() {
alert("hwllo");    
    var input1 = document.forms["form1"]["name"].value;
    var input2 = document.forms["form1"]["email_add"].value;
    var input3 = document.forms["form1"]["phone"].value;
if((input1 == "") || (input2 == "") || (input3 == "")) 
{
alert("Please input a Value");
return false;
}
else 
{
return true; 
}
}
*/
/*
//
//$.ajax({ url: 'http://127.0.0.1:5000/page_next', success: function(){},data: {'val1':arg}, type: 'POST' ,success:function(response)
//        {}  });
*/





