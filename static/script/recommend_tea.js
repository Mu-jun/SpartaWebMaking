
function find_tea() {
        /*차 종류 선택사항 추출 */
        const typequery = 'input[name="type"]:checked';
        const selectedTypes =
            document.querySelectorAll(typequery);
        let type = '';
        var typecount = 0;
        selectedTypes.forEach((el) => {
            if (++typecount == selectedTypes.length) {
                type += el.value
            } else {
                type += el.value + ','
            }
        });
        if (type === '') {
            type += "백차,녹차,홍차,황차,청차,흑차,대용차" /*선택 안하면 전부 선택한 것으로 처리*/
        }
        const typearr = type.split(','); /*선택한 차의 종류를 list 형태로 만들어줌*/

        /*차 효능 선택사항 추출 */
        const benefitquery = 'input[name="benefit"]:checked';
        const selectedBenefit =
            document.querySelectorAll(benefitquery);
        let benefit = '';
        var benecount = 0;
        selectedBenefit.forEach((el) => {
            if (++benecount == selectedBenefit.length) {
                benefit += el.value
            } else {
                benefit += el.value + ','
            }
        });
        if (benefit === '') {
            benefit += "다이어트,피부미용,피로회복,면역증진,혈액순환,소화기능,질병예방,정신건강" /*선택 안하면 전부 선택한 것으로 처리*/
        }
        let benefitarr = benefit.split(',');

        /*차 카페인 선택사항 추출 */
        const caffquery = 'input[name="caffeineOX"]:checked';
        const selectedCaffeine =
            document.querySelectorAll(caffquery);
        let caffeineOX = ""
        if (selectedCaffeine.length != 1) {
            caffeineOX = [true, false]
        } else if (selectedCaffeine == "true") {
            caffeineOX = [true]
        } else {
            caffeineOX = [false]
        }

        console.log(typearr)
        console.log(benefitarr)
        console.log(caffeineOX)

        $.ajax({
            type: "POST",
            url: "/recommend/find",
            headers: {'Content-Type': 'application/json'},
            dataType: 'json',
            data: JSON.stringify({
                    type_give : typearr,
                    benefit_give : benefitarr,
                    caffeineOX_give : caffeineOX,
                   }),
            success: function (response) {
                $('#box').empty()
                let Tea = JSON.parse(response['find_teas'])   /*서버에서 string으로 들어와서 JSON.parse 사용*/
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
                                         <p><button onclick="likeTea('${name}')" class="btn btn-outline-secondary">좋아요</button> 좋아요 수 : ${like}</p>
                                         <p><button onclick="scrapTea('${name}')" class="btn btn-outline-secondary">찜</button></p>
                                         <p> ---------------------------------------------------------------------------------------------- </p>
                                         `
                        $('#box').append(temp_html)
                }
            }
        })
    }
