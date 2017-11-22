// contact
function LoginObject(myEmail, myPasswd) {
    this.email = myEmail;
    this.password = myPasswd;
    this.toJsonString = function () { return JSON.stringify(this); };

};

function UserAddObject(myEmail, myPasswd) {
    this.email = myEmail;
	this.password = myPasswd;
	
	this.token = sessionStorage.token;
    //this.empresa_key = "5629499534213120"; //hard coded
    this.toJsonString = function () { return JSON.stringify(this); };

};

function loginDemo()
{
	//alert("testing...")
	var myData = new LoginObject(
    $("#email").val(), 
    $("#passwd").val());
	
    alert(myData.toJsonString());

	 jQuery.ajax({
         type: "POST",
         url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/usuarios_api/v1/users/login",
         data: myData.toJsonString(),
         contentType: "application/json; charset=utf-8",
         dataType: "json",
         success: function (response) {
              // do something
              sessionStorage.token = response.token;
              sessionStorage.user = response.message; //guarda el correo del usuario actual
              alert ("token generado: " + sessionStorage.token);
              alert ("Usuario loggeado: " + sessionStorage.user);
              window.location = "/";

         },
     
         error: function (error) {            
              // error handler
              alert("error: " +error)
         }

     });
}

function logout()
{
    sessionStorage.removeItem('user');
    sessionStorage.removeItem('token');
    window.location = "/"; //as update 
}

function signUp()
{
    var myData = new UserAddObject(
        $("#email").val(), 
        $("#passwd").val());

    alert(myData.toJsonString());
    
    jQuery.ajax({
        type: "POST",
        url: "https://proyecto2-rafaelantoniocomonfo.appspot.com/_ah/api/usuarios_api/v1/users/insert",
        data: myData.toJsonString(),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (response) {
            // do something
            alert (response.message);
            window.location = "/login";
        },
    
        error: function (error) {            
            // error handler
            alert("error in sing up: " + error.message);
            window.location = "/";
        }

    });
}
