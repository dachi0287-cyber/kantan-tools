F = "const f$=n=>Math.round(n).toLocaleString();"
SALES = [
 dict(slug="arari", title="粗利・粗利率計算(売価・原価)", desc="売価と原価から粗利・粗利率・原価率を計算。目標粗利率からの必要売価も逆算。",
  body='<label>売価(円)<input id="p" type="number" value="10000"></label><label>原価(円)<input id="c" type="number" value="7000"></label><label>目標粗利率(%)<input id="g" type="number" value="35"></label><div class="res" id="r"></div>',
  js=F+'''function f(){const p=+$("p").value,c=+$("c").value,g=+$("g").value/100;const a=p-c;
$("r").innerHTML=`粗利: <b>${f$(a)}円</b><br>粗利率: <b>${p?(a/p*100).toFixed(1):0}%</b>(原価率 ${p?(c/p*100).toFixed(1):0}%)<br>マークアップ率: <b>${c?(a/c*100).toFixed(1):0}%</b><br>粗利率${(g*100).toFixed(0)}%にする必要売価: <b>${g<1?f$(c/(1-g)):"-"}円</b>`}
document.querySelectorAll("input").forEach(e=>e.oninput=f);f();''',
  text="見積や値引きの判断に必要な粗利を計算します。粗利率は売価に対する粗利の割合、マークアップ率は原価に対する粗利の割合で、混同しやすいので両方を表示しています。"),
 dict(slug="mokuhyo", title="売上目標の達成率・必要日額計算", desc="月間目標・現在の売上・残り営業日から、達成率と1日あたりに必要な売上を計算。",
  body='<label>月間目標(円)<input id="t" type="number" value="3000000"></label><label>現在の売上(円)<input id="n" type="number" value="1200000"></label><label>残り営業日数<input id="d" type="number" value="12"></label><div class="res" id="r"></div>',
  js=F+'''function f(){const t=+$("t").value,n=+$("n").value,d=+$("d").value;const rem=Math.max(t-n,0);
$("r").innerHTML=`達成率: <b>${t?(n/t*100).toFixed(1):0}%</b><br>目標まで残り: <b>${f$(rem)}円</b><br>1日あたり必要額: <b>${d>0?f$(rem/d):"-"}円</b>`}
document.querySelectorAll("input").forEach(e=>e.oninput=f);f();''',
  text="月末に向けて、あといくら売ればよいかを逆算します。週次の進捗確認や、営業会議での報告に使えます。"),
 dict(slug="mitsumori", title="見積金額計算(数量・値引き・消費税)", desc="単価×数量から値引き後の小計・消費税・税込合計を計算。",
  body='<label>単価(円)<input id="u" type="number" value="50000"></label><label>数量<input id="q" type="number" value="10"></label><label>値引き率(%)<input id="d" type="number" value="5"></label><label>税率<select id="x"><option value="10">10%</option><option value="8">8%</option></select></label><div class="res" id="r"></div>',
  js=F+'''function f(){const u=+$("u").value,q=+$("q").value,d=+$("d").value/100,x=+$("x").value/100;
const s=u*q,s2=Math.floor(s*(1-d)),tax=Math.floor(s2*x);
$("r").innerHTML=`定価合計: ${f$(s)}円<br>値引き額: ${f$(s-s2)}円<br>値引き後(税抜): <b>${f$(s2)}円</b><br>消費税: ${f$(tax)}円<br>税込合計: <b>${f$(s2+tax)}円</b>`}
document.querySelectorAll("input,select").forEach(e=>e.oninput=f);f();''',
  text="見積書の金額確認用です。端数は切り捨てで計算しています。正式な見積書の端数処理は社内ルールに従ってください。"),
 dict(slug="sales-mail", title="営業メール文面ジェネレーター", desc="初回アポ依頼・訪問お礼・日程調整・見積送付・フォローの営業メールを自動作成。",
  body='<label>種類<select id="k"><option value="0">初回アポイント依頼</option><option value="1">訪問のお礼</option><option value="2">日程調整</option><option value="3">見積書の送付</option><option value="4">ご検討状況の確認</option></select></label><label>相手の会社名<input id="a" value="株式会社〇〇"></label><label>相手のお名前<input id="b" value="山田"></label><label>自社名<input id="c" value="株式会社△△"></label><label>自分の名前<input id="d" value="鈴木"></label><label>商材・用件<input id="e" value="業務効率化サービス"></label><textarea id="o" rows="14"></textarea><button id="cp">コピー</button>',
  js='''function f(){const a=$("a").value,b=$("b").value,c=$("c").value,d=$("d").value,e=$("e").value;
const H=`${a}\\n${b}様\\n\\nお世話になっております。\\n${c}の${d}です。\\n\\n`;const S=`\\n\\n何卒よろしくお願い申し上げます。\\n\\n${c}\\n${d}`;
const T=[`突然のご連絡失礼いたします。\\n${e}についてご案内したくご連絡いたしました。\\n\\n貴社の課題解決に貢献できると考え、30分ほどお時間をいただけないでしょうか。\\n候補日をお知らせいただければ、ご都合に合わせます。`,
`本日はお忙しい中、貴重なお時間をいただき誠にありがとうございました。\\n${e}についてお伝えした内容で、ご不明点がございましたらお気軽にご連絡ください。\\n\\n次のステップとして、改めてご提案資料をお送りいたします。`,
`${e}の件で、改めてお打ち合わせの日程を調整させてください。\\n以下の候補日はいかがでしょうか。\\n\\n・〇月〇日(〇) 〇時〜\\n・〇月〇日(〇) 〇時〜\\n・〇月〇日(〇) 〇時〜\\n\\n上記以外でもご都合のよい日時があればお知らせください。`,
`${e}のお見積書をお送りいたします。\\n添付ファイルをご確認いただけますと幸いです。\\n\\n内容について、ご不明点やご要望がございましたらお申し付けください。`,
`先日ご案内した${e}について、その後ご検討状況はいかがでしょうか。\\n\\nご質問や追加でご確認されたい点がございましたら、いつでもお申し付けください。\\nお打ち合わせのお時間をいただくことも可能です。`];
const sub=["ご挨拶とご提案のお願い","本日のお礼","日程調整のお願い","お見積書送付のご連絡","ご検討状況のご確認"];
$("o").value=`件名: 【${c}】${sub[$("k").value]}\\n\\n`+H+T[$("k").value]+S}
document.querySelectorAll("input,select").forEach(e=>e.oninput=f);$("cp").onclick=()=>navigator.clipboard.writeText($("o").value);f();''',
  text="営業メールの下書きを作成します。そのまま送らず、相手や状況に合わせて必ず手直ししてください。入力内容は外部に送信されません。"),
 dict(slug="eigyobi", title="営業日数計算(土日を除く)", desc="2つの日付の間の営業日数(土日除く)を計算。納期や締め切りの確認に。",
  body='<label>開始日<input id="a" type="date"></label><label>終了日<input id="b" type="date"></label><div class="res" id="r"></div>',
  js='''const d0=new Date().toISOString().slice(0,10);$("a").value=d0;$("b").value=d0;
function f(){let a=new Date($("a").value),b=new Date($("b").value);if(isNaN(a)||isNaN(b)){$("r").textContent="日付を入力";return}
let n=0,t=0;for(let d=new Date(a);d<=b;d.setDate(d.getDate()+1)){t++;const w=d.getDay();if(w!=0&&w!=6)n++}
$("r").innerHTML=`営業日数(土日除く・両端含む): <b>${n}</b>日<br>暦日数: ${t}日`}
document.querySelectorAll("input").forEach(e=>e.oninput=f);f();''',
  text="土曜・日曜を除いた日数を数えます。祝日や会社の休業日は含まれていないため、実際の営業日数は少なくなる場合があります。"),
 dict(slug="pipeline", title="案件の加重売上(受注確度)計算", desc="案件ごとの金額×受注確度で、見込み売上を合計。パイプライン管理に。",
  body='<p>1行に「金額,確度%」の形式で入力(例: 1000000,50)</p><textarea id="t" rows="8">1000000,50\n500000,80\n2000000,20</textarea><div class="res" id="r"></div>',
  js=F+'''function f(){let s=0,w=0,n=0;$("t").value.split("\\n").forEach(l=>{const p=l.split(/[,\\s]+/).map(Number);if(p.length>=2&&!isNaN(p[0])&&!isNaN(p[1])){s+=p[0];w+=p[0]*p[1]/100;n++}});
$("r").innerHTML=`案件数: ${n}件<br>案件総額: <b>${f$(s)}円</b><br>加重見込み売上: <b>${f$(w)}円</b><br>平均確度: ${s?(w/s*100).toFixed(1):0}%`}
$("t").oninput=f;f();''',
  text="受注確度を掛け合わせた見込み売上を計算します。確度の基準(A=80%、B=50%など)は社内でそろえておくと、予測の精度が上がります。"),
 dict(slug="sonneki", title="損益分岐点計算", desc="固定費・販売単価・変動費から損益分岐点の販売数量と売上高を計算。",
  body='<label>固定費(円/月)<input id="f" type="number" value="500000"></label><label>販売単価(円)<input id="p" type="number" value="3000"></label><label>変動費(1個あたり・円)<input id="v" type="number" value="1200"></label><div class="res" id="r"></div>',
  js=F+'''function f(){const fx=+$("f").value,p=+$("p").value,v=+$("v").value;const m=p-v;
$("r").innerHTML=m>0?`1個あたり利益(限界利益): <b>${f$(m)}円</b><br>損益分岐点の販売数: <b>${Math.ceil(fx/m).toLocaleString()}個</b><br>損益分岐点の売上高: <b>${f$(Math.ceil(fx/m)*p)}円</b>`:"販売単価が変動費を上回っていません"}
document.querySelectorAll("input").forEach(e=>e.oninput=f);f();''',
  text="利益がゼロになる販売数量を計算します。新商品の価格設定や、新規出店・新規施策の判断材料になります。"),
 dict(slug="shiharai", title="請求・支払期日計算(締め日・支払サイト)", desc="取引日・締め日・支払サイトから支払期日を計算。月末締め翌月末払いなどに対応。",
  body='<label>取引日(請求日)<input id="a" type="date"></label><label>締め日<select id="c"><option value="31">月末</option><option value="25">25日</option><option value="20">20日</option><option value="15">15日</option><option value="10">10日</option></select></label><label>支払月<select id="m"><option value="1">翌月</option><option value="2">翌々月</option></select></label><label>支払日<select id="p"><option value="31">末日</option><option value="25">25日</option><option value="20">20日</option><option value="15">15日</option><option value="10">10日</option></select></label><div class="res" id="r"></div>',
  js='''$("a").value=new Date().toISOString().slice(0,10);
const W=["日","月","火","水","木","金","土"];
function f(){const t=new Date($("a").value);if(isNaN(t)){$("r").textContent="日付を入力";return}
const c=+$("c").value,m=+$("m").value,p=+$("p").value;
const last=(y,mo)=>new Date(y,mo+1,0).getDate();
let y=t.getFullYear(),mo=t.getMonth();const cd=Math.min(c,last(y,mo));
if(t.getDate()>cd){mo++}
const close=new Date(y,mo,Math.min(c,last(y,mo)));
const py=new Date(y,mo+m,1);const pay=new Date(py.getFullYear(),py.getMonth(),Math.min(p,last(py.getFullYear(),py.getMonth())));
const fmt=d=>`${d.getFullYear()}年${d.getMonth()+1}月${d.getDate()}日(${W[d.getDay()]})`;
$("r").innerHTML=`締め日: <b>${fmt(close)}</b><br>支払期日: <b>${fmt(pay)}</b><br><small>※土日祝にあたる場合は、取引先との取り決めに従って前倒し・後ろ倒しになります。</small>`}
document.querySelectorAll("input,select").forEach(e=>e.oninput=f);f();''',
  text="請求書をいつ出すと、いつ入金されるかを確認できます。「月末締め翌月末払い」「20日締め翌月10日払い」などの条件に対応しています。"),
]
SALES_FAQ = {
"arari":[("粗利率と原価率の違いは？","粗利率は売価に対する粗利の割合、原価率は売価に対する原価の割合です。合計は100%になります。"),("マークアップ率とは？","原価にどれだけ上乗せしたかの割合です。粗利率とは分母が違うため、同じ数字になりません。")],
"mokuhyo":[("残り営業日数はどう数えますか？","土日祝を除いた、月末までの稼働日です。営業日の数え方は営業日数計算ツールも使えます。"),("必要額が大きすぎる場合は？","追加の案件創出や、受注見込みの高い案件の前倒しを検討する目安にしてください。")],
"mitsumori":[("値引きは税抜と税込のどちらに適用しますか？","このツールは税抜金額に値引きを適用し、そのあとで消費税を計算します。"),("端数処理はどうなりますか？","小計・消費税ともに切り捨てです。社内ルールに合わせて調整してください。")],
"sales-mail":[("そのまま送ってよいですか？","下書きとしてご利用ください。相手の状況や関係性に合わせて、必ず文面を確認・修正してください。"),("入力した情報は保存されますか？","保存も送信もされません。ブラウザ内で作成されます。")],
"eigyobi":[("祝日は除外されますか？","いいえ。土日のみを除外します。祝日や休業日は別途差し引いてください。"),("開始日と終了日は含まれますか？","はい。両端を含めて数えます。")],
"pipeline":[("確度はどう決めればよいですか？","受注フェーズごとに基準を決めるのが一般的です(例: 提案=20%、見積提出=50%、最終交渉=80%)。"),("加重売上と予算の関係は？","加重売上が目標を下回る場合は、新規案件の追加が必要というサインです。")],
"sonneki":[("損益分岐点とは？","売上と費用が等しく、利益がゼロになる点です。これを超えると黒字になります。"),("変動費と固定費の違いは？","変動費は販売数量に比例して増える費用(仕入れ・配送費など)、固定費は売上に関わらず発生する費用(家賃・人件費など)です。")],
"shiharai":[("「月末締め翌月末払い」はいつ支払われますか？","例: 4月15日の取引は4月末で締まり、5月末が支払期日です。"),("支払日が休日の場合は？","契約や取引先の規定によります。前営業日払い・翌営業日払いなど、事前に確認してください。")],
}

SALES += [
 dict(slug="funnel", title="必要な商談数・アポ数の逆算計算", desc="売上目標・平均単価・成約率から、必要な受注数・アポ数・架電数を逆算。",
  body='<label>月間売上目標(円)<input id="t" type="number" value="3000000"></label><label>平均受注単価(円)<input id="u" type="number" value="300000"></label><label>アポ→受注の成約率(%)<input id="c" type="number" value="25"></label><label>架電→アポの獲得率(%)<input id="a" type="number" value="3"></label><div class="res" id="r"></div>',
  js=F+'''function f(){const t=+$("t").value,u=+$("u").value,c=+$("c").value/100,a=+$("a").value/100;
if(!(u>0&&c>0&&a>0)){$("r").textContent="単価・率は0より大きい値を入力";return}
const o=Math.ceil(t/u),ap=Math.ceil(o/c),ca=Math.ceil(ap/a);
$("r").innerHTML=`必要な受注数: <b>${o.toLocaleString()}件</b><br>必要なアポ数: <b>${ap.toLocaleString()}件</b><br>必要な架電数: <b>${ca.toLocaleString()}件</b>`}
document.querySelectorAll("input").forEach(e=>e.oninput=f);f();''',
  text="売上目標から、受注・アポ・架電に必要な数を逆算します。成約率や獲得率は、過去の実績の平均値を入れると、実際に近い目安になります。"),
 dict(slug="ltv", title="顧客生涯価値(LTV)計算", desc="平均単価・購入頻度・継続年数から顧客生涯価値(LTV)と、獲得コストとの比率を計算。",
  body='<label>平均購入単価(円)<input id="p" type="number" value="8000"></label><label>年間購入回数<input id="n" type="number" value="4"></label><label>継続年数<input id="y" type="number" value="3"></label><label>粗利率(%)<input id="g" type="number" value="40"></label><label>顧客獲得コスト(円)<input id="k" type="number" value="15000"></label><div class="res" id="r"></div>',
  js=F+'''function f(){const p=+$("p").value,n=+$("n").value,y=+$("y").value,g=+$("g").value/100,k=+$("k").value;
const s=p*n*y,gp=s*g;
$("r").innerHTML=`売上ベースLTV: <b>${f$(s)}円</b><br>粗利ベースLTV: <b>${f$(gp)}円</b><br>LTV÷獲得コスト: <b>${k>0?(gp/k).toFixed(2):"-"}倍</b>(一般に3倍以上が目安と言われます)`}
document.querySelectorAll("input").forEach(e=>e.oninput=f);f();''',
  text="1人の顧客が取引期間全体でもたらす価値を計算します。獲得コストの上限を決めたり、継続施策に投資する判断材料にします。3倍の目安は業種で異なる一般論です。"),
 dict(slug="nouki-gyakusan", title="納期からの逆算(営業日)", desc="納期日から、必要な営業日数ぶん前の開始期限を逆算。土日を除いて計算。",
  body='<label>納期日<input id="a" type="date"></label><label>必要な営業日数<input id="n" type="number" value="10"></label><div class="res" id="r"></div>',
  js='''$("a").value=new Date(Date.now()+30*864e5).toISOString().slice(0,10);
const W=["日","月","火","水","木","金","土"];
function f(){const d=new Date($("a").value),n=+$("n").value;if(isNaN(d)||!(n>=0)){$("r").textContent="入力を確認";return}
let c=0;while(c<n){d.setDate(d.getDate()-1);const w=d.getDay();if(w!=0&&w!=6)c++}
$("r").innerHTML=`開始期限: <b>${d.getFullYear()}年${d.getMonth()+1}月${d.getDate()}日(${W[d.getDay()]})</b><br><small>※土日のみ除外。祝日・休業日は含まれていません。</small>`}
document.querySelectorAll("input").forEach(e=>e.oninput=f);f();''',
  text="納期から逆算して、いつまでに作業を始める必要があるかを求めます。祝日や会社の休業日は考慮されないため、余裕を持って確認してください。"),
]
SALES_FAQ.update({
"funnel":[("成約率や獲得率はどう決めればよいですか？","過去3か月程度の実績の平均を使います。実績がない場合は、まず仮の数値で試算し、実績が出たら置き換えてください。"),("結果が大きすぎる場合は？","単価の引き上げ、成約率の改善、紹介などの別の流入経路を検討する材料にしてください。")],
"ltv":[("LTVとは何ですか？","1人の顧客が取引期間全体で生み出す売上や利益の合計です。顧客生涯価値とも呼ばれます。"),("獲得コストはどう数えますか？","広告費や営業の人件費など、新規顧客を獲得するためにかかった費用を、獲得した顧客数で割った値です。"),("3倍という目安は絶対ですか？","いいえ。一般によく言われる目安で、業種や事業の段階によって適切な水準は異なります。")],
"nouki-gyakusan":[("営業日はどう数えますか？","土曜・日曜を除いた日数です。納期日当日は数えず、その前の日から数えます。"),("祝日は考慮されますか？","いいえ。祝日や会社の休業日は含まれません。必要に応じて、余裕を持った日数を入力してください。")],
})
