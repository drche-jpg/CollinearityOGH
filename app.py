import streamlit as st
import streamlit.components.v1 as components

# ตั้งค่าหน้าเว็บ / Set page configuration
st.set_page_config(layout="wide", page_title="Euler Line & 9-Point Circle")

# ซ่อนเมนูและ Footer ของ Streamlit เพื่อความเรียบร้อย
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Interactive Demonstration: Centroid, Orthocenter, Euler Line & 9-Point Circle")

# --- JSXGraph Engine Integration ---
html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;600&family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <script type="text/javascript" charset="UTF-8" src="https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraphcore.js"></script>
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraph.css" />
    <style>
        body { font-family: 'Prompt', 'Inter', sans-serif; display: flex; flex-direction: column; align-items: center; margin: 0; background-color: #fcfcfc; padding-bottom: 20px;}
        
        /* Information Panel */
        .info-container { width: 100%; max-width: 1000px; background: #f0f7ff; border-left: 5px solid #0d6efd; padding: 20px; margin: 10px 0 20px 0; border-radius: 8px; color: #333; font-size: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);}
        .info-container h3 { margin: 0 0 10px 0; color: #0056b3; font-size: 18px; border-bottom: 1px solid #cce3ff; padding-bottom: 8px;}
        .info-container p { margin: 8px 0; line-height: 1.6;}
        .info-container ul { margin: 10px 0; padding-left: 20px;}
        .info-container li { margin-bottom: 10px; line-height: 1.5;}
        .en-text { color: #666; font-size: 13.5px; display: block; margin-top: 2px;}
        .highlight { color: #d63384; font-weight: 600; }

        /* Controls Panel */
        .controls-container { display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 15px; justify-content: space-between; width: 100%; max-width: 1000px; padding: 20px; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 2px 8px rgba(0,0,0,0.05);}
        .control-group { display: flex; flex-direction: column; gap: 10px; min-width: 200px;}
        .control-group h4 { margin: 0 0 5px 0; font-size: 15px; color: #1e293b; border-bottom: 2px solid #f1f5f9; padding-bottom: 5px;}
        .label { cursor: pointer; user-select: none; font-size: 14px; color: #475569; display: flex; align-items: center; gap: 8px;}
        input[type="checkbox"] { transform: scale(1.2); cursor: pointer; accent-color: #0d6efd;}

        /* Metrics Panel */
        .metrics-container { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 15px; width: 100%; max-width: 1000px; margin-bottom: 20px; padding: 15px 20px; background: #f8fafc; border-radius: 12px; border: 1px solid #cbd5e1; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);}
        .metric-col { display: flex; flex-direction: column; gap: 6px; font-size: 14px; font-family: 'Courier New', monospace; color: #334155;}
        .metric-title { font-family: 'Prompt', sans-serif; font-weight: 600; font-size: 15px; border-bottom: 1px solid #94a3b8; padding-bottom: 4px; margin-bottom: 4px; color: #0f172a;}
        .val { font-weight: bold; color: #0284c7; }

        /* JSXGraph Container */
        .graph-wrapper { position: relative; width: 100%; max-width: 1000px; height: 600px; border-radius: 12px; border: 1px solid #e2e8f0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.05); background-color: white;}
        #box { width: 100%; height: 100%; background-color: transparent !important;}
        
        .copyright { margin-top: 15px; text-align: center; font-size: 13px; color: #94a3b8;}
    </style>
</head>
<body>

    <div class="info-container">
        <h3>📚 คำนิยาม & คุณสมบัติ (Definitions & Properties)</h3>
        <ul>
            <li><strong>จุดศูนย์กลางวงกลมเก้าจุด (Nine-Point Center - N):</strong> 
                จุดกึ่งกลางของเส้นตรงที่เชื่อมระหว่าง Orthocenter (H) และ Circumcenter (O) โดยมีระยะห่าง <span class="highlight">HN = NO</span> เสมอ
                <span class="en-text">The midpoint of the segment connecting H and O.</span>
            </li>
            <li><strong>เส้นออยเลอร์ (Euler Line):</strong> 
                เส้นตรงที่ลากผ่านจุด O, G, และ H มีความสัมพันธ์คือ <span class="highlight">HG = 2GO</span> และจุด N จะอยู่บนเส้นนี้พอดี
                <span class="en-text">The line passing through O, G, H, and N.</span>
            </li>
            <li><strong>รัศมีวงกลมเก้าจุด (Radius Rn):</strong> 
                มีขนาดเป็น <strong>ครึ่งหนึ่ง</strong> ของรัศมีวงกลมล้อมรอบ (R) เสมอ (<span class="highlight">Rn = R / 2</span>)
                <span class="en-text">The nine-point radius is always exactly half of the circumradius.</span>
            </li>
        </ul>
        <p style="font-size: 13px; color: #64748b; border-top: 1px dashed #cbd5e1; padding-top: 8px; margin-top: 10px;">
            * <strong>Tip:</strong> คุณสามารถใช้ลูกกลิ้งเมาส์เพื่อ Zoom เข้า-ออก หรือลากพื้นหลังเพื่อ Pan กราฟได้
        </p>
    </div>

    <div class="controls-container">
        <div class="control-group">
            <h4>1. เส้น (Lines)</h4>
            <label class="label"><input type="checkbox" id="showAlt" onchange="toggleVis()"> เส้นส่วนสูง (Altitudes)</label>
            <label class="label"><input type="checkbox" id="showMed" onchange="toggleVis()"> เส้นมัธยฐาน (Medians)</label>
            <label class="label"><input type="checkbox" id="showEuler" checked onchange="toggleVis()"> <strong style="color: #f59e0b;">เส้นออยเลอร์ (Euler Line)</strong></label>
        </div>
        <div class="control-group">
            <h4>2. วงกลมหลัก (Main Points)</h4>
            <label class="label"><input type="checkbox" id="showH" checked onchange="toggleVis()"> จุด H (Orthocenter)</label>
            <label class="label"><input type="checkbox" id="showG" checked onchange="toggleVis()"> จุด G (Centroid)</label>
            <label class="label"><input type="checkbox" id="showCircum" checked onchange="toggleVis()"> <span style="color: #3b82f6;">วงกลมล้อมรอบ (Circumcircle)</span></label>
            <label class="label"><input type="checkbox" id="showNineCirc" checked onchange="toggleVis()"> <strong style="color: #9333ea;">วงกลมเก้าจุด (9-Point Circle)</strong></label>
        </div>
        <div class="control-group">
            <h4>3. องค์ประกอบ 9 จุด (The 9 Points)</h4>
            <label class="label"><input type="checkbox" id="showMid" checked onchange="toggleVis()"> กึ่งกลางด้าน (M)</label>
            <label class="label"><input type="checkbox" id="showFeet" checked onchange="toggleVis()"> โคนเส้นส่วนสูง (F)</label>
            <label class="label"><input type="checkbox" id="showEulerPts" checked onchange="toggleVis()"> จุดออยเลอร์ (E)</label>
        </div>
    </div>

    <div class="metrics-container">
        <div class="metric-col">
            <div class="metric-title">Euler Line Distances</div>
            <span>HG: <span id="val-hg" class="val">0.00</span></span>
            <span>HN: <span id="val-hn" class="val">0.00</span></span>
            <span>NO: <span id="val-no" class="val">0.00</span></span>
            <span>GO: <span id="val-go" class="val">0.00</span></span>
        </div>
        <div class="metric-col">
            <div class="metric-title">Radii Check</div>
            <span>R (Circum): <span id="val-r" class="val">0.00</span></span>
            <span>Rn (9-Point): <span id="val-rn" class="val">0.00</span></span>
            <span style="color:#d63384; font-weight:bold; margin-top:5px;">R / Rn = <span id="val-ratio">0.00</span></span>
        </div>
        <div class="metric-col">
            <div class="metric-title">Mathematical Proof</div>
            <span>HN = NO (N is midpoint)</span>
            <span>HG = 2 × GO</span>
            <span>R = 2 × Rn</span>
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

        // Watermark (ฝังในกราฟ)
        board.create('text', [5, 5, 
            "<div style='transform: rotate(-20deg); color: rgba(148, 163, 184, 0.15); font-size: 3rem; font-family: Prompt; font-weight: 700; pointer-events: none; user-select: none; white-space: nowrap;'>Dr.Che@Math Mission Thailand</div>"
        ], {anchorX: 'middle', anchorY: 'middle', fixed: true, highlight: false, layer: 0});

        // --- 2. Base Triangle ---
        var A = board.create('point', [4, 9], {name:'A', size:5, color:'#1e293b'});
        var B = board.create('point', [1, 2], {name:'B', size:5, color:'#1e293b'});
        var C = board.create('point', [9, 2], {name:'C', size:5, color:'#1e293b'});
        var poly = board.create('polygon', [A, B, C], {borders:{strokeWidth:2.5, strokeColor:'#475569'}, fillColor:'transparent'});

        var lineBC = board.create('line', [B, C], {visible:false});
        var lineAC = board.create('line', [A, C], {visible:false});
        var lineAB = board.create('line', [A, B], {visible:false});

        // --- 3. Circumcircle & O ---
        var circumcircle = board.create('circumcircle', [A, B, C], {strokeColor:'#3b82f6', dash:2, strokeWidth:1.5});
        var O = board.create('point', [function(){return circumcircle.center.X();}, function(){return circumcircle.center.Y();}], {name:'O', color:'#3b82f6', size:4});

        // --- 4. Altitudes & H ---
        var altA = board.create('perpendicular', [lineBC, A], {strokeColor:'rgba(239, 68, 68, 0.4)', dash:1});
        var altB = board.create('perpendicular', [lineAC, B], {strokeColor:'rgba(239, 68, 68, 0.4)', dash:1});
        var altC = board.create('perpendicular', [lineAB, C], {strokeColor:'rgba(239, 68, 68, 0.4)', dash:1});
        var H = board.create('intersection', [altA, altB], {name:'H', color:'#ef4444', size:4});

        // --- 5. Medians & G ---
        var M_A = board.create('midpoint', [B, C], {name:'M_a', color:'#22c55e', size:3});
        var M_B = board.create('midpoint', [A, C], {name:'M_b', color:'#22c55e', size:3});
        var M_C = board.create('midpoint', [A, B], {name:'M_c', color:'#22c55e', size:3});
        var medA = board.create('segment', [A, M_A], {strokeColor:'rgba(34, 197, 94, 0.4)'});
        var medB = board.create('segment', [B, M_B], {strokeColor:'rgba(34, 197, 94, 0.4)'});
        var medC = board.create('segment', [C, M_C], {strokeColor:'rgba(34, 197, 94, 0.4)'});
        var G = board.create('intersection', [medA, medB], {name:'G', color:'#22c55e', size:4});

        // --- 6. The 9-Point Circle & Center N ---
        var N = board.create('midpoint', [O, H], {name:'N', color:'#9333ea', size:4});
        var nineCircle = board.create('circle', [N, M_A], {strokeColor:'#9333ea', strokeWidth:2, fillColor:'rgba(147, 51, 234, 0.05)'});

        // The Rest of the 9 Points
        var F_A = board.create('intersection', [altA, lineBC], {name:'F_a', color:'#f97316', size:3});
        var F_B = board.create('intersection', [altB, lineAC], {name:'F_b', color:'#f97316', size:3});
        var F_C = board.create('intersection', [altC, lineAB], {name:'F_c', color:'#f97316', size:3});
        var E_A = board.create('midpoint', [A, H], {name:'E_a', color:'#06b6d4', size:3});
        var E_B = board.create('midpoint', [B, H], {name:'E_b', color:'#06b6d4', size:3});
        var E_C = board.create('midpoint', [C, H], {name:'E_c', color:'#06b6d4', size:3});

        // --- 7. Euler Line ---
        var eulerLine = board.create('line', [O, H], {strokeColor:'#f59e0b', strokeWidth:2, dash:2});

        // --- Logic & UI Binding ---
        function toggleVis() {
            var sAlt = document.getElementById('showAlt').checked;
            altA.setAttribute({visible: sAlt}); altB.setAttribute({visible: sAlt}); altC.setAttribute({visible: sAlt});
            
            var sMed = document.getElementById('showMed').checked;
            medA.setAttribute({visible: sMed}); medB.setAttribute({visible: sMed}); medC.setAttribute({visible: sMed});
            
            eulerLine.setAttribute({visible: document.getElementById('showEuler').checked});
            H.setAttribute({visible: document.getElementById('showH').checked});
            G.setAttribute({visible: document.getElementById('showG').checked});
            circumcircle.setAttribute({visible: document.getElementById('showCircum').checked});
            O.setAttribute({visible: document.getElementById('showCircum').checked});
            
            var sNine = document.getElementById('showNineCirc').checked;
            nineCircle.setAttribute({visible: sNine}); N.setAttribute({visible: sNine});

            var sMid = document.getElementById('showMid').checked;
            M_A.setAttribute({visible: sMid}); M_B.setAttribute({visible: sMid}); M_C.setAttribute({visible: sMid});
            
            var sFeet = document.getElementById('showFeet').checked;
            F_A.setAttribute({visible: sFeet}); F_B.setAttribute({visible: sFeet}); F_C.setAttribute({visible: sFeet});
            
            var sEulerPts = document.getElementById('showEulerPts').checked;
            E_A.setAttribute({visible: sEulerPts}); E_B.setAttribute({visible: sEulerPts}); E_C.setAttribute({visible: sEulerPts});
        }

        // Real-time Metrics Update
        board.on('update', function() {
            document.getElementById('val-hg').innerText = H.Dist(G).toFixed(2);
            document.getElementById('val-go').innerText = G.Dist(O).toFixed(2);
            document.getElementById('val-hn').innerText = H.Dist(N).toFixed(2);
            document.getElementById('val-no').innerText = N.Dist(O).toFixed(2);
            
            var radC = circumcircle.Radius();
            var radN = nineCircle.Radius();
            document.getElementById('val-r').innerText = radC.toFixed(2);
            document.getElementById('val-rn').innerText = radN.toFixed(2);
            document.getElementById('val-ratio').innerText = (radC / radN).toFixed(2);
        });

        // Init visibility
        toggleVis();
    </script>
</body>
</html>
"""

components.html(html_code, height=1250, scrolling=True)
