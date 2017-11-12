function DeveloperObject(f1, f2, f3) {
    
    this.nameA = f1;
    this.location = f2;
    this.year = f3;
    
    this.logo = sessionStorage.urlImage;
    
    this.token = sessionStorage.token;
    
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
           url: "http://localhost:8080/_ah/api/developers_api/v1/developers/insert",
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


function getDeveloperList()
{
  try
  {
    //alert("token : " + sessionStorage.token);

    var myData = new TokenObject();
    
    alert(myData.toJsonString());

     jQuery.ajax({
           type: "POST",
           url: "http://localhost:8080/_ah/api/developers_api/v1/developers/list",
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
                url: "http://localhost:8080/up",
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