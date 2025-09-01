# Diffusion-based Large Language Models Survey

**Authors:** [Chiung-Yi Tseng](mailto:ctseng@luxmuse.ai)¹, [Danyang Zhang](mailto:danyang@vokram.com)¹, [Junhao Song](mailto:junhao.song23@imperial.ac.uk)²⁺, [Ziqian Bi](mailto:bi32@purdue.edu)³

¹AI Agent Lab, Vokram Group, London, UK  
²Imperial College London, UK  
³Purdue University, USA  
⁺Corresponding Author

## Links

📄 **[Paper](https://www.techrxiv.org/users/952417/articles/1321784-diffusion-based-large-language-models-survey)** | 💻 **[Code](https://github.com/ai-agent-lab/Diffusion-based-Large-Language-Models-Survey)** | 📚 **[Bibliography](#bibliography)**

---

## Abstract

Diffusion-based large language models (DLLMs) have emerged as a promising alternative to traditional autoregressive architectures, notably enhancing parallel generation, controllability, and robustness across multiple modalities. Originally developed from continuous diffusion methods in computer vision, recent adaptations of DLLMs have tailored discrete diffusion processes through absorbing-state kernels, latent projections, and hybrid architectures.

This survey reviews recent developments in DLLMs, beginning with their foundational concepts, including DDPM, DDIM, and their early discrete adaptations, such as mask-based, continuous-embedding, and hybrid models. We organize current methods by sampling strategy, guidance type, noise schedule, and temporal conditioning, and analyzes their efficiency, output quality, and fine-tuning.

The paper also highlights key advancements: autoregressive-diffusion unification through hyperschedules, adaptive correction sampling, and efficient caching mechanisms to enhance computational performance. Besides, it explores emerging applications, such as natural language tasks, multimodal generation, and reasoning-intensive domains. These demonstrate the versatility of DLLMs.

Furthermore, the paper identifies critical challenges, including adaptive sampling, scalable alignment strategies, deeper integration with pretrained language models, graph-based diffusion frameworks, and robust evaluation protocols. Finally, the paper proposes directions that could define future research in diffusion-based sequence generation.

## Key Contributions

- **Comprehensive Taxonomy:** We provide a systematic categorization of diffusion language models based on their architectural choices, training objectives, and sampling strategies.
- **Evolution Analysis:** We trace the development from continuous diffusion models to discrete variants specifically designed for text generation.
- **Performance Evaluation:** We analyze the trade-offs between different approaches in terms of generation quality, computational efficiency, and controllability.
- **Future Directions:** We identify promising research directions including adaptive sampling, scalable alignment, and integration with existing LLMs.
- **Extensive Bibliography:** We compile 65 key papers with verified links to help researchers navigate this rapidly evolving field.

## Survey Structure

### Evolution & Foundations
- Historical Development
- Core Challenges
- Categorization Methods

### Technical Advances
- Interoperability with AR Models
- Knowledge Transfer
- Inference Speed Optimization

### Applications & Future
- Multimodality & Reasoning
- Evaluation Metrics
- Future Research Directions

## Key Figures

![The Diffusion Process in Language Models](Overleaf/figs/diffusion.png)
*Figure 1: The Diffusion Process in Language Models*

![Evolution Timeline of DLLMs](Overleaf/figs/DLLMs_timeline.png)
*Figure 2: Evolution Timeline of DLLMs*

## Bibliography

This survey covers 65 key papers in the field of diffusion-based language models. Click on any paper title to access it directly.

### Evolution of Diffusion Language Models

- [*Deep Unsupervised Learning using Nonequilibrium Thermodynamics*](https://arxiv.org/abs/1503.03585), Sohl-Dickstein et al. ![arXiv 2015](https://img.shields.io/badge/arXiv-2015-red)
- [*Denoising Diffusion Probabilistic Models*](https://arxiv.org/abs/2006.11239), Ho et al. ![arXiv 2020](https://img.shields.io/badge/arXiv-2020-red)
- [*Denoising Diffusion Implicit Models*](https://arxiv.org/abs/2010.02502), Song et al. ![arXiv 2021](https://img.shields.io/badge/arXiv-2021-red)
- [*Diffusion-LM Improves Controllable Text Generation*](https://arxiv.org/abs/2205.14217), Li et al. ![arXiv 2022](https://img.shields.io/badge/arXiv-2022-red)
- [*DiffuSeq: Sequence to Sequence Text Generation with Diffusion Models*](https://arxiv.org/abs/2210.08933), Gong et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*SeqDiffuSeq: Text Diffusion with Encoder-Decoder Transformers*](https://arxiv.org/abs/2112.07804), Yuan et al. ![arXiv 2022](https://img.shields.io/badge/arXiv-2022-red)
- [*Composable Text Controls in Latent Space with ODEs*](https://arxiv.org/abs/2206.09010), Liu et al. ![arXiv 2022](https://img.shields.io/badge/arXiv-2022-red)

### Categorization and Methods

- [*Diffusion models in text generation: a survey*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10909201/), Yi et al. ![NCBI 2024](https://img.shields.io/badge/NCBI-2024-blue)
- [*A Survey of Diffusion Models in Natural Language Processing*](https://arxiv.org/abs/2305.14671), Zou et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*Diffusion Models in NLP: A Survey*](https://arxiv.org/abs/2303.07576), Zhu & Zhao ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*Diffusion Models: A Comprehensive Survey of Methods and Applications*](https://arxiv.org/abs/2209.00796), Yang et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*Simple and Effective Masked Diffusion Language Models*](https://arxiv.org/abs/2406.07524), Sahoo et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*Generalized Interpolating Discrete Diffusion*](http://arxiv.org/abs/2503.04482), Rütte et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*Text Diffusion with Reinforcement Learning*](https://arxiv.org/abs/2310.05793), Wang et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*Cheaper Diffusion*](https://arxiv.org/abs/2304.05729), Chen et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution*](https://arxiv.org/abs/2310.16834), Lou et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)

### Interoperability and Knowledge Transfer

- [*Scaling Diffusion Language Models via Adaptation from Autoregressive Models*](https://arxiv.org/abs/2410.17891), Gong et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*Unifying Autoregressive and Diffusion-Based Sequence Generation*](https://arxiv.org/abs/2504.06416), Fathi et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models*](https://arxiv.org/abs/2503.09573), Arriola et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*AR-Diffusion: Auto-Regressive Diffusion Model for Text Generation*](http://arxiv.org/abs/2305.09515), Wu et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*TEncDM: Understanding the Properties of the Diffusion Model in the Space of Language Model Encodings*](http://arxiv.org/abs/2402.19097), Shabalin et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*Latent Diffusion for Language Generation*](https://arxiv.org/abs/2301.10677), Lovelace et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*Continuous diffusion for mixed-type tabular data*](https://arxiv.org/abs/2305.13269), Jeon et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)

### Collaboration and Inference

- [*David helps Goliath: Inference-Time Collaboration Between Small Specialized and Large General Diffusion LMs*](http://arxiv.org/abs/2305.14771), Han et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*Energy-Based Diffusion Language Models for Text Generation*](https://arxiv.org/abs/2410.21357), Xu et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*SSD-LM: Semi-autoregressive Simplex-based Diffusion Language Model for Text Generation and Modular Control*](http://arxiv.org/abs/2210.17432), Han et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*Mercury: Ultra-Fast Language Models Based on Diffusion*](https://arxiv.org/abs/2506.17298), Khanna et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*Efficient Inference for Large Reasoning Models: A Survey*](https://arxiv.org/abs/2503.23077), Liu et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*Speculative Decoding with Big Little Decoder*](https://arxiv.org/abs/2310.01201), Kim et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion*](https://arxiv.org/abs/2501.11635), Chen et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*Accelerated Sampling for Discrete Diffusion Models*](https://arxiv.org/abs/2402.17177), Bortoli et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)

### Fine-Tuning and Optimization

- [*Using Human Feedback to Fine-tune Diffusion Models without Any Reward Model*](http://arxiv.org/abs/2311.13231), Yang et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*Large Language Diffusion Models*](https://arxiv.org/abs/2502.09992), Nie et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*TESS 2: A Large-Scale Generalist Diffusion Language Model*](https://arxiv.org/abs/2502.13917), Tae et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*Promises, Outlooks and Challenges of Diffusion Language Modeling*](http://arxiv.org/abs/2406.11473), Deschenaux & Gulcehre ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*Exploring the Frontier of Vision-Language Models: A Survey of Current Methodologies and Future Directions*](https://arxiv.org/abs/2310.09720), Ma et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*DiffuTE: Diffusion-based Text Editing with Large Language Models*](https://arxiv.org/abs/2402.01802), Chen et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*Text Diffusion with Encoder-Decoder Transformers*](https://arxiv.org/abs/2310.11685), Lin et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)

### Multimodality and Reasoning

- [*Diffusion of Thoughts: Chain-of-Thought Reasoning in Diffusion Language Models*](https://arxiv.org/abs/2402.07754), Ye et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*d1: Scaling Reasoning in Diffusion Large Language Models via Reinforcement Learning*](https://arxiv.org/abs/2504.12216), Zhao et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*The Best of Both Worlds: Integrating Language Models and Diffusion Models for Video Generation*](https://arxiv.org/abs/2503.04606), Yin et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*Diff-ZSvQA: Zero-Shot Video Question Answering via Diffusion Models*](https://arxiv.org/abs/2404.07499), Xu et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*HybridVLA: Vision-Language Action Model for Robotics*](https://arxiv.org/abs/2402.13916), Liu et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*Are Diffusion Models Really Inferior to Autoregressive Counterparts for Text Generation?*](https://arxiv.org/abs/2405.11365), Krojer et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)

### Applications

- [*ARTIST: Improving the Generation of Text-rich Images with Disentangled Diffusion Models and Large Language Models*](http://arxiv.org/abs/2406.12044), Zhang et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*TextDiffuser: Diffusion Models as Text Painters*](http://arxiv.org/abs/2305.10855), Chen et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*Gemini Diffusion*](https://deepmind.google/models/gemini-diffusion/), Google DeepMind ![DeepMind 2025](https://img.shields.io/badge/DeepMind-2025-blue)
- [*PLANNER: Generating Diversified Paragraph via Latent Language Diffusion Model*](http://arxiv.org/abs/2306.02531), Zhang et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*DPLM-2: A Multimodal Diffusion Protein Language Model*](http://arxiv.org/abs/2410.13782), Wang et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*P3Sum: Summarization with Privacy-Preserving and Personalized Prompts*](https://arxiv.org/abs/2407.18279), Liu et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*Constrained Discrete Diffusion Generation via Mixed-Integer Programming*](https://arxiv.org/abs/2311.04726), Cardei et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*DDPT: Diffusion-based Dual-space Pre-trained Transformers for Image-text Matching*](https://arxiv.org/abs/2501.08503), Li et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*Survey of Hallucination in Natural Language Generation*](https://arxiv.org/abs/2310.04541), Cao et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*Diffusion Language Models Can Perform Many Tasks with Scaling and Instruction-Finetuning*](https://arxiv.org/abs/2306.08257), Meshchaninov et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)

### Foundational Models and Theory

- [*Likelihood-Based Diffusion Language Models*](https://arxiv.org/abs/2305.18619), Gulrajani & Hashimoto ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*Diffusion Models: A Comprehensive Survey of Methods and Applications*](https://arxiv.org/abs/2209.00796), Yang et al. ![arXiv 2022](https://img.shields.io/badge/arXiv-2022-red)
- [*Structured Denoising Diffusion Models in Discrete State-Spaces*](https://arxiv.org/abs/2111.14822), Austin et al. ![arXiv 2021](https://img.shields.io/badge/arXiv-2021-red)
- [*Conditional [MASK] Discrete Diffusion Language Model*](http://arxiv.org/abs/2411.06438), Koh et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*DiffusionBERT: Improving Generative Masked Language Models with Diffusion Models*](https://arxiv.org/abs/2302.13971), He et al. ![arXiv 2023](https://img.shields.io/badge/arXiv-2023-red)
- [*A Continuous Time Framework for Discrete Denoising Models*](https://arxiv.org/abs/2209.06183), Campbell et al. ![arXiv 2022](https://img.shields.io/badge/arXiv-2022-red)
- [*DEEM: Diffusion Models Serve as the Eyes of Large Language Models for Image Perception*](https://arxiv.org/abs/2404.07499), Luo et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*DiffPO: Diffusion Model Policy Optimization*](https://arxiv.org/abs/2402.14184), Chen et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*Amortizing Intractable Inference in Diffusion Models for Vision, Language, and Control*](https://arxiv.org/abs/2501.09236), Venkatraman et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)
- [*Large Concept Models for Structured Prediction*](https://arxiv.org/abs/2410.08707), Cetin et al. ![arXiv 2024](https://img.shields.io/badge/arXiv-2024-red)
- [*Text-Driven Video Generation with Natural Language Processing*](https://arxiv.org/abs/2501.03482), He et al. ![arXiv 2025](https://img.shields.io/badge/arXiv-2025-red)

## BibTeX

```bibtex
@article{tseng2025diffusion,
  title={Diffusion-based Large Language Models Survey},
  author={Tseng, Chiung-Yi and Zhang, Danyang and Song, Junhao and Bi, Ziqian},
  journal={TechRxiv},
  year={2025},
  url={https://www.techrxiv.org/users/952417/articles/1321784-diffusion-based-large-language-models-survey}
}
```

---

*This website is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).*