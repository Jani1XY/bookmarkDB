window.addEventListener("DOMContentLoaded", (event) => {
    document.getElementById("send").addEventListener("click", addBookmark);
    document.getElementById("delete").addEventListener("click", deleteBookmark);
    statusCheck();
    checkIfInDatabase();
});

function bmSpanSet(message)
{document.getElementById("bmSpan").innerHTML = message;}

async function statusCheck()
{
    /*
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200)
        {
            // nothing o((>ω< ))o
            if(this.status == 200)
            {
                document.getElementById("status").innerHTML = "ONLINE";
                document.getElementById("status").style.color = "lightgreen";
            }

        }
    };
    xhttp.open("GET", "http://127.0.0.1:4321/ping", true);
    xhttp.send();
    */
    const response = await fetch("http://127.0.0.1:4321/ping");

    try{
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        
        if(response.status === 200){
            document.getElementById("status").innerHTML = "ONLINE";
            document.getElementById("status").style.color = "lightgreen";
        }
    }
    catch(error){
        console.error(error.message);
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function getCurrentTab() {
    return new Promise((resolve, reject) => {
      browser.tabs.query({ active: true, currentWindow: true })
        .then(tabs => {
          if (tabs.length > 0) {
            resolve(tabs[0].url); 
          } else {
            reject("No active tab found."); 
          }
        })
        .catch(error => {
          reject(error);
        });
    });
}

async function addBookmark()
{
  link = await getCurrentTab();

  try{
    things ={
        name: document.getElementById("inputName").value,
        url: link,
        folder: null
    };

    things = JSON.stringify(things);
    console.log(things);
  
      /*
      var xhttp = new XMLHttpRequest();
      xhttp.onload = function() {
          if (this.status >= 200 && this.status < 300)
          {

              console.log("Successfully send data. Server Response: ", this.responseText);
              console.log("Status Code:", this.status);
              
              bmSpanSet(this.responseText);
              
          } else {
              bmSpanSet(this.responseText);
              console.log("Failed to process. Server Response:", this.responseText);
              console.error('Error:', this.status, this.statusText);
          }
      };
      xhttp.onerror = function() {
          console.error('Some kind of network error');
          bmSpanSet("Network error");
      };
      xhttp.open("POST", "http://127.0.0.1:4321/add", true);
      xhttp.setRequestHeader("Content-Type", "application/json");
      xhttp.send(things);
      */
      
    response = await fetch("http://127.0.0.1:4321/add", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'      
      },
      body: JSON.stringify(things), 
    })
    

    if (response.ok) {
      const result = await response.json();
      console.log(result);
      console.log('Success:', result.message);
      bmSpanSet(result.message);
    } 
    else {
      console.error('Error:', response.status, response.statusText);
      bmSpanSet('Error: ' + 'Status: ' + response.status + ' Status text: ' + response.statusText);
    }


  } catch (error) {
    console.error(error.message);  
  }

}


async function checkIfInDatabase()
{
  link = await getCurrentTab();

  try {
    
    theLink = {url: link};
  
    response = await fetch("http://127.0.0.1:4321/get", {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(theLink)
  })

    if (response.ok) {
      const result = await response.json();
      console.log(result);
      console.log('Server response:', result.message);

      if (result.exsist)
      {
        document.getElementById("delete").disabled = false;
        document.getElementById("send").disabled = true;
      }
      
    } 
    else {
      console.error('Error:', response.status, response.statusText);
      bmSpanSet('Error: ' + 'Status: ' + response.status + ' Status text: ' + response.statusText);
    }

  } catch (error) {
      console.error(error);
  }
}


async function deleteBookmark()
{
  link = await getCurrentTab();

  theLink = {url: link}

  try {

    response = await fetch("http://127.0.0.1:4321/delete/one", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(theLink)
    })


    if (response.ok) {
      const result = await response.json();
      console.log(result);
      console.log('Server response:', result.message);
      bmSpanSet(result.message);

      document.getElementById("delete").disabled = true;
      document.getElementById("send").disabled = false;

      
    } 
    else {
      console.error('Error:', response.status, response.statusText);
      bmSpanSet('Error: ' + 'Status: ' + response.status + ' Status text: ' + response.statusText);
    }
    
  } catch (error) {
    console.error(error);
  }

  
}