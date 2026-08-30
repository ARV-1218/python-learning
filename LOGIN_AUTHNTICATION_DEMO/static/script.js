const name_txt = document.getElementById("name")
const pass = document.getElementById("pass")
const log_in = document.getElementById("log_in")

log_in.addEventListener("click",async function(){
    if(name_txt.value && pass.value){
    try {
        const formData = new FormData();
        formData.append("username",name_txt.value)
        formData.append("password",pass.value)
      
        const response = await fetch('/set', {
        method: 'POST',
        body: formData
        });

         const result = await response.json();
         console.log(result)
        const message = result["message"];
        
        
        if(message == "success" && response.ok){
            document.body.innerHTML =""
             
            const admin = document.createElement("button")
            admin.textContent ="VIEW ADMIN PANEL"
            admin.addEventListener("click",viewAdmin)

            const log_out = document.createElement("button")
            log_out.textContent = "Log OUT!"
            log_out.addEventListener("click",logOut)
            document.body.appendChild(admin)
            document.body.appendChild(log_out)
            getSession()
            
        }
    
    } catch (error) {
    console.error('Error submitting form:', error);
   } 
}else{
    alert("text fileds should not be empty")
}
})

async function getSession() {
    const response = await fetch("/get")
    if(response.ok)
        alert(await response.json())
}

async function logOut(){
    const response = await fetch("/clear")
    const data = await response.json()
      if (data["message"] == "logged-out") {
        window.location.href = "/";
    }
}

async function viewAdmin(){
    window.location.href = "/admin";
}
window.addEventListener("DOMContentLoaded",getSession)