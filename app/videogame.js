function VideogameObject(f1, f2, f3, f4, f5, f6) {
    
    this.title = f1;
    this.developer = f2;
    this.publisher = f3;
    this.year = f4;
    this.description = f5;
    this.genre = f6
    
    this.image = sessionStorage.urlImage;
    
    this.token = sessionStorage.token;
    
    this.toJsonString = function () { return JSON.stringify(this); };

};


function addVideogame()
{
	try
  {
    //alert("token : " + sessionStorage.token);

  	var myData = new VideogameObject(
     $("#title_vg").val(), 
     $("#developer_vg").val(),
     $("#publisher_vg").val(),
     $("#year_vg").val(),
     $("#description_vg").val(),
     $("#genre_vg").val()  
     );
  	alert(myData.toJsonString());

  	 jQuery.ajax({
           type: "POST",
           url: "http://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/videogames_api/v1/videogames/insert",
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


function getVideogameList()
{
  try
  {
    //alert("token : " + sessionStorage.token);

    var myData = new TokenObject();
    
    alert(myData.toJsonString());

     jQuery.ajax({
           type: "POST",
           url: "http://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/videogames_api/v1/videogames/list",
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
                url: "http://proyecto2-rafaelantoniocomonfo.appspot.com/up",
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

function GoBack()
{
	window.history.back();
}
