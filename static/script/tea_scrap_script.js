        $(document).ready(function () {
            showScrap();
        });

            async function get_access_token() {
                let result = await fetch('/get_access_token');
                let token = '';

                if (result.ok) token = await result.json();

                return token;
            }

            async function showScrap() {
            let access_token = await get_access_token();

            $.ajax({
                type: "GET",
                url: "/tea/scrapList",
                data: {},
                headers: {"Authorization": "Bearer "+ access_token},
                success: function (response) {
                    if (response['scrapTeas']) {
                        let scrapTea = response['scrapTeas']
                        for (let i = 0; i < scrapTea.length; i++) {
                            let name = scrapTea[i]['name']
                            let type = scrapTea[i]['type']
                            let benefit = scrapTea[i]['benefit']
                            let caffeineOX = scrapTea[i]['caffeineOX']
                            let caffeine = scrapTea[i]['caffeine']
                            let benefitdetail = scrapTea[i]['benefitdetail']
                            let desc = scrapTea[i]['desc']
                            let caution = scrapTea[i]['caution']
                            let img = scrapTea[i]['img']

                            let temp_html = `<p>name : ${name}</p>
                                         <img class="img-size" src="${img}"/>
                                         <p>${type}</p>
                                         <p>${benefit}</p>
                                         <p>${benefitdetail}</p>
                                         <p>${desc}</p>
                                         <p>${caffeineOX}</p>
                                         <p>${caffeine}</p>
                                         <p>${caution}</p>
                                         <p><button onclick="deleteScrap('${name}')" class="btn btn-outline-secondary">삭제</button></p>
                                         <p> ---------------------------------------------------------------------------------------------- </p>
                                         `
                            $('#scrapBox').append(temp_html)
                        }
                    }
                        else if(response['msg']){
                            alert(response['msg'])
                            let url_teaList = 'http://13.124.112.143/tea'
                            window.location.replace(url_teaList);

                        }

                }

            })

        }

        async function deleteScrap(name) {
            let access_token = await get_access_token();

            $.ajax({
                type: 'POST',
                url: '/tea/deleteScrap',
                data: {name_give: name},
                headers: {"Authorization": "Bearer "+ access_token},
                success: function (response) {
                    alert(response['msg']);
                    window.location.reload()
                }
            });
        }