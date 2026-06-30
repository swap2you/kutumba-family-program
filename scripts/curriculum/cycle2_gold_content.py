"""Module-specific gold-standard content for Cycle 2 deepening pass."""

from __future__ import annotations

MODULES: dict[str, dict] = {
    "c2-w1-action-and-reaction-how-karma-binds": {
        "code": "C2-W1",
        "title": "Action and Reaction: How Karma Binds",
        "key_verse": "Bhagavad-gītā 3.9",
        "key_verse_url": "https://vedabase.io/en/library/bg/3/9/",
        "memory_line": "Work done only for separate material interest causes bondage; work done for Viṣṇu should be performed without selfish attachment.",
        "essential_question": "How do intention, method, and consequence shape bondage, and how can work be offered to Kṛṣṇa?",
        "controlling_principle": "Karma is action and reaction under material nature; yajña-centered work purifies motive.",
        "scope": "BG 3.9, 3.13, 4.16–18; King Nṛga summary; intention–method–consequence analysis",
        "exclusions": "Full karma taxonomy; diagnosing others' suffering; fatalism; victim-blaming",
        "prerequisites": "C1-W2 body/self distinction helpful",
        "leads_to": "C2-W2 free will; C2-W3 reincarnation",
        "hook": (
            "A parent sends a hurried message in anger. The message takes ten seconds to send, "
            "but the reaction continues for days. Trust is damaged, explanations multiply, and the "
            "original issue becomes harder to solve. Another parent patiently repairs a child's "
            "school project. The child feels supported, yet the parent secretly expects praise and "
            "becomes resentful when none comes. Actions are not isolated dots. They carry intention, "
            "method, and consequence."
        ),
        "katha_title": "King Citraketu's lesson on karma",
        "katha_primary": "Śrīmad-Bhāgavatam 6.14–6.16 (selected)",
        "katha_chapter": "SB 6.14–6.16 — Citraketu; action, reaction, and sober instruction",
        "katha_links": [
            ("SB 6.14.1", "https://vedabase.io/en/library/sb/6/14/1/"),
            ("SB 6.15.1", "https://vedabase.io/en/library/sb/6/15/1/"),
            ("BG 3.9", "https://vedabase.io/en/library/bg/3/9/"),
        ],
        "katha_paraphrase": [
            "King Citraketu received great blessings, yet when his young son died, grief overwhelmed him. "
            "Sages and Nārada instructed him that the soul continues while bodies change — grief is natural, "
            "but mistaking the body for the whole self deepens suffering.",
            "Later, when Citraketu spoke without sufficient care toward Lord Śiva and mother Pārvatī, "
            "a reaction followed. The lesson is not cruel punishment for curiosity — it shows that words "
            "and attitudes are actions with consequences, even for a devotee.",
            "The story redirects families toward sober accountability: examine intention and method, "
            "repair what can be repaired, and offer work to Kṛṣṇa rather than separate selfish interest.",
        ],
        "katha_omitted": [
            "Graphic descriptions of Citraketu's demon birth",
            "Detailed cosmology of curse mechanics",
            "Using story to blame grieving parents",
        ],
        "katha_cautions": [
            "No frightening imagery for young children — focus on seeds and careful return of borrowed items",
            "Do not diagnose another person's suffering as their karma",
            "Honor grief in Citraketu narrative; instruction follows compassion",
        ],
        "lala_memory": "Choices are seeds. I want to plant service seeds.",
        "lala_sanskrit": "karma — action with consequence (say: KAR-mah)",
        "lala_story": "Mira borrows Amma's special bowl for pretend cooking. She returns it washed and placed on the shelf. Amma smiles. Next week, Ravi borrows the same bowl, leaves it outside, and rain makes it crack. Amma is sad; Ravi says sorry and helps glue the safe parts or replace with his savings. Same borrow — different method — different result.",
        "lala_safeguarding": "No frightening death imagery. No public shame for past mistakes. Two adults in visible space.",
        "sources": [
            ("BG-3-9", "Bhagavad-gītā", "3.9", "https://vedabase.io/en/library/bg/3/9/", "Work for Viṣṇu vs bondage"),
            ("BG-3-13", "Bhagavad-gītā", "3.13", "https://vedabase.io/en/library/bg/3/13/", "Food offered in sacrifice"),
            ("BG-4-16", "Bhagavad-gītā", "4.16", "https://vedabase.io/en/library/bg/4/16/", "What is action?"),
            ("BG-4-17", "Bhagavad-gītā", "4.17", "https://vedabase.io/en/library/bg/4/17/", "Complexity of action"),
            ("BG-4-18", "Bhagavad-gītā", "4.18", "https://vedabase.io/en/library/bg/4/18/", "Inaction in action"),
            ("SB-6-14-1", "Śrīmad-Bhāgavatam", "6.14.1", "https://vedabase.io/en/library/sb/6/14/1/", "Citraketu narrative frame"),
            ("SB-6-15-1", "Śrīmad-Bhāgavatam", "6.15.1", "https://vedabase.io/en/library/sb/6/15/1/", "Instruction on soul continuity"),
            ("SB-9-4-4", "Śrīmad-Bhāgavatam", "9.4.4", "https://vedabase.io/en/library/sb/9/4/4/", "King Nṛga — care and accountability (summary)"),
        ],
        "lectures": [
            ("SP-LEC-BG-3-9-1972", "1972-12-11", "Ahmedabad", "BG 3.9", "https://vedabase.io/en/library/lectures/december/11/1972/721211BG.AHM_eng/", "Yajña and bondage"),
            ("SP-LEC-BG-3-1973", "1973-12-21", "Los Angeles", "BG 3 lecture", "https://vedabase.io/en/library/lectures/december/21/1973/731221BG.LA_eng/", "Karma and devotion"),
            ("SP-LEC-KARMA-1975", "1975-03-23", "Melbourne", "Karma and responsibility", "https://vedabase.io/en/library/lectures/march/23/1975/750323BG.MEL_eng/", "Action and reaction overview"),
        ],
        "claims": [
            ("CLM-001", "Work performed only for separate material interest binds the living being.", "scripture-text", ["BG-3-9"], "all", "Reducing karma to fate"),
            ("CLM-002", "Work done as sacrifice for Viṣṇu should be performed without selfish attachment.", "scripture-text", ["BG-3-9"], "all", "Careless action justified by slogan"),
            ("CLM-003", "Intention, method, and consequence together shape the moral quality of an action.", "kutumba-summary", ["BG-4-16", "BG-4-17"], "parent", "Intention alone excuses harm"),
            ("CLM-004", "Karma in this module means action and reaction under material nature, not simplistic punishment.", "kutumba-summary", ["BG-3-9"], "all", "Fatalism or revenge thinking"),
            ("CLM-005", "We cannot confidently diagnose another person's suffering as the result of a specific past action.", "kutumba-summary", ["BG-4-17"], "all", "Victim-blaming"),
            ("CLM-006", "Good intention does not excuse dishonest or careless method.", "pedagogical-application", ["BG-4-16"], "kisora-kisori", "Moral excuse for harm"),
            ("CLM-007", "Offering work to Kṛṣṇa includes careful execution before, during, and after the act.", "pedagogical-application", ["BG-3-9"], "parent", "Labeling careless work 'for Kṛṣṇa'"),
            ("CLM-008", "King Nṛga's account illustrates procedural care and accountability, not fear for children.", "scripture-text", ["SB-9-4-4"], "parent", "Frightening children with cosmic punishment"),
            ("CLM-009", "Children can learn that choices plant seeds producing results without shame-based karma talk.", "pedagogical-application", ["BG-3-9"], "lala-lali", "Public comparison of children's mistakes"),
            ("CLM-010", "Repair — apology, return, replace, clarify — is part of responsible action.", "kutumba-summary", ["BG-3-9"], "all", "Avoiding restitution"),
        ],
        "case_count": 7,
        "bhakti_lab": "Before–During–After Service Method",
        "transition_recall": "Choices are seeds. I want to plant service seeds.",
    },
    "c2-w2-free-will-and-responsibility-the-next-choice-matters": {
        "code": "C2-W2",
        "title": "Free Will and Responsibility: The Next Choice Matters",
        "key_verse": "Bhagavad-gītā 18.63",
        "key_verse_url": "https://vedabase.io/en/library/bg/18/63/",
        "memory_line": "After giving knowledge, Kṛṣṇa tells Arjuna to deliberate fully and then act as he chooses.",
        "essential_question": "What can we control, what influences us, and how does the next choice matter?",
        "controlling_principle": "Conditioning is real; meaningful choice and responsibility remain under Kṛṣṇa's guidance.",
        "scope": "BG 18.61–63, 18.73, 3.33–34, 5.14–15; pause–remember–choose practice",
        "exclusions": "Unlimited independence from Kṛṣṇa; blaming victims; excusing abuse",
        "prerequisites": "C2-W1 karma foundation",
        "leads_to": "C2-W3 consciousness direction; C2-W6 integration",
        "hook": (
            "Two statements often appear in the same home. First: 'I had no choice; you made me angry.' "
            "Second: 'I should be able to control everything if I am spiritual.' Both are inaccurate. "
            "We do not control every circumstance, body, emotion, other person, or result. But we are "
            "not merely helpless machines either."
        ),
        "katha_title": "Ajāmila's calling of Nārāyaṇa",
        "katha_primary": "Śrīmad-Bhāgavatam 6.1–6.2 (selected)",
        "katha_chapter": "SB 6.1–6.2 — Ajāmila; the decisive moment and mercy",
        "katha_links": [
            ("SB 6.1.15", "https://vedabase.io/en/library/sb/6/1/15/"),
            ("SB 6.2.1", "https://vedabase.io/en/library/sb/6/2/1/"),
            ("BG 18.63", "https://vedabase.io/en/library/bg/18/63/"),
        ],
        "katha_paraphrase": [
            "Ajāmila lived by habits formed over years — some choices narrowed his freedom gradually, "
            "like a path walked many times. The tradition describes how deeply ingrained patterns matter.",
            "At the most critical moment, when fear and confusion surrounded him, he called the name "
            "Nārāyaṇa — the name of his youngest son, yet also the holy name of the Lord. That call "
            "was not an accident; it showed that even in conditioned life a turning toward the Lord "
            "can occur.",
            "The messengers of Viṣṇu intervened. The lesson for families is not sensational fear of "
            "death, but sober hope: the next choice matters, mercy is real, and guidance strengthens "
            "rather than removes responsibility.",
        ],
        "katha_omitted": [
            "Graphic Yamadūta imagery for young children",
            "Detailed afterlife courtroom narrative",
            "Using Ajāmila to excuse ongoing harmful behavior",
        ],
        "katha_cautions": [
            "Never tell victims they chose the harm done to them",
            "Unsafe situations require adult help immediately — not quiet endurance",
            "Youth track: no public confession of abuse or addiction",
        ],
        "lala_memory": "Stop — remember Kṛṣṇa — choose care.",
        "lala_sanskrit": "icchā — desire/will (say: ich-CHAH, lightly)",
        "lala_story": "Puppet Kāka sees his toy taken. His fists tighten and his voice gets loud. Teacher holds up red card: STOP. Yellow: remember — Kṛṣṇa sees me; what is the kind rule? Green: choose — ask adult for help, use words, or walk away. Kāka practices twice.",
        "lala_safeguarding": "Traffic-light pause is for low-risk triggers only. Danger = tell adult immediately. No blame for victims.",
        "sources": [
            ("BG-18-63", "Bhagavad-gītā", "18.63", "https://vedabase.io/en/library/bg/18/63/", "Deliberate and choose"),
            ("BG-18-73", "Bhagavad-gītā", "18.73", "https://vedabase.io/en/library/bg/18/73/", "Arjuna's willing alignment"),
            ("BG-18-61", "Bhagavad-gītā", "18.61", "https://vedabase.io/en/library/bg/18/61/", "Material nature and seated self"),
            ("BG-3-33", "Bhagavad-gītā", "3.33", "https://vedabase.io/en/library/bg/3/33/", "Even a wise man acts by nature"),
            ("BG-3-34", "Bhagavad-gītā", "3.34", "https://vedabase.io/en/library/bg/3/34/", "Material modes impel"),
            ("BG-5-14", "Bhagavad-gītā", "5.14", "https://vedabase.io/en/library/bg/5/14/", "Lord does not create agency or fruit"),
            ("BG-5-15", "Bhagavad-gītā", "5.15", "https://vedabase.io/en/library/bg/5/15/", "Nor does He accept sin or piety"),
            ("SB-6-1-15", "Śrīmad-Bhāgavatam", "6.1.15", "https://vedabase.io/en/library/sb/6/1/15/", "Ajāmila calls Nārāyaṇa"),
            ("SB-6-2-1", "Śrīmad-Bhāgavatam", "6.2.1", "https://vedabase.io/en/library/sb/6/2/1/", "Mercy of the holy name"),
        ],
        "lectures": [
            ("SP-LEC-BG-18-63-1972", "1972-11-25", "Hyderabad", "BG 18.63", "https://vedabase.io/en/library/lectures/november/25/1972/721125BG.HYD_eng/", "Deliberation and choice"),
            ("SP-LEC-BG-3-33-1973", "1973-12-16", "Los Angeles", "BG 3.33", "https://vedabase.io/en/library/lectures/december/16/1973/731216BG.LA_eng/", "Conditioning"),
            ("SP-LEC-FREE-WILL-1975", "1975-06-23", "Los Angeles", "Responsibility", "https://vedabase.io/en/library/lectures/june/23/1975/750623BG.LA_eng/", "Control and surrender"),
        ],
        "claims": [
            ("CLM-001", "Kṛṣṇa instructs Arjuna to deliberate fully and then act as he chooses.", "scripture-text", ["BG-18-63"], "all", "Choice without deliberation"),
            ("CLM-002", "Material nature, the body, prior conditioning, and other agents limit control.", "scripture-text", ["BG-18-61", "BG-3-33"], "parent", "Denying conditioning"),
            ("CLM-003", "Responsibility is not the same as controlling every result.", "kutumba-summary", ["BG-5-14", "BG-5-15"], "all", "Perfectionism or helplessness"),
            ("CLM-004", "Conditioning explains behavior without excusing harm to others.", "kutumba-summary", ["BG-3-34"], "kisora-kisori", "Using conditioning to avoid accountability"),
            ("CLM-005", "Victims of abuse or coercion did not freely choose the harm done to them.", "kutumba-summary", ["BG-18-63"], "all", "Victim-blaming"),
            ("CLM-006", "The pause–remember–choose method trains intervention at urge, not only after damage.", "pedagogical-application", ["BG-18-63"], "all", "Suppressing emotion without choice"),
            ("CLM-007", "Arjuna's choice in BG 18.73 shows willing alignment after hearing — not mere compliance.", "scripture-text", ["BG-18-73"], "parent", "Forced conformity"),
            ("CLM-008", "Calling upon the Lord at the decisive moment opens the path of mercy.", "scripture-text", ["SB-6-1-15"], "all", "Sensational fear-based preaching"),
            ("CLM-009", "Environmental supports — reminders, device boundaries, mentor help — strengthen good choice.", "pedagogical-application", ["BG-18-63"], "parent", "Willpower-only moralism"),
            ("CLM-010", "Children can learn traffic-light pause for strong feelings without being blamed for feelings.", "pedagogical-application", ["BG-18-63"], "lala-lali", "Shaming anger in young children"),
        ],
        "case_count": 7,
        "bhakti_lab": "Pause–Remember–Choose Practice",
        "transition_recall": "Stop — remember Kṛṣṇa — choose care.",
    },
    "c2-w3-birth-death-and-reincarnation": {
        "code": "C2-W3",
        "title": "Birth, Death and Reincarnation",
        "key_verse": "Bhagavad-gītā 2.22",
        "key_verse_url": "https://vedabase.io/en/library/bg/2/22/",
        "memory_line": "As a person puts aside worn clothes and accepts new ones, the soul leaves an old body and receives another.",
        "essential_question": "How do we speak truthfully about death and continuity with calm hope rather than fear?",
        "controlling_principle": "The soul continues through changing bodies; consciousness and choice shape direction.",
        "scope": "BG 2.13, 2.20, 2.22, 2.27, 8.5–6; bedtime remembrance; grief-compassionate responses",
        "exclusions": "Guessing destinations; ghost entertainment; frightening imagery for young children",
        "prerequisites": "C1-W2 body/self; C2-W1–W2 choice",
        "leads_to": "C2-W4 modes; deeper Cycle 3",
        "hook": (
            "A child asks at bedtime, 'What happens when someone dies?' Adults often move toward one "
            "of two extremes. We may avoid the question because it is uncomfortable, or give a "
            "frightening amount of detail because we think philosophy requires bluntness. Kṛṣṇa gives "
            "a sober middle path: the body changes and ends, but the soul is not destroyed."
        ),
        "katha_title": "Bhārata Mahārāja's remembrance",
        "katha_primary": "Śrīmad-Bhāgavatam 5.8–5.9 (selected)",
        "katha_chapter": "SB 5.8–5.9 — Bhārata; consciousness at life's end",
        "katha_links": [
            ("SB 5.8.1", "https://vedabase.io/en/library/sb/5/8/1/"),
            ("SB 5.9.1", "https://vedabase.io/en/library/sb/5/9/1/"),
            ("BG 2.22", "https://vedabase.io/en/library/bg/2/22/"),
        ],
        "katha_paraphrase": [
            "Bhārata Mahārāja was a great king who left his kingdom to practice devotion in the forest. "
            "He served with great care, yet a tender attachment to a young deer distracted his remembrance.",
            "When his human body ended, the story describes how the consciousness he had cultivated — "
            "including that attachment — influenced his next situation. The lesson is not horror; it is "
            "sober: what we remember and repeat shapes direction.",
            "For families, the katha supports bedtime remembrance and honest answers: the soul continues, "
            "the body is temporary like worn garments, and Kṛṣṇa is the shelter for those who remember Him.",
        ],
        "katha_omitted": [
            "Graphic death or animal-birth descriptions for Lāla–Lālī",
            "Speculation about a deceased relative's next body",
            "Ghost stories or paranormal claims",
        ],
        "katha_cautions": [
            "NO frightening imagery for ages 4–6 — use doll clothes and caterpillar picture only as illustration",
            "Offer opt-out for families with recent bereavement",
            "Grief is respected even when soul is eternal",
        ],
        "lala_memory": "Kṛṣṇa, please help me remember You.",
        "lala_sanskrit": "dehī — the one inside the body (say: DAY-hee)",
        "lala_story": "Doll Devi has three dresses: baby blue, school yellow, warm shawl. Teacher changes dresses while children hold Devi's name card. 'Dress changed — Devi is still Devi.' Caterpillar picture: 'Sometimes nature shows change — our proof is Kṛṣṇa's words in BG 2.22.'",
        "lala_safeguarding": "NO frightening death imagery. Feelings cards: sad, confused, peaceful, worried — all OK to share with trusted adult. Redirect graphic questions to parents.",
        "sources": [
            ("BG-2-13", "Bhagavad-gītā", "2.13", "https://vedabase.io/en/library/bg/2/13/", "Life stages"),
            ("BG-2-20", "Bhagavad-gītā", "2.20", "https://vedabase.io/en/library/bg/2/20/", "Soul not destroyed"),
            ("BG-2-22", "Bhagavad-gītā", "2.22", "https://vedabase.io/en/library/bg/2/22/", "Garment analogy"),
            ("BG-2-27", "Bhagavad-gītā", "2.27", "https://vedabase.io/en/library/bg/2/27/", "Death certain for one who is born"),
            ("BG-8-5", "Bhagavad-gītā", "8.5", "https://vedabase.io/en/library/bg/8/5/", "Remembering at end"),
            ("BG-8-6", "Bhagavad-gītā", "8.6", "https://vedabase.io/en/library/bg/8/6/", "Consciousness shapes direction"),
            ("SB-5-8-1", "Śrīmad-Bhāgavatam", "5.8.1", "https://vedabase.io/en/library/sb/5/8/1/", "Bhārata in the forest"),
            ("SB-5-9-1", "Śrīmad-Bhāgavatam", "5.9.1", "https://vedabase.io/en/library/sb/5/9/1/", "Consciousness and next life"),
        ],
        "lectures": [
            ("SP-LEC-BG-2-22-1973", "1973-08-22", "London", "BG 2.22", "https://vedabase.io/en/library/lectures/london/august/22/1973/7310822BG.LON_eng/", "Garment analogy"),
            ("SP-LEC-BG-2-20-1973", "1973-08-20", "London", "BG 2.20", "https://vedabase.io/en/library/lectures/london/august/20/1973/7310820BG.LON_eng/", "Soul not slain"),
            ("SP-LEC-TRANS-1975", "1975-03-25", "Melbourne", "Transmigration", "https://vedabase.io/en/library/lectures/march/25/1975/750325BG.MEL_eng/", "Sober transmigration teaching"),
        ],
        "claims": [
            ("CLM-001", "The embodied soul passes through bodily stages and accepts new bodies as garments change.", "scripture-text", ["BG-2-13", "BG-2-22"], "all", "Bodies chosen like closet clothes"),
            ("CLM-002", "The soul is not destroyed when the body stops working.", "scripture-text", ["BG-2-20"], "all", "Frightening children with destruction imagery"),
            ("CLM-003", "The garment analogy is helpful but limited — bodies are not casually selected.", "kutumba-summary", ["BG-2-22"], "all", "Oversimplifying rebirth"),
            ("CLM-004", "Repeated consciousness and remembrance shape future direction.", "scripture-text", ["BG-8-6"], "parent", "Superstition about one final thought"),
            ("CLM-005", "Grief for the bodily separation of loved ones is compatible with spiritual truth.", "kutumba-summary", ["BG-2-27"], "all", "Dismissing grief as 'ignorance'"),
            ("CLM-006", "We do not guess a specific deceased person's destination or species.", "kutumba-summary", ["BG-2-22"], "all", "Speculation and gossip"),
            ("CLM-007", "Bedtime remembrance replaces uncontrolled media with one minute of Kṛṣṇa focus.", "pedagogical-application", ["BG-8-5"], "all", "Forced emotional disclosure"),
            ("CLM-008", "Young children learn continuity through doll-clothes and life-stage pictures — not horror.", "pedagogical-application", ["BG-2-13"], "lala-lali", "Graphic death content"),
            ("CLM-009", "Present choices matter because consciousness is being shaped daily.", "kutumba-summary", ["BG-8-6", "SB-5-9-1"], "kisora-kisori", "Fatalism"),
            ("CLM-010", "Answers to children should be truthful, calm, brief, and developmentally appropriate.", "pedagogical-application", ["BG-2-20"], "all", "Avoidance or blunt overload"),
        ],
        "case_count": 6,
        "bhakti_lab": "Bedtime Remembrance Routine",
        "transition_recall": "Kṛṣṇa, please help me remember You.",
    },
    "c2-w4-the-three-modes-of-material-nature": {
        "code": "C2-W4",
        "title": "The Three Modes of Material Nature",
        "key_verse": "Bhagavad-gītā 14.5",
        "key_verse_url": "https://vedabase.io/en/library/bg/14/5/",
        "memory_line": "Material nature has three modes—goodness, passion and ignorance—that condition the eternal living being.",
        "essential_question": "How do goodness, passion, and ignorance influence perception and habit without labeling people?",
        "controlling_principle": "Modes are changing influences; describe conditions, not fixed identities.",
        "scope": "BG 14.5–9, 14.17–18, 14.26; environment design; clarity before chanting",
        "exclusions": "Labeling people/cultures; food policing; mental-health stereotypes",
        "prerequisites": "C2-W1–W3",
        "leads_to": "C2-W5 māyā; C2-W6 integration",
        "hook": (
            "The same family can experience three very different evenings. On one evening, the room is "
            "reasonably clean, the meal is timely, voices are calm, and a short reading feels possible. "
            "On another, everyone is rushing, several screens are active, plans keep changing, and "
            "irritation rises. On a third, dishes remain for days, people oversleep, avoid responsibility, "
            "and feel too dull to begin anything."
        ),
        "katha_title": "The brāhmaṇa who saw the modes in daily life",
        "katha_primary": "Bhagavad-gītā 14 / illustrative Bhāgavatam frame",
        "katha_chapter": "BG 14 — modes in ordinary situations",
        "katha_links": [
            ("BG 14.5", "https://vedabase.io/en/library/bg/14/5/"),
            ("BG 14.6", "https://vedabase.io/en/library/bg/14/6/"),
            ("BG 14.7", "https://vedabase.io/en/library/bg/14/7/"),
        ],
        "katha_paraphrase": [
            "A thoughtful brāhmaṇa in a busy town learned to watch his own day through the lens Kṛṣṇa "
            "gives in the Fourteenth Chapter: sometimes clarity and order prevailed; sometimes restlessness "
            "and grasping; sometimes fog, delay, and forgetfulness.",
            "He did not call his neighbors 'a mode.' He noticed conditions: noise, hunger, fatigue, "
            "competition, untidiness — and chose one small elevating action before sitting to chant.",
            "His students learned that modes mix and change, that goodness can still bind through pride, "
            "and that devotion beyond the modes is possible through Kṛṣṇa's mercy.",
        ],
        "katha_omitted": [
            "Fixed personality typing",
            "Cultural or gender mode labels",
            "Food shaming",
        ],
        "katha_cautions": [
            "Describe room conditions, not people as sattva/rajas/tamas labels",
            "Medical diets and allergies are never criticized",
        ],
        "lala_memory": "I can choose habits that help me hear Kṛṣṇa.",
        "lala_sanskrit": "sattva — goodness/clarity (say: SUT-tva)",
        "lala_story": "Three weather faces on the wall: clear sky, windy storm, sleepy fog. Teacher tells three mini-stories about the same playroom — tidy and quiet, noisy chase, messy and dark. Children match weather face to room, then do 3-item tidy reset.",
        "lala_safeguarding": "Never call a child a mode. Weather describes the room, not the person's worth.",
        "sources": [
            ("BG-14-5", "Bhagavad-gītā", "14.5", "https://vedabase.io/en/library/bg/14/5/", "Three modes named"),
            ("BG-14-6", "Bhagavad-gītā", "14.6", "https://vedabase.io/en/library/bg/14/6/", "Goodness characteristics"),
            ("BG-14-7", "Bhagavad-gītā", "14.7", "https://vedabase.io/en/library/bg/14/7/", "Passion characteristics"),
            ("BG-14-8", "Bhagavad-gītā", "14.8", "https://vedabase.io/en/library/bg/14/8/", "Ignorance characteristics"),
            ("BG-14-9", "Bhagavad-gītā", "14.9", "https://vedabase.io/en/library/bg/14/9/", "Modes compete"),
            ("BG-14-17", "Bhagavad-gītā", "14.17", "https://vedabase.io/en/library/bg/14/17/", "Fruits of modes"),
            ("BG-14-18", "Bhagavad-gītā", "14.18", "https://vedabase.io/en/library/bg/14/18/", "Mode dominance"),
            ("BG-14-26", "Bhagavad-gītā", "14.26", "https://vedabase.io/en/library/bg/14/26/", "Bhakti transcends modes"),
            ("BG-17-8", "Bhagavad-gītā", "17.8", "https://vedabase.io/en/library/bg/17/8/", "Food in goodness (careful use)"),
        ],
        "lectures": [
            ("SP-LEC-BG-14-5-1973", "1973-11-23", "Los Angeles", "BG 14.5", "https://vedabase.io/en/library/lectures/november/23/1973/731123BG.LA_eng/", "Three modes"),
            ("SP-LEC-BG-14-1974", "1974-06-08", "Paris", "BG 14", "https://vedabase.io/en/library/lectures/june/08/1974/740608BG.PAR_eng/", "Modes in life"),
            ("SP-LEC-MODES-1975", "1975-07-01", "Denver", "Material nature", "https://vedabase.io/en/library/lectures/july/01/1975/750701BG.DEN_eng/", "Transcending modes"),
        ],
        "claims": [
            ("CLM-001", "Material nature has three modes — goodness, passion, and ignorance — born of prakṛti.", "scripture-text", ["BG-14-5"], "all", "Fourth mode inventing"),
            ("CLM-002", "Modes describe tendencies and influences, not fixed labels on persons.", "kutumba-summary", ["BG-14-9"], "all", "Calling people 'tamasic'"),
            ("CLM-003", "Goodness tends toward clarity and order but can bind through pride and comfort.", "scripture-text", ["BG-14-6", "BG-14-17"], "parent", "Superiority over others"),
            ("CLM-004", "Passion tends toward restlessness, craving, and competition.", "scripture-text", ["BG-14-7"], "all", "Celebrating hustle as virtue"),
            ("CLM-005", "Ignorance tends toward dullness, neglect, and confusion.", "scripture-text", ["BG-14-8"], "all", "Mocking struggle as identity"),
            ("CLM-006", "Environmental design — remove, add, move earlier, simplify — supports bhakti.", "pedagogical-application", ["BG-14-5"], "parent", "External purity without devotion"),
            ("CLM-007", "Bhakti practiced with determination helps one transcend the modes.", "scripture-text", ["BG-14-26"], "all", "Modes talk replacing chanting"),
            ("CLM-008", "Children can identify calm, restless, and dull patterns in stories without labeling classmates.", "pedagogical-application", ["BG-14-5"], "lala-lali", "Public mode labeling"),
            ("CLM-009", "Food examples illustrate general tendencies; do not police medical or family food needs.", "kutumba-summary", ["BG-17-8"], "all", "Food shaming"),
            ("CLM-010", "Colored-filter lamp demonstrates perception shift — pedagogical analogy, not literal physics.", "pedagogical-application", ["BG-14-5"], "all", "Over-literalizing analogy"),
        ],
        "case_count": 7,
        "bhakti_lab": "Clarity Before Chanting",
        "transition_recall": "I can choose habits that help me hear Kṛṣṇa.",
    },
    "c2-w5-māyā-decorating-the-prison-cell": {
        "code": "C2-W5",
        "title": "Māyā: Decorating the Prison Cell",
        "key_verse": "Bhagavad-gītā 7.14",
        "key_verse_url": "https://vedabase.io/en/library/bg/7/14/",
        "memory_line": "Kṛṣṇa's material energy is difficult to overcome, but those who surrender to Him can cross beyond it.",
        "essential_question": "How does māyā misdirect attention, and how do boundary plus shelter restore devotion?",
        "controlling_principle": "Māyā is Kṛṣṇa's material energy; surrender and practice cross it — people are not māyā.",
        "scope": "BG 7.14, 2.62–63, 15.7, 9.10; prison-cell analogy; attention boundaries",
        "exclusions": "Misogynistic 'women are māyā'; world-hatred; diagnosing addiction publicly",
        "prerequisites": "C2-W4 modes",
        "leads_to": "C2-W6 integration; Cycle 3 bhakti",
        "hook": (
            "A person receives a notification while reading Bhagavad-gītā. 'I will check for ten seconds,' "
            "the mind says. Twenty minutes later, the person has moved through messages, news, shopping, "
            "and comparison, and can barely remember the verse. Nothing forced the hand physically. Yet the "
            "sequence felt automatic."
        ),
        "katha_title": "The fish in the well",
        "katha_primary": "Śrīmad-Bhāgavatam 7.5 / Prahlāda instruction context",
        "katha_chapter": "SB 7.5 — limited vision within māyā's covering",
        "katha_links": [
            ("SB 7.5.23", "https://vedabase.io/en/library/sb/7/5/23/"),
            ("BG 7.14", "https://vedabase.io/en/library/bg/7/14/"),
            ("BG 2.62", "https://vedabase.io/en/library/bg/2/62/"),
        ],
        "katha_paraphrase": [
            "Prahlāda Mahārāja taught that persons absorbed only in family, shop, and neighborhood comfort "
            "may mistake a small well for the whole ocean — like a fish who has never seen the sea.",
            "The covering of māyā is not that matter is unreal in every sense; it is that misplaced "
            "attachment makes us forget Kṛṣṇa and our actual interest.",
            "Crossing māyā comes through surrender to Kṛṣṇa and devotional shelter — not hatred of the "
            "world, not demeaning women, and not mere white-knuckle control without replacement practice.",
        ],
        "katha_omitted": [
            "Misogynistic slogans",
            "Detailed hell descriptions",
            "Public addiction disclosure",
        ],
        "katha_cautions": [
            "Explicitly reject 'women are māyā' every session",
            "People are souls; māyā is energy that covers remembrance",
        ],
        "lala_memory": "People are not māyā. I can stop, chant once, and choose help.",
        "lala_sanskrit": "māyā — Kṛṣṇa's material energy (say: MAH-yah)",
        "lala_story": "Shiny puppet toy flashes and beeps during cleanup time. Children practice: put down, three breaths, one chant, pick up one toy for Kṛṣṇa. Sticky-note path shows how each 'just one look' adds up.",
        "lala_safeguarding": "Say clearly: People are not māyā. No inappropriate media displayed in class.",
        "sources": [
            ("BG-7-14", "Bhagavad-gītā", "7.14", "https://vedabase.io/en/library/bg/7/14/", "Divine energy; surrender"),
            ("BG-2-62", "Bhagavad-gītā", "2.62", "https://vedabase.io/en/library/bg/2/62/", "Contemplation chain begins"),
            ("BG-2-63", "Bhagavad-gītā", "2.63", "https://vedabase.io/en/library/bg/2/63/", "Anger and bewilderment"),
            ("BG-15-7", "Bhagavad-gītā", "15.7", "https://vedabase.io/en/library/bg/15/7/", "Living entities struggle with māyā"),
            ("BG-9-10", "Bhagavad-gītā", "9.10", "https://vedabase.io/en/library/bg/9/10/", "Material nature under Kṛṣṇa"),
            ("SB-7-5-23", "Śrīmad-Bhāgavatam", "7.5.23", "https://vedabase.io/en/library/sb/7/5/23/", "Well and ocean illustration"),
            ("BG-7-25", "Bhagavad-gītā", "7.25", "https://vedabase.io/en/library/bg/7/25/", "Yogamāyā vs Mahāmāyā (intro only)"),
            ("BG-18-66", "Bhagavad-gītā", "18.66", "https://vedabase.io/en/library/bg/18/66/", "Surrender shelter"),
        ],
        "lectures": [
            ("SP-LEC-BG-7-14-1972", "1972-02-19", "Vrindavan", "BG 7.14", "https://vedabase.io/en/library/lectures/february/19/1972/720219BG.VRN_eng/", "Māyā difficult to overcome"),
            ("SP-LEC-MAYA-1973", "1973-09-05", "Stockholm", "Māyā", "https://vedabase.io/en/library/lectures/september/05/1973/730905BG.STO_eng/", "Material energy"),
            ("SP-LEC-BG-2-62-1973", "1973-08-17", "London", "BG 2.62", "https://vedabase.io/en/library/lectures/august/17/1973/730817BG.LON_eng/", "Attention chain"),
        ],
        "claims": [
            ("CLM-001", "Kṛṣṇa's material energy (māyā) is difficult to overcome without surrender to Him.", "scripture-text", ["BG-7-14"], "all", "Self-sufficiency"),
            ("CLM-002", "Māyā consists of the three modes and covers knowledge of Kṛṣṇa.", "scripture-text", ["BG-7-14"], "parent", "Calling matter totally unreal"),
            ("CLM-003", "Contemplating sense objects leads through attachment to desire and loss of intelligence.", "scripture-text", ["BG-2-62", "BG-2-63"], "kisora-kisori", "Blaming objects only"),
            ("CLM-004", "Decorating the prison cell means making comfort, image, or control the ultimate project.", "kutumba-summary", ["BG-7-14"], "parent", "Neglecting household duty"),
            ("CLM-005", "Women, children, and all persons are souls — never 'māyā.'", "kutumba-summary", ["BG-7-14"], "all", "Misogynistic misuse"),
            ("CLM-006", "Boundary plus shelter — limit, replacement practice, devotee support — beats prohibition alone.", "pedagogical-application", ["BG-7-14"], "all", "Willpower-only plans"),
            ("CLM-007", "The fish-in-the-well analogy illustrates limited vision, not literal geography.", "pedagogical-application", ["SB-7-5-23"], "all", "Mocking family life"),
            ("CLM-008", "Stop–name–redirect trains attention without shame spirals.", "pedagogical-application", ["BG-2-62"], "all", "Hiding compulsive behavior publicly while shaming privately"),
            ("CLM-009", "Responsible material arrangement for Kṛṣṇa differs from ultimate absorption in decoration.", "kutumba-summary", ["BG-9-10"], "parent", "World-rejection"),
            ("CLM-010", "Children learn shiny distractions pull away from helping; people remain sacred.", "pedagogical-application", ["BG-7-14"], "lala-lali", "Displaying inappropriate ads"),
        ],
        "case_count": 7,
        "bhakti_lab": "Attention Boundary and Japa Shelter",
        "transition_recall": "People are not māyā. I can stop, chant once, and choose help.",
    },
    "c2-w6-integration-night-choice-consequence-and-the-modes": {
        "code": "C2-W6",
        "title": "Integration Night: Choice, Consequence and the Modes",
        "key_verse": "Bhagavad-gītā 18.63",
        "key_verse_url": "https://vedabase.io/en/library/bg/18/63/",
        "memory_line": "Knowledge should lead to thoughtful, responsible choice under Kṛṣṇa's guidance.",
        "essential_question": "How do karma, choice, rebirth, modes, and māyā fit one family decision?",
        "controlling_principle": "Five-lens analysis without blame, fatalism, or fixed labels.",
        "scope": "Review BG 3.9, 18.63, 2.22, 14.5, 7.14; five-lens case lab; continuity planning",
        "exclusions": "New overloaded līlā; gossip disguised as cases; public scoring",
        "prerequisites": "C2-W1–W5",
        "leads_to": "Cycle 3 — Kṛṣṇa, guru, bhakti",
        "hook": (
            "A family has a recurring Friday problem. Everyone arrives late. The parent blames traffic, "
            "the children blame hunger, and another adult says, 'This is our karma; nothing can change.' "
            "The home is rushed, devices remain active, and no one prepared food on time. By the time "
            "kīrtana begins, irritation has already spread."
        ),
        "katha_title": "Integration — choice and consequence review",
        "katha_primary": "Facilitator synthesis (no new principal līlā)",
        "katha_chapter": "Cycle 2 synthesis — five lenses on one family evening",
        "katha_links": [
            ("BG 3.9", "https://vedabase.io/en/library/bg/3/9/"),
            ("BG 18.63", "https://vedabase.io/en/library/bg/18/63/"),
            ("BG 14.5", "https://vedabase.io/en/library/bg/14/5/"),
            ("BG 7.14", "https://vedabase.io/en/library/bg/7/14/"),
        ],
        "katha_paraphrase": [
            "Facilitator recalls the Friday evening every family recognized: lateness, hunger, active devices, "
            "and the sentence 'nothing can change.' The group pauses — not to assign blame, but to see clearly.",
            "Lens by lens: actions and reactions from rushed choices; what was controlled vs influenced; "
            "mode-like conditions in the room; false promises of convenience; and devotional shelter — "
            "a five-minute reset, pause–remember–choose, and food prepared as service.",
            "No new hero story is required. Kṛṣṇa has already given the tools across Cycle 2. Tonight the "
            "family practices weaving them together and chooses one method to continue in the off week.",
        ],
        "katha_omitted": [
            "New copyrighted narrative overload",
            "Real family gossip",
            "Competitive scoring",
        ],
        "katha_cautions": [
            "Fictional cases only in group work",
            "Testimonies only with consent",
            "No winning table",
        ],
        "lala_memory": "We have tools: seeds, pause, remembrance, tidy sky, boundaries.",
        "lala_sanskrit": "review — no new term required",
        "lala_story": "Puppet family rushes on Friday. Children pick tool cards: seed (prepare snack), traffic light (pause before shouting), tidy sky (reset rug), bedtime star (remember Kṛṣṇa). Puppet family tries again — calmer kīrtana.",
        "lala_safeguarding": "Fictional puppets only. No quizzes on deceased relatives or karma diagnosis.",
        "sources": [
            ("BG-3-9", "Bhagavad-gītā", "3.9", "https://vedabase.io/en/library/bg/3/9/", "C2-W1 review"),
            ("BG-18-63", "Bhagavad-gītā", "18.63", "https://vedabase.io/en/library/bg/18/63/", "C2-W2 review"),
            ("BG-2-22", "Bhagavad-gītā", "2.22", "https://vedabase.io/en/library/bg/2/22/", "C2-W3 review"),
            ("BG-14-5", "Bhagavad-gītā", "14.5", "https://vedabase.io/en/library/bg/14/5/", "C2-W4 review"),
            ("BG-7-14", "Bhagavad-gītā", "7.14", "https://vedabase.io/en/library/bg/7/14/", "C2-W5 review"),
            ("BG-14-26", "Bhagavad-gītā", "14.26", "https://vedabase.io/en/library/bg/14/26/", "Devotion beyond modes"),
            ("BG-2-62", "Bhagavad-gītā", "2.62", "https://vedabase.io/en/library/bg/2/62/", "Attention chain review"),
            ("BG-8-6", "Bhagavad-gītā", "8.6", "https://vedabase.io/en/library/bg/8/6/", "Consciousness direction review"),
        ],
        "lectures": [
            ("SP-LEC-CYCLE-1973", "1973-12-28", "Los Angeles", "Summary lecture", "https://vedabase.io/en/library/lectures/december/28/1973/731228BG.LA_eng/", "Integration prep"),
            ("SP-LEC-BG-18-63-1972", "1972-11-25", "Hyderabad", "BG 18.63", "https://vedabase.io/en/library/lectures/november/25/1972/721125BG.HYD_eng/", "Choice under guidance"),
            ("SP-LEC-KARMA-1975", "1975-03-23", "Melbourne", "Karma overview", "https://vedabase.io/en/library/lectures/march/23/1975/750323BG.MEL_eng/", "Cycle 2 thread"),
        ],
        "claims": [
            ("CLM-001", "Cycle 2 knowledge should produce thoughtful, responsible choice — not fatalism.", "kutumba-summary", ["BG-18-63"], "all", "'Nothing can change' resignation"),
            ("CLM-002", "Five-lens analysis includes action, choice, modes, false promise, and shelter.", "pedagogical-application", ["BG-3-9", "BG-18-63", "BG-14-5", "BG-7-14"], "all", "Single-lens blame"),
            ("CLM-003", "Karma diagnosis of another person's suffering is prohibited in case work.", "kutumba-summary", ["BG-3-9"], "all", "Victim-blaming cases"),
            ("CLM-004", "Mode language describes conditions, not permanent identities.", "kutumba-summary", ["BG-14-5"], "all", "Mode-labeling classmates"),
            ("CLM-005", "Integration week uses synthesis, not a new overloaded principal līlā.", "pedagogical-application", [], "all", "Narrative overload"),
            ("CLM-006", "Families choose one Cycle 2 method to continue during the off week.", "pedagogical-application", ["BG-18-63"], "all", "No practical continuity"),
            ("CLM-007", "Children demonstrate at least one tool: pause, seed, remembrance, reset, or boundary.", "pedagogical-application", [], "lala-lali", "Performative testing"),
            ("CLM-008", "Case discussions use fictional facts only — no indirect gossip.", "kutumba-summary", [], "all", "Real family exposure"),
            ("CLM-009", "Assessment is private — no winning table or public score.", "pedagogical-application", [], "all", "Competitive shaming"),
            ("CLM-010", "Surrender includes practical boundaries and responsible action together.", "kutumba-summary", ["BG-7-14", "BG-18-63"], "parent", "Splitting devotion from duty"),
        ],
        "case_count": 8,
        "bhakti_lab": "Five-Lens Family Case Lab",
        "transition_recall": "We have tools: seeds, pause, remembrance, tidy sky, boundaries.",
    },
}
