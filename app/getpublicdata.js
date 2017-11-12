
function getData() 
{
	sessionStorage.empresa = "kubeet";

    jQuery.support.cors = true;
    
    //Llama todas las funciones que toman el usuario actual y regresan todos sus entradas en la BD
    //getTweetsData();
    getVideogamesData();
    getPublishersData();
    getDevelopersData();
    getGenresData();
    
    alert ("Usuario loggeado: " + sessionStorage.user);
}

function getVideogamesData()
{
	try
    {                         
     $.ajax({
	    url: "/getvideogames",
	    dataType: 'json',
	    cache: false,
	    contentType: false,
	    processData: true,
	    data: {user: sessionStorage.user},                         
	    type: 'get',
	    crossDomain: true,
	    success: function(response) {
	  	entries = response; //all the entities returned by the handler in public_rest_api
	    //alert(response);
		  entries.forEach(function (i) 
		  {
		     var nombre = "<div class='col-md-3 col-sm-3 wow fadeInUp' " +
			" data-wow-delay='0.2s'> " +
		                "<img src='" + i.image + "'" +
		                " class='img-responsive img-circle' alt='team img' heigth='150' width='150'" +
		                " >" +
		                " <div class='section-title wow bounceIn'> " +
		                "<h3>" + "Title: " + i.title + "</h3>" +
		                "<h5>" + "Developer: " + i.developer + "</h5>" +
		                "<h5>" + "Publisher: " + i.publisher + "</h5>" +
		                "<h5>" + "Release year: " + i.year + "</h5>" +
		                "<h5>" + "Description: " + i.description + "</h5>" +
		                "<h5>" + "Genre: " + i.genre + "</h5>" +
		                "</div>" +
		                "</div>" 
		               $("#videogames").append(nombre);
		   });
	   
 	 	}
        });          
     
    }
 	catch(e)
    {
      alert("error : " +  e);
     }
}

function getPublishersData()
{
	try
    {                         
     $.ajax({
	    url: "/getpublishers",
	    dataType: 'json',
	    cache: false,
	    contentType: false,
	    processData: true,
	    data: {user: sessionStorage.user}, //only the entities of current user are returned                       
	    type: 'get',
	    crossDomain: true,
	    success: function(response) {
	  	entries = response; //all the entities returned by the handler in public_rest_api
	    //alert(response);
		  entries.forEach(function (i) 
		  {
		     var nombre = "<div class='col-md-3 col-sm-3 wow fadeInUp' " +
			" data-wow-delay='0.2s'> " +
		                "<img src='" + i.logo + "'" +
		                " class='img-responsive img-circle' alt='team img' heigth='150' width='150'" +
		                " >" +
		                " <div class='section-title wow bounceIn'> " +
		                "<h3>" + "Name: " +i.nameA + "</h3>" +
		                "<h5>" + "Location: "+ i.location + "</h5>" +
		                "<h5>" + "Year: " + i.year + "</h5>" +
		                "</div>" +
		                "</div>" 
		               $("#publishers").append(nombre);
		   });
	   
 	 	}
        });          
     
    }
 catch(e)
    {
      alert("error : " +  e);
     }
}

function getDevelopersData()
{
	try
    {                         
     $.ajax({
	    url: "/getdevelopers",
	    dataType: 'json',
	    cache: false,
	    contentType: false,
	    processData: true,
	    data: {user: sessionStorage.user}, //only the entities of current user are returned                       
	    type: 'get',
	    crossDomain: true,
	    success: function(response) {
	  	entries = response; //all the entities returned by the handler in public_rest_api
	    //alert(response);
		  entries.forEach(function (i) 
		  {
		     var nombre = "<div class='col-md-3 col-sm-3 wow fadeInUp' " +
			" data-wow-delay='0.2s'> " +
		                "<img src='" + i.logo + "'" +
		                " class='img-responsive img-circle' alt='team img' heigth='150' width='150'" +
		                " >" +
		                " <div class='section-title wow bounceIn'> " +
		                "<h3>" + "Name: " + i.nameA + "</h3>" +
		                "<h5>" + "Location: " + i.location + "</h5>" +
		                "<h5>" + "Year: " + i.year + "</h5>" +
		                "</div>" +
		                "</div>" 
		               $("#developers").append(nombre);
		   });
	   
 	 	}
        });          
     
    }
 catch(e)
    {
      alert("error : " +  e);
     }
}

function getGenresData()
{
	try
    {                         
     $.ajax({
	    url: "/getgenres",
	    dataType: 'json',
	    cache: false,
	    contentType: false,
	    processData: true,
	    data: {user: sessionStorage.user}, //only the entities of current user are returned                       
	    type: 'get',
	    crossDomain: true,
	    success: function(response) {
	  	entries = response; //all the entities returned by the handler in public_rest_api
	    //alert(response);
		  entries.forEach(function (i) 
		  {
		     var nombre = "<div class='col-md-3 col-sm-3 wow fadeInUp' " +
			" data-wow-delay='0.2s'> " +
		                " <div class='section-title wow bounceIn'> " +
		                "<h3>" + "Genre: " + i.nameA + "</h3>" +
		                "<h5>" + "Description: " + i.description + "</h5>" +
		                "</div>" +
		                "</div>" 
		               $("#genres").append(nombre);
		   });
	   
 	 	}
        });          
     
    }
 catch(e)
    {
      alert("error : " +  e);
     }
}

function getTweetsData()
{
	try
    {                         
     $.ajax({
	    url: "/gettweets",
	    dataType: 'json',
	    cache: false,
	    contentType: false,
	    processData: true,
	    data: {empresa: sessionStorage.empresa},                         
	    type: 'get',
	    crossDomain: true,
	    success: function(response) {
	  	tweets = response;
	    //alert(response);
		  tweets.forEach(function (tweet) 
		  {
		     var nombre = "<div class='col-md-3 col-sm-3 wow fadeInUp' " +
			" data-wow-delay='0.2s'> " +
		                "<img src='" + tweet.urlImage + "'" +
		                " class='img-responsive img-circle' alt='team img' heigth='150' width='150'" +
		                " >" +
		                " <div class='section-title wow bounceIn'> " +
		                "<h3>" + tweet.title + "</h3>" +
		                "<h5>" + tweet.description + "</h5>" +
		                "</div>" +
		                "</div>" 
		               $("#tweets").append(nombre);
		   });
	   
 	 	}
        });          
     
    }
 catch(e)
    {
      alert("error : " +  e);
     }
}


