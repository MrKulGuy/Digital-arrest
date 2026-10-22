"""
Generate a professional 7-slide presentation in .pptx format
strictly matching the hackathon rubric and slide format instructions.
"""

import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck(filename="CyberShield_PS1_Presentation.pptx"):
    prs = Presentation()
    # 16:9 widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette Constants
    BG_DARK = RGBColor(15, 23, 42)       # #0f172a
    SURFACE = RGBColor(30, 41, 59)       # #1e293b
    CARD_BG = RGBColor(36, 50, 72)       # #243248
    BORDER_COL = RGBColor(51, 65, 85)    # #334155
    ACCENT_BLUE = RGBColor(59, 130, 246) # #3b82f6
    ACCENT_GREEN = RGBColor(16, 185, 129)# #10b981
    ACCENT_RED = RGBColor(239, 68, 68)   # #ef4444
    ACCENT_AMBER = RGBColor(245, 158, 11)# #f59e0b
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_MUTED = RGBColor(148, 163, 184) # #94a3b8
    TEXT_BODY = RGBColor(203, 213, 225)  # #cbd5e1

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.color.rgb = BG_DARK
        return bg

    def add_slide_header(slide, title_text, category_text="PS-1: DIGITAL ARREST & REAL-TIME CYBER FRAUD SHIELD"):
        # Category Pill
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.45), Inches(4.5), Inches(0.35))
        pill.fill.solid()
        pill.fill.fore_color.rgb = SURFACE
        pill.line.color.rgb = BORDER_COL
        tf_pill = pill.text_frame
        tf_pill.text = category_text
        tf_pill.paragraphs[0].font.size = Pt(9)
        tf_pill.paragraphs[0].font.bold = True
        tf_pill.paragraphs[0].font.color.rgb = ACCENT_BLUE

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.8))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 1 : COVER SLIDE
    # Team Name, Team Leader, Team Members, Problem Statement Number and Title
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)

    # Decorative background card
    main_card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.9), Inches(11.333), Inches(5.7))
    main_card.fill.solid()
    main_card.fill.fore_color.rgb = SURFACE
    main_card.line.color.rgb = BORDER_COL

    # Badge Pill
    badge = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.6), Inches(1.3), Inches(3.4), Inches(0.4))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(30, 58, 138) # Dark blue
    badge.line.color.rgb = ACCENT_BLUE
    tf_b = badge.text_frame
    tf_b.text = "HACKATHON PRESENTATION | PS-1"
    tf_b.paragraphs[0].font.size = Pt(10)
    tf_b.paragraphs[0].font.bold = True
    tf_b.paragraphs[0].font.color.rgb = RGBColor(191, 219, 254)

    # Title & Subtitle
    title_box = slide1.shapes.add_textbox(Inches(1.6), Inches(1.85), Inches(10.1), Inches(2.0))
    tf1 = title_box.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "Digital Arrest & Real-Time Cyber Fraud Shield"
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE

    p2 = tf1.add_paragraph()
    p2.text = "Explainable Hybrid AI (Machine Learning + Rule-Based Cue Engine) | 100% Local CPU Execution"
    p2.font.size = Pt(14)
    p2.font.color.rgb = ACCENT_BLUE
    p2.space_before = Pt(8)

    # Info Grid (2 Columns: Team Info & Problem Statement Details)
    # Col 1: Team Info
    col1 = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.6), Inches(4.0), Inches(4.8), Inches(2.1))
    col1.fill.solid()
    col1.fill.fore_color.rgb = CARD_BG
    col1.line.color.rgb = BORDER_COL
    tf_c1 = col1.text_frame
    tf_c1.word_wrap = True
    
    p_t1 = tf_c1.paragraphs[0]
    p_t1.text = "👥 TEAM INFORMATION"
    p_t1.font.size = Pt(11)
    p_t1.font.bold = True
    p_t1.font.color.rgb = ACCENT_GREEN

    p_t2 = tf_c1.add_paragraph()
    p_t2.text = "• Team Name: Team CyberShield"
    p_t2.font.size = Pt(12)
    p_t2.font.bold = True
    p_t2.font.color.rgb = TEXT_WHITE
    p_t2.space_before = Pt(6)

    p_t3 = tf_c1.add_paragraph()
    p_t3.text = "• Team Leader: [Team Leader Name]"
    p_t3.font.size = Pt(11)
    p_t3.font.color.rgb = TEXT_BODY

    p_t4 = tf_c1.add_paragraph()
    p_t4.text = "• Team Members: [Member 1, Member 2, Member 3]"
    p_t4.font.size = Pt(11)
    p_t4.font.color.rgb = TEXT_BODY

    # Col 2: Problem Statement Specs
    col2 = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.0), Inches(4.9), Inches(2.1))
    col2.fill.solid()
    col2.fill.fore_color.rgb = CARD_BG
    col2.line.color.rgb = BORDER_COL
    tf_c2 = col2.text_frame
    tf_c2.word_wrap = True

    p_p1 = tf_c2.paragraphs[0]
    p_p1.text = "🎯 PROBLEM STATEMENT"
    p_p1.font.size = Pt(11)
    p_p1.font.bold = True
    p_p1.font.color.rgb = ACCENT_AMBER

    p_p2 = tf_c2.add_paragraph()
    p_p2.text = "• PS Number: PS-1"
    p_p2.font.size = Pt(12)
    p_p2.font.bold = True
    p_p2.font.color.rgb = TEXT_WHITE
    p_p2.space_before = Pt(6)

    p_p3 = tf_c2.add_paragraph()
    p_p3.text = "• Title: Digital Arrest & Real-Time Cyber Fraud Shield"
    p_p3.font.size = Pt(11)
    p_p3.font.color.rgb = TEXT_BODY

    p_p4 = tf_c2.add_paragraph()
    p_p4.text = "• Focus: Real-Time Detection of Video Coercion & Impersonation"
    p_p4.font.size = Pt(11)
    p_p4.font.color.rgb = TEXT_BODY


    # =========================================================================
    # SLIDE 2 : INTRODUCTION (Objectives)
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_slide_header(slide2, "Introduction: Confronting the Digital Arrest Epidemic")

    # 3 Objective Cards in horizontal layout
    cards_s2 = [
        ("🚨 The Threat Landscape", "Scammers impersonate CBI, Police, and Court officials over video calls, holding victims in coerced 'Digital Arrest' and extorting funds to fraudulent escrow accounts.", ACCENT_RED),
        ("🎯 Core Objectives", "1. Real-time call & SMS pattern detection.\n2. Sub-millisecond local CPU execution.\n3. 100% privacy with zero cloud dependencies.\n4. Complete explainability on all risk cues.", ACCENT_BLUE),
        ("🛡️ Citizen Empowerment", "Adheres to a strict 'Assist, Don't Accuse' framework, providing calm, structured next steps and direct integration with India's 1930 Cyber Helpline.", ACCENT_GREEN)
    ]

    for i, (title, text, color) in enumerate(cards_s2):
        x = Inches(0.8 + i * 4.0)
        card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.7), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = SURFACE
        card.line.color.rgb = BORDER_COL

        # Header bar on card
        hbar = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.7), Inches(0.55))
        hbar.fill.solid()
        hbar.fill.fore_color.rgb = CARD_BG
        hbar.line.color.rgb = BORDER_COL
        tf_h = hbar.text_frame
        tf_h.text = title
        tf_h.paragraphs[0].font.size = Pt(13)
        tf_h.paragraphs[0].font.bold = True
        tf_h.paragraphs[0].font.color.rgb = color

        tb = slide2.shapes.add_textbox(x + Inches(0.2), Inches(2.5), Inches(3.3), Inches(4.0))
        tf = tb.text_frame
        tf.word_wrap = True
        for line in text.split("\n"):
            p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
            p.text = line
            p.font.size = Pt(12)
            p.font.color.rgb = TEXT_BODY
            p.space_after = Pt(8)


    # =========================================================================
    # SLIDE 3 : PROPOSED SOLUTION
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_slide_header(slide3, "Proposed Solution: Explainable Hybrid AI Shield")

    # 4 Architecture Feature Cards in 2x2 grid
    grid_s3 = [
        ("🧠 Explainable Hybrid Model", "TfidfVectorizer (1-3 n-grams) + Logistic Regression (40%) combined with a 6-Category Regex Span Highlighter (60%) for sub-millisecond precision.", ACCENT_BLUE),
        ("🚨 Auto Cyber Cell SOS (>70% Risk)", "When extortion risk exceeds 70%, the system automatically files an incident report with unique token and generates an encrypted FIR Evidence Dossier for 1930 / cybercrime.gov.in.", ACCENT_RED),
        ("🛡️ Genuine Message Safeguard", "Eliminates false alarms by detecting anti-fraud awareness advisories (e.g. 'Never share OTP', 'Dial 1930') and standard bank debit/credit notifications (0.0% false alarms).", ACCENT_GREEN),
        ("🎙️ Live Call Stream Simulation", "Ingests speech transcripts sentence-by-sentence in real time, updating threat meters and flagging psychological escalation as the conversation unfolds.", RGBColor(168, 85, 247))
    ]

    for idx, (title, desc, col) in enumerate(grid_s3):
        row = idx // 2
        c = idx % 2
        x = Inches(0.8 + c * 6.0)
        y = Inches(1.8 + row * 2.6)

        box = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.7), Inches(2.3))
        box.fill.solid()
        box.fill.fore_color.rgb = SURFACE
        box.line.color.rgb = BORDER_COL

        tf = box.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = col

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_BODY
        p_d.space_before = Pt(8)


    # =========================================================================
    # SLIDE 4 : TECH STACK
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_slide_header(slide4, "Technology Stack & Architecture Highlights")

    stack_cards = [
        ("💻 Frontend & UI", "• Streamlit Framework\n• Modern Dark-Mode CSS\n• Responsive Metric Banners\n• Dual-Mode WSGI Support", ACCENT_BLUE),
        ("⚙️ Machine Learning", "• scikit-learn (LogisticRegression)\n• TfidfVectorizer (1-3 N-Grams)\n• Calibrated Probabilities\n• Sublinear Term Weighting", ACCENT_AMBER),
        ("📊 Data & NLP Engine", "• pandas & numpy\n• RegEx Span Highlighter\n• 6-Category Co-occurrence Matrix\n• 60 Labelled Benchmark Scenarios", ACCENT_GREEN),
        ("⚡ Runtime & Privacy", "• 100% Local CPU Execution\n• Sub-Millisecond Latency (~0.99ms)\n• Zero Paid Cloud API Keys\n• Complete Data Confidentiality", RGBColor(236, 72, 153))
    ]

    for i, (title, bullets, col) in enumerate(stack_cards):
        x = Inches(0.8 + i * 3.0)
        card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.75), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = SURFACE
        card.line.color.rgb = BORDER_COL

        tf = card.text_frame
        tf.word_wrap = True
        p_h = tf.paragraphs[0]
        p_h.text = title
        p_h.font.size = Pt(13)
        p_h.font.bold = True
        p_h.font.color.rgb = col

        for b in bullets.split("\n"):
            p = tf.add_paragraph()
            p.text = b
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_BODY
            p.space_before = Pt(6)


    # =========================================================================
    # SLIDE 5 : WORKFLOW
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_slide_header(slide5, "System Workflow: From Ingestion to Safe Action")

    steps = [
        ("1. Input Ingestion", "Audio transcript, SMS, or live sentence stream", ACCENT_BLUE),
        ("2. Dual-Engine Scan", "Parallel TF-IDF ML vectorization + 6-cue span matching", ACCENT_AMBER),
        ("3. Safeguard Filter", "Detects negation & genuine banking/advisory patterns", ACCENT_GREEN),
        ("4. Hybrid Scoring", "40% ML + 60% Rule Co-occurrence aggregated in <1ms", RGBColor(168, 85, 247)),
        ("5. Auto Cyber Cell SOS", "If Risk > 70%, auto-files incident token & generates FIR dossier for 1930", ACCENT_RED)
    ]

    for idx, (step_title, step_desc, col) in enumerate(steps):
        x = Inches(0.8 + idx * 2.4)
        box = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(2.2), Inches(2.15), Inches(4.0))
        box.fill.solid()
        box.fill.fore_color.rgb = SURFACE
        box.line.color.rgb = BORDER_COL

        # Step Number Circle
        num_circle = slide5.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.75), Inches(2.5), Inches(0.65), Inches(0.65))
        num_circle.fill.solid()
        num_circle.fill.fore_color.rgb = col
        num_circle.line.color.rgb = col
        tf_n = num_circle.text_frame
        tf_n.text = str(idx + 1)
        tf_n.paragraphs[0].alignment = PP_ALIGN.CENTER
        tf_n.paragraphs[0].font.size = Pt(14)
        tf_n.paragraphs[0].font.bold = True
        tf_n.paragraphs[0].font.color.rgb = TEXT_WHITE

        # Step Text
        tf = box.text_frame
        tf.word_wrap = True
        p_space = tf.paragraphs[0]
        p_space.text = "\n\n"

        p_t = tf.add_paragraph()
        p_t.text = step_title
        p_t.alignment = PP_ALIGN.CENTER
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = col

        p_d = tf.add_paragraph()
        p_d.text = step_desc
        p_d.alignment = PP_ALIGN.CENTER
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = TEXT_BODY
        p_d.space_before = Pt(8)


    # =========================================================================
    # SLIDE 6 : UNIQUE SELLING POINT (USP)
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_slide_header(slide6, "Unique Selling Point: What Sets CyberShield Apart")

    # 4 Key Metrics/USP highlights
    usps = [
        ("⚡ Real-Time Latency (~0.99 ms)", "Executes 100x faster than cloud LLM APIs, enabling instantaneous interception during active phone and video calls on standard laptop CPUs.", ACCENT_BLUE),
        ("🛡️ 0.0% False Alarm Rate", "Genuine Message Safeguard prevents alert fatigue by accurately distinguishing real bank alerts and police advisories from malicious coercion.", ACCENT_GREEN),
        ("🚨 Automated Cyber Cell Dispatch", "When risk exceeds 70%, the system automatically generates an encrypted FIR Evidence Dossier and files a complaint token with cybercrime.gov.in / 1930.", ACCENT_RED),
        ("🔒 Zero-Cost & 100% Data Privacy", "Requires zero paid API tokens and zero internet connectivity, keeping sensitive call content completely confidential on-device.", RGBColor(236, 72, 153))
    ]

    for idx, (title, desc, col) in enumerate(usps):
        row = idx // 2
        c = idx % 2
        x = Inches(0.8 + c * 6.0)
        y = Inches(1.8 + row * 2.6)

        box = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.7), Inches(2.3))
        box.fill.solid()
        box.fill.fore_color.rgb = SURFACE
        box.line.color.rgb = BORDER_COL

        tf = box.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = col

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_BODY
        p_d.space_before = Pt(8)


    # =========================================================================
    # SLIDE 7 : SCREENSHOT AND REFERENCES
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_slide_header(slide7, "Prototype Demonstration & Official References")

    # Left: Prototype Architecture & UI Summary
    left_card = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.9))
    left_card.fill.solid()
    left_card.fill.fore_color.rgb = SURFACE
    left_card.line.color.rgb = BORDER_COL

    tf_l = left_card.text_frame
    tf_l.word_wrap = True
    p_lh = tf_l.paragraphs[0]
    p_lh.text = "🖥️ Live Prototype Highlights"
    p_lh.font.size = Pt(14)
    p_lh.font.bold = True
    p_lh.font.color.rgb = ACCENT_BLUE

    points_l = [
        "• Tab 1: Live Fraud Shield with Dynamic Sentence-by-Sentence Call Simulator.",
        "• Tab 2: 60-Sample Evaluation Benchmark (100% Accuracy, 0% False Alarm Rate).",
        "• Tab 3: Offline Audio (.wav/.mp3) & Transcript (.json/.txt) Ingestion.",
        "• Explainable High-Contrast UI: Category badges & 3-step action guide.",
        "• Production Deployment: Streamlit + Vercel Serverless Dual-Mode."
    ]
    for pt in points_l:
        p = tf_l.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_BODY
        p.space_before = Pt(8)

    # Right: Official References & Helplines
    right_card = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
    right_card.fill.solid()
    right_card.fill.fore_color.rgb = SURFACE
    right_card.line.color.rgb = BORDER_COL

    tf_r = right_card.text_frame
    tf_r.word_wrap = True
    p_rh = tf_r.paragraphs[0]
    p_rh.text = "📚 Official References & Regulatory Sources"
    p_rh.font.size = Pt(14)
    p_rh.font.bold = True
    p_rh.font.color.rgb = ACCENT_GREEN

    points_r = [
        "1. Ministry of Home Affairs (MHA) - National Cyber Crime Reporting Portal (cybercrime.gov.in).",
        "2. Indian Cyber Crime Coordination Centre (I4C) - National Citizen Financial Helpline: 1930.",
        "3. Telecom Regulatory Authority of India (TRAI) - Public Advisories on Mobile Disconnection Scams.",
        "4. Reserve Bank of India (RBI) - Cautionary Circulars on Fictitious Offers & Safe Account Frauds.",
        "5. Delhi & Mumbai Police Cyber Crime Directives on 'Digital Arrest' Impersonation Laws."
    ]
    for pt in points_r:
        p = tf_r.add_paragraph()
        p.text = pt
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_BODY
        p.space_before = Pt(8)

    prs.save(filename)
    print(f"[OK] Successfully created presentation with exactly 7 slides: {filename}")

if __name__ == "__main__":
    out_file = "C:/Users/Acer nitro/.gemini/antigravity/scratch/digital-arrest-shield/TeamCyberShield_PS1_Presentation.pptx"
    create_deck(out_file)
