export const profile = {
  name: 'Hyeonseop Yoon',
  hangul: '윤현섭',
  role: 'Applied NLP / AI Researcher',
  location: 'Seoul, Korea',
  email: 'xianxie31@korea.ac.kr',
  github: 'https://github.com/PFSV',
  portfolio: 'https://github.com/PFSV/portfolio',
  huggingFace: 'https://huggingface.co/hyunseop',
  orcid: 'https://orcid.org/0009-0000-0905-4337',
  cv: '/assets/cv/hyeonseop_yoon_cv.pdf',
  statement:
    'I build grounded, evidence-driven language systems that connect retrieval research with production constraints.',
} as const;

export const nav = [
  { label: 'Home', href: '/' },
  { label: 'Publications', href: '/#publications' },
  { label: 'Experience', href: '/#experience' },
  { label: 'Work', href: '/work/' },
  { label: 'CV', href: profile.cv },
] as const;

export type EvidenceLevel = 'Runnable code' | 'Public model + evaluation' | 'Case study';

export type Project = {
  slug: string;
  title: string;
  summary: string;
  contribution: string;
  result: string;
  evidence: EvidenceLevel;
  links: { label: string; href: string }[];
  command?: string;
  note: string;
  tags: string[];
};

export const projects: Project[] = [
  {
    slug: 'grounded-qa',
    title: 'Grounded QA for enterprise contact centers',
    summary:
      'A verified-unit QA design that returns an operator-approved answer or abstains instead of generating unsupported policy text.',
    contribution:
      'Designed the architecture and retrieval/evaluation harness; found question-identity leakage in an early setup and rebuilt the held-out evaluation.',
    result:
      'The documented held-out evaluation reports hybrid retrieval with query augmentation at approximately R@1 0.881–0.930.',
    evidence: 'Case study',
    links: [
      {
        label: 'Paper (arXiv)',
        href: 'https://arxiv.org/abs/2609.00844',
      },
      {
        label: 'Method and limitations',
        href: 'https://github.com/PFSV/portfolio/blob/main/projects/grounded-qa-contact-center.md',
      },
    ],
    note:
      'Accepted to the GroundLM Workshop at EMNLP 2026. Production code and raw evaluation data remain private, so this is not presented as an open-source reproduction.',
    tags: ['grounding', 'retrieval', 'evaluation', 'abstention'],
  },
  {
    slug: 'retrieval-embeddings',
    title: 'Korean retrieval embeddings',
    summary:
      'Two public Korean retrieval encoders with model cards and documented AutoRAG evaluation.',
    contribution:
      'Fine-tuned and evaluated BGE-M3- and Qwen3-based encoders, then recorded when the fine-tuned checkpoint did not generalize well enough to use.',
    result:
      'On the documented 720-item, 114-query AutoRAG evaluation, the BGE-M3 variant reports MRR 0.7773 and Hit@10 0.9474.',
    evidence: 'Public model + evaluation',
    links: [
      {
        label: 'BGE-M3 model card',
        href: 'https://huggingface.co/hyunseop/rtfin-bge-m3-ko-h100',
      },
      {
        label: 'Qwen3 model card',
        href: 'https://huggingface.co/hyunseop/rtfin-qwen3-embedding-h100',
      },
      {
        label: 'Evaluation context',
        href: 'https://github.com/PFSV/portfolio/blob/main/projects/korean-retrieval-embeddings.md',
      },
    ],
    note:
      'Enterprise corpora and training data are not redistributed. Reported values apply only to the documented evaluation.',
    tags: ['embeddings', 'Korean NLP', 'AutoRAG', 'Hugging Face'],
  },
  {
    slug: 'vision-cardio',
    title: 'VisionCardio',
    summary:
      'An on-device rPPG research prototype spanning model training, Core ML export, and a SwiftUI application.',
    contribution:
      'Built the data/training pipeline, model export, application integration, and bounded coaching policy.',
    result:
      'With a strict participant split, the documented UBFC validation heart-rate MAE improved from 5.63 to 2.80 bpm after fine-tuning.',
    evidence: 'Runnable code',
    links: [
      { label: 'Source', href: 'https://github.com/PFSV/vision-cardio' },
      { label: 'Model', href: 'https://huggingface.co/hyunseop/vision-cardio-rppg' },
    ],
    command:
      'git clone https://github.com/PFSV/vision-cardio.git\ncd vision-cardio\nbash scripts/demo_exercise_coach_policy.sh',
    note:
      'The smoke demo exercises the deterministic coaching policy without private datasets or GPU access. Heart-rate estimation is a wellness research prototype, not a medical device.',
    tags: ['rPPG', 'PyTorch', 'Core ML', 'SwiftUI'],
  },
  {
    slug: 'pycag',
    title: 'pycag',
    summary:
      'An alpha Cache-Augmented Generation toolkit for bounded corpora and Llama-family models.',
    contribution:
      'Packaged corpus consolidation, reusable KV-cache prefill, and single/batch query CLIs while documenting where CAG is a poor fit.',
    result: 'Published as pycag 0.1.0 with CI and a deterministic corpus-building smoke path.',
    evidence: 'Runnable code',
    links: [
      { label: 'Source', href: 'https://github.com/PFSV/cag' },
      { label: 'PyPI', href: 'https://pypi.org/project/pycag/' },
    ],
    command:
      'git clone https://github.com/PFSV/cag.git\ncd cag\npython3 -m unittest discover -s tests -v\npython3 scripts/01_build_corpus.py --output /tmp/pycag-corpus.txt',
    note:
      'The smoke path needs only the repository sample. Building a KV cache additionally requires a compatible model and suitable memory.',
    tags: ['CAG', 'LLM', 'Python', 'Hugging Face'],
  },
];

export const publications = [
  {
    year: '2026',
    title: 'Staged Linguistic Seeding: Grounded Query Expansion for Verified-Unit QA in AI Contact Centers',
    venue: 'GroundLM Workshop at EMNLP 2026',
    href: 'https://arxiv.org/abs/2609.00844',
  },
  {
    year: '2024',
    title: 'Metaphor in Mind and Machine',
    venue: 'OHBM 2024 / Aperture Neuro',
    href: 'https://doi.org/10.52294/001c.120592',
  },
  {
    year: '2023',
    title: 'Comparative Analysis of Brain and NLP Models for Reasoning Tasks',
    venue: 'Brain Engineering Society of Korea',
    href: 'https://github.com/PFSV/portfolio/blob/main/projects/brain-and-language-research.md',
  },
  {
    year: '2022',
    title: 'Korean Twitter Bot Detection based on Deep Learning',
    venue: 'Korea Software Congress / KIISE',
    href: 'https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11224455',
  },
] as const;

export const service = [
  {
    year: '2026',
    role: 'Reviewer',
    venue: 'Grounding Language Models (GroundLM) Workshop at EMNLP 2026',
  },
  {
    year: '2026',
    role: 'Reviewer',
    venue: 'Vision-Language Models for Real-World Deployment (VLM4RWD) Workshop at NeurIPS 2026',
  },
] as const;

export const experience = [
  {
    period: 'Mar 2024 — Present',
    organization: 'MAUM.AI',
    role: 'AI Research Engineer · AICC R&D',
    description:
      'Research and engineering for production language systems across automotive, insurance, finance, and public-sector domains: retrieval, agent systems, model adaptation, evaluation, and serving.',
  },
  {
    period: 'Dec 2023 — Feb 2024',
    organization: 'Seoul National University',
    role: 'Researcher · Cognitive & Systems Neuroscience Laboratory',
    description:
      'Analyzed recurrent neural-network models of working memory, sensory encoding, and decision bias; reviewed training dynamics and visualized information flow between units.',
  },
  {
    period: 'Aug 2022 — Sep 2023',
    organization: 'Korea University',
    role: 'Researcher · Brain Signal Processing Laboratory',
    description:
      'Compared human fMRI representations with language-model embeddings using representational similarity analysis across reasoning and conceptual-metaphor tasks.',
  },
] as const;

export const honors = [
  {
    year: '2023',
    title: 'Outstanding Poster Award',
    issuer: 'Korean Society for Human Brain Mapping',
    detail: 'Metaphor in Mind and Machine',
  },
  {
    year: '2023',
    title: 'Outstanding Poster Award',
    issuer: 'Brain Engineering Society of Korea',
    detail: 'Comparative Analysis of Brain and NLP Models for Reasoning Tasks',
  },
  {
    year: '2022',
    title: 'Outstanding Research Award',
    issuer: 'Korea Software Congress, KIISE',
    detail: 'Korean Twitter Bot Detection based on Deep Learning',
  },
] as const;

export const capabilities = [
  'retrieval and reranking evaluation',
  'grounded QA and abstention design',
  'embedding fine-tuning and model cards',
  'LLM adaptation and serving',
  'PyTorch, Hugging Face, vLLM',
  'Docker, Postgres/pgvector, SLURM/H100',
] as const;
