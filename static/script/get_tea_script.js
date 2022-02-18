
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

        /* 찜 좋아요 기능 스크립트 --승신 */

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