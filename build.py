#!/usr/bin/env python3
"""静的ツールサイト生成。使い方: SITE_URL=https://example.com ADSENSE=ca-pub-xxxx python3 build.py"""
import os, html, datetime
SITE = (os.environ.get("SITE_URL") or "").rstrip("/")
ADS = os.environ.get("ADSENSE") or ""
NAME = "かんたんツール帳"
OUT = "dist"
TODAY = datetime.date.today().isoformat()

TOOLS = [
 dict(slug="moji-count", title="文字数カウント", desc="文字数・行数・バイト数を即座にカウント。原稿用紙換算にも対応。",
  body='<textarea id="t" rows="10" placeholder="ここに文章を入力"></textarea><div class="res" id="r"></div>',
  js='''const t=$("t"),r=$("r");function f(){const s=t.value;const ns=s.replace(/\\s/g,"");
r.innerHTML=`文字数: <b>${[...s].length}</b>(空白除く <b>${[...ns].length}</b>)<br>行数: <b>${s?s.split("\\n").length:0}</b><br>バイト数(UTF-8): <b>${new Blob([s]).size}</b><br>原稿用紙(400字): <b>${(Math.ceil([...s].length/400*10)/10)}</b>枚`}
t.oninput=f;f();''',
  text="文章の文字数を数えるツールです。ブログ記事やレポート、SNS投稿の文字数制限の確認に使えます。すべてブラウザ内で処理され、入力内容は送信されません。"),
 dict(slug="tax-calc", title="消費税計算(10%・8%)", desc="税込・税抜を相互に計算。軽減税率8%にも対応。",
  body='<label>金額(円)<input id="a" type="number" value="1000"></label><label>税率<select id="p"><option value="10">10%</option><option value="8">8%(軽減)</option></select></label><div class="res" id="r"></div>',
  js='''function f(){const a=+$("a").value,p=+$("p").value/100;
$("r").innerHTML=`税抜 ${a.toLocaleString()}円 → 税込 <b>${Math.floor(a*(1+p)).toLocaleString()}円</b>(税 ${Math.floor(a*p).toLocaleString()}円)<br>税込 ${a.toLocaleString()}円 → 税抜 <b>${Math.ceil(a/(1+p)).toLocaleString()}円</b>`}
document.querySelectorAll("input,select").forEach(e=>e.oninput=f);f();''',
  text="消費税の計算ツールです。端数は切り捨て(税込)・切り上げ(税抜)で表示しています。実際の端数処理は事業者ごとに異なる場合があります。"),
 dict(slug="wareki", title="和暦・西暦変換", desc="西暦から和暦(令和・平成・昭和・大正・明治)へ、和暦から西暦へ変換。",
  body='<label>西暦<input id="y" type="number" value="2026"></label><div class="res" id="r"></div>',
  js='''const E=[["令和",2019],["平成",1989],["昭和",1926],["大正",1912],["明治",1868]];
function f(){const y=+$("y").value;const e=E.find(x=>y>=x[1]);
$("r").innerHTML=e?`${y}年 = <b>${e[0]}${y-e[1]+1==1?"元":y-e[1]+1}年</b>`:"明治以前は対応していません";}
$("y").oninput=f;f();''',
  text="西暦を和暦に変換します。改元の年は新元号の元年として表示しています(例: 2019年=令和元年)。"),
 dict(slug="date-diff", title="日数計算(2つの日付の間)", desc="2つの日付の間の日数・週数を計算。期限や経過日数の確認に。",
  body='<label>開始日<input id="a" type="date"></label><label>終了日<input id="b" type="date"></label><div class="res" id="r"></div>',
  js='''const d=new Date().toISOString().slice(0,10);$("a").value=d;$("b").value=d;
function f(){const a=new Date($("a").value),b=new Date($("b").value);const n=Math.round((b-a)/864e5);
$("r").innerHTML=isNaN(n)?"日付を入力":`<b>${n}</b>日(${(n/7).toFixed(1)}週間)`}
document.querySelectorAll("input").forEach(e=>e.oninput=f);f();''',
  text="2つの日付の間の日数を計算します。開始日と終了日の差を表示します(当日を含めたい場合は+1してください)。"),
 dict(slug="percent", title="割合・割引計算", desc="○%引きの価格、○は○○の何%か、増減率をまとめて計算。",
  body='<label>元の値<input id="a" type="number" value="5000"></label><label>割引率(%)<input id="p" type="number" value="20"></label><label>比較する値<input id="b" type="number" value="3000"></label><div class="res" id="r"></div>',
  js='''function f(){const a=+$("a").value,p=+$("p").value,b=+$("b").value;
$("r").innerHTML=`${p}%引き: <b>${Math.round(a*(1-p/100)).toLocaleString()}</b>(割引額 ${Math.round(a*p/100).toLocaleString()})<br>${b} は ${a} の <b>${a?(b/a*100).toFixed(1):0}%</b><br>${a}→${b} の増減率: <b>${a?((b-a)/a*100).toFixed(1):0}%</b>`}
document.querySelectorAll("input").forEach(e=>e.oninput=f);f();''',
  text="セールの割引価格や、前年比などの増減率を計算できます。"),
 dict(slug="bmi", title="BMI計算", desc="身長と体重からBMIと適正体重を計算。",
  body='<label>身長(cm)<input id="h" type="number" value="170"></label><label>体重(kg)<input id="w" type="number" value="65"></label><div class="res" id="r"></div>',
  js='''function f(){const h=$("h").value/100,w=+$("w").value;const b=w/(h*h);
const c=b<18.5?"低体重":b<25?"普通体重":b<30?"肥満(1度)":"肥満(2度以上)";
$("r").innerHTML=`BMI: <b>${b.toFixed(1)}</b>(${c})<br>適正体重(BMI22): <b>${(22*h*h).toFixed(1)}kg</b>`}
document.querySelectorAll("input").forEach(e=>e.oninput=f);f();''',
  text="日本肥満学会の基準(18.5未満=低体重、18.5〜25未満=普通、25以上=肥満)で判定します。医療上の判断は医師にご相談ください。"),
 dict(slug="jikyu", title="時給・月収・年収換算", desc="時給から月収・年収を、または年収から時給をざっくり換算。",
  body='<label>時給(円)<input id="a" type="number" value="1200"></label><label>1日の労働時間<input id="h" type="number" value="8"></label><label>月の出勤日数<input id="d" type="number" value="20"></label><div class="res" id="r"></div>',
  js='''function f(){const a=+$("a").value,h=+$("h").value,d=+$("d").value;const m=a*h*d;
$("r").innerHTML=`月収(額面): <b>${m.toLocaleString()}円</b><br>年収(額面): <b>${(m*12).toLocaleString()}円</b><br>手取り目安(約80%): ${Math.round(m*.8).toLocaleString()}円/月`}
document.querySelectorAll("input").forEach(e=>e.oninput=f);f();''',
  text="アルバイトや副業の収入目安を計算します。手取りは社会保険・税金で変わるため、約80%の概算です。"),
 dict(slug="kaigyo", title="改行削除・テキスト整形", desc="PDFコピペの余計な改行や空白を一括削除。",
  body='<textarea id="t" rows="8" placeholder="整形したい文章"></textarea><div><button id="b1">改行を削除</button> <button id="b2">空行を削除</button> <button id="b3">全角→半角英数</button> <button id="b4">コピー</button></div><textarea id="o" rows="8" readonly></textarea>',
  js='''const t=$("t"),o=$("o");
$("b1").onclick=()=>o.value=t.value.replace(/\\r?\\n/g,"");
$("b2").onclick=()=>o.value=t.value.replace(/^\\s*\\n/gm,"");
$("b3").onclick=()=>o.value=t.value.replace(/[Ａ-Ｚａ-ｚ０-９]/g,c=>String.fromCharCode(c.charCodeAt(0)-0xFEE0));
$("b4").onclick=()=>navigator.clipboard.writeText(o.value);''',
  text="PDFや Web ページからコピーした文章の不要な改行を取り除きます。処理はすべてブラウザ内で完結します。"),
]


FAQ = {
"moji-count":[("空白や改行は文字数に含まれますか？","「文字数」は空白・改行を含む総数、「空白除く」は含まない数です。提出先の指定に合わせて使い分けてください。"),("バイト数は何のために使いますか？","SMSやデータベースの項目など、バイト数で上限が決まっている場面の確認に使います。UTF-8では日本語は1文字あたり約3バイトです。"),("入力した文章は保存されますか？","保存も送信もされません。処理はすべてお使いのブラウザ内で行われます。")],
"tax-calc":[("軽減税率8%の対象は何ですか？","飲食料品(酒類・外食を除く)と定期購読の新聞が対象です。テイクアウトは8%、店内飲食は10%です。"),("端数処理はどうなりますか？","本ツールは税込を切り捨て、税抜を切り上げで表示します。請求書では事業者ごとの端数処理ルールに従ってください。"),("インボイス制度の計算にも使えますか？","税率ごとの消費税額の目安確認に使えます。正式な適格請求書の記載は会計ソフト等でご確認ください。")],
"wareki":[("令和は何年から始まりましたか？","2019年(令和元年)5月1日からです。本ツールは年単位の変換のため、2019年は令和元年と表示します。"),("平成と昭和の境目はいつですか？","昭和は1926〜1988年、平成は1989〜2018年です。"),("西暦から和暦を暗算するには？","令和は西暦-2018、平成は西暦-1988、昭和は西暦-1925で求められます。")],
"date-diff":[("当日を含めた日数にするには？","表示された日数に1を足してください。たとえば期間の初日も数える場合に使います。"),("営業日の計算はできますか？","本ツールは暦日数のみです。土日祝を除く計算は別途ご確認ください。"),("週数の小数は何を表しますか？","日数を7で割った値です。10日なら約1.4週間です。")],
"percent":[("○%引きはどう計算しますか？","元の値×(1−割引率÷100)です。5,000円の20%引きは4,000円です。"),("増減率の求め方は？","(新しい値−元の値)÷元の値×100です。前年比や値上がり率に使います。"),("割増(○%上乗せ)にも使えますか？","割引率にマイナスの値を入れると、上乗せ後の価格が計算できます。")],
"bmi":[("BMIの計算式は？","体重(kg)÷身長(m)の2乗です。"),("適正体重はどう決まりますか？","BMIが22になる体重が、統計的に病気になりにくいとされ、適正体重の目安とされています。"),("筋肉質でも当てはまりますか？","BMIは体脂肪を区別しないため、筋肉量の多い方は実態と合わない場合があります。")],
"jikyu":[("手取りは額面の何割ですか？","おおむね75〜85%です。社会保険料や所得税・住民税で変わります。"),("副業の収入にも使えますか？","時給や1日の時間を入力すれば、副業の月収の目安がわかります。"),("扶養の範囲かどうか知りたいです。","年収の目安が出るので、103万円・130万円などの基準と比較してください。制度の詳細は公式情報をご確認ください。")],
"kaigyo":[("PDFからコピーすると改行が入るのはなぜですか？","PDFは行ごとに文字が配置されているため、コピー時に各行の末尾に改行が入ります。"),("全角英数字を半角にするとどうなりますか？","「ＡＢＣ１２３」が「ABC123」になります。全角カナや記号は変換しません。"),("入力内容は外部に送られますか？","送信されません。すべてブラウザ内で処理されます。")],
}

CSS="""body{font-family:system-ui,-apple-system,"Hiragino Sans","Noto Sans JP",sans-serif;max-width:720px;margin:0 auto;padding:16px;line-height:1.7;color:#222}
header a{font-weight:bold;text-decoration:none;color:#0b5}label{display:block;margin:8px 0}input,select,textarea{width:100%;padding:8px;font-size:16px;box-sizing:border-box}
.res{background:#f2faf5;border-radius:8px;padding:12px;margin:12px 0;font-size:18px}button{padding:8px 12px;margin:4px 0}.ad{min-height:90px;margin:16px 0;text-align:center}
ul.l{padding-left:1.2em}footer{margin-top:32px;font-size:13px;color:#666}"""

def page(title, desc, path, inner, extra_head=""):
    ads = f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADS}" crossorigin="anonymous"></script>' if ADS else ""
    return f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">{('<link rel="canonical" href="'+SITE+path+'">') if SITE else ""}
<style>{CSS}</style>{ads}{extra_head}</head><body><header><a href="./">{NAME}</a></header>{inner}
<footer><a href="privacy.html">プライバシーポリシー</a> / &copy; {NAME}</footer></body></html>'''

def ad_slot():
    return '<div class="ad"><!-- ad slot: AdSenseの広告ユニットをここに貼る --></div>'

def w(path, s):
    p=os.path.join(OUT,path.lstrip("/")); os.makedirs(os.path.dirname(p) or ".",exist_ok=True); open(p,"w",encoding="utf-8").write(s)

urls=["/"]
for t in TOOLS:
    others="".join(f'<li><a href="{o["slug"]}.html">{o["title"]}</a></li>' for o in TOOLS if o is not t)
    qa=FAQ.get(t["slug"],[])
    faq_html="".join(f"<h3>{q}</h3><p>{a}</p>" for q,a in qa)
    import json as _j
    ld=_j.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qa]},ensure_ascii=False)
    inner=f'''<h1>{t["title"]}</h1><p>{t["desc"]}</p>{t["body"]}{ad_slot()}<h2>このツールについて</h2><p>{t["text"]}</p>
<h2>よくある質問</h2>{faq_html}<h2>ほかのツール</h2><ul class="l">{others}</ul><script>const $=i=>document.getElementById(i);{t["js"]}</script>'''
    w(f'/{t["slug"]}.html', page(f'{t["title"]}｜{NAME}', t["desc"], f'/{t["slug"]}.html', inner, f'<script type="application/ld+json">{ld}</script>'))
    urls.append(f'/{t["slug"]}.html')

lst="".join(f'<li><a href="{t["slug"]}.html"><b>{t["title"]}</b></a> - {t["desc"]}</li>' for t in TOOLS)
w("/index.html", page(f"{NAME}｜無料の便利ツール集","登録不要・無料で使える日本語の便利ツール集。","/", f'<h1>{NAME}</h1><p>登録不要・無料。入力内容は送信されません。</p><ul class="l">{lst}</ul>'))
w("/privacy.html", page("プライバシーポリシー","プライバシーポリシー","/privacy.html", f'''<h1>プライバシーポリシー</h1><p>当サイトのツールは入力内容をサーバーに送信せず、ブラウザ内で処理します。</p>
<p>当サイトはGoogle AdSense等の第三者配信の広告サービスを利用する場合があり、広告配信事業者はCookieを使用して利用者の興味に応じた広告を表示します。Cookieを無効にする方法や詳細は各社のポリシーをご確認ください。アクセス解析ツールを導入した場合も同様にCookieを使用しますが、個人を特定する情報は収集しません。</p>'''))
urls.append("/privacy.html")
if SITE: w("/sitemap.xml",'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)+"</urlset>")
w("/robots.txt","User-agent: *\nAllow: /\n"+(f"Sitemap: {SITE}/sitemap.xml\n" if SITE else ""))
if ADS: w("/ads.txt",f"google.com, pub-{ADS.replace('ca-pub-','')}, DIRECT, f08c47fec0942fa0\n")
print(f"生成: {len(urls)}ページ -> {OUT}/")
