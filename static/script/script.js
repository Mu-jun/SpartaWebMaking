        /* 01_login script */


        $(document).ready(function () {

        });

        function makeid() {

            let save_id = $('#user_id').val()
            let save_pass = $('#user_pass').val()
            let save_nick = $('#user_nick').val()


            $.ajax({
                type: "POST",
                url: "/sign/signup",
                data: {
                    id_give: save_id,
                    pw_give: save_pass,
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

                }

            })
        }

                function login() {

            let load_id = $('#user_id').val()
            let load_pass = $('#user_pass').val()
            let load_nick = $('#user_nick').val()


            $.ajax({
                type: "POST",
                url: "/sign/log_in",
                data: {
                    id_give: load_id,
                    pw_give: load_pass,
                    nickname_give: load_nick,
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
                        let img = Tea[i]['lmg']

                        let temp_html = `<p>name : ${name}</p>
                                         <p>${type}</p>
                                         <p>${benefit}</p>
                                         <p>${desc}</p>
                                         <p>${caffeine}</p>
                                         <p>${caution}</p>
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
                            let img = Tea[i]['lmg']

                        let temp_html = `<p>name : ${name}</p>
                                         <p>${type}</p>
                                         <p>${benefit}</p>
                                         <p>${desc}</p>
                                         <p>${caffeine}</p>
                                         <p>${caution}</p>
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
