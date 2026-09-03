#!/usr/bin/env python3
"""Generate the public, web-facing CV PDF."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "public/assets/cv/hyeonseop_yoon_cv.pdf"
INK = colors.HexColor("#172033")
BLUE = colors.HexColor("#123f73")
MUTED = colors.HexColor("#5b6472")
LINE = colors.HexColor("#cbd3dc")


def register_fonts():
    regular = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    pdfmetrics.registerFont(TTFont("Noto", regular))
    pdfmetrics.registerFont(TTFont("Noto-Bold", bold))


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.line(18 * mm, 13 * mm, 192 * mm, 13 * mm)
    canvas.setFont("Noto", 7.4)
    canvas.setFillColor(MUTED)
    canvas.drawString(18 * mm, 8.5 * mm, "Hyeonseop Yoon · Curriculum Vitae · September 2026")
    canvas.drawRightString(192 * mm, 8.5 * mm, str(doc.page))
    canvas.restoreState()


def make_styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle("Name", parent=base["Title"], fontName="Noto-Bold", fontSize=23,
                               leading=27, textColor=INK, alignment=TA_CENTER, spaceAfter=3),
        "headline": ParagraphStyle("Headline", parent=base["Normal"], fontName="Noto", fontSize=9.5,
                                   leading=13, textColor=BLUE, alignment=TA_CENTER, spaceAfter=3),
        "contact": ParagraphStyle("Contact", parent=base["Normal"], fontName="Noto", fontSize=8,
                                  leading=11, textColor=MUTED, alignment=TA_CENTER, spaceAfter=10),
        "section": ParagraphStyle("Section", parent=base["Heading2"], fontName="Noto-Bold", fontSize=10.5,
                                  leading=14, textColor=BLUE, spaceBefore=9, spaceAfter=5,
                                  borderWidth=0, borderPadding=0),
        "entry": ParagraphStyle("Entry", parent=base["Normal"], fontName="Noto", fontSize=8.25,
                                leading=11.4, textColor=INK, spaceAfter=2),
        "small": ParagraphStyle("Small", parent=base["Normal"], fontName="Noto", fontSize=7.6,
                                leading=10.4, textColor=MUTED, spaceAfter=2),
        "bullet": ParagraphStyle("Bullet", parent=base["Normal"], fontName="Noto", fontSize=7.8,
                                 leading=10.6, textColor=INK, leftIndent=9, firstLineIndent=-5,
                                 bulletIndent=2, spaceAfter=1.5),
    }


def p(text, style):
    return Paragraph(text, style)


def rule():
    table = Table([[""]], colWidths=[174 * mm], rowHeights=[0.4])
    table.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.7, BLUE)]))
    return table


def section(story, title, styles):
    story.extend([p(title.upper(), styles["section"]), rule(), Spacer(1, 2.5)])


def dated_entry(story, date, title, subtitle, styles, detail=None):
    left = p(f"<b>{title}</b><br/><font color='#123f73'>{subtitle}</font>", styles["entry"])
    right = p(date, styles["small"])
    table = Table([[left, right]], colWidths=[139 * mm, 35 * mm])
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    story.append(table)
    if detail:
        story.append(p(detail, styles["small"]))


def bullet(story, text, styles):
    story.append(Paragraph(f"• {text}", styles["bullet"]))


def build():
    register_fonts()
    styles = make_styles()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(OUTPUT), pagesize=A4, rightMargin=18 * mm, leftMargin=18 * mm,
        topMargin=15 * mm, bottomMargin=17 * mm,
        title="Hyeonseop Yoon — Curriculum Vitae", author="Hyeonseop Yoon",
        subject="Applied NLP and AI Research",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=footer)])
    story = [
        p("Hyeonseop Yoon", styles["name"]),
        p("Applied NLP / AI Researcher · Grounded Retrieval, Agent Systems, Evaluation", styles["headline"]),
        p(
            "Seoul, Korea · <link href='mailto:xianxie31@korea.ac.kr'>xianxie31@korea.ac.kr</link> · "
            "<link href='https://pfsv.github.io'>pfsv.github.io</link> · "
            "<link href='https://github.com/PFSV'>GitHub</link> · "
            "<link href='https://orcid.org/0009-0000-0905-4337'>ORCID</link>",
            styles["contact"],
        ),
    ]

    section(story, "Profile", styles)
    story.append(p(
        "AI research engineer building grounded, evidence-driven language systems under production constraints. "
        "Experience spans retrieval and reranking, query expansion, RAG and agent systems, LLM adaptation, "
        "evaluation, and on-premise serving. Earlier research connected NLP representations with human cognition "
        "and neural signals.", styles["entry"]))

    section(story, "Professional Experience", styles)
    dated_entry(story, "Mar 2024 — Present", "MAUM.AI", "AI Research Engineer · AICC R&D", styles)
    bullet(story, "Lead research and engineering across retrieval, RAG, agent orchestration, model adaptation, evaluation, and serving for automotive, insurance, finance, and public-sector systems.", styles)
    bullet(story, "Developed a cascaded reranking and domain-adaptation pipeline that improved documented FAQ accuracy from 69.4% to 96.3% on a client evaluation set.", styles)
    bullet(story, "Built verified-unit QA and staged linguistic seeding for two contact-center domains; the resulting application study was accepted to GroundLM at EMNLP 2026.", styles)
    bullet(story, "Built structure-aware retrieval for constrained policy and technical documents, improving an internal exact-match evaluation from 4/59 to 47/59.", styles)
    bullet(story, "Delivered on-premise LLM and RAG systems, including model fine-tuning, quantization, synthetic-data generation, offline deployment, distributed serving, and observability.", styles)
    dated_entry(story, "Dec 2023 — Feb 2024", "Seoul National University",
                "Researcher · Cognitive & Systems Neuroscience Laboratory", styles)
    bullet(story, "Reviewed and analyzed RNN models of visual working memory, sensory encoding, and decision bias; inspected training dynamics and visualized unit-level information flow.", styles)
    dated_entry(story, "Aug 2022 — Sep 2023", "Korea University",
                "Researcher · Brain Signal Processing Laboratory", styles)
    bullet(story, "Fine-tuned transformer and recurrent language models for reasoning tasks and extracted hidden representations and attention patterns.", styles)
    bullet(story, "Compared model representations with voxel-level fMRI signals using representational similarity analysis and whole-brain mapping.", styles)

    section(story, "Selected Projects", styles)
    dated_entry(story, "2024 — 2026", "Production Grounded AI Systems",
                "MAUM.AI · Automotive, insurance, rail, and public-sector deployments", styles)
    bullet(story, "K-company automotive AICC: domain-specific FAQ retrieval, slot-filling agent, long-term session memory, model compression, and low-latency inference across multiple service locations.", styles)
    bullet(story, "K-company rail service: on-premise voice chatbot and offline regulation-search agents using synthetic corpus generation and grounded retrieval.", styles)
    bullet(story, "K-company insurance systems: document-layout parsing, policy-code mapping agents, knowledge distillation, retrieval over internal regulations, and distributed model serving.", styles)
    dated_entry(story, "2026", "pycag", "Open-source Cache-Augmented Generation toolkit", styles,
                "PyPI package and public source: github.com/PFSV/cag")
    dated_entry(story, "2025 — 2026", "Korean Retrieval Embeddings", "BGE-M3 and Qwen3-based public encoders", styles,
                "Model cards document training scope, AutoRAG evaluation, and limitations.")
    dated_entry(story, "2025", "VisionCardio", "On-device rPPG research prototype", styles,
                "PyTorch training, Core ML export, SwiftUI integration, and deterministic wellness coaching policy.")

    section(story, "Publications", styles)
    story.append(p("<b>[P4] Staged Linguistic Seeding: Grounded Query Expansion for Verified-Unit QA in AI Contact Centers.</b> <b>Hyeonseop Yoon</b>, Jeong-Eun Park. <i>GroundLM Workshop at EMNLP 2026.</i> <link href='https://arxiv.org/abs/2609.00844'>arXiv:2609.00844</link>", styles["entry"]))
    story.append(p("<b>[P3] Metaphor in Mind and Machine.</b> Hyeonseop Yoon et al. <i>OHBM 2024 / Aperture Neuro.</i> <link href='https://doi.org/10.52294/001c.120592'>DOI</link>", styles["entry"]))
    story.append(p("<b>[P2] Comparative Analysis of Brain and NLP Models for Reasoning Tasks.</b> Hyeonseop Yoon et al. <i>Brain Engineering Society of Korea, 2023.</i>", styles["entry"]))
    story.append(p("<b>[P1] Korean Twitter Bot Detection based on Deep Learning.</b> Hyeonseop Yoon et al. <i>Korea Software Congress, KIISE, 2022.</i>", styles["entry"]))

    section(story, "Academic Service", styles)
    dated_entry(story, "2026", "Reviewer", "Grounding Language Models (GroundLM) Workshop at EMNLP", styles)
    dated_entry(story, "2026", "Reviewer", "Vision-Language Models for Real-World Deployment (VLM4RWD) Workshop at NeurIPS", styles)

    section(story, "Selected Honors", styles)
    dated_entry(story, "2023", "Outstanding Poster Award", "Korean Society for Human Brain Mapping", styles,
                "Metaphor in Mind and Machine")
    dated_entry(story, "2023", "Outstanding Poster Award", "Brain Engineering Society of Korea", styles,
                "Comparative Analysis of Brain and NLP Models for Reasoning Tasks")
    dated_entry(story, "2022", "Outstanding Research Award", "Korea Software Congress, KIISE", styles,
                "Korean Twitter Bot Detection based on Deep Learning")
    section(story, "Additional Experience & Skills", styles)
    story.append(p("<b>Open Source Contribution Academy Masters</b> (Aug–Dec 2022) — Developed and maintained VisualPython, a Python-based GUI framework for statistics, machine learning, and deep learning workflows.", styles["entry"]))
    story.append(p("<b>Data Youth Campus</b> (Jul–Sep 2022) — Completed an NLP and deep-learning convergence program; built a Korean spam-detection system.", styles["entry"]))
    story.append(p("<b>Technical:</b> Python, PyTorch, Hugging Face, vLLM, RAG, BM25/SPLADE/dense retrieval, LoRA/ORPO, Docker, PostgreSQL/pgvector, Ray, SLURM/H100, Core ML, SQL, NumPy, pandas, scikit-learn", styles["entry"]))
    story.append(p("<b>Language:</b> Korean (native), English (TEPS 394, Feb 2024; lived in the United Kingdom, 2011–2013)", styles["entry"]))
    story.append(p("<b>Military status:</b> Not completed", styles["entry"]))

    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    build()
