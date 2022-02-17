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
    let response = await fetch('/sign/signup', {
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
    let response = await fetch('/sign/signin',{
            method:"POST",
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify({ 
                'id_give': id,
                'pass_give': password,                
            })
        }).then(result=>{
            if(result.ok) return result.json();
            else return null;
        });

    return response;
}

// sign out
function sign_signout() {
    unset_token();
}

// status
function unset_token() {
    fetch('/unset_token');
}

async function get_access_token() {
    let result = await fetch('get_access_token');    
    let token = '';

    if(result.ok) token = await result.json();
    
    return token;
}

async function get_refresh_token() {
    let result = await fetch('get_refresh_token');
    let token = '';

    if(result.ok) token = await result.json();
    console.log(token);
    return token;
}

function refreshing(refresh_token) {
    $.ajax({
        type: "GET",
        url: "/refresh",
        headers: {"Authorization": "Bearer "+ refresh_token},
        success: function(response){
            console.log(response.json())           
        }
    })
}

function get_payload(token) {

    console.log(token)

    let payload = '';
    if(token){
        let base64Payload = token.split('.')[1]; //value 0 -> header, 1 -> payload, 2 -> VERIFY SIGNATURE
        payload = atob(base64Payload);
        
        console.log(payload);
    }
    return payload;
}

function get_payload_exp(token) {

    let exp = get_payload(token).split("exp")[1].slice(2,12);
    console.log(exp);

    return +exp;
}

async function check_token() {
    let isToken = false;
    let date = new Date();
    let numberic_date = parseInt(date/1000)           
    
    let access_token = await get_access_token();            

    if(access_token) {
        let access_payload_exp = get_payload_exp(access_token);            

        if(access_payload_exp > numberic_date) {
            isToken = true;
        } else {
            let refresh_token = await get_access_token();                        
            let refresh_payload_exp = get_payload_exp(refresh_token);            

            if(refresh_payload_exp > numberic_date) {
                refresh();
                isToken = true;
            }
            
        }
    }
    return isToken;
}

// sign information change
async function signDelete(password) {
    await check_token();
    let access_token = await get_access_token();

    let response = await fetch('/sign/delete_user',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            "Authorization": "Bearer "+ access_token
        },
        body: JSON.stringify({'pass_give': password})
    }).then(result=>result.json());
    
    return response;
}

async function signChangePassword(currentPassword,newPassword) {
    await check_token();   
    let access_token = await get_access_token();
    let response = await fetch('/sign/change_pass',{
            method:"POST",
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                "Authorization": "Bearer "+ access_token
            },
            body: JSON.stringify({
                'pass_give': currentPassword,
                'new_pass_give': newPassword                    
            })
        }).then(result=>result.json());

    return response;    
}