// register form
let emptyRegForm = $("#empty_form");
let regForm = $(".reg_form");
let clone = emptyRegForm.clone();

// remove empty register form
emptyRegForm.remove()



// add new form
$("#add_reg").on("click", function(event){
event.preventDefault()

    // form mgt
    let totalFormEle = $("#id_form-TOTAL_FORMS");
    let totalFormCount = +totalFormEle.attr("value")
    let emptyClone = clone.clone()

    // create new form
    emptyClone.find('input, select').each(function(event){
        
        //get name attr
        let eachName = $(this).attr('name');

        //skip if undefined
        if( typeof(eachName) == 'undefined') return true

        //change name attr
        let newName = eachName.replace('__prefix__', totalFormCount)
        $(this).attr('name', newName)
    })

    // change totalCount
    $("#id_form-TOTAL_FORMS").attr('value', ++totalFormCount)
    emptyClone.attr('id', 'clone')

    regForm.append(emptyClone)
});

