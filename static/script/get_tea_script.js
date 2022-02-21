
        /* get_tea script */

         $(document).ready(function () {
            showTea();
        });

        // 차 정보 보이게 하기
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

        // 이름순 정렬
        function sortName() {
            $.ajax({
                type: "GET",
                url: "/tea/list",
                data: {},
                success: function (response) {
                    $('#box').empty()
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
        // 좋아요순 정렬
        function sortLike() {
            $.ajax({
                type: "GET",
                url: "/tea/list",
                data: {},
                success: function (response) {
                    $('#box').empty()
                    let Tea = response['all_teas']
                    Tea.sort()
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
            let count = 0; // 검색된 차 개수
            let teaKeyword = $('#teaName').val(); // 검색어
            $.ajax({
                type: "POST",
                url: "/tea/search",
                headers: {'Content-Type': 'application/json'},
                dataType: 'json',
                data: JSON.stringify({
                    teaKeyword: teaKeyword,
                }),
                success: function (response) {
                    $('#box').empty()
                    let Tea = JSON.parse(response['search_teas'])
                    for (let i = 0; i < Tea.length; i++){

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
                        count++;
                }
                    let count_html =`<p>${count}개 찾았습니다</p>`
                    $('#box').append(count_html)
                }
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

        /* like+scrap 스크립트 */

        /*
        async function likeTea(name) {
            let access_token = await get_access_token();

            $.ajax({
                type: 'POST',
                url: '/tea/like_all',
                data: {name_give: name},
                headers: {"Authorization": "Bearer "+ access_token},
                success: function (response) {
                    if(response['alreadyScrap']) {
                        alert(response['alreadyScrap']);
                        window.location.reload()
                    }
                    else if(response['successScrap']){
                        alert(response['successScrap']);
                        window.location.reload()
                    }
                }
            });
        }

         */

        async function get_access_token() {
    let result = await fetch('/get_access_token');
    let token = '';

    if(result.ok) token = await result.json();

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
