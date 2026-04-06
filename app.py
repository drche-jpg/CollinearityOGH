import streamlit as st
import streamlit.components.v1 as components

# ตั้งค่าหน้าเว็บ / Set page configuration
st.set_page_config(layout="wide", page_title="Collinearity Proof: O, G, H")

# ซ่อนเมนูและ Footer ของ Streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Interactive Proof: การร่วมเส้นตรงเดียวกันของจุด O, G และ H (Collinearity of O, G, H)")

# --- JSXGraph Engine Integration (Bilingual & Larger Labels) ---
html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;600;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <script type="text/javascript" charset="UTF-8" src="https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraphcore.js"></script>
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraph.css" />
    <style>
        body { font-family: 'Prompt', 'Inter', sans-serif; display: flex; flex-direction: column; align-items: center; margin: 0; background-color: #fcfcfc; padding-bottom: 20px;}
        
        /* Information Panel */
        .info-container { width: 100%; max-width: 1000px; background: #f0f7ff; border-left: 5px solid #0d6efd; padding: 20px; margin: 10px 0 20px 0; border-radius: 8px; color: #333; font-size: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);}
        .info-container h3 { margin: 0 0 10px 0; color: #0056b3; font-size: 18px; border-bottom: 1px solid #cce3ff; padding-bottom: 8px;}
        .info-container p { margin: 8px 0; line-height: 1.6;}
        .en-text { color: #475569; font-size: 0.9em; display: block; margin-top: 4px; font-family: 'Inter', sans-serif;}
        
        /* Controls Panel */
        .controls-container { display: flex; flex-direction: column; gap: 15px; width: 100%; max-width: 1000px; padding: 20px; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 2px 8px rgba(0,0,0,0.05); margin-bottom: 15px;}
        .btn-group { display: flex; gap: 10px; flex-wrap: wrap; }
        button { font-family: 'Prompt', 'Inter', sans-serif; padding: 10px 20px; cursor: pointer; border: none; border-radius: 8px; background: #e9ecef; font-weight: 600; font-size: 14.5px; color: #495057; transition: all 0.2s; }
        button:hover { background: #dee2e6; transform: translateY(-1px); }
        .active-btn { background: #34495e; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.15); }
        .active-btn:hover { background: #2c3e50; }
        
        #explanation { margin-top: 10px; padding: 15px; background: #f8fafc; border-left: 4px solid #3b82f6; border-radius: 6px; min-height: 80px; font-size: 15px; line-height: 1.6; color: #334155;}

        /* Metrics Panel */
        .metrics-container { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 15px; width: 100%; max-width: 1000px; margin-bottom: 20px; padding: 15px 20px; background: #f8fafc; border-radius: 12px; border: 1px solid #cbd5e1; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);}
        .metric-col { display: flex; flex-direction: column; gap: 6px; font-size: 14px; font-family: 'Courier New', monospace; color: #334155; flex: 1; min-width: 200px;}
        .metric-title { font-family: 'Prompt', 'Inter', sans-serif; font-weight: 600; font-size: 15px; border-bottom: 1px solid #94a3b8; padding-bottom: 4px; margin-bottom: 6px; color: #0f172a;}
        .val { font-weight: bold; color: #0284c7; }
        .ratio-val { font-weight: bold; color: #d63384; font-size: 15px;}

        /* JSXGraph Container */
        .graph-wrapper { position: relative; width: 100%; max-width: 1000px; height: 600px; border-radius: 12px; border: 1px solid #e2e8f0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.05); background-color: white;}
        #box { width: 100%; height: 100%; background-color: transparent !important;}
        
        .copyright { margin-top: 15px; text-align: center; font-size: 13px; color: #94a3b8;}
    </style>
</head>
<body>

    <div class="info-container">
        <h3>📚 แนวคิดการพิสูจน์ (Proof Concept)</h3>
        <p>แทนที่จะ "สร้าง" จุด H บนเส้นตรงออยเลอร์ บทพิสูจน์นี้จะเริ่มจาก <strong>จุดออร์โทเซนเตอร์ (H)</strong> และ <strong>จุดเซอร์คัมเซนเตอร์ (O)</strong> ที่แท้จริง จากนั้นลากเส้นเชื่อมทั้งสองจุด แล้วพิสูจน์ว่าเส้นตรงนี้จะตัดกับเส้นมัธยฐานด้วยอัตราส่วน <strong>2:1</strong> เสมอ ซึ่งเป็นคุณสมบัติของ <strong>จุดเซนทรอยด์ (G)</strong> พอดี!</p>
        <span class="en-text">Instead of constructing point H on the Euler line, this proof starts with the true <strong>Orthocenter (H)</strong> and <strong>Circumcenter (O)</strong>, connects them, and proves that this segment intersects the median at a perfect <strong>2:1</strong> ratio—the defining property of the <strong>Centroid (G)</strong>.</span>
        
        <p style="font-size: 13.5px; color: #64748b; border-top: 1px dashed #cbd5e1; padding-top: 8px; margin-top: 12px;">
            * <strong>Tip:</strong> คุณสามารถใช้ลูกกลิ้งเมาส์เพื่อ Zoom หรือลากพื้นหลังเพื่อ Pan กราฟได้ (Use mouse wheel to Zoom, drag background to Pan).
        </p>
    </div>

    <div class="controls-container">
        <div class="btn-group">
            <button id="btn1" onclick="setStep(1)">1: สร้างจุด (Setup) O & H</button>
            <button id="btn2" onclick="setStep(2)">2: เส้นขนาน (Parallel) AH || OM</button>
            <button id="btn3" onclick="setStep(3)">3: จุดตัด (Intersection) X</button>
            <button id="btn4" onclick="setStep(4)">4: เซนทรอยด์ (Centroid Check)</button>
        </div>
        <div id="explanation"></div>
    </div>

    <div class="metrics-container">
        <div class="metric-col">
            <div class="metric-title">1. ระยะทางเส้นขนาน<br><span style="font-size: 13px; color: #475569;">(Parallel Distances)</span></div>
            <span>AH (Altitude): <span id="val-ah" class="val">0.00</span></span>
            <span>OM (Bisector): <span id="val-om" class="val">0.00</span></span>
            <span style="margin-top:4px;">Ratio <span class="ratio-val">AH / OM = <span id="val-ah-om">0.00</span></span></span>
        </div>
        <div class="metric-col">
            <div class="metric-title">2. จุดตัดเส้นมัธยฐาน<br><span style="font-size: 13px; color: #475569;">(Median Intersection)</span></div>
            <span>AX (Vertex to X): <span id="val-ax" class="val">0.00</span></span>
            <span>XM (X to Midpoint): <span id="val-xm" class="val">0.00</span></span>
            <span style="margin-top:4px;">Ratio <span class="ratio-val">AX / XM = <span id="val-ax-xm">0.00</span></span></span>
        </div>
        <div class="metric-col">
            <div class="metric-title">3. ตรวจสอบเส้นออยเลอร์<br><span style="font-size: 13px; color: #475569;">(Euler Line Check)</span></div>
            <span>HX (H to X): <span id="val-hx" class="val">0.00</span></span>
            <span>XO (X to O): <span id="val-xo" class="val">0.00</span></span>
            <span style="margin-top:4px;">Ratio <span class="ratio-val">HX / XO = <span id="val-hx-xo">0.00</span></span></span>
        </div>
    </div>

    <div class="graph-wrapper">
        <div id="box" class="jxgbox"></div>
    </div>

    <div class="copyright">
        &copy; 2026 Dr.Che @ Math Mission Thailand. All rights reserved.
    </div>

    <script>
        // --- 1. Init Board ---
        var board = JXG.JSXGraph.initBoard('box', {
            boundingbox: [-2, 12, 12, -2], 
            axis: false, 
            showCopyright: false, 
            keepaspectratio: true,
            zoom: {wheel: true, needshift: false},
            pan: {enabled: true, needshift: false}
        });

        // Watermark
        board.create('text', [5, 5, 
            "<div style='transform: rotate(-20deg); color: rgba(148, 163, 184, 0.15); font-size: 3.5rem; font-family: Prompt; font-weight: 700; pointer-events: none; user-select: none; white-space: nowrap;'>Dr.Che@Math Mission Thailand</div>"
        ], {anchorX: 'middle', anchorY: 'middle', fixed: true, highlight: false, layer: 0});

        // --- 2. Base Triangle (เพิ่มขนาดและทำตัวหนาให้กับ Label) ---
        var labelStyle = {fontSize: 22, bold: true, strokeColor: '#1e293b'};
        
        var A = board.create('point', [3, 10], {name:'A', size:5, color:'#34495e', label: labelStyle});
        var B = board.create('point', [1, 2], {name:'B', size:5, color:'#34495e', label: labelStyle});
        var C = board.create('point', [9, 2], {name:'C', size:5, color:'#34495e', label: labelStyle});
        var polyABC = board.create('polygon', [A, B, C], {borders:{strokeWidth:2.5, strokeColor:'#34495e'}, fillColor:'transparent'});

        var lineAB = board.create('line', [A, B], {visible:false});
        var lineBC = board.create('line', [B, C], {visible:false});
        var lineAC = board.create('line', [A, C], {visible:false});

        // --- 3. Points: O, H, G(X) (เพิ่มขนาดและทำตัวหนา) ---
        var cc = board.create('circumcircle', [A, B, C], {visible:false});
        var O = board.create('point', [function(){return cc.center.X();}, function(){return cc.center.Y();}], 
            {name:'O', color:'#007bff', size:5, label: {fontSize: 22, bold: true, strokeColor: '#007bff'}});
        
        var altC = board.create('perpendicular', [lineAB, C], {visible:false});
        var altA = board.create('perpendicular', [lineBC, A], {visible:false});
        var H = board.create('intersection', [altC, altA], 
            {name:'H', color:'#dc3545', size:5, label: {fontSize: 22, bold: true, strokeColor: '#dc3545'}});

        var G = board.create('point', [
            function(){ return (A.X() + B.X() + C.X()) / 3; },
            function(){ return (A.Y() + B.Y() + C.Y()) / 3; }
        ], {name:'G', color:'#28a745', size:5, label: {fontSize: 22, bold: true, strokeColor: '#28a745'}});

        // --- 4. Visual Elements for Steps ---
        var M = board.create('midpoint', [B, C], 
            {name:'M', color:'#7f8c8d', size:4, visible:false, label: {fontSize: 20, bold: true, strokeColor: '#7f8c8d'}});
        var mAC = board.create('midpoint', [A, C], {name:'', visible:false});
        
        var bisectBC = board.create('perpendicular', [lineBC, M], {strokeColor:'#007bff', dash:2, strokeWidth:1.5, visible:false});
        var bisectAC = board.create('perpendicular', [lineAC, mAC], {strokeColor:'#007bff', dash:2, strokeWidth:1.5, visible:false});
        var visualAltA = board.create('segment', [A, board.create('intersection',[altA, lineBC],{visible:false})], {strokeColor:'#dc3545', dash:2, strokeWidth:1.5, visible:false});
        var visualAltC = board.create('segment', [C, board.create('intersection',[altC, lineAB],{visible:false})], {strokeColor:'#dc3545', dash:2, strokeWidth:1.5, visible:false});

        var segAH = board.create('segment', [A, H], {strokeColor:'#dc3545', strokeWidth:3, visible:false});
        var segOM = board.create('segment', [O, M], {strokeColor:'#007bff', strokeWidth:3, visible:false});

        var lineHO = board.create('segment', [H, O], {strokeColor:'#9b59b6', strokeWidth:2.5, visible:false});
        var medAM = board.create('segment', [A, M], {strokeColor:'#28a745', dash:1, strokeWidth:2.5, visible:false});

        var triAHX = board.create('polygon', [A, H, G], {fillColor:'#dc3545', fillOpacity:0.15, borders:{strokeColor:'#dc3545', dash:2, strokeWidth:2}, visible:false});
        var triMOX = board.create('polygon', [M, O, G], {fillColor:'#007bff', fillOpacity:0.15, borders:{strokeColor:'#007bff', dash:2, strokeWidth:2}, visible:false});

        // --- 5. Step Logic (Bilingual) ---
        function setStep(step) {
            for(let i=1; i<=4; i++) {
                document.getElementById('btn'+i).className = (i === step) ? 'active-btn' : '';
            }
            let exp = document.getElementById('explanation');
            
            // Reset Visibilities
            M.setAttribute({visible: false}); bisectBC.setAttribute({visible: false}); bisectAC.setAttribute({visible: false});
            visualAltA.setAttribute({visible: false}); visualAltC.setAttribute({visible: false});
            segAH.setAttribute({visible: false}); segOM.setAttribute({visible: false});
            lineHO.setAttribute({visible: false}); medAM.setAttribute({visible: false});
            triAHX.setAttribute({visible: false}); triMOX.setAttribute({visible: false});
            
            if(step === 1) {
                exp.innerHTML = "<strong>ขั้นที่ 1:</strong> เริ่มต้นด้วยการหา <strong>Orthocenter (H)</strong> จากจุดตัดของส่วนสูง (สีแดง) และ <strong>Circumcenter (O)</strong> จากจุดตัดของเส้นแบ่งครึ่งตั้งฉาก (สีน้ำเงิน)<br><span class='en-text'><strong>Step 1:</strong> Start by finding the <strong>Orthocenter (H)</strong> from the intersection of the altitudes (red) and the <strong>Circumcenter (O)</strong> from the perpendicular bisectors (blue).</span>";
                bisectBC.setAttribute({visible: true}); bisectAC.setAttribute({visible: true});
                visualAltA.setAttribute({visible: true}); visualAltC.setAttribute({visible: true});
                G.setAttribute({visible: false});
            }
            if(step === 2) {
                exp.innerHTML = "<strong>ขั้นที่ 2:</strong> ให้ <strong>M</strong> เป็นจุดกึ่งกลาง BC เนื่องจากส่วนสูง AH และเส้นแบ่งครึ่ง OM ตั้งฉากกับฐาน BC ทั้งคู่ ดังนั้นส่วนของเส้นตรง <strong>AH จึงขนานกับ OM (AH || OM)</strong><br><span class='en-text'><strong>Step 2:</strong> Let <strong>M</strong> be the midpoint of BC. Since both the altitude AH and bisector OM are perpendicular to the base BC, the segments are parallel <strong>(AH || OM)</strong>.</span>";
                M.setAttribute({visible: true}); segAH.setAttribute({visible: true}); segOM.setAttribute({visible: true});
                G.setAttribute({visible: false});
            }
            if(step === 3) {
                exp.innerHTML = "<strong>ขั้นที่ 3:</strong> ลากเส้นมัธยฐาน AM และเส้นตรงเชื่อมจุด H กับ O ให้จุดตัดของเส้นทั้งสองชื่อว่า <strong>จุด X</strong><br><span class='en-text'><strong>Step 3:</strong> Draw the median AM and the line connecting H to O. Let their point of intersection be called <strong>Point X</strong>.</span>";
                M.setAttribute({visible: true}); segAH.setAttribute({visible: true}); segOM.setAttribute({visible: true});
                lineHO.setAttribute({visible: true}); medAM.setAttribute({visible: true});
                G.setAttribute({name: 'X', visible: true}); 
            }
            if(step === 4) {
                exp.innerHTML = "<strong>ขั้นที่ 4:</strong> เนื่องจาก AH || OM ทำให้ ΔAHX ∼ ΔMOX เราทราบว่าระยะ AH เป็น 2 เท่าของ OM (ดูสัดส่วนด้านล่าง) อัตราส่วนด้านคล้ายจึงเป็น 2:1 ส่งผลให้ AX = 2*XM เนื่องจาก <strong>X</strong> แบ่งเส้นมัธยฐาน 2:1 <strong>จุด X จึงต้องเป็นจุดเซนทรอยด์ (G)!</strong><br><span class='en-text'><strong>Step 4:</strong> Because AH || OM, ΔAHX ∼ ΔMOX. The length AH is twice OM (see ratio below), so the similarity ratio is 2:1. Thus, AX = 2*XM. Since <strong>X</strong> divides the median 2:1, <strong>Point X must be the Centroid (G)!</strong></span>";
                M.setAttribute({visible: true}); lineHO.setAttribute({visible: true}); medAM.setAttribute({visible: true});
                triAHX.setAttribute({visible: true}); triMOX.setAttribute({visible: true});
                G.setAttribute({name: 'G', visible: true}); 
            }
            board.update();
        }

        // --- 6. Real-time Metrics Update ---
        board.on('update', function() {
            let dAH = A.Dist(H);
            let dOM = O.Dist(M);
            document.getElementById('val-ah').innerText = dAH.toFixed(2);
            document.getElementById('val-om').innerText = dOM.toFixed(2);
            document.getElementById('val-ah-om').innerText = (dOM > 0.001) ? (dAH / dOM).toFixed(2) : "0.00";

            let dAX = A.Dist(G);
            let dXM = G.Dist(M);
            document.getElementById('val-ax').innerText = dAX.toFixed(2);
            document.getElementById('val-xm').innerText = dXM.toFixed(2);
            document.getElementById('val-ax-xm').innerText = (dXM > 0.001) ? (dAX / dXM).toFixed(2) : "0.00";

            let dHX = H.Dist(G);
            let dXO = G.Dist(O);
            document.getElementById('val-hx').innerText = dHX.toFixed(2);
            document.getElementById('val-xo').innerText = dXO.toFixed(2);
            document.getElementById('val-hx-xo').innerText = (dXO > 0.001) ? (dHX / dXO).toFixed(2) : "0.00";
        });

        // เริ่มต้นที่ Step 1
        setStep(1);
    </script>
</body>
</html>
"""

# เพิ่ม height ขึ้นเล็กน้อยเพื่อรองรับข้อความภาษาอังกฤษที่เพิ่มขึ้นมา
components.html(html_code, height=1350, scrolling=True)
