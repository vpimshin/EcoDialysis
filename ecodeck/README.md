To regenerate the deck after edits:

 cd /home/victor/projects/EcoDialysis/ecodeck && python3 build.py
 # then PDF:
 cd /home/victor/projects/EcoDialysis && \
   google-chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
     --print-to-pdf=EcoDialysis_Final_Pitch_EN.pdf \
     file://$PWD/EcoDialysis_Final_Pitch_EN.html

The slide editing API in content_en.py / content_fr.py is:

 add(sid, kind, title, body_html, notes)
 # kind ∈ {"cover","divider","content","appendix"}
 # C("per","s26",...) → renders clickable source chips that jump to Appendix I anchors
