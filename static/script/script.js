
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
