function PublisherObject(f1, f2, f3) {
    
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

function addPublisher()
{
    if ("user" in sessionStorage)
    {
        try
        {
            //alert("token : " + sessionStorage.token);
    
            var myData = new PublisherObject(
            $("#name_pub").val(), 
            $("#location_pub").val(),
            $("#year_pub").val() 
            );
            alert(myData.toJsonString());
    
            jQuery.ajax({
                type: "POST",
                url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/publishers_api/v1/publishers/insert",
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
    else
    {
       alert("No puedes agregar sin haber iniciado sesión");
       GoBack();
    }
}

function getPublisherList()
{
  try
  {
    //alert("token : " + sessionStorage.token);

    var myData = new TokenObject();
    
    alert(myData.toJsonString());

     jQuery.ajax({
           type: "POST",
           url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/publishers_api/v1/publishers/list",
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

//goes to the html to update a publisher and sets up a sessionStorage variable
function goToUpdatePublisher(theKey)
{
    sessionStorage.updateModelKey = theKey;

    window.location.href='/publisherupdate';
    //window.location = "/publisherupdate.html"; 
}

//requests and sets the values of the given object in the input boxes in publisherupdate.html on load
function setupUpdatePublisher()
{
    //alert("token: " + sessionStorage.token + ", key to update: " + sessionStorage.updateModelKey);

    var myData = new KeyObject(sessionStorage.updateModelKey);

    jQuery.support.cors = true;
    try
    {
        jQuery.ajax({
            type: "POST",
            url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/publishers_api/v1/publishers/get",
            data: myData.toJsonString(),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) { //si no funciona, quizas se deba recorrer como arreglo, tal como se hace en getpublicdata.js?
                 entity = response.data;

                entity.forEach(function (i){
                    $("#name_pub").val(i.nameA);
                    $("#location_pub").val(i.location);
                    $("#year_pub").val(i.year);
                    $("#url_photo").val(i.logo)
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

//makes the actual update when the user clicks the button in publisherupdate.html
function updatePublisher()
{
    addPublisher ();
    //we could also try just calling the update api from web_token_api
    deletePublisher (sessionStorage.updateModelKey);
}

//borra el publisher con la clave dada
function deletePublisher(theKey)
{
    var myData = new KeyObject(theKey);    

    jQuery.support.cors = true;
    try
    {
        jQuery.ajax({
            type: "POST",
            url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/publishers_api/v1/publishers/delete",
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
