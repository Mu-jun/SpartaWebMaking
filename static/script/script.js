        /* 01_login script */

/*
        $(document).ready(function () {

        });

*/

        function makeid() {

            let save_id = $('#ID').val()
            let save_pass = $('#PW').val()
            let save_pass_cf = $('#confirm_PW').val()
            let save_nick = $('#NickName').val()


            $.ajax({
                type: "POST",
                url: "/sign/signup",
                data: {
                    id_give: save_id,
                    pw_give: save_pass,
                    pw_cf_give: save_pass_cf,
                    nickname_give: save_nick,
                },
                success: function (response) {

                    if(response['fail']){
                        alert(response["fail"]);
                        window.location.reload();
                    }
                    else if(response['result'])
                    {
                        alert(response["result"]);
                        window.location.reload();
                    }
                    else if(response['result2'])
                    {
                        alert(response["result2"]);
                    }

                }

            })
        }

        function login() {

            let load_id = $('#id_login').val()
            let load_pass = $('#id_pass').val()


            $.ajax({
                type: "POST",
                url: "/sign/log_in",
                data: {
                    id_give: load_id,
                    pw_give: load_pass
                },
                success: function (response) {

                    if(response["success"]) {
                        alert(response["success"]);
                        let url_main = 'http://localhost:5000'

                        window.location.replace(url_main);
                    }
                    else if(response["fail"]){
                        alert(response["fail"]);
                        window.location.reload();
                    }

                }

            })
        }

        function checkID() {
            let id = $('#user_id').val();

            if ($('#user_id').val() == '') {
                alert('ID를 입력해라.')
                return;
            }

            $.ajax({
                type: "POST",
                url: "/sign/checkID",
                //dataType: "json",
                headers: {'Content-Type': 'application/json'},
                data: JSON.stringify(id),
                success: function (response) {

                    if(response["success"]) {
                        alert(response["success"]);                        
                    }
                    else if(response["fail"]){
                        alert(response["fail"]);
                    }                    
                }
            })
        }

        function checkNickname() {
            let nickname = $('#user_nick').val();

            if ($('#user_nick').val() == '') {
                alert('닉네임을 입력해라.')
                return;
            }

            $.ajax({
                type: "POST",
                url: "/sign/checkNickname",
                headers: {'Content-Type': 'application/json'},
                data: JSON.stringify(nickname),
                success: function (response) {

                    if(response["success"]) {
                        alert(response["success"]);                        
                    }
                    else if(response["fail"]){
                        alert(response["fail"]);                        
                    }                    
                }
            })
            
        }

        /* get_tea script */

         $(document).ready(function () {
            showTea();
        });

        // 이름순 정렬
        function showTea() {
            $.ajax({
                type: "GET",
                url: "/tea/list",
                data: {},
                success: function (response) {
                    let Tea = response['all_teas']
                    for(let i =0; i<Tea.length; i++){
                        let name = Tea[i]['name']
                        let type = Tea[i]['type']
                        let benefit = Tea[i]['benefit']
                        let caffeineOX = Tea[i]['caffeineOX']
                        let caffeine = Tea[i]['caffeine']
                        let benefitdetail = Tea[i]['benefitdetail']
                        let desc = Tea[i]['desc']
                        let caution = Tea[i]['caution']
                        let img = Tea[i]['img']
                        let like = Tea[i]['like']

                        let temp_html = `<p>name : ${name}</p>
                                         <img class="img-size" src="${img}"/>
                                         <p>${type}</p>
                                         <p>${benefit}</p>
                                         <p>${benefitdetail}</p>
                                         <p>${desc}</p>
                                         <p>${caffeineOX}</p>
                                         <p>${caffeine}</p>
                                         <p>${caution}</p>
                                         <p><button onclick="likeTea('${name}')" class="btn btn-outline-secondary">좋아요</button>좋아요 수 : ${like}</p>
                                         <p><button onclick="scrapTea('${name}')" class="btn btn-outline-secondary">찜</button></p>
                                         <p> ---------------------------------------------------------------------------------------------- </p>
                                         `
                        $('#box').append(temp_html)
                    }
                }
            })
        }

        // 검색 기능
        function search(){
            $.ajax({
                type: "GET",
                url: "/tea/list",
                data: {},
                success: function (response) {
                    $('#box').empty()
                    let teaKeyword = $('#teaName').val();
                    let Tea = response['all_teas']

                    for(let i =0; i<Tea.length; i++){
                        if(Tea[i]['name']==teaKeyword) {
                            let name = Tea[i]['name']
                            let type = Tea[i]['type']
                            let benefit = Tea[i]['benefit']
                            let caffeineOX = Tea[i]['caffeineOX']
                            let caffeine = Tea[i]['caffeine']
                            let benefitdetail = Tea[i]['benefitdetail']
                            let desc = Tea[i]['desc']
                            let caution = Tea[i]['caution']
                            let img = Tea[i]['img']
                            let like = Tea[i]['like']

                        let temp_html = `<p>name : ${name}</p>
                                         <img class="img-size" src="${img}"/>
                                         <p>${type}</p>
                                         <p>${benefit}</p>
                                         <p>${benefitdetail}</p>
                                         <p>${desc}</p>
                                         <p>${caffeineOX}</p>
                                         <p>${caffeine}</p>
                                         <p>${caution}</p>
                                         <p><button onclick="likeTea('${name}')" class="btn btn-outline-secondary">좋아요</button> 좋아요 수 : ${like}</p>
                                         <p><button onclick="scrapTea('${name}')" class="btn btn-outline-secondary">찜</button></p>
                                         <p> ---------------------------------------------------------------------------------------------- </p>
                                         `
                        $('#box').append(temp_html)
                        }
                }}
            })
        }

        // enter 키 검색
        function enter() {
            if (window.event.keyCode == 13) {
                search();
            }
        }

        async function likeTea(name) {
            let access_token = await get_access_token();

            $.ajax({
                type: 'POST',
                url: '/tea/like',
                data: {name_give: name},
                headers: {"Authorization": "Bearer "+ access_token},
                success: function (response) {
                    alert(response['msg']);
                    window.location.reload()
                }
            });
        }

        async function get_access_token() {
            let result = await fetch('/get_access_token');
            let token = await result.text()
            return token;
        }

        async function scrapTea(name) {
            let access_token = await get_access_token();

            $.ajax({
                type: 'POST',
                url: '/tea/scrap',
                data: {name_give: name},
                headers: {"Authorization": "Bearer "+ access_token},
                success: function (response) {

                    if(response['alreadyScrap']) {
                        alert(response['alreadyScrap']);
                        window.location.reload()
                    }
                    else if(response['successScrap']){
                        alert(response['successScrap']);
                    }
                }
            });
        }



        /* 로그인 페이지 스크립트 */
        /* ------------------------ Click on login and Sign Up to  changue and view the effect ----------------------------- */

        function cambiar_login() {
            document.querySelector('.cont_forms').className = "cont_forms cont_forms_active_login";
            document.querySelector('.cont_form_login').style.display = "block";
            document.querySelector('.cont_form_sign_up').style.opacity = "1";

            setTimeout(function () {
                document.querySelector('.cont_form_login').style.opacity = "1";
            }, 400);

            setTimeout(function () {
                document.querySelector('.cont_form_sign_up').style.display = "none";
            }, 200);
        }


        function cambiar_sign_up(at) {
            document.querySelector('.cont_forms').className = "cont_forms cont_forms_active_sign_up";
            document.querySelector('.cont_form_sign_up').style.display = "block";
            document.querySelector('.cont_form_login').style.opacity = "0";

            setTimeout(function () {
                document.querySelector('.cont_form_sign_up').style.opacity = "1";
            }, 100);

            setTimeout(function () {
                document.querySelector('.cont_form_login').style.display = "none";
            }, 400);


        }


        function ocultar_login_sign_up() {

            document.querySelector('.cont_forms').className = "cont_forms";
            document.querySelector('.cont_form_sign_up').style.opacity = "0";
            document.querySelector('.cont_form_login').style.opacity = "0";

            setTimeout(function () {
                document.querySelector('.cont_form_sign_up').style.display = "none";
                document.querySelector('.cont_form_login').style.display = "none";
            }, 500);

        }