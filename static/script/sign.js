async function sign_checkID(id) {
    let isPassibleID = false;

    let response = await fetch('/sign/checkID', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(id)
    }).then(result=>result.json());    

    let result

    if(response['success']) {
        isPassibleID = true;
        result = response['success'];
    }else if (response['fail']) {
        result = response['fail'];
    }    

    return {
        'isPassible': isPassibleID,
        'msg' : result
    }
    
}