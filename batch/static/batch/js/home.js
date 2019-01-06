const batchModel = $("#addBatch")
batchModel.modal()

//create new batch
$("#create_batch_form").submit(function(event){
event.preventDefault()

    form = $(this)
    formData = $(this).serialize()
    form_action = form.attr("actions")

    form.find('.err').html(null) // clear errors

    $.post(form_action, formData).done((response)=>{
        
        //success
        if(response['status']) {
            
            swal({
                'icon': 'success',
                'timer': 3000,
                'title': 'Success',
                'text': response['msg']
            }).then(function(){

                batchModel.modal('close')
                location.reload(true) // reload the page
            })

        }else{
        //unsuccess

            for(err in response.errors){
                
                // show err msg
                let fieldID = `#id_${err}`
                let input = form.find(fieldID)
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

// remove batch
$('#batch_remove a').on('click', function(event){
event.preventDefault()

    swal({
        title: "Are you sure?",
        text: "Once deleted, you will not be able to recover relevent this batch data !",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        
        if (willDelete) window.location.href = $(this).attr("href")
        else swal("Your batch data is safe!");
        
    });
})