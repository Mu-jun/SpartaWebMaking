// signup
async function sign_checkID(id) {
    let isPassibleID = false;

    let response = await fetch('/sign/checkID', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(id)
    }).then(result=>result.json());
    
    let result = '';

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

async function sign_checkNickname(nickname) {
    let isPassibleNickname = false;
    let response = await fetch('/sign/checkNickname', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(nickname)
    }).then(result=>result.json());

    let result = '';

    if(response['success']) {
        isPassibleNickname = true;
        result = response['success'];
    }else if (response['fail']) {
        result = response['fail'];
    }    

    return {
        'isPassible': isPassibleNickname,
        'msg' : result
    }

}

async function sign_signup(id,password,nickname) {
    let response = await fetch('/sign/signup_test', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
          },
        body: JSON.stringify({ 
            'id_give': id,
            'pass_give': password,
            'nickname_give': nickname
        })
    }).then(result=>{
        console.log(result);
        if(result.ok) return result.json();
        else return null;
    });

    return response;
}

//  sign in
async function sign_signin(id,password) {
    let response = await fetch('/signin')
}

// sign information

async function test_delete_user(id,password) {

    
}