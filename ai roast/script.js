
const name_btn = document.getElementById("name")
const abt = document.getElementById("abt_para")
const btn= document.getElementById("submit")
const roasts_p =document.getElementById("roasts")

const dialog_overlay = document.getElementById("dialog_overlay");
const dialog_roast = document.getElementById("dialog_roast");
const close_dialog = document.getElementById("close_dialog");
const roast_again = document.getElementById("roast_again")
const roasts = [
    "You really thought this was a good idea.",
    "I've seen better decisions made by a potato.",
    "Your confidence is impressive considering the evidence.",
    "You somehow managed to make this worse.",
    "Even your computer is disappointed in you."
];
btn.addEventListener('click',function(){
    if(name_btn.value && abt.value){

    //alert("Your roast is created.")
    createRoasts(name_btn.value,abt.value)
    }else{
        alert("Please enter the details :(")
    }
})

function createRoasts(name,abt){
    const selected_index_roast = getRangeIndex(0,roasts.length)
     abt = abt.toLowerCase()
    .replace(/\bi\b/g, "you")
    .replace(/\bam\b/g, "are");
    
   const roast_struc = [`So ${name}. Heres what i got to know,${abt}.But honestly ${roasts[selected_index_roast]}`,`Hello ${name}. ${abt} !!???.But honestly ${roasts[selected_index_roast]}`]
  
    const selected_index_roastStruc =getRangeIndex(0,roast_struc.length)
    
   
    
   dialog_roast.textContent = roast_struc[selected_index_roastStruc]
    dialog_overlay.classList.add("show");
  
}

function getRangeIndex(min,max){
   const index =(Math.floor(Math.random() * (max-min) ))
   return index
}

close_dialog.addEventListener("click",()=>dialog_overlay.classList.remove("show"))
dialog_overlay.addEventListener("click", function(event) {
    if (event.target === dialog_overlay) {
        dialog_overlay.classList.remove("show");
    }
});

roast_again.addEventListener("click",() => createRoasts(name_btn.value,abt.value))