const user_name = document.getElementById("user_name")
const passW = document.getElementById("passW")
const submit_btn = document.getElementById("submit")
const logout_btn = document.getElementById("logout")



async function sendValues() {
    if(user_name.value && passW.value){
        const payload ={
        "username":user_name.value,
        "password":passW.value
         }
    const response = await fetch("/login", {
      method: "POST", 
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload), 
    })
        
        if (response.redirected){
            console.log(response)
            window.location.href = response.url
            
        }else{
            const data = await response.json()
            console.log(data)
        }
    
}
}
if(logout_btn){
logout_btn.addEventListener("click",function(){
    alert("HI")
})
}


if(submit_btn)
    submit_btn.addEventListener("click",sendValues)

