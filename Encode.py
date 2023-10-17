import random
d={'A':'•―','B':'―•••','C':'―•―•','D':'―••','E':"•",'F':"••―•",'G':"― ―•",'H':"••••",'I':"••",'J':"•― ― ―",'K':"―•―",'L':"•―••",'M':"― ―",'N':"―•",'O':"― ― ―",'P':"•― ―•",'Q':'― ―•―','R':'•―•','S':'•••','T':'―','U':'••―','V':'•••―','W':'•― ―','X':'―••―','Y':'―•― ―','Z':'― ―••','1':'•― ― ― ―','2':'••― ― ―','3':'•••― ― ―','4':'••••―','5':'•••••','6':'―••••','7':'― ―•••','8':'― ― ―••','9':'― ― ― ―•','0':'― ― ― ― ―','a':'•―','b':'―•••','c':'―•―•','d':'―••','e':"•",'f':"••―•",'g':"― ―•",'h':"••••",'i':"••",'j':"•― ― ―",'k':"―•―",'l':"•―••",'m':"― ―",'n':"―•",'o':"― ― ―",'p':"•― ―•",'q':'― ―•―','r':'•―•','s':'•••','t':'―','u':'••―','v':'•••―','w':'•― ―','x':'―••―','y':'―•― ―','z':'― ―••'}
l=["A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","Q","W","E","R","T","Y","U","I","O","P","<",">","/","?","`","~","+","|","!","@","#","$","%","^","&","*", ' ' , ' ' , ' ' , ' ' , ' ' ,'ᴤ','ᴥ','ᴦ','ᴧ','ᴨ','ᴩ','ᴪ','ᴫ','ᴬ','ᴭ','ᴮ','ᴯ','ᴰ','ᴱ','ᴲ','ᴳ','ᴴ','ᴵ','ᴶ','ᴷ','ᴸ','ᴹ','ᴺ','ᴻ','ᴼ','ᴽ','ᴾ','ᴿ','ᵀ','ᵁ','ᵂ','ᵃ','ᵄ','ᵅ','ᵆ','ᵇ','ᵈ','ᵉ','ᵊ','ᵋ','ᵌ','ᵍ','ᵎ','ᵏ','ᵐ','ᵑ','ᵒ','ᵓ','ᵔ','ᵕ','ᵖ','ᵗ','ᵘ','ᵙ','ᵚ','ᵛ','ᵜ','ᵝ','ᵞ','ᵟ','ᵠ','ᵡ','ᵢ','ᵣ','ᵤ','ᵥ','ᵦ','ᵧ','ᵨ','ᵩ','ᵪ','ᵫ','ᵬ','ᵭ','ᵮ','ᵯ','ᵰ','ᵱ','ᵲ','ᵳ','ᵴ','ᵵ','ᵶ','ᵷ','ᵸ','ᵹ','ᵺ','ᵻ','ᵼ','ᵽ','ᵾ','ᵿ','ᶀ','ᶁ','ᶂ','ᶃ','ᶄ','ᶅ','ᶆ','ᶇ','ᶈ','ᶉ','ᶊ','ᶋ','ᶌ','ᶍ','ᶎ','ᶏ','ᶐ','ᶑ','ᶒ','ᶓ','ᶔ','ᶕ','ᶖ','ᶗ','ᶘ','ᶙ','ᶚ','ᶛ','ᶜ','ᶝ','ᶞ','ᶟ','ᶠ','ᶡ','ᶢ','ᶣ','ᶤ','ᶥ','ᶦ','ᶧ','ᶨ','ᶩ','ᶪ','ᶫ','ᶬ','ᶭ','ᶮ','ᶯ','ᶰ','ᶱ','ᶲ','ᶳ','ᶴ','ᶵ','ᶶ','ᶷ','ᶸ','ᶹ','ᶺ','ᶻ','ᶼ','ᶽ','ᶾ','ᶿ','᷀','᷁','᷂','᷃','᷄','᷅','᷆','᷇','᷈','᷉','᷊','Ḁ','ḁ','Ḃ','ḃ','Ḅ','ḅ','Ḇ','ḇ','Ḉ','ḉ','Ḋ','ḋ','Ḍ','ḍ','Ḏ','ḏ','Ḑ','ḑ','Ḓ','ḓ','Ḕ','ḕ','Ḗ','ḗ','Ḙ','ḙ','Ḛ','ḛ','Ḝ','ḝ','Ḟ','ḟ','Ḡ','ḡ','Ḣ','ḣ','Ḥ','ḥ','Ḧ','ḧ','Ḩ','ḩ','Ḫ','ḫ','Ḭ','ḭ','Ḯ','ḯ','Ḱ','ḱ','Ḳ','ḳ','Ḵ','ḵ','Ḷ','ḷ','Ḹ','ḹ','Ḻ','ḻ','Ḽ','ḽ','Ḿ','ḿ','Ṁ','ṁ','Ṃ','ṃ','Ṅ','ṅ','Ṇ','ṇ','Ṉ','ṉ','Ṋ','ṋ','Ṍ','ṍ','Ṏ','ṏ','Ṑ','ṑ','Ṓ','ṓ','Ṕ','ṕ','Ṗ','ṗ','Ṙ','ṙ','Ṛ','ṛ','Ṝ','ṝ','Ṟ','ṟ','Ṡ','ṡ','Ṣ','ṣ','Ṥ','ṥ','Ṧ','ṧ','Ṩ','ṩ','Ṫ','ṫ','Ṭ','ṭ','Ṯ','ṯ','Ṱ','ṱ','Ṳ','ṳ','Ṵ','ṵ','Ṷ','ṷ','Ṹ','ṹ','Ṻ','ṻ','Ṽ','ṽ','Ṿ','ṿ','Ẁ','ẁ','Ẃ','ẃ','Ẅ','ẅ','Ẇ','ẇ','Ẉ','ẉ','Ẋ','ẋ','Ẍ','ẍ','Ẏ','ẏ','Ẑ','ẑ','Ẓ','ẓ','Ẕ','ẕ','ẖ','ẗ','ẘ','ẙ','ẚ','ẛ','ẜ','ẝ','ẞ','ẟ','Ạ','ạ','Ả','ả','Ấ','ấ','Ầ','ầ','Ẩ','ẩ','Ẫ','ẫ','Ậ','ậ','Ắ','ắ','Ằ','ằ','Ẳ','ẳ','Ẵ','ẵ','Ặ','ặ','Ẹ','ẹ','Ẻ','ẻ','Ẽ','ẽ','Ế','ế','Ề','ề','Ể','ể','Ễ','ễ','Ệ','ệ','Ỉ','ỉ','Ị','ị','Ọ','ọ','Ỏ','ỏ','Ố','ố','Ồ','ồ','Ổ','ổ','Ỗ','ỗ','Ộ','ộ','Ớ','ớ','Ờ','ờ','Ở','ở','Ỡ','ỡ','Ợ','ợ','Ụ','ụ','Ủ','ủ','Ứ','ứ','Ừ','ừ','Ử','ử','Ữ','ữ','Ự','ự','Ỳ','ỳ','Ỵ','ỵ','Ỷ','ỷ','Ỹ','ỹ','Ỻ','ỻ','Ỽ','ỽ','Ỿ','ỿ','ἀ','ἁ','ἂ','ἃ','ἄ','ἅ','ἆ','ἇ','Ἀ','Ἁ','Ἂ','Ἃ','Ἄ','Ἅ','Ἆ','Ἇ','ἐ','ἑ','ἒ','ἓ','ἔ','ἕ','἖','἗','Ἐ','Ἑ','Ἒ','Ἓ','Ἔ','Ἕ','἞','἟','ἠ','ἡ','ἢ','ἣ','ἤ','ἥ','ἦ','ἧ','Ἠ','Ἡ','Ἢ','Ἣ','Ἤ','Ἥ','Ἦ','Ἧ','ἰ','ἱ','ἲ','ἳ','ἴ','ἵ','ἶ','ἷ','Ἰ','Ἱ','Ἲ','Ἳ','Ἴ','Ἵ','Ἶ','Ἷ','ὀ','ὁ','ὂ','ὃ','ὄ','ὅ','Ὀ','Ὁ','Ὂ','Ὃ','Ὄ','Ὅ','ὐ','ὑ','ὒ','ὓ','ὔ','ὕ','ὖ','ὗ','Ὑ','Ὓ','Ὕ','Ὗ','ὠ','ὡ','ὢ','ὣ','ὤ','ὥ','ὦ','ὧ','Ὠ','Ὡ','Ὢ','Ὣ','Ὤ','Ὥ','Ὦ','Ὧ','ὰ','ά','ὲ','έ','ὴ','ή','ὶ','ί','ὸ','ό','ὺ','ύ','ὼ','ώ','ᾀ','ᾁ','ᾂ','ᾃ','ᾄ','ᾅ','ᾆ','ᾇ','ᾈ','ᾉ','ᾊ','ᾋ','ᾌ','ᾍ','ᾎ','ᾏ','ᾐ','ᾑ','ᾒ','ᾓ','ᾔ','ᾕ','ᾖ','ᾗ','ᾘ','ᾙ','ᾚ','ᾛ','ᾜ','ᾝ','ᾞ','ᾟ','ᾠ','ᾡ','ᾢ','ᾣ','ᾤ','ᾥ','ᾦ','ᾧ','ᾨ','ᾩ','ᾪ','ᾫ','ᾬ','ᾭ','ᾮ','ᾯ','ᾰ','ᾱ','ᾲ','ᾳ','ᾴ','ᾶ','ᾷ','Ᾰ','Ᾱ','Ὰ','Ά','ᾼ','᾽','ι','᾿','῀','῁','ῂ','ῃ','ῄ','῅','ῆ','ῇ','Ὲ','Έ','Ὴ','Ή','ῌ','῍','῎','῏','ῐ','ῑ','ῒ','ΐ','῔','῕','ῖ','ῗ','Ῐ','Ῑ','Ὶ','Ί','῜','῝','῞','῟','ῠ','ῡ','ῢ','ΰ','ῤ','ῥ','ῦ','ῧ','Ῠ','Ῡ','Ὺ','Ύ','Ῥ','῭','΅','`','⅏','⅐','⅑','⅒','⅓','⅔','⅕','⅖','⅗','⅘','⅙','⅚','⅛','⅜',"⛩",'ს','ტ','უ','ფ','ქ','ღ','ყ','შ','ჩ','ც','ძ','წ','ჭ','ხ','ჯ','ჰ','ჱ','ჲ','ჳ','ჴ','ჵ','ჶ','ჷ','ჸ','ჹ','ჺ','჻','ჼ','ჽ','ჾ','ჿ','ᄀ','ᄁ','ᄂ','ᄃ','ᄄ','ᄅ','ᄆ','ᄇ','ᄈ','ᄉ','ᄊ','ᄋ','ᄌ','ᄍ','ᄎ','ᄏ','ᄐ','ᄑ','ᄒ','ᄓ','ᄔ','ᄕ','ᄖ','ᄗ','ᄘ','ᄙ','ᄚ','ᄛ','ᄜ','ᄝ','ᄞ','ᄟ','ᄠ','ᄡ','ᄢ','ᄣ','ᄤ','ᄥ','ᄦ','ᄧ','ᄨ','ᄩ','ᄪ','ᄫ','ᄬ','ᄭ','ᄮ','ᄯ','ᄰ','ᄱ','ᄲ','ᄳ','ᄴ','ᄵ','ᄶ','ᄷ','ᄸ','ᄹ','ᄺ','ᄻ','ᄼ','ᄽ','ᄾ','ᄿ','ᅀ','ᅁ','ᅂ','ᅃ','ᅄ','ᅅ','ᅆ','ᅇ','ᅈ','ᅉ','ᅊ','ᅋ','ᅌ','ᅍ','ᅎ','ᅏ','ᅐ','ᅑ','ᅒ','ᅓ','ᅔ','ᅕ','ᅖ','ᅗ','ᅘ','ᅙ','ᅚ','ᅛ','ᅜ','ᅝ','ᅞ','ᅟ','ᅠ','ᅡ','ᅢ','ᅣ','ᅤ','ᅥ','ᅦ','ᅧ','ᅨ','ᅩ','ᅪ','ᅫ','ᅬ','ᅭ','ᅮ','ᅯ','ᅰ','ᅱ','ᅲ','ᅳ','ᅴ','ᅵ','ᅶ','ᅷ','ᅸ','ᅹ','ᅺ','ᅻ','ᅼ','ᅽ','ᅾ','ᅿ','ᆀ','ᆁ','ᆂ','ᆃ','ᆄ','ᆅ','ᆆ','ᆇ','ᆈ','ᆉ','ᆊ','ᆋ','ᆌ','ᆍ','ᆎ','ᆏ','ᆐ','ᆑ','ᆒ','ᆓ','ᆔ','ᆕ','ᆖ','ᆗ','ᆘ','ᆙ','ᆚ','ᆛ','ᆜ','ᆝ','ᆞ','ᆟ','ᆠ','ᆡ','ᆢ','ᆣ','ᆤ','ᆥ','ᆦ','ᆧ','ᆨ','ᆩ','ᆪ','ᆫ','ᆬ','ᆭ','ᆮ','ᆯ','ᆰ','ᆱ','ᆲ','ᆳ','ᆴ','ᆵ','ᆶ','ᆷ','ᆸ','ᆹ','ᆺ','ᆻ','ᆼ','ᆽ','ᆾ','ᆿ','ᇀ','ᇁ','ᇂ','ᇃ','ᇄ','ᇅ','ᇆ','ᇇ','ᇈ','ᇉ','ᇊ','ᇋ','ᇌ','ᇍ','ᇎ','ᇏ','ᇐ','ᇑ','ᇒ','ᇓ','ᇔ','ᇕ','ᇖ','ᇗ','ᇘ','ᇙ','ᇚ','ᇛ','ᇜ','ᇝ','ᇞ','ᇟ','ᇠ','ᇡ','ᇢ','ᇣ','ᇤ','ᇥ','ᇦ','ᇧ','ᇨ','ᇩ','ᇪ','ᇫ','ᇬ','ᇭ','ᇮ','ᇯ','ᇰ','ᇱ','ᇲ','ᇳ','ᇴ','ᇵ','ᇶ','ᇷ','ᇸ','ᇹ','ᇺ','ᇻ','ᇼ','ᇽ','ᇾ','ᇿ','ᚁ','ᚂ','ᚃ','ᚄ','ᚅ','ᚆ','ᚇ','ᚈ','ᚉ','ᚊ','ᚋ','ᚌ','ᚍ','ᚎ','ᚏ','ᚐ','ᚑ','ᚒ','ᚓ','ᚔ','ᚕ','ᚖ','ᚗ','ᚘ','ᚙ','ᚚ','᚛','᚜','ᚠ','ᚡ','ᚢ','ᚣ','ᚤ','ᚥ','ᚦ','ᚧ','ᚨ','ᚩ','ᚪ','ᚫ','ᚬ','ᚭ','ᚮ','ᚯ','ᚰ','ᚱ','ᚲ','ᚳ','ᚴ','ᚵ','ᚶ','ᚷ','ᚸ','ᚹ','ᚺ','ᚻ','ᚼ','ᚽ','ᚾ','ᚿ','ᛀ','ᛁ','ᛂ','ᛃ','ᛄ','ᛅ','ᛆ','ᛇ','ᛈ','ᛉ','ᛊ','ᛋ','ᛌ','ᛍ','ᛎ','ᛏ','ᛐ','ᛑ','ᛒ','ᛓ','ᛔ','ᛕ','ᛖ','ᛗ','ᛘ','ᛙ','ᛚ','ᛛ','ᛜ','ᛝ','ᛞ','ᛟ','ᛠ','ᛡ','ᛢ','ᛣ','ᛤ','ᛥ','ᛦ','ᛧ','ᛨ','ᛩ','ᛪ','᛫','᛬','᛭','ᛮ','ᛯ','ᛰ','ᴀ','ᴁ','ᴂ','ᴃ','ᴄ','ᴅ','ᴆ','ᴇ','ᴈ','ᴉ','ᴊ','ᴋ','ᴌ','ᴍ','ᴎ','ᴏ','ᴐ','ᴑ','ᴒ','ᴓ','ᴔ','ᴕ','ᴖ','ᴗ','ᴘ','ᴙ','ᴚ','ᴛ','ᴜ','ᴝ','ᴞ','ᴟ','ᴠ','ᴡ','ᴢ','ᴣ','Ӏ','Ӂ','ӂ','Ӄ','ӄ','Ӆ','ӆ','Ӈ','ӈ','Ӊ','ӊ','Ӌ','ӌ','Ӎ','ӎ','ӏ','Ӑ','ӑ','Ӓ','ӓ','Ӕ','ӕ','Ӗ','ӗ','Ә','ә','Ӛ','ӛ','Ӝ','ӝ','Ӟ','ӟ','Ӡ','ӡ','Ӣ','ӣ','Ӥ','ӥ','Ӧ','ӧ','Ө','ө','Ӫ','ӫ','Ӭ','ӭ','Ӯ','ӯ','Ӱ','ӱ','Ӳ','ӳ','Ӵ','ӵ','Ӷ','ӷ','Ӹ','ӹ','Ӻ','ӻ','Ӽ','ӽ','Ӿ','ӿ','Ԁ','ԁ','Ԃ','ԃ','Ԅ','ԅ','Ԇ','ԇ','Ԉ','ԉ','Ԋ','ԋ','Ԍ','ԍ','Ԏ','ԏ','Ԑ','ԑ','Ԓ','ԓ','Ԕ','ԕ','Ԗ','ԗ','Ԙ','ԙ','Ԛ','ԛ','Ԝ','ԝ','Ԟ','ԟ','Ԡ','ԡ','Ԣ','ԣ','Ԥ','ԥ','Ԧ','ԧ','Ԩ','ԩ','Ԫ','ԫ','Ԭ','ԭ','Ԯ','ԯ','԰','Ա','Բ','Գ','Դ','Ե','Զ','Է','Ը','Թ','Ժ','Ի','Լ','Խ','Ծ','Կ','Հ','Ձ','Ղ','Ճ','Մ','Յ','Ն','Շ','Ո','Չ','Պ','Ջ','Ռ','Ս','Վ','Տ','Ր','Ց','Ւ','Փ','Ք','Օ','Ֆ','ՙ','՚','՛','՜','՝','՞','՟','ՠ','ա','բ','գ','դ','ե','զ','է','ը','թ','ժ','ի','լ','խ','ծ','կ','հ','ձ','ղ','ճ','մ','յ','ն','շ','ո','չ','պ','ջ','ռ','ս','վ','տ','ր','ց','ւ','փ','ք','օ','ֆ','և','֋','֌','֍','֎','֏','א','ב','ג','ד؀','؁','؂','؃','؄','؅','؆','؇','؈','؉','؊','؋','،','؍','؎','؏','ؐ','ؑ','ؒ','ؓ','ؔ','ؕ','ؖ','ؗ','ؘ','ؙ','ؚ','۩',' ۝','۞','ݙ','ݚ','ݛ','ݜ','ݝ','ݞ','ݟ','ݠ','ݡ','ݢ','ݣ','ݤ','ݥ','ݦ','ݧ','ݨ','ݩ','ݪ','ݫ','ʨ','ʩ','ʪ','ʫ','ʬ','ʭ','ʮ','ʯ','ʰ','ʱ','ʲ','ʳ','ʴ','ʵ','ʶ','ʷ','ʸ','ʹ','ʺ','ʻ','ʼ','ʽ','ʾ','ʿ','ˀ','ˁ','˂','˃','˄','˅','ˆ','ˇ','ˈ','ˉ','ˊ','ˋ','ˌ','ˍ','ˎ','ˏ','ː','ˑ','˒','˓','˔','˕','˖','˗','˘','˙','˚','˛','˜','˝','˞','˟','ˠ','ˡ','ˢ','ˣ','ˤ','˥','˦','˧','˨','˩','˪','˫','ˬ','˭','ˮ','˯','˰','˱','˲','˳','˴','˵','˶','˷','˸','˹','˺','˻','˼','˽','˾','˿','̀','́','̂','̃','̄','̅','̆','̇','̈','̉','̊','̋','̌','̍','̎','̏','̐','̑','̒','̓','̔','̕','̖','̗','̘','̙','̚','̛','̜','̝','̞','̟','̠','̡','̢','̣','̤','̥','̦','̧','̨','̩','̪','̫','̬','̭','̮','̯','̰','̱','̲','̳','̴','̵','̶','̷','̸','̹','̺','̻','̼','̽','̾','̿','̀','́','͂','̓','̈́','ͅ','͆','͇','͈','͉','͊','͋','͌','͍','͎','͏','͐','͑','͒','͓','͔','͕','͖','͗','͘','͙','͚','͛','͜','͝','͞','͟','͠','͡','͢','ͣ','ͤ','ͥ','ͦ','ͧ','ͨ','ͩ','ͪ','ͫ','ͬ','ͭ','ͮ','ͯ','Ͱ','ͱ','Ͳ','ͳ','ʹ','͵','Ͷ','ͷ','͸','͹','ͺ','ͻ','ͼ','ͽ',';','Ϳ','΀','΁','΂','΃','΄','΅','Ά','·','Έ','Ή','Ί','Ό','Ύ','Ώ','ΐ','Α','Β','Γ','Δ','Ε','Ζ','Η','Θ','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ','Σ','Τ','Υ','Φ','Χ','Ψ','Ω','Ϊ','Ϋ','ά','έ','ή','ί','ΰ','α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ','ς','σ','τ','υ','φ','χ','ψ','ω','ϊ','ϋ','ό','ύ','ώ','Ϗ','ϐ','ϑ','ϒ','ϓ','ϔ','ϕ','ϖ','ϗ','Ϙ','ϙ','Ϛ','ϛ','Ϝ','ϝ','Ϟ','ϟ','Ϡ','ϡ','Ϣ','ϣ','Ϥ','ϥ','Ϧ','ϧ','Ϩ','ϩ','Ϫ','ϫ','Ϭ','ϭ','Ϯ','ϯ','ϰ','ϱ','ϲ','ϳ','ϴ','ϵ','϶','Ϸ','ϸ','Ϲ','Ϻ','ϻ','ϼ','Ͻ','Ͼ','Ͽ','Ѐ','Ё','Ђ','Ѓ','Є','Ѕ','І','Ї','Ј','Љ','Њ','Ћ','Ќ','Ѝ','Ў','Џ','А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я','а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','ѐ','ё','ђ','ѓ','є','ѕ','і','ї','ј','љ','њ','ћ','ќ','ѝ','ў','џ','Ѡ','ѡ','Ѣ','ѣ','Ѥ','ѥ','Ѧ','ѧ','Ѩ','ѩ','Ѫ','ѫ','Ѭ','ѭ','Ѯ','ѯ','Ѱ','ѱ','Ѳ','ѳ','Ѵ','ѵ','Ѷ','ѷ','Ѹ','ѹ','Ѻ','ѻ','Ѽ','ѽ','Ѿ','ѿ','Ҁ','ҁ','҂','҃','҄','҅','҆','҇','҈','҉','Ҋ','ҋ','Ҍ','ҍ','Ҏ','ҏ','Ґ','ґ','Ғ','ғ','Ҕ','ҕ','Җ','җ','Ҙ','ҙ','Қ','қ','Ҝ','ҝ','Ҟ','ҟ','Ҡ','ҡ','Ң','ң','Ҥ','ҥ','Ҧ','ҧ','Ҩ','ҩ','Ҫ','ҫ','Ҭ','ҭ','Ү','ү','Ұ','ұ','Ҳ','ҳ','Ҵ','ҵ','Ҷ','ҷ','Ҹ','ҹ','Һ','һ','Ҽ','ҽ','Ҿ','ҿ','ɍ','Ɏ','ɏ','ɐ','ɑ','ɒ','ɓ','ɔ','ɕ','ɖ','ɗ','ɘ','ə','ɚ','ɛ','ɜ','ɝ','ɞ','ɟ','ɠ','ɡ','ɢ','ɣ','ɤ','ɥ','ɦ','ɧ','ɨ','ɩ','ɪ','ɫ','ɬ','ɭ','ɮ','ɯ','ɰ','ɱ','ɲ','ɳ','ɴ','ɵ','ɶ','ɷ','ɸ','ɹ','ɺ','ɻ','ɼ','ɽ','ɾ','ɿ','ʀ','ʁ','ʂ','ʃ','ʄ','ʅ','ʆ','ʇ','ʈ','ʉ','ʊ','ʋ','ʌ','ʍ','ʎ','ʏ','ʐ','ʑ','ʒ','ʓ','ʔ','ʕ','ʖ','ʗ','ʘ','ʙ','ʚ','ʛ','ʜ','ʝ','ʞ','ʟ','ʠ','ʡ','ʢ','ʣ','ʤ','ʥ','ʦ','ʧ','ɍ','Ɏ','ɏ','ɐ','ɑ','ɒ','ɓ','ɔ','ɕ','ɖ','ɗ','ɘ','ə','ɚ','ɛ','ɜ','ɝ','ɞ','ɟ','ɠ','ɡ','ɢ','ɣ','ɤ','ɥ','ɦ','ɧ','ɨ','ɩ','ɪ','ɫ','ɬ','ɭ','ɮ','ɯ','ɰ','ɱ','ɲ','ɳ','ɴ','ɵ','ɶ','ɷ','ɸ','ɹ','ɺ','ɻ','ɼ','ɽ','ɾ','ɿ','ʀ','ʁ','ʂ','ʃ','ʄ','ʅ','ʆ','ʇ','ʈ','ʉ','ʊ','ʋ','ʌ','ʍ','ʎ','ʏ','ʐ','ʑ','ʒ','ʓ','ʔ','ʕ','ʖ','ʗ','ʘ','ʙ','ʚ','ʛ','ʜ','ʝ','ʞ','ʟ','ʠ','ʡ','ʢ','ʣ','ʤ','ʥ','ʦ','ʧ','ǲ','ǳ','Ǵ','ǵ','Ƕ','Ƿ','Ǹ','ǹ','Ǻ','ǻ','Ǽ','ǽ','Ǿ','ǿ','Ȁ','ȁ','Ȃ','ȃ','Ȅ','ȅ','Ȇ','ȇ','Ȉ','ȉ','Ȋ','ȋ','Ȍ','ȍ','Ȏ','ȏ','Ȑ','ȑ','Ȓ','ȓ','Ȕ','ȕ','Ȗ','ȗ','Ș','ș','Ț','ț','Ȝ','ȝ','Ȟ','ȟ','Ƞ','ȡ','Ȣ','ȣ','Ȥ','ȥ','Ȧ','ȧ','Ȩ','ȩ','Ȫ','ȫ','Ȭ','ȭ','Ȯ','ȯ','Ȱ','ȱ','Ȳ','ȳ','ȴ','ȵ','ȶ','ȷ','ȸ','ȹ','Ⱥ','Ȼ','ȼ','Ƚ','Ⱦ','ȿ','ɀ','Ɂ','ɂ','Ƀ','Ʉ','Ʌ','Ɇ','ɇ','Ɉ','ɉ','Ɋ','ɋ','Ɍ','Ơ','ơ','Ƣ','ƣ','Ƥ','ƥ','Ʀ','Ƨ','ƨ','Ʃ','ƪ','ƫ','Ƭ','ƭ','Ʈ','Ư','ư','Ʊ','Ʋ','Ƴ','ƴ','Ƶ','ƶ','Ʒ','Ƹ','ƹ','ƺ','ƻ','Ƽ','ƽ','ƾ','ƿ','ǀ','ǁ','ǂ','ǃ','Ǆ','ǅ','ǆ','Ǉ','ǈ','ǉ','Ǌ','ǋ','ǌ','Ǎ','ǎ','Ǐ','ǐ','Ǒ','ǒ','Ǔ','ǔ','Ǖ','ǖ','Ǘ','ǘ','Ǚ','ǚ','Ǜ','ǜ','ǝ','Ǟ','ǟ','Ǡ','ǡ','Ǣ','ǣ','Ǥ','ǥ','Ǧ','ǧ','Ǩ','ǩ','Ǫ','ǫ','Ǭ','ǭ','Ǯ','ǯ','ǰ','Ǳ','Ŕ','ŕ','Ŗ','ŗ','Ř','ř','Ś','ś','Ŝ','ŝ','Ş','ş','Š','š','Ţ','ţ','Ť','ť','Ŧ','ŧ','Ũ','ũ','Ū','ū','Ŭ','ŭ','Ů','ů','Ű','ű','Ų','ų','Ŵ','ŵ','Ŷ','ŷ','Ÿ','Ź','ź','Ż','ż','Ž','ž','ſ','ƀ','Ɓ','Ƃ','ƃ','Ƅ','ƅ','Ɔ','Ƈ','ƈ','Ɖ','Ɗ','Ƌ','ƌ','ƍ','Ǝ','Ə','Ɛ','Ƒ','ƒ','Ɠ','Ɣ','ƕ','Ɩ','Ɨ','Ƙ','ƙ','ƚ','ƛ','Ɯ','Ɲ','ƞ','Ɵ','ĕ','Ė','ė','Ę','ę','Ě','ě','Ĝ','ĝ','Ğ','ğ','Ġ','ġ','Ģ','ģ','Ĥ','ĥ','Ħ','ħ','Ĩ','ĩ','Ī','ī','Ĭ','ĭ','Į','į','İ','ı','Ĳ','ĳ','Ĵ','ĵ','Ķ','ķ','ĸ','Ĺ','ĺ','Ļ','ļ','Ľ','ľ','Ŀ','ŀ','Ł','ł','Ń','ń','Ņ','ņ','Ň','ň','ŉ','Ŋ','ŋ','Ō','ō','Ŏ','ŏ','Ő','ő','Œ','œ','Ý','Þ','ß','à','á','â','ã','ä','å','æ','ç','è','é','ê','ë','ì','í','î','ï','ð','ñ','ò','ó','ô','õ','ö','÷','ø','ù','ú','û','ü','ý','þ','ÿ','Ā','ā','Ă','ă','Ą','ą','Ć','ć','Ĉ','ĉ','Ċ','ċ','Č','č','Ď','ď','Đ','đ','Ē','ē','Ĕ',' · ', ' ¸ ', ' ¹ ', ' º ', ' » ', ' ¼ ', ' ½ ', ' ¾ ', ' ¿ ', ' À ', ' Á ', ' Â ', ' Ã ', ' Ä ', ' Å ', ' Æ ','Ç','È','É','Ê','Ë','Ì','Í','Î','Ï','Ð','Ñ','Ò','Ó','Ô','Õ','Ö','×','Ø','Ù','Ú','Û','Ü',' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ',' ',' ', ' ', ' ',' ', '¢', '£', '¤', '¥', '¦', '§', '¨', '©', ' ª ', ' « ', ' ¬ ',' ® ', ' ¯ ', ' ° ', ' ± ', ' ² ', ' ³ ', ' ´ ', ' µ ', ' ¶ ']
s=input("enter the string to be coverted ")
q=""
t=""
p=""
lo=['1','3','5','7','9']
le=['2','4','6','8']
for i in s:
    for j in d:
        if i==j:
            q=q+d[i]+random.choice(l)
        if i==" " :
            q=q+" "
for k in q:
    if k=="•":
            t=t+random.choice(lo)
    elif k=="―":
        t=t+random.choice(le)
    else:
        t=t+k
for i in t:
    if i=="  ":
        p=p+" "
    else:
        p=p+i
print(p)
