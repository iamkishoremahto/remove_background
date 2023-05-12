
upload_btn.addEventListener("click",function(){
    document.getElementById("file_upload").click()
    
  });

file_upload.addEventListener("change", function(){
    fileInput = document.getElementById('file_upload')
    document.getElementById('upload_btn_wrapper').innerHTML = `<div class="custom-loader"></div>`
    file = fileInput.files[0]
    
    upload(file)
    // console.log(file.name)
})
function change_upload_area(image_url){
    document.getElementById('home_wrapper').innerHTML = `
    
    
     
    <div class="col-md-8">
    <div id="show_area">
        <img src = "${image_url}" alt='removebg_image'
            class="img-fluid">
        <a href = ${image_url} class='btn btn-primary'
            download>Download</a>
    </div>
</div>
    `
}
async function upload(file){
    var formData = new FormData();
    formData.append("file", file);
    var request = new XMLHttpRequest();
    request.open("POST", "/upload");
    await request.send(formData);
    request.onload = function(){
        var image_url = request.responseText;
        change_upload_area(image_url)
        console.log(image_url)
    }
    

}
 