        $(document).ready(function () {
            showScrap();
        });

                function showScrap() {
            $.ajax({
                type: "GET",
                url: "/tea/scrapList",
                data: {},
                success: function (response) {
                    let scrapTea = response['scrapTeas']
                    for(let i =0; i<scrapTea.length; i++){
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
            })

        }

        function deleteScrap(name) {
            $.ajax({
                type: 'POST',
                url: '/tea/deleteScrap',
                data: {name_give: name},
                success: function (response) {
                    alert(response['msg']);
                    window.location.reload()
                }
            });
        }