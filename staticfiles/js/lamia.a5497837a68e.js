showModal = (name,desc,url,plc,catgry) => {
    console.log(name,desc,url)
    
    $("#label").text(name)
    $("#myModal").modal("show")
    $(".mod-img").attr("src",url)
    $("#img-desc").text(desc)
    $("#myurl").val(window.place.origin + url)
    $("#img-place").text("Place: " + plc)
    $("#img-category").text("Category: " + catgry)
   
}

copyUrl = () => {
    $("#myurl").select()
    document.execCommand('copy');
    alert("You Have Copied The Link Successfully")
}

