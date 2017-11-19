function DeveloperObject(f1, f2, f3) {
    
    this.nameA = f1;
    this.location = f2;
    this.year = f3;
    
    this.logo = sessionStorage.urlImage;
    
    this.token = sessionStorage.token;
    
    this.toJsonString = function () { return JSON.stringify(this); };
};



function TokenObject() {
    
    this.tokenint = sessionStorage.token;
    this.toJsonString = function () { return JSON.stringify(this); };

};


function KeyObject(f1) {
    
    this.tokenint = sessionStorage.token;
    this.entityKey = f1;
    this.toJsonString = function () { return JSON.stringify(this); };

};

function addDeveloper()
{
	try
  {
    //alert("token : " + sessionStorage.token);

  	var myData = new DeveloperObject(
     $("#name_dev").val(), 
     $("#location_dev").val(),
     $("#year_dev").val() 
     );
  	alert(myData.toJsonString());

  	 jQuery.ajax({
           type: "POST",
           url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/developers_api/v1/developers/insert",
           data: myData.toJsonString(),
           contentType: "application/json; charset=utf-8",
           dataType: "json",
           success: function (response) {
                // do something
                alert (response.code + " " + response.message);
           },
       
           error: function (error) {            
                // error handler
                alert("error :" + error.message)
           }

       });

   }
   catch(error)
   {
    alert(error);
   }

}

function getDeveloperList()
{
  try
  {
    //alert("token : " + sessionStorage.token);

    var myData = new TokenObject();
    
    alert(myData.toJsonString());

     jQuery.ajax({
           type: "POST",
           url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/developers_api/v1/developers/list",
           data: myData.toJsonString(),
           contentType: "application/json; charset=utf-8",
           dataType: "json",
           success: function (response) {
                // do something
                
                alert (response.data);
           },
       
           error: function (error) {            
                // error handler
                alert("error :" + error.message)
           }

       });

   }
   catch(error)
   {
   	alert(error);
   }

}

function goToUpdateDeveloper(theKey)
{
    sessionStorage.updateModelKey = theKey;

    window.location.href='/developerupdate';

    //window.location = "/developerupdate.html";
}

function setupUpdateDeveloper()
{
    //alert("token: " + sessionStorage.token + ", key to update: " + sessionStorage.updateModelKey);

    var myData = new KeyObject(sessionStorage.updateModelKey);

    jQuery.support.cors = true;
    try
    {
        jQuery.ajax({
            type: "POST",
            url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/developers_api/v1/developers/get",
            data: myData.toJsonString(),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) { 
                 
                entity = response.data;

                entity.forEach(function (i){
                    $("#name_dev").val(i.nameA);
                    $("#location_dev").val(i.location);
                    $("#year_dev").val(i.year);
                    $("#url_photo").val(i.logo);
                    uploadDemo(); 
                });
                 
            },
        
            error: function (error) {            
                 // error handler
                 alert("error :" + error.message)
                 GoBack(); //regresa para evitar que se repita el error
            }
 
        });
    }
    catch(e)
    {
      alert("error : " +  e);
      GoBack(); //regresa para evitar que se repita el error
    }
}

function updateDeveloper()
{
    addDeveloper ();
    //we could also try just calling the update api from web_token_api
    deleteDeveloper (sessionStorage.updateModelKey);
}

function deleteDeveloper(theKey)
{
    var myData = new KeyObject(theKey);

    jQuery.support.cors = true;
    try
    {
        jQuery.ajax({
            type: "POST",
            url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/developers_api/v1/developers/delete",
            data: myData.toJsonString(), 
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) { //si no funciona, quizas se deba recorrer como arreglo, tal como se hace en getpublicdata.js?
                 alert (response.message);
            },
            error: function (error) {            
                 // error handler
                 alert("error :" + error.message)
            }
        });
    }
    catch(e)
    {
      alert("error : " +  e);
    }

    GoBack();
}

//Sets the selected image as preview
function uploadDemo()
{
    var file_data = $("#uploaded_file").prop("files")[0];
    var form_data = new FormData();
    form_data.append("uploaded_file", file_data)

    jQuery.support.cors = true;
    try
    {
     $.ajax({
                url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/up",
                dataType: 'text',
                cache: false,
                contentType: false,
                processData: false,
                data: form_data,
                type: 'post',
                crossDomain: true,
                success: function(response){

                                document.getElementById("preview").src=response;

                                sessionStorage.urlImage = response;

                                document.getElementById("url_photo").value = response;
                }
      });
    }
    catch(e)
    {
      alert("error : " +  e);
     }
}

//Goes back to index.html
function GoBack()
{
    //window.history.back();
    window.location = "/";
}
