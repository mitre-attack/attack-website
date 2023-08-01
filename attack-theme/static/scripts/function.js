function toggleNav(){
    navSize = document.getElementById("mySidebar").style.width
    displayType = document.getElementById("mySidebar").style.display
    if (displayType == 'none' || displayType == ''){
      document.getElementById("mySidebar").style.width = ''
      document.getElementById("mySidebar").style.display = 'block'
    }
    else{
      document.getElementById("mySidebar").style.width = '0px'
      document.getElementById("mySidebar").style.display = ''
    }
  }