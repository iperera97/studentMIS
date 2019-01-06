//student create model goes here
let studentModel = $('#create_studentModal')
studentModel.modal()

//create couseform get data and send to the server
$("#createCourseForm").submit(function(event){
event.preventDefault()

    let formData = $(this).serialize()
    $("#createCourseForm .err").html(null) // clear errors

    // send data to the server
    $.post('/courses/create/', formData).done(response => {

        //success
        if(response['status']) {
            
            swal({
                'icon': 'success',
                'timer': 3000,
                'title': 'Success',
                'text': response['msg']
            }).then(function(){
                studentModel.modal('close')
                location.reload(true) // reload the page
            })

        }else{
        //unsuccess
            let courseForm = $("#createCourseForm")

            for(err in response.errors){
                
                let fieldID = `#id_${err}`
                let input = courseForm.find(fieldID)
                let eachErr = response.errors[err]

                let errDiv = $("<div>")
                errDiv.addClass("err")

                eachErr.forEach(errItem=>{
                    
                    let span = $("<span>")
                    span.addClass("red lighten-1")
                    span.html(errItem.message)
                    
                    errDiv.append(span)
                })

                input.after(errDiv)
            }

        }
    }).fail(err => console.log(err))
})

// delete course
$("#course_remove_btn a").on("click", function(event){
event.preventDefault()

    swal({
        title: "Are you sure?",
        text: "Once deleted, you will not be able to recover relevent this course data !",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        
        if (willDelete) window.location.href = $(this).attr("href")
                
    });
})