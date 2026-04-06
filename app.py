import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Euler Line: Collinearity Proof", layout="wide")
st.title("Advanced Proof: Collinearity of O, G, and H")
st.markdown("Instead of constructing $H$ on the Euler line, this proof takes the true Orthocenter ($H$) and Circumcenter ($O$) and proves that the segment connecting them passes exactly through the Centroid ($G$). Drag the vertices to explore.")

# --- JSXGraph HTML/JS Engine ---
html_code = """
<!DOCTYPE html>
<html>
<head>
    <script type="text/javascript" charset="UTF-8" src="https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraphcore.js"></script>
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraph.css" />
    <style>
        body { font-family: sans-serif; color: #333; margin: 0; padding: 10px; }
        .controls-container { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 15px; flex-wrap: wrap; gap: 20px;}
        .btn-group { display: flex; gap: 10px; flex-wrap: wrap; }
        button { padding: 8px 16px; cursor: pointer; border: 1px solid #ccc; border-radius: 4px; background: #f8f9fa; font-weight: bold;}
        button:hover { background: #e2e6ea; }
        .active-btn { background: #333; color: white; border-color: #333; }
        .active-btn:hover { background: #000; }
        
        .toggles { display: flex; flex-direction: column; gap: 8px; background: #f4f4f4; padding: 10px; border-radius: 8px; border: 1px solid #ddd; min-width: 200px;}
        .toggle-row { display: flex; align-items: center; gap: 8px; font-weight: bold; font-size: 14px;}
        
        #explanation { margin-top: 15px; padding: 15px; background: #f8f9fa; border-left: 4px solid #333; border-radius: 4px; min-height: 80px; font-size: 15px; line-height: 1.5;}
    </style>
</head>
<body>

    <div class="controls-container">
        <div class="btn-group">
            <button id="btn1" class="active-btn" onclick="setStep(1)">1: Setup (O & H)</button>
            <button id="btn2" onclick="setStep(2)">2: Parallel Segments</button>
            <button id="btn3" onclick="setStep(3)">3: Intersection</button>
            <button id="btn4" onclick="setStep(4)">4: Similarity & Centroid</button>
        </div>
        
        <div class="toggles">
            <div class="toggle-row">
                <input type="checkbox" id="chkO" onchange="manualToggle()">
                <span style="color: blue;">Show Circumcenter (O)</span>
            </div>
            <div class="toggle-row">
                <input type="checkbox" id="chkG" onchange="manualToggle()">
                <span style="color: green;">Show Centroid (G)</span>
            </div>
            <div class="toggle-row">
                <input type="checkbox" id="chkH" onchange="manualToggle()">
                <span style="color: red;">Show Orthocenter (H)</span>
            </div>
        </div>
    </div>

    <div id="box" class="jxgbox" style="width:100%; height:550px; border-radius: 8px; border: 1px solid #ddd;"></div>
    
    <div id="explanation"></div>

    <script>
        // --- 1. Initialize Board ---
        var board = JXG.JSXGraph.initBoard('box', {boundingbox: [-2, 12, 12, -2], axis:false, showCopyright:false, keepaspectratio:true});
        
        // --- 2. Base Geometry ---
        var A = board.create('point', [3, 10], {name:'A', size:4, color:'#333'});
        var B = board.create('point', [1, 2], {name:'B', size:4, color:'#333'});
        var C = board.create('point', [9, 2], {name:'C', size:4, color:'#333'});
        var polyABC = board.create('polygon', [A, B, C], {borders:{strokeWidth:2, strokeColor:'#333'}, fillColor:'transparent'});

        // --- 3. Mathematical Points ---
        
        // Circumcenter (O)
        var cc = board.create('circumcircle', [A, B, C], {visible:false});
        var O = board.create('point', [function(){return cc.center.X();}, function(){return cc.center.Y();}], {name:'O', color:'blue', size:5});
        
        // Orthocenter (H) - Created via intersecting altitudes
        var lineAB = board.create('line', [A, B], {visible:false});
        var lineBC = board.create('line', [B, C], {visible:false});
        var altC = board.create('perpendicular', [lineAB, C], {visible:false});
        var altA = board.create('perpendicular', [lineBC, A], {visible:false});
        var H = board.create('intersection', [altC, altA], {name:'H', color:'red', size:5});

        // Centroid (G)
        var G = board.create('point', [
            function(){ return (A.X() + B.X() + C.X()) / 3; },
            function(){ return (A.Y() + B.Y() + C.Y()) / 3; }
        ], {name:'G', color:'green', size:5});

        // --- 4. Step Specific Visuals ---
        
        // Step 1: Altitudes and Bisectors
        var mBC = board.create('midpoint', [B, C], {name:'M', color:'gray', size:3, visible:false});
        var mAC = board.create('midpoint', [A, C], {name:'', visible:false});
        var bisectBC = board.create('perpendicular', [lineBC, mBC], {strokeColor:'blue', dash:2, strokeWidth:1, visible:false});
        var bisectAC = board.create('perpendicular', [board.create('line',[A,C],{visible:false}), mAC], {strokeColor:'blue', dash:2, strokeWidth:1, visible:false});
        var visualAltA = board.create('segment', [A, board.create('intersection',[altA, lineBC],{visible:false})], {strokeColor:'red', dash:2, strokeWidth:1, visible:false});
        var visualAltC = board.create('segment', [C, board.create('intersection',[altC, lineAB],{visible:false})], {strokeColor:'red', dash:2, strokeWidth:1, visible:false});

        // Step 2: Parallel Segments
        var segAH = board.create('segment', [A, H], {strokeColor:'red', strokeWidth:2, visible:false});
        var segOM = board.create('segment', [O, mBC], {strokeColor:'blue', strokeWidth:2, visible:false});

        // Step 3: Intersection 
        var lineHO = board.create('segment', [H, O], {strokeColor:'purple', strokeWidth:2, visible:false});
        var medAM = board.create('segment', [A, mBC], {strokeColor:'green', dash:1, strokeWidth:2, visible:false});

        // Step 4: Similarity Polygons
        var triAHX = board.create('polygon', [A, H, G], {fillColor:'red', fillOpacity:0.15, borders:{strokeColor:'red', dash:2}, visible:false});
        var triMOX = board.create('polygon', [mBC, O, G], {fillColor:'blue', fillOpacity:0.15, borders:{strokeColor:'blue', dash:2}, visible:false});

        // --- 5. Logic & Visibility Management ---

        function manualToggle() {
            O.setAttribute({visible: document.getElementById('chkO').checked});
            G.setAttribute({visible: document.getElementById('chkG').checked});
            H.setAttribute({visible: document.getElementById('chkH').checked});
        }

        function setStep(step) {
            // UI Button styling
            for(let i=1; i<=4; i++) {
                document.getElementById('btn'+i).className = (i === step) ? 'active-btn' : '';
            }

            let exp = document.getElementById('explanation');
            
            // Step 1: Setup
            if(step === 1) {
                exp.innerHTML = "<strong>Step 1: The True Points.</strong> We start by plotting the true Orthocenter <strong>H</strong> (intersection of the red altitudes) and the true Circumcenter <strong>O</strong> (intersection of the blue perpendicular bisectors).";
                
                document.getElementById('chkO').checked = true;
                document.getElementById('chkG').checked = false;
                document.getElementById('chkH').checked = true;

                mBC.setAttribute({visible: false});
                bisectBC.setAttribute({visible: true}); bisectAC.setAttribute({visible: true});
                visualAltA.setAttribute({visible: true}); visualAltC.setAttribute({visible: true});
                segAH.setAttribute({visible: false}); segOM.setAttribute({visible: false});
                lineHO.setAttribute({visible: false}); medAM.setAttribute({visible: false});
                triAHX.setAttribute({visible: false}); triMOX.setAttribute({visible: false});
                
                G.setAttribute({name: 'G'}); // Reset name just in case
            }
            
            // Step 2: Parallel
            if(step === 2) {
                exp.innerHTML = "<strong>Step 2: Parallel Segments.</strong> Let <strong>M</strong> be the midpoint of BC. Since the altitude from A is perpendicular to BC, and the bisector from O is also perpendicular to BC, the segment <strong>AH is parallel to OM</strong>. A known property is that AH = 2*OM.";
                
                document.getElementById('chkO').checked = true;
                document.getElementById('chkG').checked = false;
                document.getElementById('chkH').checked = true;

                mBC.setAttribute({visible: true});
                bisectBC.setAttribute({visible: false}); bisectAC.setAttribute({visible: false});
                visualAltA.setAttribute({visible: false}); visualAltC.setAttribute({visible: false});
                segAH.setAttribute({visible: true}); segOM.setAttribute({visible: true});
                lineHO.setAttribute({visible: false}); medAM.setAttribute({visible: false});
                triAHX.setAttribute({visible: false}); triMOX.setAttribute({visible: false});
            }

            // Step 3: Intersection
            if(step === 3) {
                exp.innerHTML = "<strong>Step 3: Intersection X.</strong> We draw the median AM and connect H to O. Let the point where they intersect be called <strong>Point X</strong>.";
                
                document.getElementById('chkO').checked = true;
                document.getElementById('chkG').checked = true;
                document.getElementById('chkH').checked = true;

                G.setAttribute({name: 'X'}); // Temporarily call it X

                mBC.setAttribute({visible: true});
                segAH.setAttribute({visible: true}); segOM.setAttribute({visible: true});
                lineHO.setAttribute({visible: true}); medAM.setAttribute({visible: true});
                triAHX.setAttribute({visible: false}); triMOX.setAttribute({visible: false});
            }

            // Step 4: Similarity
            if(step === 4) {
                exp.innerHTML = "<strong>Step 4: Centroid Confirmation.</strong> Because AH || OM, alternate interior angles are equal, making ΔAHX ∼ ΔMOX (AA Similarity). Since AH = 2*OM, the ratio of sides is 2:1. Therefore, AX = 2*XM. Because <strong>X</strong> divides the median AM in a 2:1 ratio, <strong>Point X must be the Centroid (G)</strong>! This proves O, G, and H are perfectly collinear.";
                
                document.getElementById('chkO').checked = true;
                document.getElementById('chkG').checked = true;
                document.getElementById('chkH').checked = true;

                G.setAttribute({name: 'G'}); // Rename back to G

                mBC.setAttribute({visible: true});
                segAH.setAttribute({visible: false}); segOM.setAttribute({visible: false}); // Hide to focus on triangles
                lineHO.setAttribute({visible: true}); medAM.setAttribute({visible: true});
                triAHX.setAttribute({visible: true}); triMOX.setAttribute({visible: true});
            }

            // Apply toggle states to points
            manualToggle();
        }

        // Initialize at Step 1
        setStep(1);
    </script>
</body>
</html>
"""

# Render the HTML component in Streamlit
components.html(html_code, height=750)