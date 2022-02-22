from pymongo import MongoClient
#client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@52.78.104.136', 27017)
db = client.dbchacha

# https://products.aspose.app/cells/ko/conversion/csv-to-json
# 데이터가 들어있는 엑셀 파일을 만들고, CSV(쉼표로 구분, UTF-8) 파일로 내보내기 하여 저장한다.
# 위 사이트에서 CSV 파일을 JSON 파일로 변환한다.
# 값을 아래에 붙여넣은 후, '찾아 바꾸기'(모두)를 이용하여 깨지는 부분들을 수정해 준다.
  # true 를 True 로 바꾼다.
  # false 를 False 로 바꾼다.
  # null 을 None 으로 바꾼다.
  # \/ 를 / 로 바꾼다.
  # "caffeine": 0, 을 "caffeine": "0", 으로 바꾼다. 카페인 함량이 있는 경우 10mg/200ml 과 같이 텍스트로 표현되기에 자료형 맞춰줌.
    # "caffeine": 부분을 빼고 0 을 "0" 으로 바꿔서는 안됨! 좋아요 갯수는 integer로 남아야 하기 때문
# 이 파일을 실행하기 전에는 반드시 기존 DB의 값들을 날리고 사용한다. 중복으로 들어가기 때문.


db.tealist.insert_many([
 {
  "eng_name": "Daejak",
  "name": "대작",
  "type": "녹차",
  "eng_type": "Green Tea",
  "benefit": "다이어트 면역증진 정신건강",
  "benefitdetail": "콜레스테롤,지방분해,비만예방,항산화효과,스트레스 완화",
  "desc": "가장 많이 자란, 큰(大) 잎으로 만든 차이다. 첫맛이 매우 강하고 뒷맛의 떫음이 세다. 현실적으로 녹차의 풍부한 맛을 내기는 어렵기 때문에 구하기도 힘들고 유통도 많이 되지 않는다. ",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "녹차의 타닌 성분은 칼슘, 철분과 결합하려는 성질이 있어 영양분의 흡수를 방해하기 때문에 식후에 바로 섭취는 좋지 않다. 특히 골다공증, 빈혈, 위장장애의 경우  주의해야 한다. 또한 카페인의 각성 효과에 유의하여야 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EB%85%B9%EC%B0%A8_Green+Tea/%EB%85%B9_%EB%8C%80%EC%9E%91%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Matcha",
  "name": "말차",
  "type": "녹차",
  "eng_type": "Green Tea",
  "benefit": "다이어트 혈액순환 질병예방",
  "benefitdetail": "콜레스테롤,지방분해,비만예방,항산화효과,혈압강하,혈관건강,항암작용,혈당 낮춤",
  "desc": "가루녹차라고도 한다. 어린 순을 채취하여 찌고 말린 후 갈아서 가루 상태로 만든 것이다. 떫은 맛이 적고 아미노산과 엽록소가 많다. 그대로 물에 타 마시거나 차빵, 차국수, 차아이스크림 등 다양한 식품의 소재로 활용된다. ",
  "caffeineOX": True,
  "caffeine": " 60mg/200ml",
  "caution": "말차의 경우 특히 높은 카페인 함유량에 유의하여야 한다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EB%85%B9%EC%B0%A8_Green+Tea/%EB%85%B9_%EB%A7%90%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Sejak",
  "name": "세작",
  "type": "녹차",
  "eng_type": "Green Tea",
  "benefit": "소화기능 혈액순환 피로회복",
  "benefitdetail": "콜레스테롤,지방분해,비만예방,혈압강하,혈관건강,간기능 개선",
  "desc": "우전 다음의 어린 잎으로 만든 차이며, 곡우(4월 20일경)에서 4월 말경까지 또는 입하(5월 5~6일경)까지 수확한 순과 잎으로 만든다. 녹차 특유의 맛이 우전보다 강하고 떫은 맛이 적은 대신에 우전 특유의 부드러움이 덜하다.",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "녹차의 타닌 성분은 칼슘, 철분과 결합하려는 성질이 있어 영양분의 흡수를 방해하기 때문에 식후에 바로 섭취는 좋지 않다. 특히 골다공증, 빈혈, 위장장애의 경우  주의해야 한다. 또한 카페인의 각성 효과에 유의하여야 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EB%85%B9%EC%B0%A8_Green+Tea/%EB%85%B9%EC%B0%A8_%EC%84%B8%EC%9E%91%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Woojeon",
  "name": "우전",
  "type": "녹차",
  "eng_type": "Green Tea",
  "benefit": "다이어트 혈액순환 질병예방",
  "benefitdetail": "콜레스테롤,지방분해,비만예방,항산화효과,혈압강하,혈관건강,항암작용,혈당 낮춤",
  "desc": "봄비가 내려 백곡이 윤택해진다는 곡우(4월 20일경) 전에 딴 아주 어린 찻잎이나 순으로 만든 차이다. 녹차 중 최고급 차로 분류된다. 첫맛이 매우 부드럽고 뒷맛에 떫음이 없다.",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "녹차의 타닌 성분은 칼슘, 철분과 결합하려는 성질이 있어 영양분의 흡수를 방해하기 때문에 식후에 바로 섭취는 좋지 않다. 특히 골다공증, 빈혈, 위장장애의 경우  주의해야 한다. 또한 카페인의 각성 효과에 유의하여야 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EB%85%B9%EC%B0%A8_Green+Tea/%EB%85%B9_%EC%9A%B0%EC%A0%84%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Jakseol Tea",
  "name": "작설차",
  "type": "녹차",
  "eng_type": "Green Tea",
  "benefit": "피부미용 질병예방 혈액순환 피로회복",
  "benefitdetail": "항산과효과,혈압강하,혈관건강,항암작용,혈당 낮춤,간기능 개선",
  "desc": "찻잎의 모양에 따라 붙여진 이름으로, 그 모양이 참새의 혀를 닮았다고 해서 붙여진 이름이다.",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "녹차의 타닌 성분은 칼슘, 철분과 결합하려는 성질이 있어 영양분의 흡수를 방해하기 때문에 식후에 바로 섭취는 좋지 않다. 특히 골다공증, 빈혈, 위장장애의 경우  주의해야 한다. 또한 카페인의 각성 효과에 유의하여야 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EB%85%B9%EC%B0%A8_Green+Tea/%EB%85%B9_%EC%9E%91%EC%84%A4%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Sencha",
  "name": "전차",
  "type": "녹차",
  "eng_type": "Green Tea",
  "benefit": "다이어트 혈액순환 피로회복",
  "benefitdetail": "콜레스테롤,지방분해,비만예방,혈압강하,혈관건강,간기능 개선",
  "desc": "찻잎을 증기로 쪄서 찻잎의 효소를 파괴하여 만든 차이다. 일반적으로 5월에 따는 햇차와 6월에 따는 두물차를 찐 다음 비벼서 말린다. 우려낸 차는 담황색을 보이며 부드러운 향을 갖는다. 특히 일본에서 소비되는 녹차의 대부분은 전차가 차지하고 있다.",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "녹차의 타닌 성분은 칼슘, 철분과 결합하려는 성질이 있어 영양분의 흡수를 방해하기 때문에 식후에 바로 섭취는 좋지 않다. 특히 골다공증, 빈혈, 위장장애의 경우  주의해야 한다. 또한 카페인의 각성 효과에 유의하여야 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EB%85%B9%EC%B0%A8_Green+Tea/%EB%85%B9_%EC%A0%84%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Jungjak",
  "name": "중작",
  "type": "녹차",
  "eng_type": "Green Tea",
  "benefit": "질병예방 혈액순환 피로회복",
  "benefitdetail": "항산과효과,혈압강하,혈관건강,항암작용,혈당 낮춤,간기능 개선",
  "desc": "세작과 대작의 중간이라는 의미로 입하(立夏) 후 5월 중순경까지 딴 차로 만든다. 첫맛은 강하고 뒷맛에선 떫음이 느껴진다. 애호가들은 우전이나 세작을 선호하지만, 중작 또한 맛이 많이 떨어지지 않아 색, 향, 맛을 모두 즐길 수 있는 대중적인 녹차이다.",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "녹차의 타닌 성분은 칼슘, 철분과 결합하려는 성질이 있어 영양분의 흡수를 방해하기 때문에 식후에 바로 섭취는 좋지 않다. 특히 골다공증, 빈혈, 위장장애의 경우  주의해야 한다. 또한 카페인의 각성 효과에 유의하여야 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EB%85%B9%EC%B0%A8_Green+Tea/%EB%85%B9_%EC%A4%91%EC%9E%91%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Chunseol Tea",
  "name": "춘설차",
  "type": "녹차",
  "eng_type": "Green Tea",
  "benefit": "다이어트 면역증진 정신건강",
  "benefitdetail": "콜레스테롤,지방분해,비만예방,항산화효과,스트레스 완화",
  "desc": "무등산 해발 700m 근방에서 눈이 녹기 전 돋아난 차의 여린 잎으로 만든 차를 말한다. ",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "녹차의 타닌 성분은 칼슘, 철분과 결합하려는 성질이 있어 영양분의 흡수를 방해하기 때문에 식후에 바로 섭취는 좋지 않다. 특히 골다공증, 빈혈, 위장장애의 경우  주의해야 한다. 또한 카페인의 각성 효과에 유의하여야 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EB%85%B9%EC%B0%A8_Green+Tea/%EB%85%B9_%EC%B6%98%EC%84%A4%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Brown Rice Green Tea",
  "name": "현미녹차",
  "type": "녹차",
  "eng_type": "Green Tea",
  "benefit": "다이어트 혈액순환 피로회복",
  "benefitdetail": "콜레스테롤,지방분해,비만예방,혈압강하,혈관건강,간기능 개선",
  "desc": "중제차에 볶은 현미를 혼합하여 만든 녹차로, 녹차의 산뜻한 맛과 볶은 현미의 구수한 맛이 조화를 이루어 누구나 부담없이 마시기 편한 차이다.",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "녹차의 타닌 성분은 칼슘, 철분과 결합하려는 성질이 있어 영양분의 흡수를 방해하기 때문에 식후에 바로 섭취는 좋지 않다. 특히 골다공증, 빈혈, 위장장애의 경우  주의해야 한다. 또한 카페인의 각성 효과에 유의하여야 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EB%85%B9%EC%B0%A8_Green+Tea/%EB%85%B9_%ED%98%84%EB%AF%B8%EB%85%B9%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Gyeolmyeongja Tea",
  "name": "결명자차",
  "type": "대용차",
  "eng_type": "ETC",
  "benefit": "소화기능 혈액순환 질병예방",
  "benefitdetail": "시력증진, 이뇨작용, 고혈압, 위장병, 당뇨",
  "desc": "눈 건강에 좋은 차로 유명하며 숙취 해소나 변비, 고혈압 등에도 효과가 있다. 음용수용 차로 많이 쓰이지만 보리차, 현미차와 달리 이뇨작용이 있기 때문에 수분 섭취에 도움이 되지 않아 권장할 수 없다. ",
  "caffeineOX": False,
  "caffeine": "0",
  "caution": "혈압을 낮추는 효과가 있기에 저혈압인 사람들에게는 좋지 않으며, 몸이 찬 사람에게도 좋지 않다고 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/etc/%EA%B2%B0%EB%AA%85%EC%9E%90.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Goji Berry Tea",
  "name": "구기자차",
  "type": "대용차",
  "eng_type": "ETC",
  "benefit": "혈액순환 질병예방 피로회복",
  "benefitdetail": "혈압조절,지방간 개선,노화방지,눈 건강",
  "desc": "구기자는 진시황이 불로초로 여겨 구했다는 설이 있으며, 남자의 양기에 좋다고 여겨져왔다. 구기자나무의 잎을 말려 차로 음용한다. 맛과 향은 다소 심심하여 오미자와 함께 끓여먹으면 좋다.",
  "caffeineOX": False,
  "caffeine": "0",
  "caution": "포도당과 아미노산의 흡수를 촉진하므로 과한 섭취시 체중이 늘 수 있다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/etc/%EA%B5%AC%EA%B8%B0%EC%9E%90%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Sceaux-de-salomon Tea",
  "name": "둥굴레차",
  "type": "대용차",
  "eng_type": "ETC",
  "benefit": "혈액순환 피로회복 소화기능",
  "benefitdetail": "혈압 강하,항염작용, 관절건강,숙면유도,노화방지",
  "desc": "둥굴레차는 백합과 식물인 둥굴레의 뿌리로 만드는 차로, 뿌리 모양이 둥글고 굴레 모양의 마디가 있어 붙여진 이름이다. 이 뿌리를 말려 약재로 사용하기도 하는 등 건강에 좋은 차로 유명하며 구수한 맛도 좋아 즐기기에 편하다. ",
  "caffeineOX": False,
  "caffeine": "0",
  "caution": "장이 약한 사람은 설사나 속쓰림 증상이 있을 수 있으며, 백합과 식물에 알러지가 있는 경우 피하는 것이 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/etc/%EB%91%A5%EA%B5%B4%EB%A0%88%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Rooibos Tea",
  "name": "루이보스차",
  "type": "대용차",
  "eng_type": "ETC",
  "benefit": "소화기능 정신건강 혈액순환 피부미용",
  "benefitdetail": "항산화효과,암예방,철분흡수 도움,숙면유도",
  "desc": "색감이 홍차와 유사해 홍차 대용품으로도 이용되었던 차. 때문에 가향 블렌딩이나 밀크티 등으로 즐기기도 한다. 둥글레차와 비슷한 맛에 설탕 없이조 약간의 단맛이 있으며 뒷맛이 개운하다",
  "caffeineOX": False,
  "caffeine": "0",
  "caution": "부작용이 매우 드물지만 과다 섭취시 에스트로겐 생성이 증가될 수 있다는 보고가 있다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/etc/%EB%A3%A8%EC%9D%B4%EB%B3%B4%EC%8A%A4.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Buckwheat Tea",
  "name": "메밀차",
  "type": "대용차",
  "eng_type": "ETC",
  "benefit": "혈액순환 다이어트 질병예방",
  "benefitdetail": "고혈압 완화,간 건강,노폐물 배출,변비 개선,당뇨 개선,눈 건강",
  "desc": "메밀을 볶아서 물을 붓고 끓인 대용차. 차게해서 먹거나 따뜻하게 해서 먹어도 달달한 맛이 있이 풍부하며 대표적인 무카페인·저칼로리 식품이다. ",
  "caffeineOX": False,
  "caffeine": "0",
  "caution": "몸이 찬 사람들에게는 설사나 유통을 유발할 수 있으며, 임산부 건강에 좋지 않다. 혈압이 낮은 사람에게도 좋지 않다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/etc/%EB%A9%94%EB%B0%80%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Mogwa Tea",
  "name": "모과차",
  "type": "대용차",
  "eng_type": "ETC",
  "benefit": "소화기능 질병예방 면역증진",
  "benefitdetail": "소화촉진,감기,입덧방지,소염작용,위 건강,간 건강,기침완화,빈혈완화",
  "desc": "모과 열매를 얇게 썰어서 말려두었다가 설탕에 절여 따뜻한 물에 넣어 마신다. 흔히 생강 조각을 함께 넣어 즐기기도 한다.",
  "caffeineOX": False,
  "caffeine": "0",
  "caution": "설사를 완화하는 작용이 있어 변비를 일으키는 경우도 있으며, 위궤양이 있는 사람에게 좋지 않다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/etc/%EB%AA%A8%EA%B3%BC%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Dandelion Tea",
  "name": "민들레차",
  "type": "대용차",
  "eng_type": "ETC",
  "benefit": "질병예방 피부미용",
  "benefitdetail": "뼈 건강,간 건강,항산화효과,당뇨,비뇨기질병,항암효과",
  "desc": "민들레 꽃잎을 우려낸 대용차이다. 고소한 첫맛과 향긋한 끝맛의 풍미가 깊으며 여름에는 얼음을 넣고 시원하게 마시기도 한다. 비타민이 매우 풍부하여 항산화 작용이 탁월하다.",
  "caffeineOX": False,
  "caffeine": "0",
  "caution": "대체로 안전하나, 당뇨병약이나 혈액희석제, 변비약을 먹고 있다면 피할 필요가 있다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/etc/%EB%AF%BC%EB%93%A4%EB%A0%88%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Barley Tea",
  "name": "보리차",
  "type": "대용차",
  "eng_type": "ETC",
  "benefit": "혈액순환 소화기능 다이어트",
  "benefitdetail": "변비예방,체온조절,피부미용,항염효과",
  "desc": "보리를 볶아 만든 대용차로, 식수 대용으로 가장 많이 사용된다. 특유의 구수한 맛이 익숙하다.",
  "caffeineOX": False,
  "caffeine": "0",
  "caution": "부작용이 거의 없지만 보리의 성질이 차기 때문에 몸이 찬 사람에게는 좋지 않을 수 있다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/etc/%EB%B3%B4%EB%A6%AC%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Omija Tea",
  "name": "오미자차",
  "type": "대용차",
  "eng_type": "ETC",
  "benefit": "혈액순환 질병예방 피로회복 피부미용",
  "benefitdetail": "혈류개선,항산화 효과,당뇨,항암,간 기능,호흡기,면역력 증진",
  "desc": "오미자라는 이름은 그 열매에 다섯 가지의 기본 맛(신맛 쓴맛 짠맛 쓴맛 매운맛)이 모두 있다는 의미이다. 중국과 우리나라에서 오랫동안 약재로 사용해왔다.",
  "caffeineOX": False,
  "caffeine": "0",
  "caution": "당뇨병약을 먹고 있다면, 오미자의 혈당을 낮추는 효능이 약과 함께 작용하여 혈당을 너무 떨어뜨릴 수 있다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/etc/%EC%98%A4%EB%AF%B8%EC%9E%90%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Yuja Tea",
  "name": "유자차",
  "type": "대용차",
  "eng_type": "ETC",
  "benefit": "소화기능 질병예방 면역증진",
  "benefitdetail": "소화촉진,변비 개선,노폐물 제거,고지혈증 예방",
  "desc": "유자를 설탕이나 꿀에 절여 만든 유자청을 물에 희석하여 마시는 차. 비타민C가 풍부하여 감기에 마시는 차로 인기가 좋다. 은은한 단맛과 새콤하고 쌉싸름한 유자향을 즐길 수 있다. ",
  "caffeineOX": False,
  "caffeine": "0",
  "caution": "감기약의 성분이 비타민C를 만나면 해로운 성분으로 변하기에, 감기약과 함께 섭취한다면 한 시간 정도의 가격을 두고 섭취하는 것이 좋다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/etc/%EC%9C%A0%EC%9E%90%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Job's Tears Tea",
  "name": "율무차",
  "type": "대용차",
  "eng_type": "ETC",
  "benefit": "혈액순환 질병예방 면역증진",
  "benefitdetail": "혈당수치 개선,위 건강,폐 건강,이뇨작용,부종완화,뼈 건강,항암,해열",
  "desc": "볏과의 곡물인 율무 열매를 볶은 후 가루를 내어 즐기는 차이다. 본래 율무는 단백질과 미네랄이 풍부하여 다이어트에 도움을 줄 수 있지만 시중에 판매되는 율무차는 대부분 설탕의 함량이 매우 높으므로 주의하여야 한다.",
  "caffeineOX": False,
  "caffeine": "0",
  "caution": "자궁수축 작용이 있어 임신 초기에 섭취하면 유산의 위험이 있다고 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/etc/%EC%9C%A8%EB%AC%B4%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Chamomile Tea",
  "name": "카모마일",
  "type": "대용차",
  "eng_type": "ETC",
  "benefit": "질병예방 정신건강 피부미용",
  "benefitdetail": "숙면유도,통증감소,혈당조절,항산화효과",
  "desc": "카모마일은 데이지과의 식물로 '땅에서 나는 사과'라는 의미를 가지고 있다. 약 5천년전부터 약초로 사용해 온 식물로 꽃의 약효가 뛰어나다",
  "caffeineOX": False,
  "caffeine": "0",
  "caution": "알러지가 있을 수 있으며, 자궁 수축 부작용이 있을 수 있어 임신 중인 여성은 피해야 한다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/etc/%EC%B9%B4%EB%AA%A8%EB%A7%88%EC%9D%BC.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Peppermint Tea",
  "name": "페퍼민트차",
  "type": "대용차",
  "eng_type": "ETC",
  "benefit": "피로회복 면역증진 정신건강",
  "benefitdetail": "위장 건강,집중력 개선,눈 건강,구취제거,졸음방지,면역력 증진,진통",
  "desc": "청량하고 시원한 향이 특징인 허브 종류 중 하나이다. 차로만 우려 마시는 것이 아니라 모히또나 에이드, 칵테일 등 여러 가지 음료와 주류에도 첨가 사용하고 있다. ",
  "caffeineOX": False,
  "caffeine": "0",
  "caution": "박하 알러지가 있을 수 있으며, 위 식도염류의 질환을 앓고 있는 사람에게 좋지 않다. 카페인이 없음에도 각성효과가 있으니 불면증에 유의해야 한다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/etc/%ED%8E%98%ED%8D%BC%EB%AF%BC%ED%8A%B8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Hibiscus Tea",
  "name": "히비스커스",
  "type": "대용차",
  "eng_type": "ETC",
  "benefit": "혈액순환 다이어트 피부미용",
  "benefitdetail": "혈압 강하,콜레스테롤 강하,우울증 개선,소화,면역력 증진",
  "desc": "로젤 열매를 말린 후 끓여 우려낸 대용차. 빵이나 쿠키, 케이크와 어울리며 루비색의 빛깔이 아름답다. 새콤한 맛이며 쓴 맛이 별로 없다",
  "caffeineOX": False,
  "caffeine": "0",
  "caution": "임산부와 모유 수유중인 여성은 호르몬에 영향을 받기 때문에 유의가 필요하다",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/etc/%ED%9E%88%EB%B9%84%EC%8A%A4%EC%BB%A4%EC%8A%A4.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Gongmi",
  "name": "공미",
  "type": "백차",
  "eng_type": "White Tea",
  "benefit": "다이어트 소화기능 면역증진",
  "benefitdetail": "지방분해,숙취해소,감기예방,심장건강,항암효과,스트레스 완화,치아건강,구취개선",
  "desc": "찻잎의 여린 끝을 원료로 만들어 비교적 작고, 잎도 보드랍다. 옅은 오렌지빛의 빛깔과 달달한 맛이 난다.",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "성기능 쇠약자, 심장박동이 과하게 빠른 심장병자, 고혈압이 심한 자, 변비가 심한 자, 신경쇠약자, 철분 결핍성 빈혈 환자는 너무 진하게 마시면 좋지 않으며 공복에 마셔도 좋지 않다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EB%B0%B1%EC%B0%A8_White+Tea/%EB%B0%B1_%EA%B3%B5%EB%AF%B8%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Baekmokdan",
  "name": "백목단",
  "type": "백차",
  "eng_type": "White Tea",
  "benefit": "다이어트 질병예방 피로회복",
  "benefitdetail": "항산화 효과,심장질환 예방,치아건강,항암효과,당뇨예방,해열,해독",
  "desc": "잔에 담그면 목단 꽃이 피듯 하얗기 때문에 백목단이라고 한다. 달큰하지만 부드럽고 깔끔한 맛이 특징이며 꽃향기가 나고, 탕색은 살구빛 혹은 오렌지색으로 은은하다.",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "성기능 쇠약자, 심장박동이 과하게 빠른 심장병자, 고혈압이 심한 자, 변비가 심한 자, 신경쇠약자, 철분 결핍성 빈혈 환자는 너무 진하게 마시면 좋지 않으며 공복에 마셔도 좋지 않다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EB%B0%B1%EC%B0%A8_White+Tea/%EB%B0%B1_%EB%B0%B1%EB%AA%A9%EB%8B%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Baekhoeunchim",
  "name": "백호은침",
  "type": "백차",
  "eng_type": "White Tea",
  "benefit": "피부미용 혈액순환 질병예방 정신건강",
  "benefitdetail": "혈류개선,콜레스테롤,심장건강,항암효과,스트레스완화,치아건강,구취개선",
  "desc": "백차의 으뜸이라 칭할 정도로 유명하고 가격이 높은 차이다. 동그란 떡 모양으로 가공되는데, 아주 어린 최고급 새싹만을 모아 압축한 것이다. 맛이 굉장히 섬세하고 은은하며 어린 풀 향을 가득 느낄 수 있다. ",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "성기능 쇠약자, 심장박동이 과하게 빠른 심장병자, 고혈압이 심한 자, 변비가 심한 자, 신경쇠약자, 철분 결핍성 빈혈 환자는 너무 진하게 마시면 좋지 않으며 공복에 마셔도 좋지 않다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EB%B0%B1%EC%B0%A8_White+Tea/%EB%B0%B1_%EB%B0%B1%ED%98%B8%EC%9D%80%EC%B9%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Sumi",
  "name": "수미",
  "type": "백차",
  "eng_type": "White Tea",
  "benefit": "다이어트 질병예방 피로회복",
  "benefitdetail": "항산화 효과,심장질환 예방,치아건강,항암효과,당뇨예방,해열,해독",
  "desc": "대백차, 수선화차의 잎으로 만든다. 잎이 비교적 크고, 또 줄기도 좀 있는데, 보통 4월 말에 채집한다.",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "성기능 쇠약자, 심장박동이 과하게 빠른 심장병자, 고혈압이 심한 자, 변비가 심한 자, 신경쇠약자, 철분 결핍성 빈혈 환자는 너무 진하게 마시면 좋지 않으며 공복에 마셔도 좋지 않다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EB%B0%B1%EC%B0%A8_White+Tea/%EB%B0%B1_%EC%88%98%EB%AF%B8%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Daehongpo",
  "name": "대홍포",
  "type": "청차",
  "eng_type": "Dark Green Tea",
  "benefit": "면역증진 혈액순환 피부미용",
  "benefitdetail": "감기예방,혈류개선,치아건강,구취제거,다이어트",
  "desc": "어두운 잎사귀를 길게 꼬아 만든 형태로, 과일맛과 단맛이 섞여 있다. 암반 지역에서 자란 잎사귀를 써서 미네랄이 풍부하다. ",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "카페인 성분이 있어 각성효과가 있으니 수면장애에 주의하여야 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EC%B2%AD%EC%B0%A8_Dark+Green+Tea/%EC%B2%AD_%EB%8C%80%ED%99%8D%ED%8F%AC.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Dongjeong Tea",
  "name": "동정차",
  "type": "청차",
  "eng_type": "Dark Green Tea",
  "benefit": "질병예방 혈액순환 피로회복",
  "benefitdetail": "항산과효과,혈압강하,혈관건강,항암작용,혈당 낮춤,간기능 개선",
  "desc": "옥구슬처럼 보이는 녹색 잎사귀 모양을 갖는다. 달콤하고 부드러운 맛이며 꽃향기가 난다. 추가로 굽는 과정을 거치면 엠버 동정차라고 부르는데, 풍부하고 진한 꿀 향기에 살짝 훈제 풍미가 느껴진다. ",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "카페인 성분이 있어 각성효과가 있으니 수면장애에 주의하여야 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EC%B2%AD%EC%B0%A8_Dark+Green+Tea/%EC%B2%AD_%EB%8F%99%EC%A0%95%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Baekho-o-lyong",
  "name": "백호오룡",
  "type": "청차",
  "eng_type": "Dark Green Tea",
  "benefit": "질병예방 혈액순환 피로회복",
  "benefitdetail": "항산과효과,혈압강하,혈관건강,항암작용,혈당 낮춤,간기능 개선",
  "desc": "화이트 팁, 실버 팁, 동방미인이라고도 불린다. 크고 긴 잎사귀에 달콤한 과일 맛과 꽃향기가 더해져 신비로운 분위기를 풍긴다. ",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "카페인 성분이 있어 각성효과가 있으니 수면장애에 주의하여야 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EC%B2%AD%EC%B0%A8_Dark+Green+Tea/%EC%B2%AD_%EB%B0%B1%ED%98%B8%EC%98%A4%EB%A3%A1.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Oolong tea",
  "name": "우롱차",
  "type": "청차",
  "eng_type": "Dark Green Tea",
  "benefit": "면역증진 혈액순환 피부미용 정신건강",
  "benefitdetail": "감기예방,혈류개선,치아건강,구취제거,다이어트",
  "desc": "청차를 대표하는 차로서, 오룡차 또는 우롱차로 일컫는다. 찻잎의 산화 도중에 가열하여 산화를 중지시킨 후 잘 비벼서 말리는 것으로 완성한다. 은은한 연녹색부터 진한 오렌지빛까지 다양한 빛깔을 가질 수 있으며, 꽃향이나 감귤향 등 여러가지 향이 복합적으로 나타난다. ",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "카페인 성분이 있어 각성효과가 있으니 수면장애에 주의하여야 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EC%B2%AD%EC%B0%A8_Dark+Green+Tea/%EC%B2%AD_%EC%9A%B0%EB%A1%B1%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Cheolgwaneum",
  "name": "철관음",
  "type": "청차",
  "eng_type": "Dark Green Tea",
  "benefit": "다이어트 소화기능 피로회복",
  "benefitdetail": "콜레스테롤,지방분해,비만예방,혈압강하,혈관건강,간기능 개선",
  "desc": "찻잎의 모양이 관음(觀音)과 같고 무겁기가 철(鐵)과 같다고 하여 청나라 건륭(乾隆)황제에 의해 하사된 이름이다. 차 잎은 철색, 우려낸 것은 금황색이다. 달콤한 과일 향과 함께 은은하고 부드러운 단맛이 난다.  보통의 우롱차보다 영양 성분 함량이 많다. ",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "카페인 성분이 있어 각성효과가 있으니 수면장애에 주의하여야 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EC%B2%AD%EC%B0%A8_Dark+Green+Tea/%EC%B2%AD_%EC%B2%A0%EA%B4%80%EC%9D%8C.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Pojong Tea",
  "name": "포종차",
  "type": "청차",
  "eng_type": "Dark Green Tea",
  "benefit": "면역증진 혈액순환 피부미용",
  "benefitdetail": "감기예방,혈류개선,치아건강,구취제거,다이어트",
  "desc": "가볍게 산화시킨 우롱차로, 섬세하고 신선한 맛과 라일락 향을 풍긴다.",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "카페인 성분이 있어 각성효과가 있으니 수면장애에 주의하여야 한다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%EC%B2%AD%EC%B0%A8_Dark+Green+Tea/%EC%B2%AD_%ED%8F%AC%EC%A2%85%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Fruit tea",
  "name": "과일홍차",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "질병예방 소화기능 정신건강",
  "benefitdetail": "항산화 효과,감기예방,심장건강,항암효과,스트레스 완화,치아건강,구취개선",
  "desc": "레몬, 딸기, 사과, 패션푸르트, 레몬, 라임, 복숭아 등 다양한 과일향을 입혀 상쾌하게 즐기는 홍차이다. 차갑게 즐기기에도 적합하다.",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EA%B3%BC%EC%9D%BC%ED%99%8D%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Keemun",
  "name": "기문",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "다이어트 소화기능 면역증진",
  "benefitdetail": "지방분해,숙취해소,감기예방,심장건강,항암효과,스트레스 완화,치아건강,구취개선",
  "desc": "중국의 대표적인 홍차로 인도의 다즐링, 스리랑카의 우바와 함께 세계 3대 홍차로 꼽힌다. 찻잎의 색이 흑색이고, 우려낸 차는 밝은 오렌지색에 가까운 선홍색으로 난초의 향과 같은 독특한 향이 일품이다. 맛은 부드러운 편이고, 잉글리시 브렉퍼스트나 얼 그레이의 베이스로 많이 쓰인다.",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EA%B8%B0%EB%AC%B8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Flower Tea",
  "name": "꽃잎홍차",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "다이어트 질병예방 정신건강 피로회복",
  "benefitdetail": "지방분해,감기예방,심장건강,항암효과,스트레스완화,치아건강,구취개선",
  "desc": "다양한 꽃잎향과 과일향을 첨가한 홍차로 뒷맛이 향긋한 것이 특징이다. 장미의 잎과 향을 첨가한 로즈 티가 대표적이다. ",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EA%BD%83%EC%9E%8E%ED%99%8D%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Nilgiri",
  "name": "닐기리",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "다이어트 질병예방 면역증진",
  "benefitdetail": "지방분해,숙취해소,감기예방,심장건강,항암효과,치아건강,구취개선",
  "desc": "남인도 고원지대에서 재배된다. 신선하고 깔끔한 꽃향기, 날카롭고 산뜻한 맛이 일품이다. 주로 실론과 블렌딩을 하는데에 쓰인다",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EB%8B%90%EA%B8%B0%EB%A6%AC.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Darjeeling",
  "name": "다즐링",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "다이어트 소화기능 면역증진 피부미용",
  "benefitdetail": "지방분해,숙취해소,감기예방,심장건강,항암효과,스트레스 완화,치아건강,구취개선",
  "desc": "3대 명품 홍차 중의 하나이며 머스캣 향이 나는 특징 때문에 홍차의 샴페인이라 불리기도 한다. 가볍고 깔끔한 풍미로 은은하게 즐기며 주로 스트레이트로 음용한다. ",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EB%8B%A4%EC%A6%90%EB%A7%81.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Lapsang Souchong",
  "name": "랍상소총",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "혈액순환 질병예방 정신건강",
  "benefitdetail": "혈류개선,콜레스테롤,심장건강,항암효과,스트레스완화,치아건강,구취개선",
  "desc": "랍상소총이라는 이름은 최초의 홍차인 '정산소종'의 중국어 발음을 영어로 표현한 것이다. 소나무 태운 연기를 훈연하여 만들기에 강렬한 스모키한 향을 가지고 있어 호불호가 갈린다. 향에 비해 맛은 순하고 부드러운 편이며, 훈연향 너머로 달콤하게 느껴지는 과일향과 청량감이 매력이다.",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EB%9E%8D%EC%83%81%EC%86%8C%EC%B4%9D.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Russian Caravan",
  "name": "러시안캐러반",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "다이어트 소화기능 면역증진",
  "benefitdetail": "지방분해,숙취해소,감기예방,심장건강,항암효과,스트레스 완화,치아건강,구취개선",
  "desc": "랍상소총이나 기문과 같은 중국의 홍차에 인도차를 섞어서 만든다. 러시아에서는 이 홍차와 함께 술을 조금 부어넣은 잼을 즐기며 몸을 덥히기도 한다. ",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EB%9F%AC%EC%8B%9C%EC%95%88%EC%BA%90%EB%9F%AC%EB%B0%98.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Lady Grey",
  "name": "레이디그레이",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "혈액순환 질병예방 정신건강",
  "benefitdetail": "혈류개선,콜레스테롤,심장건강,항암효과,스트레스완화,치아건강,구취개선",
  "desc": "트와이닝(TWININGS)사의 베스트셀러 홍차 중 하나로, 입문용으로 유명하다. 상큼한 오렌지향과 레몬향을 블렌드하여 얼그레이보다 좀 더 상큼하고 달콤한 향이 난다.",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D%EC%B0%A8_%EB%A0%88%EC%9D%B4%EB%94%94%EA%B7%B8%EB%A0%88%EC%9D%B4.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Royal Blend",
  "name": "로열블렌드",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "다이어트 소화기능 면역증진",
  "benefitdetail": "지방분해,숙취해소,감기예방,심장건강,항암효과,스트레스 완화,치아건강,구취개선",
  "desc": "영국 왕실에 납품되는 블렌드 홍차라는 의미로, 제조사마다 구성이 조금씩 다르다. 주로 밀크티용으로 제작된다. ",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EB%A1%9C%EC%97%B4%EB%B8%94%EB%A0%8C%EB%93%9C.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Morning",
  "name": "모닝",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "다이어트 질병예방 면역증진",
  "benefitdetail": "지방분해,숙취해소,감기예방,심장건강,항암효과,치아건강,구취개선",
  "desc": "실론 40%, 아쌈 40%, 다즐링 20%의 비율로 프랑스 포숑사의 블렌드 홍차이며 카페인이 강한 밀크티용 홍차이다.",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EB%AA%A8%EB%8B%9D.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Assam",
  "name": "아쌈",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "혈액순환 질병예방 정신건강 피부미용",
  "benefitdetail": "혈류개선,콜레스테롤,심장건강,항암효과,스트레스완화,치아건강,구취개선",
  "desc": "짙은 붉은색이 빠르게 우러나오며 향이 강한 남성적인 홍차이다. 우유와 블렌딩하기에 적합해 밀크티로 인기가 많고 설탕을 섞어 마시기도 한다.",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EC%95%84%EC%8C%88.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Irish Breakfast",
  "name": "아이리쉬브렉퍼스트",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "혈액순환 면역증진 정신건강",
  "benefitdetail": "혈류개선,콜레스테롤,심장건강,항암효과,스트레스완화,치아건강,구취개선",
  "desc": "아쌈을 주종으로 한 블렌드 홍차로, 굉장히 강렬한 맛과 향을 가지며 달콤한 밀크티용으로 주로 쓰인다. ",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EC%95%84%EC%9D%B4%EB%A6%AC%EC%89%AC%EB%B8%8C%EB%A0%89%ED%8D%BC%EC%8A%A4%ED%8A%B8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Lady Grey",
  "name": "얼그레이",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "다이어트 질병예방 면역증진",
  "benefitdetail": "지방분해,숙취해소,감기예방,심장건강,항암효과,치아건강,구취개선",
  "desc": "영국의 수상이었던 얼 그레이 백작의 이름을 딴 홍차로, 그가 중국을 방문하여 배운 블렌딩 기법으로 만든 차라고 전해진다. 중국의 흑차에 베르가못향을 더한 훈제차로 시원한 느낌을 가져 텁텁할 때 마시면 좋다. 스트레이트 또는 아이스 티로 즐긴다. ",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EC%96%BC%EA%B7%B8%EB%A0%88%EC%9D%B4.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Uva",
  "name": "우바",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "질병예방 소화기능 정신건강 피로회복",
  "benefitdetail": "항산화 효과,감기예방,심장건강,항암효과,스트레스 완화,치아건강,구취개선",
  "desc": "스리랑카 실론이 원산지로, 세계 3대 홍차 중의 하나이다. 맛이 진하며 달콤한 장미향을 느낄 수 있고, 투명하고 밝은 홍색의 수색을 갖는다. 골든팁이 많이 들어가 있어 골든링이 선명하게 보이는 홍차이다. 레몬을 넣어 마시거나 아이스티, 밀크티로 즐기기에도 좋다.",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EC%9A%B0%EB%B0%94.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "English Breakfast",
  "name": "잉글리시브렉퍼스트",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "다이어트 질병예방 면역증진",
  "benefitdetail": "지방분해,숙취해소,감기예방,심장건강,항암효과,치아건강,구취개선",
  "desc": "실론(스리랑카)과 인도 차를 블렌드한 것으로 주로 밀크티용이다. 향과 맛이 강하고 카페인이 많은 편이다. 가는 찻잎을 써서 빨리 우러나기 때문에 영국에서는 주로 아침 식사와 함께 마신다.",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EC%9E%89%EA%B8%80%EB%A6%AC%EC%8B%9C%EB%B8%8C%EB%A0%89%ED%8D%BC%EC%8A%A4%ED%8A%B8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "English Afternoon",
  "name": "잉글리시애프터눈",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "질병예방 소화기능 정신건강",
  "benefitdetail": "항산화 효과,감기예방,심장건강,항암효과,스트레스 완화,치아건강,구취개선",
  "desc": "아쌈을 주종으로 3가지 홍차를 블렌드하여, 베르가못 나무의 향을 첨가한 홍차이다. 진한 홍색에 감, 배 등의 과일향이 나며 맛이 부드럽다. 식사 또는 디저트와 함께하기보다는 차 자체만으로 즐기기에 좋은 은은한 향의 차이다.",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EC%9E%89%EA%B8%80%EB%A6%AC%EC%8B%9C%EC%95%A0%ED%94%84%ED%84%B0%EB%88%88.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "China Tea",
  "name": "차이나티",
  "type": "홍차",
  "eng_type": "Black Tea",
  "benefit": "질병예방 소화기능 정신건강",
  "benefitdetail": "항산화 효과,감기예방,심장건강,항암효과,스트레스 완화,치아건강,구취개선",
  "desc": "랍상소총과 기문을 블렌딩한 홍차로 솔잎향이 강한 특징을 갖는다. ",
  "caffeineOX": True,
  "caffeine": "30~60mg/200ml",
  "caution": "카페인이 포함되어 있기 때문에 신체적으로 카페인에 민감하다면 양을 조절해 먹어야 하며, 탄닌 성분은 비타민과 같은 영양제의 흡수를 막기 때문에 이를 유의해야 한다. 체온을 높이기 때문에 고열일 때는 홍차보다는 해열작용이 있는 백차가 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%8D%EC%B0%A8_Black+Tea/%ED%99%8D_%EC%B0%A8%EC%9D%B4%EB%82%98%ED%8B%B0.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Gwaksanhanga",
  "name": "곽산황아",
  "type": "황차",
  "eng_type": "Yellow Tea",
  "benefit": "다이어트 소화기능 질병예방 피로회복",
  "benefitdetail": "콜레스테롤,지방분해,비만예방,혈압강하,혈관건강,간기능 개선",
  "desc": "찻잎이 작설처럼 뾰족하게 생겼으며 잎이 가늘고 잔털이 많다. 맛이 녹차와 유사하며, 고소한 콩 볶은 듯한 향과 달큼하고 깔끔한 맛이 느껴진다. ",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "산화도가 낮은 양성의 차로, 몸을 차게 하므로 생리 중에는 삼가는 것이 좋다. 이때는 온한 기운을 가진 일부 청차 또는 흑차(숙성차)를 마시는 것이 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%A9%EC%B0%A8_Yellow+Tea/%ED%99%A9_%EA%B3%BD%EC%82%B0%ED%99%A9%EC%95%84.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Gunsaneumchim",
  "name": "군산은침",
  "type": "황차",
  "eng_type": "Yellow Tea",
  "benefit": "혈액순환 피로회복 피부미용 면역증진",
  "benefitdetail": "혈류개선,스트레스 완화,감기예방,숙취개선,다이어트,충치예방",
  "desc": "마오쩌둥이 생전 가장 사랑했던 차로 알려졌다. 황차 중 가장 유명한 차로, 맛이 달고 상쾌하며 말린 바나나 향과 옥수수 향이 함께 느껴지는 부드러운 맛이다. ",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "산화도가 낮은 양성의 차로, 몸을 차게 하므로 생리 중에는 삼가는 것이 좋다. 이때는 온한 기운을 가진 일부 청차 또는 흑차(숙성차)를 마시는 것이 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%A9%EC%B0%A8_Yellow+Tea/%ED%99%A9_%EA%B5%B0%EC%82%B0%EC%9D%80%EC%B9%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Mongjeonghanga",
  "name": "몽정황아",
  "type": "황차",
  "eng_type": "Yellow Tea",
  "benefit": "혈액순환 피로회복 피부미용 정신건강",
  "benefitdetail": "혈류개선,스트레스 완화,감기예방,숙취개선,스트레스 완화,다이어트,충치예방",
  "desc": "사천성 서부의 야안시에 있는 몽산에서 만드는 황차로, 1950년대부터 대량으로 생산되었다. 그윽하지만 상큼한 향을 맡을 수 있고, 구수하고 달콤한 맛을 내며 끝맛이 깔끔하다. 우려낸 차빛은 밝은 황금색이 감도는 녹색이다. ",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "산화도가 낮은 양성의 차로, 몸을 차게 하므로 생리 중에는 삼가는 것이 좋다. 이때는 온한 기운을 가진 일부 청차 또는 흑차(숙성차)를 마시는 것이 좋다.",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%99%A9%EC%B0%A8_Yellow+Tea/%ED%99%A9_%EB%AA%BD%EC%A0%95%ED%99%A9%EC%95%84.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Pu'er Tea",
  "name": "생보이차",
  "type": "흑차",
  "eng_type": "Dark Tea",
  "benefit": "다이어트 혈액순환 질병예방 피로회복",
  "benefitdetail": "콜레스테롤,지방분해,비만예방,혈압강하,혈관건강,간기능 개선",
  "desc": "숙성을 통해 더욱 깊고 다양한 맛과 향을 낸다. 숙성된 보이차는 떫은 맛이 사라지고 부드럽고 구수한 맛이 나며, 진한 녹색이 변해 어두운 색상을 띈다. 보통은 2~3년을 숙성하며 25년 이상 숙성하는 경우도 있다.",
  "caffeineOX": True,
  "caffeine": "10mg/200ml",
  "caution": "흑차는 지방분해 효과가 탁월하지만 공복에 진하게 마신다면 위장에 부담을 줄 수 있다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%9D%91%EC%B0%A8_Dark+Tea/%ED%9D%91_%EC%83%9D%EB%B3%B4%EC%9D%B4%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Ripe Pu'er Tea",
  "name": "숙보이차",
  "type": "흑차",
  "eng_type": "Dark Tea",
  "benefit": "다이어트 면역증진 혈액순환",
  "benefitdetail": "지방분해,노폐물 배출,체온조절,혈압강하,항산화 효과,",
  "desc": "생보이차의 숙성 속도를 보완하기 위해, 잎을 물에 적셔 커다란 덩어리로 만든 후 따뜻하고 습도가 높은 곳에서 발효를 촉진시켜 만든다. 부드럽고 구수한 맛이 풍부하며 떫은 맛이 거의 없다.",
  "caffeineOX": True,
  "caffeine": "10mg/200ml",
  "caution": "흑차는 지방분해 효과가 탁월하지만 공복에 진하게 마신다면 위장에 부담을 줄 수 있다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%9D%91%EC%B0%A8_Dark+Tea/%ED%9D%91_%EC%88%99%EB%B3%B4%EC%9D%B4%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Yugbo Tea",
  "name": "육보차",
  "type": "흑차",
  "eng_type": "Dark Tea",
  "benefit": "다이어트 소화기능 정신건강",
  "benefitdetail": "콜레스테롤,지방분해,비만예방,항산화효과,스트레스 완화",
  "desc": "보이차와는 생산지와 제조방법이 달라 제조방법과 맛, 향에서 많은 차이가 나는 흑차이다. 차를 우려낸 탕색은 짙은 적색이며 맛이 진하면서도 순하고 독특한 과일향의 풍미가 있다.",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "흑차는 지방분해 효과가 탁월하지만 공복에 진하게 마신다면 위장에 부담을 줄 수 있다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%9D%91%EC%B0%A8_Dark+Tea/%ED%9D%91_%EC%9C%A1%EB%B3%B4%EC%B0%A8.png",
  "like": 0,
  "user_id": None
 },
 {
  "eng_name": "Cheongtaejeon",
  "name": "청태전",
  "type": "흑차",
  "eng_type": "Dark Tea",
  "benefit": "다이어트 피부미용 혈액순환",
  "benefitdetail": "지방분해,노폐물 배출,체온조절,혈압강하,항산화 효과,",
  "desc": "중국의 보이차와 달리 우리 나라 고유의 흑차이다. 이름의 뜻은 '푸른 이끼가 낀 엽전'으로 생긴 것 그대로를 표현한다. 주로 전라남도 장흥군에서 재배된다. 진홍빛의 차색은 오미자차와 비슷하지만 맛과 향은 옥수수차나 보리차와 가깝다. 생강, 오가피, 귤 껍질을 같이 넣고 우리면 향과 맛이 더 좋아진다.",
  "caffeineOX": True,
  "caffeine": "10~30mg/200ml",
  "caution": "흑차는 지방분해 효과가 탁월하지만 공복에 진하게 마신다면 위장에 부담을 줄 수 있다. ",
  "img": "https://s3.ap-northeast-2.amazonaws.com/alphafly.shop/tea_image/%ED%9D%91%EC%B0%A8_Dark+Tea/%ED%9D%91_%EC%B2%AD%ED%83%9C%EC%A0%84.png",
  "like": 0,
  "user_id": None
 }
])
