function GenreObject(f1, f2) {
    
    this.nameA = f1;
    this.description = f2;
    
    this.token = sessionStorage.token;
    
    this.toJsonString = function () { return JSON.stringify(this); };
};


function addGenre()
{
	try
  {
    //alert("token : " + sessionStorage.token);

  	var myData = new GenreObject(
     $("#name_gen").val(), 
     $("#description_gen").val()
     );
  	alert(myData.toJsonString());

  	 jQuery.ajax({
           type: "POST",
           url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/genres_api/v1/genres/insert",
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


function TokenObject() {
    
    this.tokenint = sessionStorage.token;
    this.toJsonString = function () { return JSON.stringify(this); };

};

function KeyObject(f1) {
    
    this.tokenint = sessionStorage.token;
    this.entityKey = f1;
    this.toJsonString = function () { return JSON.stringify(this); };

};


function getGenresList()
{
  try
  {
    //alert("token : " + sessionStorage.token);

    var myData = new TokenObject();
    
    alert(myData.toJsonString());

     jQuery.ajax({
           type: "POST",
           url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/genres_api/v1/genres/list",
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

function goToUpdateGenre(theKey)
{
    sessionStorage.updateModelKey = theKey;

    window.location.href='/genreupdate';
    //window.location = "/genreupdate.html";
}

function setupUpdateGenre()
{
    //alert("token: " + sessionStorage.token + ", key to update: " + sessionStorage.updateModelKey);

    var myData = new KeyObject(sessionStorage.updateModelKey);


    jQuery.support.cors = true;
    try
    {
        jQuery.ajax({
            type: "POST",
            url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/genres_api/v1/genres/get",
            data: myData.toJsonString(),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) { //si no funciona, quizas se deba recorrer como arreglo, tal como se hace en getpublicdata.js?
                 alert (response.data);

                 $("#name_gen").val() = response.data.nameA;
                 $("#description_gen").val() = response.data.description;
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

function updateGenre()
{
    //we could also try just calling the update api from web_token_api
    deleteGenre(sessionStorage.updateModelKey); //borra primero
    addGenre () //después agregalo con o sin cambios
}

function deleteGenre(theKey)
{
    jQuery.support.cors = true;
    try
    {
        jQuery.ajax({
            type: "POST",
            url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/genres_api/v1/genres/delete",
            data: {tokenint: sessionStorage.token, entityKey: theKey}, //if this doesn't work, declare an object type and send the json
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) { 
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
