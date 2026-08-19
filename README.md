# introduction-to-ai
Repository for the course "Introduction to Artificial Intelligence" at IMT Atlantique. It contains the slides of all courses.

Lab sessions are on [this page](https://mee-labs.gitlab-pages.imt-atlantique.fr/intro2ai/).

## Communication

The communication for the course happens on **Discord**! The link will be provided during the first class.

Each binôme has its **own dedicated Discord channel** (see [Teams](#teams-binômes) below). Announcements, questions, and project validation all go through Discord.

## Course outline

The course alternates lessons and lab sessions, with the **main project running throughout** (see [Main Project](#what-is-expected-for-the-main-project)). From Session 3 onward, each lab applies its techniques to your own project data.

| Session | Date | Content |
| :--- | :--- | :--- |
| **1** | Sep 25 | Course 1 — Generalities; Lab 1 (Python, venv, numpy, data manipulation); project-definition |
| **2** | Oct 2 | **Project validation** presentations |
| **3** | Oct 9 | Course and Lab 2 — Supervised Learning |
| **4** | Oct 16 | Course and Lab 3 — Unsupervised Learning |
| **5** | Oct 23 | Course and Lab 4 — Deep Learning; project milestone  |
| — | — | **Holiday break** |
| **Exam** | Nov 6 | Written exam on courses 1–4 (Generalities, Supervised, Unsupervised, Deep Learning) |
| **6** | Nov 6 | Course and Lab 5 — Foundation Models |
| **7** | Nov 13 | Course 6 — Adaptation |
| **8** | Nov 13 | Debate on societal impacts of AI |
| **9** | Nov 20, 27, Dec 4 | Project-dedicated sessions |
| **10** | Dec 11 | **Final presentations** |

## Teams (binômes)

The project is carried out in **binômes** (pairs). Binômes are split into **4 groups of at most 7 teams each**. Your group is the audience for your presentations (validation and final), and project topics must be unique within a group.

If a group has an odd number of students, **trinômes** (three students) and **monômes** (a single student) are accepted, within the same limit of **7 teams per group**.

**On Discord:** each binôme has its **own dedicated channel**. As soon as your binôme is formed, chose a channel (numbered), and write **the full names of both members** in that channel.

## Code setup and environment

You will need a working **Python** environment throughout the class. Across the labs we will use **numpy**, then **scikit-learn** (supervised / unsupervised learning), **PyTorch** (deep learning), and **Hugging Face** (foundation models).

**No prior setup is required**, but we expect that you know how to handle a virtual environment. We will have a setup session for the virtual environments (`venv`) and data manipulation in Lab 1.

**Compute:**
- You can run everything on **Google Colab** using your **own individual account** (note that we do not have institutional Colab access, so use your personal token.)
- We also have **local machines** available for running code. If you want access, **ask a teacher**.

## Tools and AI assistants

- You may use **any AI tool** introduced in class (e.g. UMAP / t-SNE / PCA for visualization, neural networks, foundation models, etc.).
- You may use **any AI assistant** to help you (e.g. ChatGPT, Claude, ...).
- The evaluation **emphasizes comprehension**, not the raw performance of your solution, so be pedagogical, and don't focus only on results.

## Evaluation in this course

- **Short quiz on Wooclap** at the start of each lesson session (first ~10 minutes), on the previous lesson. Don't be late, or you won't be able to access the quiz!
- **Project validation presentation** (Session 2): a **10-minute presentation**, including questions, covering your project, and in particular the chosen task, data, metrics, and existing methods. You attend the other presentations in your group and are encouraged to ask questions. **If your project is not validated, you will have to take a re-take, with a penalty on your grade.**
- **Exam** (individual), covering the content of **courses 1 to 4** (Generalities, Supervised Learning, Unsupervised Learning, Deep Learning). The exam is on paper and you won't have the right to use your laptop (or any electronic device). You are authorized to prepare two **manuscript** A4 pages (recto and verso).
- **Final presentation:** a **15-minute presentation**, questions included.

**Attendance:** you are expected to attend all sessions. The quizzes run in the first ~10 minutes of each lesson session, so arriving on time matters.

## What is expected for the Main Project

Short version: **Exploration of different AI approaches to your own project.**

Long version: this course is built around the main project, and **you choose it in the very first session**. You have a lot of freedom, which we expect you to use. The overarching goal is to explore different strategies of AI, motivate them, and conclude about their performance.

From the third session onward, every lab applies its techniques to your project data. The work you do in the labs may therefore builds your final project deliverable.

We encourage students to get creative and test combinations of the various ideas that we present. We will value the quality of the explanation, not the quantitative performance!

**Reserve your topic early:** as soon as you have an idea, post a **one-line project title** in your binôme's Discord channel — **well before Session 2** — so a teacher can validate it. This early check makes sure that **no two binômes in the same group work on the same topic** (titles are reserved on a first-come basis within a group).

See `main_project.pdf` for the full project brief, criteria, and timeline.

## Competences

This course is evaluated by competence, and each competence is assessed using three levels: **"–"** (in progress), **"="** (mastered, expected level), and **"+"** (expert / beyond expectations). The module is validated when **at least 3 of the 4 competences reach at least the "=" level**, except for the BC03 that leads to automatic re-take if not validated.

The competences instantiated for this course are:

| Competence | Statement |
| :--- | :--- |
| **BC03** | Diagnose an AI problem: identify the relevant task, data and metrics, and situate the main paradigms of modern machine learning (supervised and unsupervised learning, deep learning, foundation models, adaptation) and their limitations. |
| **BC04** | Design and develop an original solution, based on modern AI methods, to a technical problem chosen by the binôme (either imagined by the students or proposed by the teaching team), taking into account the constraints of the task and the data. |
| **BC07** | Implement and rigorously compare several AI methods for a given task, and justify the technical choices through a reproducible experimental approach (protocol, metrics, hyperparameters). |
| **BC02** | Contribute to a collective and take a reflective view on AI: present and discuss an AI approach clearly and pedagogically, listen to and question the work of the other binômes, collaborate effectively within the binôme, and critically assess AI methods with respect to TES issues. |

### How competences are evaluated

Each competence is assessed through one or more summative situations (that sets the level), and is informed by formative situations (which give feedback without penalty). When a competence is demonstrated several times, it is evaluated based on all demonstrations. 

| Competence | Formative | Summative (sets the level) |
| :--- | :--- | :--- |
| **BC03** | Wooclap quizzes | **Exam** (paradigms, courses 1–4) + **validation presentation** (diagnostic part: task, data, metrics, existing methods) |
| **BC04** | Lab milestones applied to the project | **Final project presentation** (originality, relevance of the strategy) |
| **BC07** | Labs (toy examples + project) | **Final project presentation** (implementation, comparison, reproducibility of experiments) |
| **BC02** | Questions asked in session; the debate | **Validation presentation** + **final project presentation** (clarity, pedagogy, listening), including a **reflective part**: critique of the approach with respect to TES issues |

A competence not validated in a summative situation may be subject to a **re-take**; in particular, a project not validated in Session 2 (BC03) leads to a re-take with a penalty on the final grade ('-' by default, '=' if the final presentation make up for the validation, and impossible to reach '+').

## Contact

- Teachers: Axel MARMORET, Nicolas FARRUGIA, Bastien PASDELOUP, Kaiteng JIANG, Joseph JABOUR
- Course communication: **Discord**
- mails (if needed): name.surname@imt-atlantique.fr
