window.addEventListener("DOMContentLoaded", (event) => {
    document.getElementById("send").addEventListener("click", addBookmark);
    statusCheck();
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
      chrome.tabs.query({ currentWindow: true, active: true }, (tabs) => {
        if (chrome.runtime.lastError) {
          reject(chrome.runtime.lastError);
        } else {
          resolve(tabs[0].url);
        }
      });
    });
}

function addBookmark()
{
    link = "";
    getCurrentTab()
    .then(link => {

        things ={
            name: document.getElementById("inputName").value,
            url: link,
            folder: null
        }

        things = JSON.stringify(things);
        console.log(things);
    
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

    })
}