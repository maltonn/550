
function Randint(mx){
  return Math.floor(Math.random() * mx);
}

function GetPrice(menu){
  for(let i=0;i<menus.length;i++){
    if(menus[i][0]==menu){
      return menus[i][1]
    }
  }
}

menus_list_btn.addEventListener('click',()=>{
    for(j=0;j<menus.length;j++){
      elm=document.createElement('div')
      elm.innerHTML='<div>'+menus[j][0]+'</div><div>￥'+menus[j][1]+'</div>'
      menus_list.appendChild(elm)
    }
    menus_list.style.transform="translateY(0)"
    close_menus_list.style.display="block"
})
close_menus_list.addEventListener('click',function(){
  this.style.display="none"
  menus_list.style.transform="translateY(100%)"
  setTimeout(()=>{
    menus_list.innerHTML=""
  },300)
})


settings_btn.addEventListener('click',()=>{
  settings.style.transform="translateY(0)"
  close_settings.style.display="block"
})
close_settings.addEventListener('click',function(){
  this.style.display="none"
  settings.style.transform="translateY(100%)"
})


main_btn.addEventListener('click',()=>{
  main_contents.innerHTML=''
  r=Randint(colab.length)
  menu=colab[r]
  for(let i=0;i<menu.length;i++){
    div=document.createElement('div')
    div.classList.add('menu')
    div.innerText=menu[i]+' (¥'+GetPrice(menu[i])+')'
    if(menu[i].length>=6){
      div.style.fontSize="1.5rem"
    }
    main_contents.appendChild(div)
  }
})