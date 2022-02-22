 function save_tea() {

        /* 대분류1 '효능' 처리 부분 */
        const query = 'input[name="benefit"]:checked';
        const selectedEls =
            document.querySelectorAll(query);

        let result = '';
        selectedEls.forEach((el) => {
            result += el.value + ' ';
        });

        let type = $('#type option:selected').val()         /* 종류 */

        /* 차 종류(영문)처리 부분 */
        if (type === "대용차") {
            var eng_type = "ETC";
        } else if (type === "홍차") {
            var eng_type = "Black Tea";
        } else if (type === "녹차") {
            var eng_type = "Green Tea";
        } else if (type === "홍차") {
            var eng_type = "Black Tea";
        } else if (type === "백차") {
            var eng_type = "White Tea";
        } else if (type === "청차") {
            var eng_type = "Dark Green Tea";
        } else if (type === "황차") {
            var eng_type = "Yellow Tea";
        } else if (type === "흑차") {
            var eng_type = "Dark Tea";
        }

        let name = $('#name').val()                         /* 차이름 */
        let eng_name = $('#eng_name').val()                 /* 영문명 */
        let benefit = result                                /* 효능 */
        let caffeine = $('#caffeine').val()                 /* 카페인함유량 */
        var caffeineOX = Boolean(caffeine)                  /* 카페인함유여부 */
        let benefitdetail = $('#benefitdetail').val()       /* 상세효능 */
        let desc = $('#desc').val()                         /* 상세설명 */
        let caution = $('#caution').val()                   /* 주의사항 */
        let img = $('#img').val()                           /* 이미지주소 */

        $.ajax({
            type: "POST",
            url: "/save",
            headers: {'Content-Type': 'application/json'},
            dataType: 'json',
            data: JSON.stringify({
                name_give: name,
                eng_name_give: eng_name,
                type_give: type,
                eng_type_give: eng_type,
                benefit_give: benefit,
                benefitdetail_give: benefitdetail,
                caffeineOX_give: caffeineOX,
                caffeine_give: caffeine,
                desc_give: desc,
                caution_give: caution,
                img_give: img,
            }),
            success: function (response) { // 성공하면
                alert(response["msg"]);
                window.location.reload()
            }
        })
    }
