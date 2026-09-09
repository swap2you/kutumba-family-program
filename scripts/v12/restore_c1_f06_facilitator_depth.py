#!/usr/bin/env python3
"""V12.1 F06 — Restore C1 facilitator depth into MAIN-FACILITATOR-GUIDE-V12.md.

Merges V11.1 depth (commit 7a61b82 / generate_c1_v11_1_depth.py data) with V12 verse
layers. Core teaching is INLINED — no "Use week research ANALOGIES-AND-LIMITS…" shells.
Also deepens younger/older teacher guides, activity packs, and research files.
"""
from __future__ import annotations

from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
VERSE_YAML = Path(__file__).with_name("verse_data.yaml")

NEXT = {
    "C1-W1": "C1-W2 — I Am Not This Body",
    "C1-W2": "C1-W3 — The Nature of the Soul",
    "C1-W3": "C1-W4 — Why Human Life Is Rare and Valuable",
    "C1-W4": "C1-W5 — The Temporary World and the Search for Permanent Happiness",
    "C1-W5": "C1-W6 — Integration Night: Who Am I, and How Should Our Family Live?",
    "C1-W6": "Cycle Utsava / protected off week, then Cycle 2 when families are ready — do not teach C2 ontology tonight",
}

WEEKS = {
    "C1-W1": {
        "slug": "c1-w1-what-is-kutumba-and-why-are-we-here",
        "title": "What Is KUTUMBA, and Why Are We Here?",
        "question": "Why are we committing as a family?",
        "conclusion": "Protected weekly hearing plus home practice creates a path for family growth.",
        "misconception": "Coming to the session without home practice is enough.",
        "memory": "Regular hearing and service to Śrīmad-Bhāgavatam steadies our family's devotion.",
        "supports": [
            ("ŚB 1.2.17", "https://vedabase.io/en/library/sb/1/2/17/", "The Lord in the heart cleanses desire from the faithful hearer."),
            ("ŚB 1.2.19", "https://vedabase.io/en/library/sb/1/2/19/", "Passion and ignorance recede as goodness increases through hearing."),
            ("ŚB 1.1.4", "https://vedabase.io/en/library/sb/1/1/4/", "Sages assemble and inquire about duty — model of protected hearing community."),
        ],
        "analogies": [
            ("Protected garden plot", "A small plot watered every week grows roots even when you cannot see bloom yet.", "Not a guaranteed bloom timetable; devotion is not horticulture. Watering is pedagogy for regularity, not proof of results."),
            ("Team practice night", "Teams improve when show-up and home drills both happen — Saturday alone is incomplete.", "Sports glory is not the spiritual goal; do not turn KUTUMBA into competition."),
            ("Path with a fence", "Clear is/isn't boundaries keep the path walkable for newcomers and regulars.", "Boundaries are not hostility; compassion stays; we do not shame families."),
        ],
        "examples": [
            ("Naimiṣāraṇya assembly", "ŚB Canto 1 opening", "https://vedabase.io/en/library/sb/1/1/", "Sages gather to hear and ask about the highest duty. KUTUMBA borrows the *pattern* of protected hearing — not a claim that our living room equals Naimiṣāraṇya."),
            ("Regular Bhāgavata hearing emphasis", "ŚB 1.2.18 context", "https://vedabase.io/en/library/sb/1/2/18/", "The primary verse itself teaches that steady Bhāgavata service establishes firm devotion. Paraphrase only; do not invent purport lines."),
        ],
        "cases": [
            {
                "sit": "A family never misses Saturday 2–4, but weekdays have zero hearing, memory line, or gratitude act.",
                "wrong": "Attendance alone equals spiritual growth.",
                "principle": "ŚB 1.2.18 — nityaṁ bhāgavata-sevayā: regularity of hearing/service, not event tourism.",
                "source": "https://vedabase.io/en/library/sb/1/2/18/",
                "response": "Thank them for showing up. Affirm that Saturday is precious. Then invite one tiny home cue (same chair, same five minutes).",
                "action": "Write a 5-minute if-then plan: After dinner dishes, we say the memory line once.",
                "not": "You're not serious. Other families are more advanced. Coming here is worthless without perfection.",
            },
            {
                "sit": "A family chants at home but withdraws from association because community feels awkward.",
                "wrong": "Alone is always safer and more spiritual than community.",
                "principle": "Hearing in association (Bhāgavata and devotees) is part of the verse's seva frame; friendship supports steadiness.",
                "source": "https://vedabase.io/en/library/sb/1/2/18/",
                "response": "Honor their home sincerity. Name one low-pressure shared moment (arrive early, sit near a friend, stay for snack only).",
                "action": "Choose one association micro-step this month — not a full social overhaul.",
                "not": "You're proud / antisocial. Real devotees never feel awkward.",
            },
            {
                "sit": "A parent compares children's seriousness in front of other families.",
                "wrong": "Ranking children produces devotion.",
                "principle": "KUTUMBA charter: no ranking; growth is personal and private where needed.",
                "source": "Program charter / privacy practice (pedagogy)",
                "response": "Redirect privately: compare only to your own family's last week, never to another child.",
                "action": "Each child names one personal minimum practice — no public scoreboard.",
                "not": "Look how advanced that child is. Shame your kid into chanting.",
            },
        ],
        "qa": [
            ("Do we have to be perfect?", "No. Minimum versions are allowed. Regularity of hearing and service matters more than dramatic intensity (ŚB 1.2.18)."),
            ("Can science prove this verse?", "Science may help design habits and family rituals. Doctrine about cleansing the heart and steady bhakti rests on śāstra, not lab proof."),
            ("What if my child resists?", "No force. Shorten the practice. Parent models calmly. Offer a private support conversation — never public pressure."),
            ("Is KUTUMBA a replacement for the temple?", "No. It is a family growth rhythm that supports hearing, practice, and temple friendship — not a substitute institution."),
            ("What if we miss a Saturday?", "Return without shame. Restart the home cue. Do not invent make-up rankings or penalties."),
        ],
        "discovery": [
            "What word in today's theme (KUTUMBA / hearing / home practice) is new or unclear?",
            "Where have you seen the tension between 'showing up' and 'practicing at home'?",
            "What would a five-minute minimum version look like in your kitchen this week?",
        ],
        "understanding": [
            "State this week's conclusion in one sentence.",
            "Name the primary scripture and its KUTUMBA teaching meaning in your own words.",
            "What does this week *not* teach (e.g., ranking, guaranteed bloom, temple replacement)?",
        ],
        "application": [
            "What is our family cue (exact time + place) for home practice?",
            "Who will start the practice if others are tired?",
            "What is the minimum version on a hard week?",
        ],
        "young_story": "Long ago, wise people gathered in a peaceful forest place to hear about the Lord and ask how to live. We are not those sages — but we can borrow their *habit*: set a protected time, hear together, and take one small practice home. Today we learn that regular hearing and kind service help a family's heart grow steady.",
        "young_craft": "Garden watering card: draw a small plant; inside write the memory phrase. Children 'water' the card by tracing a drop each time they practice at home.",
        "young_object": "Small cup with a paper 'seed' labeled Hear → Practice.",
        "older_puzzle": "Match: Hearing / Saṅkalpa / Charter / Association",
        "activity_core": "Orientation bingo + family purpose card",
    },
    "C1-W2": {
        "slug": "c1-w2-i-am-not-this-body",
        "title": "I Am Not This Body",
        "question": "How should knowing I am not only this body change how we speak about bodies?",
        "conclusion": "Body changes; conscious self continues — care for the body without mistaking it for the self.",
        "misconception": "Psychology or photos prove the soul.",
        "memory": "My body changes; I continue as the conscious self.",
        "supports": [
            ("BG 2.22", "https://vedabase.io/en/library/bg/2/22/", "As one puts on new garments, the soul accepts new bodies — analogy with limits; full ontology reserved for W3."),
            ("BG 2.20", "https://vedabase.io/en/library/bg/2/20/", "Supporting: the soul is not slain when the body is slain — preview only; deep teaching next week."),
        ],
        "analogies": [
            ("Changing garments", "Clothes change; the wearer continues. Helps children grasp body vs self.", "Clothes are chosen; bodies are not fashion accessories. Do not teach contempt for the body."),
            ("Life-stage photos", "Same person across childhood, youth, elder photos — continuity of the 'I'.", "Photos are not ontology proof; memory and personality also change in expression."),
            ("Driver and vehicle", "The operator uses the vehicle; the operator is not the metal.", "Avoid harsh dualism ('body is trash'). Care for the vehicle for service."),
        ],
        "examples": [
            ("Arjuna's grief at Kurukṣetra opening", "BG Ch. 1–2 narrative", "https://vedabase.io/en/library/bg/1/", "Arjuna's distress is tied to bodily relationships. Kṛṣṇa's teaching begins by clarifying the embodied self — paraphrase only; no invented dialogue."),
            ("Garment analogy support", "BG 2.22", "https://vedabase.io/en/library/bg/2/22/", "Scriptural analogy for changing bodies; keep limits explicit in class."),
        ],
        "cases": [
            {
                "sit": "A sibling teases another about appearance during snack.",
                "wrong": "Body comments are harmless jokes.",
                "principle": "BG 2.13 — respectful speech about changing bodies; dignity of every person.",
                "source": "https://vedabase.io/en/library/bg/2/13/",
                "response": "Stop the tease gently. Affirm both children's dignity. Repair with a kind sentence.",
                "action": "Family speech pledge: no appearance jokes at home this week.",
                "not": "Toughen up. It's just a joke. Spiritual people ignore feelings.",
            },
            {
                "sit": "A teen builds identity almost entirely around fitness metrics.",
                "wrong": "The body project *is* the self.",
                "principle": "Care for body as vehicle; self continues beyond stages (BG 2.13).",
                "source": "https://vedabase.io/en/library/bg/2/13/",
                "response": "Affirm health goals. Separate 'I care for this body' from 'I am only this body.'",
                "action": "Keep healthy routine; add one non-body identity practice (memory line / service).",
                "not": "Fitness is māyā — stop exercising. Your body doesn't matter.",
            },
            {
                "sit": "A relative asks a child's weight publicly at a gathering.",
                "wrong": "Public body talk is normal and fine.",
                "principle": "Privacy + respect; body is not public property.",
                "source": "Program privacy practice + BG 2.13 dignity",
                "response": "Change the subject warmly; protect the child without shaming the relative in front of others if possible.",
                "action": "Parents agree on a redirect line beforehand.",
                "not": "Announce the child's stats. Lecture the relative with anger in front of the child.",
            },
        ],
        "qa": [
            ("Do photos prove the soul?", "No. Photos help pedagogy about continuity. Ontology rests on śāstra (BG 2.13+), not albums."),
            ("Should we ignore the body?", "No. Care for health, rest, and hygiene. Refuse identity = body, not refuse care."),
            ("Is this teaching reincarnation details?", "This week introduces continuity of the self through stages and points to transmigration modestly. Deep soul ontology is W3."),
            ("What about disability or illness?", "Every body deserves dignity and care. Never imply someone is 'less' because of bodily condition."),
            ("Can psychology replace this lesson?", "Psychology may help speech and body-image habits. It does not prove ātman."),
        ],
        "discovery": [
            "What changes about your body that you can notice without shame?",
            "Where have body jokes hurt someone at home or school?",
            "What would respectful body-speech sound like this week?",
        ],
        "understanding": [
            "State BG 2.13's teaching meaning in one sentence.",
            "Name one analogy and its limit.",
            "What does this week *not* claim about science or photos?",
        ],
        "application": [
            "What family speech rule will we keep for seven days?",
            "How will we care for the body *as service* this week?",
            "What is our minimum respectful redirect when teasing starts?",
        ],
        "young_story": "Think of three pictures of the same child: small, a little bigger, and bigger still. The face changes, but we still say the same name. Today we learn: the body changes; the person — the conscious self — continues. We speak kindly about every body.",
        "young_craft": "Paper-doll clothes: one face card, three outfits. Children swap clothes and say: 'Clothes change; I continue.'",
        "young_object": "Consent photo timeline (family-provided or stick figures) — no forced photo sharing.",
        "older_puzzle": "Match: Body / Self / Analogy / Respect",
        "activity_core": "Life-stage timeline + body/self grid",
    },
    "C1-W3": {
        "slug": "c1-w3-the-nature-of-the-soul",
        "title": "The Nature of the Soul",
        "question": "If I am a soul, how should I live?",
        "conclusion": "The jīva is eternal, conscious, individual, minute, and related to Kṛṣṇa in service — not God Himself.",
        "misconception": "All souls are God / we are the Supreme.",
        "memory": "I am an eternal soul — conscious, individual, and meant for Kṛṣṇa's service.",
        "supports": [
            ("BG 15.7", "https://vedabase.io/en/library/bg/15/7/", "Living entities are eternal fragmental parts of Kṛṣṇa — qualitative likeness, quantitative difference."),
            ("BG 2.17", "https://vedabase.io/en/library/bg/2/17/", "That which pervades the body is indestructible."),
            ("ŚB 5.10 (Jaḍa Bharata context)", "https://vedabase.io/en/library/sb/5/10/", "Narrative support: soul beyond bodily status labels — gentle paraphrase only."),
        ],
        "analogies": [
            ("Sun and sunray", "Ray shares light-nature with the sun but is not the sun.", "Ray is not the sun — blocks 'I am God.'"),
            ("Spark from fire", "Same nature, dependent existence.", "Not independent Godhood; dependence remains."),
            ("House and resident", "Resident is not the house; still cares for the house.", "Can feel impersonal if overused — keep personhood of the jīva clear."),
        ],
        "examples": [
            ("Jaḍa Bharata and King Rahūgaṇa", "ŚB 5.9–5.10", "https://vedabase.io/en/library/sb/5/10/", "Bodily labels (carrier, king, appearance) do not define the soul. Classroom retelling must be nonviolent and symbolic; no invented dialogue."),
            ("Fragmental part teaching", "BG 15.7", "https://vedabase.io/en/library/bg/15/7/", "Supports individuality + relationship to Kṛṣṇa without claiming Supreme identity."),
        ],
        "cases": [
            {
                "sit": "A child proudly says, 'I am God.'",
                "wrong": "Soul equals the Supreme.",
                "principle": "BG 15.7 — eternal fragmental part; BG 2.20 — eternal individual self.",
                "source": "https://vedabase.io/en/library/bg/15/7/",
                "response": "Smile; correct gently: we are tiny parts meant to serve, not the whole.",
                "action": "Practice the sentence: 'I am a soul who serves Kṛṣṇa.'",
                "not": "You're blasphemous. Shame the child publicly.",
            },
            {
                "sit": "An adult dismisses soul talk as anti-science.",
                "wrong": "Science has disproved the soul.",
                "principle": "Different domains: empiricism measures bodies/behavior; śāstra teaches ātman.",
                "source": "Program science boundary + BG 2.20",
                "response": "Agree that labs measure physical processes. Clarify we are not claiming a lab proof of ātman tonight.",
                "action": "Offer the deferral line; invite reading the verse URL later.",
                "not": "Scientists are demons. Faith means never asking questions.",
            },
            {
                "sit": "A family neglects sleep and hygiene 'because we are soul.'",
                "wrong": "Body contempt is spiritual.",
                "principle": "Care without identity confusion — resident cares for house.",
                "source": "Pedagogy limit of house analogy + prior W2 care theme",
                "response": "Restore basic care as service readiness, not as identity.",
                "action": "Pick one body-care act (sleep time / water / bathing) as service this week.",
                "not": "The body is illusion so ignore doctors. Only weak people rest.",
            },
        ],
        "qa": [
            ("Are we God?", "No. We are eternal fragmental parts meant for service (BG 15.7)."),
            ("Can science prove the soul?", "N/A as proof. Empiricism does not establish ātman; we teach from śāstra."),
            ("Is the soul created at birth?", "BG 2.20 teaches the soul is never born and never dies — paraphrase carefully; avoid speculative cosmology debates."),
            ("Do animals have souls?", "Gauḍīya teaching affirms life in many forms; keep class focused on human family practice tonight without species contempt."),
            ("What should I *do* if I am a soul?", "Live as a servant of Kṛṣṇa: hear, remember, serve, speak respectfully — start with this week's home cue."),
        ],
        "discovery": [
            "What does 'eternal' mean in kid words?",
            "Where do people confuse 'soul' with 'I am God'?",
            "What is one way a soul shows service at home?",
        ],
        "understanding": [
            "List three truths about the jīva from today's teaching.",
            "Name what the jīva is *not*.",
            "Cite BG 2.20's teaching meaning in your own words.",
        ],
        "application": [
            "What offering or service act will we do this week?",
            "How will we correct 'I am God' language at home?",
            "What body-care act will we keep as service?",
        ],
        "young_story": "A lamp and its light are related — the light is not the whole lamp. We are tiny living sparks from the Lord, meant to shine by serving Him. We are not the Supreme. We care for our body-house and remember Kṛṣṇa.",
        "young_craft": "Sun-and-ray craft: big sun labeled Kṛṣṇa; small ray labeled Me (servant).",
        "young_object": "Flashlight beam demo: beam is light-like, not the flashlight.",
        "older_puzzle": "Match: Jīva / Fragmental part / Eternal / Service",
        "activity_core": "Is/is-not sort + offering craft",
    },
    "C1-W4": {
        "slug": "c1-w4-why-human-life-is-rare-and-valuable",
        "title": "Why Human Life Is Rare and Valuable",
        "question": "What deserves protected family time?",
        "conclusion": "Human life gives a rare opportunity for deliberate self-realization — protect inquiry and practice time.",
        "misconception": "Use fear or death-pressure to motivate children.",
        "memory": "Human life is a rare chance to ask who I am and serve Kṛṣṇa.",
        "supports": [
            ("BG 2.40", "https://vedabase.io/en/library/bg/2/40/", "No loss or diminution in this endeavor; a little progress protects from fear."),
            ("CC Madhya 24.229–282 (Nārada–Mṛgāri)", "https://vedabase.io/en/library/cc/madhya/24/", "Mercy and authorized instruction transform harmful conduct — not SB 6.x / SB 4.8."),
        ],
        "analogies": [
            ("Rare ticket", "A hard-to-get ticket is meant to be used, not forgotten in a drawer.", "Not a scare tactic; opportunity language, not threat language."),
            ("Crossroads sign", "Choice of path matters when the road splits.", "No species contempt; no mocking other forms of life."),
            ("Seed season", "Plant while the season is open.", "No guaranteed harvest timing; avoid pressuring children with panic."),
        ],
        "examples": [
            ("Nārada and the hunter Mṛgāri", "CC Madhya 24.229–282", "https://vedabase.io/en/library/cc/madhya/24/229/", "Nārada meets a hunter, teaches him, and the hunter's life turns toward care and devotion (bow broken; careful steps even toward ants — paraphrase gently). Source is Madhya 24 — not SB 6.x or SB 4.8."),
            ("Rare human form teaching", "ŚB 11.9.29", "https://vedabase.io/en/library/sb/11/9/29/", "Primary: after many births, human form is rare and purpose-capable — use it for the highest good."),
        ],
        "cases": [
            {
                "sit": "Screens eat the family's only quiet evening block every night.",
                "wrong": "Entertainment first is always fine.",
                "principle": "ŚB 11.9.29 — protect opportunity for inquiry and practice.",
                "source": "https://vedabase.io/en/library/sb/11/9/29/",
                "response": "No shame spiral. Name one protected 10-minute block as 'Must.'",
                "action": "Move one optional screen slot after the spiritual cue.",
                "not": "You're wasting your human life forever. Terrify the kids.",
            },
            {
                "sit": "A parent uses death scare to make a child chant.",
                "wrong": "Fear creates lasting urgency.",
                "principle": "Compassion and opportunity — not terror. BG 2.40 supports steady endeavor without fear-panic.",
                "source": "https://vedabase.io/en/library/bg/2/40/",
                "response": "Stop fear tactics. Replace with invitation and short joyful practice.",
                "action": "Rewrite the family ask: 'We get to practice' not 'or else.'",
                "not": "If you don't chant you'll be punished / die badly.",
            },
            {
                "sit": "Calendar is full; no inquiry time remains.",
                "wrong": "Busy equals successful human life.",
                "principle": "Human form is for realization — trade one optional for hearing.",
                "source": "https://vedabase.io/en/library/sb/11/9/29/",
                "response": "Audit optional activities with kindness; keep duties; protect one inquiry slot.",
                "action": "Time-jar: Must / Should / Optional — move one item.",
                "not": "Quit school/work to prove spirituality.",
            },
        ],
        "qa": [
            ("Should we scare kids so they take life seriously?", "No. Teach opportunity and mercy. Fear tactics are out of bounds."),
            ("Where is the Mṛgāri story from?", "Caitanya-caritāmṛta Madhya 24.229–282 — not ŚB 6.x or ŚB 4.8."),
            ("Does valuing human life mean disrespecting animals?", "No. No species contempt. Care and compassion remain."),
            ("What if we only have five minutes?", "Five protected minutes of hearing/inquiry still honor the opportunity (aligns with BG 2.40 little progress)."),
            ("Is this week about leaving family life?", "No. It is about protecting inquiry inside family life."),
        ],
        "discovery": [
            "What currently wins your family's evening time?",
            "Where have you heard fear used as a spiritual motivator?",
            "What would a protected 'Must' block look like?",
        ],
        "understanding": [
            "Paraphrase ŚB 11.9.29's teaching meaning.",
            "Name the correct Mṛgāri source range.",
            "What motivation style is forbidden this week?",
        ],
        "application": [
            "Which Optional activity can move this week?",
            "What is our protected inquiry cue?",
            "How will we tell the Mṛgāri story without gore or fear?",
        ],
        "young_story": "A hunter met a kind teacher named Nārada. The hunter learned to be careful and kind — even watching his steps — and his life changed by mercy. Human life is a special chance to learn who we are and to serve Kṛṣṇa. We do not scare friends; we invite them.",
        "young_craft": "Rare-ticket craft: paper ticket 'Human life — use for kindness + hearing.'",
        "young_object": "Time-jar with three labeled cups: Must / Should / Optional.",
        "older_puzzle": "Match: Human form / Priority / Compassion / Opportunity",
        "activity_core": "Time-jar + priority maze",
    },
    "C1-W5": {
        "slug": "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness",
        "title": "The Temporary World and the Search for Permanent Happiness",
        "question": "How can enjoyment become gratitude and service?",
        "conclusion": "Temporary things can be used well but cannot provide permanent fulfillment.",
        "misconception": "Material things and family affection are worthless.",
        "memory": "Temporary joys can be used with gratitude; lasting fulfillment is in Kṛṣṇa.",
        "supports": [
            ("BG 5.22", "https://vedabase.io/en/library/bg/5/22/", "Pleasures born of sense contact are temporary — supporting application, not the locked primary."),
            ("BG 9.27", "https://vedabase.io/en/library/bg/9/27/", "Whatever you do, eat, offer, give — do as offering unto Me."),
        ],
        "analogies": [
            ("Sparkler vs lamp", "Brief flash vs lasting light.", "Lawful joy is not condemned; sparklers can be enjoyed with gratitude."),
            ("Saltwater drink", "Increases thirst rather than finishing it.", "Not a medical claim; pedagogical image for endless hankering."),
            ("Offering plate", "Enjoyment becomes service when offered.", "Not empty ritualism — mood and remembrance matter."),
        ],
        "examples": [
            ("Great souls do not return to temporary misery", "BG 8.15", "https://vedabase.io/en/library/bg/8/15/", "Primary: lasting shelter in the Lord ends the cycle of return to temporary misery — paraphrase carefully."),
            ("Dhruva — mixed motive purified", "ŚB 4.8–4.9", "https://vedabase.io/en/library/sb/4/8/", "Temporary ambition can be redirected toward the Lord; do not promise identical results to children."),
        ],
        "cases": [
            {
                "sit": "After each weekend, the family chases the next purchase for a happiness spike.",
                "wrong": "The next thing will finally satisfy.",
                "principle": "BG 8.15 lasting shelter; BG 5.22 temporary contact pleasure.",
                "source": "https://vedabase.io/en/library/bg/8/15/",
                "response": "Pause with gratitude before buying; name what already blesses the home.",
                "action": "One gratitude sentence before any non-essential purchase this week.",
                "not": "You're materialistic garbage. Never enjoy anything.",
            },
            {
                "sit": "A parent shames a child's joy in a toy.",
                "wrong": "Material joy is sinful; affection is worthless.",
                "principle": "Affection is not worthless; temporary joys can be received with thanks and offering mood (BG 9.27).",
                "source": "https://vedabase.io/en/library/bg/9/27/",
                "response": "Allow lawful joy; add a simple offering/thank-you to Kṛṣṇa.",
                "action": "Toy joy + one sentence: 'Thank You, Kṛṣṇa.'",
                "not": "Throw it away to prove detachment.",
            },
            {
                "sit": "Work always defeats prayer time in family conflicts.",
                "wrong": "Career alone is permanent security.",
                "principle": "Temporary world framing — protect one non-negotiable spiritual cue.",
                "source": "https://vedabase.io/en/library/bg/8/15/",
                "response": "Honor livelihood duties; still protect one small lasting-shelter practice.",
                "action": "Calendar a non-negotiable 5–10 minute cue.",
                "not": "Quit your job tonight or you're not devoted.",
            },
        ],
        "qa": [
            ("Are toys and family hugs bad?", "No. Lawful affection and joy can be received with gratitude; they are temporary, not worthless."),
            ("What is the primary verse this week?", "BG 8.15 — lasting shelter in the Lord; BG 5.22 is support only."),
            ("Does hedonic adaptation prove Kṛṣṇa?", "No. Psychology may illustrate fading contact pleasure; doctrine rests on śāstra."),
            ("How do we offer ordinary acts?", "BG 9.27 mood: remember Kṛṣṇa in doing, eating, giving — start with one act."),
            ("Is renunciation required for kids?", "No. Teach gratitude and offering inside family life."),
        ],
        "discovery": [
            "What temporary joy faded faster than you expected?",
            "Where does our family already say thank you?",
            "What lasting shelter practice is smallest but real?",
        ],
        "understanding": [
            "Contrast temporary contact joy vs lasting shelter in one sentence each.",
            "Name primary vs supporting verses for this week.",
            "What misconception must we refuse about affection?",
        ],
        "application": [
            "What will we offer (food/act/word) this week?",
            "Where will we pause for gratitude before a purchase or treat?",
            "What is our non-negotiable spiritual cue?",
        ],
        "young_story": "A sparkler is bright and short. A lamp can light a whole room for longer. Fun things can be good — we say thank you — but the brightest lasting light is remembering Kṛṣṇa. We do not throw away love; we add gratitude.",
        "young_craft": "Sparkler vs lamp drawing: label Temporary / Lasting.",
        "young_object": "Offering-plate drawing; place a flower or snack card on it.",
        "older_puzzle": "Match: Temporary / Lasting / Gratitude / Offering",
        "activity_core": "Temp-vs-lasting sort + sparkler/lamp craft",
    },
    "C1-W6": {
        "slug": "c1-w6-integration-night-who-am-i-and-how-should-our-family-live",
        "title": "Integration Night: Who Am I, and How Should Our Family Live?",
        "question": "Can our family explain and apply what we learned?",
        "conclusion": "Identity, purpose, and practice must form one coherent family life.",
        "misconception": "Competition or ranking of families.",
        "memory": "We remember who we are and how our family chooses to live.",
        "supports": [
            ("ŚB 1.2.18", "https://vedabase.io/en/library/sb/1/2/18/", "W1 — hearing and service steady devotion."),
            ("BG 2.13", "https://vedabase.io/en/library/bg/2/13/", "W2 — body changes; self continues."),
            ("BG 2.20", "https://vedabase.io/en/library/bg/2/20/", "W3 — eternal soul."),
            ("ŚB 11.9.29", "https://vedabase.io/en/library/sb/11/9/29/", "W4 — rare human opportunity."),
            ("BG 8.15", "https://vedabase.io/en/library/bg/8/15/", "W5 — lasting shelter (locked as W5 primary for review)."),
        ],
        "analogies": [
            ("Necklace of beads", "Weeks link as one life, not isolated events.", "No ranking beads; every family's strand is private."),
            ("Family recipe card", "Ingredients must combine: hearing, identity, opportunity, shelter, practice.", "Not culinary perfectionism."),
            ("Station map", "Retrieval practice strengthens memory of the chain.", "Not exam culture or scoring families."),
        ],
        "examples": [
            ("Cycle 1 chain review", "W1–W5 primaries", "https://vedabase.io/en/library/bg/8/15/", "Integration retrieves prior examples — Naimiṣāraṇya pattern, garment/stages, jīva nature, Mṛgāri mercy (Madhya 24), lasting shelter — without new unproven stories."),
            ("W5 locked as BG 8.15", "BG 8.15", "https://vedabase.io/en/library/bg/8/15/", "When reviewing temporary vs lasting, keep BG 8.15 as the W5 primary (not BG 5.22 as primary)."),
        ],
        "cases": [
            {
                "sit": "A family fears presenting because they think it is a contest.",
                "wrong": "Presentation equals ranking.",
                "principle": "Non-competitive rubric: understanding, application, teamwork, source accuracy — no ranking.",
                "source": "Program project rubric / charter",
                "response": "Offer drawing-only or one-sentence options; celebrate presence.",
                "action": "Choose share format tonight that feels safe.",
                "not": "Score families aloud. Compare presentations.",
            },
            {
                "sit": "One child dominates every share.",
                "wrong": "Loudest equals wisest.",
                "principle": "Team roles — greeting / drawing / sentence.",
                "source": "Pedagogy",
                "response": "Assign roles; invite quieter voices first.",
                "action": "Rotate who speaks the reunification sentence.",
                "not": "Only the talented child may speak.",
            },
            {
                "sit": "Parents want Cycle 2 immediately despite confusion on W2–W3.",
                "wrong": "Speed equals progress.",
                "principle": "Review-before-C2; extend C1 if unclear.",
                "source": "Cycle architecture",
                "response": "Private recommendation to extend review; no public labeling of 'behind.'",
                "action": "Pick one unclear week for a home re-teach.",
                "not": "You're slow. Other families finished.",
            },
        ],
        "qa": [
            ("Do we have to present?", "A share is invited; drawing-only and short formats are honored. No forced performance."),
            ("What is W5's primary in the review chain?", "BG 8.15."),
            ("Will families be ranked?", "No. Ranking is a misconception to block."),
            ("Can we start Cycle 2 next week no matter what?", "Only if the family can explain and apply the chain; otherwise extend C1 review."),
            ("What if we missed a week?", "Retrieve what you can; no shame; use stations to refill gaps."),
        ],
        "discovery": [
            "Which week bead feels strongest in your family?",
            "Which week still feels foggy?",
            "What format of share feels safe tonight?",
        ],
        "understanding": [
            "List the five primary references in order.",
            "State the Cycle 1 conclusion in one sentence.",
            "What must we never do with presentations?",
        ],
        "application": [
            "What one practice will continue for the next 30 days?",
            "Who holds the family recipe card at home?",
            "Do we extend C1 review or proceed after Utsava — decision pending calm discussion?",
        ],
        "young_story": "We collected five shiny beads: Hear, Body/Self, Soul, Rare Chance, Lasting Light. Tonight we string them together and smile — no prizes, no ranking. We remember who we are and how our family chooses to live.",
        "young_craft": "Bead necklace (paper beads) labeled W1–W5.",
        "young_object": "Station map cards for retrieval walk.",
        "older_puzzle": "Match: Integration / Retrieval / Presentation / Review",
        "activity_core": "Retrieval stations + presentation prep",
    },
}


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def load_verse(code: str) -> dict:
    data = yaml.safe_load(VERSE_YAML.read_text(encoding="utf-8"))
    return data[code.lower().replace("-", "_")]


def speaking_script(code: str, w: dict, v: dict) -> str:
    """10–12+ minute speakable prose — not an outline."""
    p_ref, p_url = v["reference"], v["url"]
    meaning = v["kutumba_teaching_meaning"]
    an0, an1, an2 = w["analogies"]
    ex0, ex1 = w["examples"][0], w["examples"][1]
    c0 = w["cases"][0]
    supports = "\n".join(f"- {s[0]} — {s[1]} — {s[2]}" for s in w["supports"])

    openers = {
        "C1-W1": f"""Friends, welcome to Cycle 1, Week 1. Before we discuss techniques, schedules, or crafts, we start with why we are here at all.

KUTUMBA means we are choosing a protected weekly rhythm so our families can grow in Krishna consciousness together — without ranking children, without turning devotion into a contest, and without pretending that one Saturday can replace a life of practice.

Our essential question is: {w['question']}

Please open with me the primary verse for tonight: {p_ref}. The stable link is {p_url}. I will not read a full purport into the room. I will give our KUTUMBA teaching meaning, which is an original paraphrase for classroom use:

"{meaning}"

Say that back in your own words to the person beside you for twenty seconds.

Here is the conclusion I want every facilitator and parent to be able to repeat: {w['conclusion']}

Notice the two halves: protected weekly hearing *and* home practice. If we only attend, we become event tourists. If we only stay home and never associate, we lose the friendship that steadies hearing. ŚB 1.2.17–19 around our primary point the same direction: hearing cleanses, passion and ignorance can recede, and steady devotion can become established — always as śāstra teaching, never as a laboratory claim.

Let me make this concrete with a garden. A protected garden plot that is watered weekly grows roots even when flowers are not visible yet. That is pedagogy for regularity. The limit is important: watering does not guarantee a bloom on our preferred calendar. We refuse to promise spiritual fireworks.

Now a household picture. Imagine a family that never misses 2:00–4:00 and yet has zero weekday cue. The tempting conclusion is: "Attendance equals growth." We reject that. The compassionate response is gratitude for showing up, then one five-minute if-then plan after dinner.

We also refuse the opposite error: "Community is dangerous; alone is always holier." Hearing in association is part of Bhāgavata service. Awkwardness is not sin.

Finally, we refuse ranking. Comparing children's seriousness in the hallway is not leadership.

Supporting readings you may skim this week:
{supports}

Devotional pattern: the Naimiṣāraṇya assembly shows sages gathering to inquire about duty ({ex0[2]}). We borrow the *pattern* of protected hearing — we do not claim our room equals that forest.

In a moment we will split into tracks. Parents stay to discuss cues and misconceptions. Younger and older friends practice the memory line with teachers. We reunite at 3:10 to hear one sentence per family: "This week we will…"

Memory line: {w['memory']}
""",
        "C1-W2": f"""Welcome back. Tonight's title is simple and easy to misuse: {w['title']}.

Essential question: {w['question']}

Primary reading: {p_ref} — {p_url}

KUTUMBA teaching meaning: "{meaning}"

Conclusion: {w['conclusion']}

If you remember only one boundary, remember this: psychology insights and family photos can help us teach respectfully. They do **not** prove the soul. Our doctrine rests on śāstra.

Walk through the verse with me in plain language. In one body we all recognize childhood, youth, and later age. The sober person is not bewildered when the embodied self continues beyond one body's stage — including, the verse indicates, the passage to another body. We will not dump cosmology on K–2 tonight. We will teach dignity: the body changes; the conscious person continues; speech about bodies should be kind.

Analogy one — changing garments (supported by BG 2.22): clothes change, wearer continues. Limit: clothes are chosen; bodies are not costumes for mockery; bodies deserve care.

Analogy two — life-stage photos: same name across pictures. Limit: photos are pedagogy, not proof.

Analogy three — driver and vehicle: operator is not the metal. Limit: refuse harsh dualism. Maintain the vehicle for service.

Scriptural frame: Arjuna's opening grief is tangled with bodily relationships ({ex0[2]}). Kṛṣṇa's teaching begins by clarifying the embodied self. Paraphrase only.

Household case: sibling appearance teasing at snack. Mistaken conclusion: "just a joke." Principle: respectful speech. Action: repair language and make a seven-day pledge.

We are not teaching body neglect. Sleep, food, medicine, and hygiene remain acts of responsibility. We are teaching identity clarity.

Supporting readings:
{supports}

Tracks next. Memory line: {w['memory']}
""",
        "C1-W3": f"""Tonight we go one step deeper than last week. Week 2 said the body changes and the self continues. Week 3 asks what kind of self that is.

Essential question: {w['question']}

Primary: {p_ref} — {p_url}

Teaching meaning: "{meaning}"

Conclusion: {w['conclusion']}

Please hear the is/is-not map clearly. The jīva is eternal, conscious, and individual. The jīva is a minute fragmental part related to Kṛṣṇa in service (BG 15.7). The jīva is **not** the temporary body. The jīva is **not** the Supreme Personality of Godhead.

If a child says "I am God," we smile and correct: "You are a dear spark meant to serve, not the whole sun."

Sun-and-ray, spark-from-fire, house-and-resident — all are pedagogy with limits. Rays are not the sun. Residents still care for the house.

Narrative support: Jaḍa Bharata's teaching context in ŚB 5.10 reminds us bodily status labels do not define the soul ({ex0[2]}). Keep retellings gentle and nonviolent.

Science boundary for this week is explicit: **N/A — no empirical claim is used to prove or disprove ātman.** Laboratory methods measure bodies and behavior. If asked for science proof of the soul, say so out loud and defer doctrine to śāstra.

Case: neglecting hygiene "because we are soul." That is body contempt, not spirituality. Restore care as service readiness.

Supporting readings:
{supports}

Memory: {w['memory']}
""",
        "C1-W4": f"""Essential question: {w['question']}

Primary locked verse: {p_ref} — {p_url}

Teaching meaning: "{meaning}"

Conclusion: {w['conclusion']}

This week can slide into fear if we are careless. We will not scare children with death pressure. We will speak of rare opportunity, mercy, and protected time.

Supporting narrative — correct source discipline: Nārada and Mṛgāri is **Caitanya-caritāmṛta Madhya 24.229–282** ({ex0[2]}). It is **not** ŚB 6.x and **not** ŚB 4.8. Useful anchors: intro 24.229, name 24.242, bow 24.255–256, careful steps 24.270–272, conclusion 24.278–282. Paraphrase only; no gore.

The hunter's turn toward careful life illustrates mercy transforming human opportunity — it does not authorize terror tactics at home.

Analogies: rare ticket, crossroads, seed season — each teaches urgency-without-panic. Limits: no species contempt; no guaranteed timetable; no shaming.

BG 2.40 support: a little sincere progress is not lost — this helps families who only have five minutes.

Case: screens consume the only quiet block. Action: one Must jar slot before Optional screens.

Case: parent uses death scare. Stop it. Rewrite the ask as invitation.

Supporting readings:
{supports}

Memory: {w['memory']}
""",
        "C1-W5": f"""Essential question: {w['question']}

Primary (locked): {p_ref} — {p_url}

Teaching meaning: "{meaning}"

Conclusion: {w['conclusion']}

Pause with me on the phrase “temporary world of misery” in the teaching meaning. We are not training children to despise birthdays, toys, or parents’ hugs. We are training families to stop asking temporary things to do a permanent job. That distinction keeps tonight compassionate and honest.

Hold two truths at once. First: temporary contact joys fade and cannot be final shelter. Second: family affection, lawful fun, and beautiful objects are **not** worthless. Shame is not renunciation.

BG 5.22 supports the temporary nature of sense-contact pleasure. BG 9.27 shows how ordinary acts can turn toward offering. Neither replaces BG 8.15 as primary.

Sparkler vs lamp: enjoy the sparkler; remember the lamp. Saltwater image: hankering can increase with acquisition — pedagogical, not medical. Offering plate: thank You, Kṛṣṇa.

Devotional example: Dhruva's arc shows mixed motives can be purified toward the Lord ({ex1[2]}) — do not promise identical results.

Case: purchase chase. Add gratitude pause. Case: shaming a child's toy. Allow joy; add thanks. Case: work forever defeats prayer. Protect one cue without quitting livelihood theatrics.

If someone cites "science proves detachment," correct: gratitude research may support well-being habits; it does not prove Kṛṣṇa or the metaphysics of BG 8.15.

Supporting readings:
{supports}

Memory: {w['memory']}
""",
        "C1-W6": f"""Tonight is integration night — not a new ontology dump and not a contest.

Essential question: {w['question']}

Primary frame: Cycle 1 review chain, with W5 locked as **BG 8.15**.
Review links: ŚB 1.2.18 · BG 2.13 · BG 2.20 · ŚB 11.9.29 · BG 8.15
Teaching meaning: "{meaning}"

Conclusion: {w['conclusion']}

If your family missed a week, you are still welcome. Retrieval is mercy, not a quiz show. We will refill gaps without announcing who is “behind.” The goal is one coherent family life: hearing, identity clarity, soul nature, protected human opportunity, and lasting shelter in the Lord.

We will walk five stations or five beads:

1) Hearing steadies devotion (ŚB 1.2.18).
2) Body changes; self continues (BG 2.13).
3) Eternal individual soul — not God Himself (BG 2.20 / BG 15.7).
4) Human life is rare opportunity — mercy, not fear; Mṛgāri from Madhya 24 (ŚB 11.9.29).
5) Lasting shelter in the Lord (BG 8.15).

Analogies: necklace, recipe card, station map — all refuse ranking and exam culture.

Shares tonight are invitational. Drawing-only is success. One sentence is success. Rubric lenses are understanding, application, teamwork, and source accuracy — never placement.

If a family is still confused on identity weeks, recommend extending C1 review privately. Speed is not progress.

Supporting review set:
{supports}

Memory: {w['memory']}
""",
    }

    body = openers[code]
    c1, c2 = w["cases"][1], w["cases"][2]
    qa_spoken = "\n\n".join(
        f"If someone asks, “{q}” — answer: {a}" for q, a in w["qa"]
    )
    disc_spoken = "\n".join(f"- {q}" for q in w["discovery"])
    expand = f"""
I am going to teach the analogies slowly, with limits in the same breath, because an analogy without a limit becomes a new false doctrine.

First: **{an0[0]}**. {an0[1]} Limit: {an0[2]}

Second: **{an1[0]}**. {an1[1]} Limit: {an1[2]}

Third: **{an2[0]}**. {an2[1]} Limit: {an2[2]}

Hold those as teaching tools, not as replacements for {p_ref}.

Now two sourced examples, paraphrased only.

Example A — {ex0[0]} ({ex0[1]}). {ex0[3]} Link: {ex0[2]}

Example B — {ex1[0]} ({ex1[1]}). {ex1[3]} Link: {ex1[2]}

Next I will walk all three household cases out loud so you can copy the pattern at home. Please listen for seven fields every time: situation, mistaken conclusion, principle, source, compassionate response, action, and what not to say.

Case 1.
Situation: {c0['sit']}
Mistaken conclusion: {c0['wrong']}
Principle and source: {c0['principle']} ({c0['source']})
Compassionate response: {c0['response']}
Family action: {c0['action']}
What not to say: {c0['not']}

Case 2.
Situation: {c1['sit']}
Mistaken conclusion: {c1['wrong']}
Principle and source: {c1['principle']} ({c1['source']})
Compassionate response: {c1['response']}
Family action: {c1['action']}
What not to say: {c1['not']}

Case 3.
Situation: {c2['sit']}
Mistaken conclusion: {c2['wrong']}
Principle and source: {c2['principle']} ({c2['source']})
Compassionate response: {c2['response']}
Family action: {c2['action']}
What not to say: {c2['not']}

I will now ask the room three discovery questions. You may answer in a whisper to a partner:
{disc_spoken}

Understanding check — please be ready to say in one sentence: {w['conclusion']}. Name the primary: {p_ref}. Name what we are not teaching tonight: ranking, speculation, and the misconception “{w['misconception']}”.

Application — before you leave the shared opening, decide silently: time + place for home practice; who starts if others are tired; and the minimum version if the week is hard. Five minutes counts. Memory line plus one kind action counts.

Let me demonstrate a minimum home practice out loud so nobody leaves confused. Tonight after dinner, or at the same chair each evening, someone says the memory line once: “{w['memory']}.” Then one family member paraphrases {p_ref} in a single sentence. Then one gratitude or service act — thanking someone, offering water, putting shoes away as kindness, or a short prayer. If the house is chaotic, keep only the memory line and one kind action. That still honors tonight’s conclusion: {w['conclusion']}

When we reunite at 3:10, I will not score families. I will ask for one sentence: “This week we will…” Drawings count. Whispered parent sentences count. Loud brilliance is not holier than quiet sincerity.

Likely questions you may hear from adults — rehearse these answers with me:

{qa_spoken}

A short word on boundaries. We do not invent quotations. We do not dump full purports into Git or into the room. We do not diagnose families medically or spiritually in public. We do not guarantee initiation, advancement, or certification. We do not claim human, temple, CPO, or publication approval. Science may help habits; it does not prove ātman or replace śāstra.

Operational covenant aloud: Saturday 2:00–4:00; snack and water only; parents onsite; private struggles stay private; no false approval labels.

Recite with me before tracks:
- Essential question: {w['question']}
- Conclusion: {w['conclusion']}
- Memory line: {w['memory']}
- Misconception to block: {w['misconception']}
- Primary: {p_ref} — {p_url}

Parents: your job in the parent circle is not to perform brilliance. It is to leave with a cue, a minimum version, and a kinder sentence than the one you might have used last week. Younger and older teachers will deepen practice in age bands. We reunite at 3:10 for one family sentence: “This week we will…”

That is the heart of tonight's teaching. Let us practice it, not merely admire it.
"""
    return (body + expand).strip()


def facilitator_md(code: str, w: dict, v: dict) -> str:
    script = speaking_script(code, w, v)
    an_lines = "\n".join(
        f"### {i}. {a[0]}\n- **Teaches:** {a[1]}\n- **Limit (say out loud):** {a[2]}\n"
        for i, a in enumerate(w["analogies"], 1)
    )
    ex_lines = "\n".join(
        f"### {i}. {e[0]}\n- **Provenance:** {e[1]}\n- **URL:** {e[2]}\n- **Classroom paraphrase use:** {e[3]}\n"
        for i, e in enumerate(w["examples"], 1)
    )
    case_lines = []
    for i, c in enumerate(w["cases"], 1):
        case_lines.append(
            f"""### Constructed case {i}

| Field | Content |
|---|---|
| Situation | {c['sit']} |
| Mistaken conclusion | {c['wrong']} |
| Principle | {c['principle']} |
| Source | {c['source']} |
| Compassionate response | {c['response']} |
| Family action | {c['action']} |
| What not to say | {c['not']} |
"""
        )
    qa_lines = "\n".join(f"| {q} | {a} |" for q, a in w["qa"])
    disc = "\n".join(f"{i}. {q}" for i, q in enumerate(w["discovery"], 1))
    und = "\n".join(f"{i}. {q}" for i, q in enumerate(w["understanding"], 1))
    app = "\n".join(f"{i}. {q}" for i, q in enumerate(w["application"], 1))
    supports = "\n".join(f"- {s[0]} — {s[1]} — {s[2]}" for s in w["supports"])
    next_w = NEXT[code]

    return f"""# {code} Main Facilitator Guide — Saturday 2:00–4:00

**KUTUMBA • Families Growing in Krishna Consciousness**  
**Program Director: Swapnil Patil**  
**Status:** Internal founding-cohort teaching material — human/temple review EXTERNAL_OPEN  
**Controlling guide:** This V12 file is authoritative for Saturday delivery. Core teaching is inlined below.

## Two-minute summary

{w['conclusion']}  
Primary: **{v['reference']}** ({v['url']}).  
Essential question: {w['question']}

## Essential question

{w['question']}

## 15-minute night-before prep

1. Open {v['url']} and reread Devanāgarī, IAST, and KUTUMBA teaching meaning below.
2. Rehearse the **speaking script** section aloud once (aim for clear 10–15 minute delivery with pauses).
3. Pack younger + older materials and memory cards.
4. Review misconception to block: **{w['misconception']}**
5. Confirm snack/water only (no weekly meal); parents onsite; privacy reminder card visible.
6. For C1-W4: verify Mṛgāri source cards say **CC Madhya 24.229–282** (not SB 6.x / SB 4.8).

## 60-minute deep prep

1. Read the inlined analogies, examples, and three cases in this guide until you can teach them without notes.
2. Mark which discovery / understanding / application questions you will actually ask.
3. Choose one analogy and one case as your "must teach" pair; keep the others ready for Q&A.
4. Walk the room: parent circle, younger zone, older zone, reunification seats.
5. Pre-write the home-practice minimum version on a card (5 minutes counts).
6. Review deferral line: laboratory methods measure bodies/behavior; ātman/bhakti claims rest on śāstra — no false science proof.
7. Skim `project/CYCLE-CONTRIBUTION.md` for this week's artifact layer.
8. Optional enrichment only (not a substitute for this guide): research folder files.

## Exact primary and supporting readings

### Primary (locked)

- **Reference:** {v['reference']}
- **URL:** {v['url']}
- **Devanāgarī:** {v['devanagari']}
- **IAST:** {v['iast']}
- **KUTUMBA teaching meaning:** {v['kutumba_teaching_meaning']}
- **Rights:** {v['rights_status']}

### Supporting readings

{supports}

## Teaching map with exact Saturday 2:00–4:00 time cues

| Time | Block | Facilitator focus |
|---|---|---|
| 1:50–2:00 | Arrival | Welcome; privacy; parents onsite; materials check |
| 2:00–2:10 | Opening mantras | Keep simple; invitation not volume contest |
| 2:10–2:30 | Shared opening / Prem-kī-Kathā + verse | Deliver opening of speaking script; state memory line |
| 2:30–3:10 | Parallel tracks | Parent circle / younger / older — see track transition |
| 3:10–3:30 | Reunification / bhakti lab | Family synthesis sentence; no ranking |
| 3:30–3:40 | Snack + water only | No weekly meal service |
| 3:40–3:55 | Saṅkalpa / project / Q&A | Home cue + project artifact + likely questions |
| 3:55–4:00 | Closing | Next-week title only; no early ontology |

## 10–20 minute speaking script (deliverable prose)

> Facilitation note: Speak naturally. Pause for the 20-second pair share where indicated. Do not replace this with "see research."

{script}

## Analogies with limits (inline — teach from here)

{an_lines}

## Scriptural and devotional examples (inline paraphrase)

{ex_lines}

## Three constructed household cases (inline)

{''.join(case_lines)}

## Discovery questions

{disc}

## Understanding questions

{und}

## Application questions

{app}

## Five likely Q&A

| Question | Source-based direction |
|---|---|
{qa_lines}

## Misconceptions to block

- {w['misconception']}
- Confusing analogy with scripture quotation
- Importing next week's full ontology early
- Ranking families or children
- Claiming science proves or disproves ātman / bhakti metaphysics
- False human, temple, CPO, or publication approval labels

## What not to speculate about

- Invented quotations, purport dumps, or unverified lecture lines
- Private medical or spiritual diagnoses of families
- Guarantees of advancement, initiation, or certification
- Graphic retellings (especially Mṛgāri) or fear-based death pressure on children
- For W4: any claim that Mṛgāri is located in SB 6.x or SB 4.8

## Track transition (say at ~2:28)

> Parents remain in the parent circle. Younger friends go with [younger teacher]. Older students go with [older teacher]. We reunite at 3:10. We do not rank groups.

## Family reunification synthesis (3:10–3:30)

Invite one sentence per family tied to the essential question:  
> "This week we will…"  
Accept drawings or whispered parent sentences for shy children. No scoreboard.

## Project contribution

Advance the cumulative project **Who Am I, and How Should Our Family Live?** using `project/CYCLE-CONTRIBUTION.md`.  
This week layer must connect to {v['reference']} and tonight's conclusion. Store artifacts for Week 6. Non-competitive.

## Home practice (5–15 minutes)

1. Say the memory line once: *{w['memory']}*
2. Paraphrase {v['reference']} in one family sentence.
3. Do one gratitude or service act.
4. Minimum version if exhausted: memory line + one kind action only.

## Next-week preview

Name only: **{next_w}**.  
Do not teach next week's ontology in depth tonight.

## Do not claim

Human/temple/CPO approval; publication readiness; BBT ownership of KUTUMBA teaching meanings; science proving ātman; ranking results; guaranteed spiritual outcomes.
"""


def research_files(code: str, w: dict, v: dict) -> None:
    base = WEEKLY / w["slug"] / "research"
    supports = "\n".join(
        f"| {s[0]} | {s[1]} | {s[2]} | Prefer paraphrase; no purport dump |" for s in w["supports"]
    )
    write(
        base / "SCRIPTURAL-EXAMPLES.md",
        f"""# {code} Scriptural Examples

## Primary anchor (locked)

| Reference | URL | Teaching paraphrase | Limitation |
|---|---|---|---|
| {v['reference']} | {v['url']} | {v['kutumba_teaching_meaning']} | Exact BBT English translation not copied; KUTUMBA teaching meaning is original paraphrase |

## Supporting primary references

| Reference | URL | Teaching use | Limitation |
|---|---|---|---|
{supports}

## Expanded classroom notes

1. Open the primary URL before teaching and keep it visible to adults.
2. State the teaching meaning in plain English; invite one paraphrase from the room.
3. Name what this week does **not** teach (see facilitator misconceptions).
4. For narrative supports, stay inside the cited URL range — especially Mṛgāri = CC Madhya 24.229–282 only.
5. Do not invent verse wording or purport claims.

## Cross-check

Controlling delivery text lives in `teacher/MAIN-FACILITATOR-GUIDE-V12.md` (inline). This file is enrichment + traceability.
""",
    )

    drows = "\n".join(
        f"| {t} | {s} | {u} | {use} |" for t, s, u, use in [(e[0], e[1], e[2], e[3]) for e in w["examples"]]
    )
    write(
        base / "DEVOTIONAL-AND-HISTORICAL-EXAMPLES.md",
        f"""# {code} Devotional and Historical Examples

## Selected examples (traceable)

| Example | Provenance | URL | Classroom use / limitation |
|---|---|---|---|
{drows}

## Policy

- Paraphrase only; no full purport dumps; no invented deity dialogue.
- Bhakta-mālā and unverified anecdote chains are not used as controlling proof.
- Supplementary examples never replace the locked primary verse.
- W4 Mṛgāri must remain CC Madhya 24.229–282 (not SB 6.x / SB 4.8).
""",
    )

    cases = []
    for i, c in enumerate(w["cases"], 1):
        cases.append(
            f"""### Constructed case {i} — fictional / anonymized

- **Situation:** {c['sit']}
- **Tempting mistaken conclusion:** {c['wrong']}
- **Relevant principle / source:** {c['principle']} — {c['source']}
- **Compassionate response:** {c['response']}
- **Family action:** {c['action']}
- **What not to say:** {c['not']}
- **Age adaptation:** Younger — one sentence + one action; Older — name the mistaken conclusion explicitly; Adults — connect to home cue.
"""
        )
    write(base / "CASE-STUDIES.md", f"# {code} Case Studies\n\n" + "\n".join(cases))

    arows = "\n".join(
        f"| {a[0]} | {a[1]} | pedagogy / śāstra-aligned | {a[2]} | younger object lesson | adult discussion |"
        for a in w["analogies"]
    )
    write(
        base / "ANALOGIES-AND-LIMITS.md",
        f"""# {code} Analogies and Limits

| Analogy | Teaching value | Source status | Failure point / limit | Younger use | Older/adult use |
|---|---|---|---|---|---|
{arows}

## Rule

Label every analogy as pedagogy. Never present analogy as if it were a śāstra quotation. Facilitators must speak the limit in the same breath as the image.

## Inline requirement

The controlling facilitator guide already inlines these analogies — do not teach from a "see research" stub.
""",
    )

    # Science
    sci = {
        "C1-W1": """## Empirical aids for habit design (not doctrinal proof)

### Implementation Intentions and Goal Achievement (2006)
- **Authors:** Gollwitzer, P. M., & Sheeran, P.
- **DOI:** https://doi.org/10.1016/S0065-2601(06)38002-1
- **Finding used:** If-then plans increase follow-through on intended actions.
- **Limitation:** Does not prove devotion or heart-cleansing; helps design saṅkalpa cues only.
- **Application:** "After dinner dishes, we say the memory line."

### Family Routines and Rituals (2002)
- **Authors:** Fiese, B. H., et al.
- **DOI:** https://doi.org/10.1111/1467-8624.t01-1-00525
- **Finding used:** Predictable family rituals associate with child well-being and belonging.
- **Limitation:** Does not prove spiritual efficacy of Bhāgavata hearing.
- **Application:** Protected Saturday + tiny home ritual language.
""",
        "C1-W2": """## Empirical aids for respectful speech pedagogy (not soul proof)

### Body Image and Self-Concept in Childhood/Adolescence (2011)
- **Authors:** Smolak, L.
- **DOI:** https://doi.org/10.1146/annurev-clinpsy-032210-104544
- **Finding used:** Body-image concerns can shape speech and peer comparison.
- **Limitation:** Never claim psychology proves ātman; use only for respectful-language pedagogy.
- **Application:** Anti-teasing pledges; dignity language.
""",
        "C1-W3": """## Explicit decision — N/A for metaphysical proof

**N/A — no empirical claim is used this week to prove or disprove the soul (ātman).**

**Reason:** Laboratory and behavioral methods measure bodies, brains, and behavior. BG 2.20 teachings about the eternal jīva are śāstra claims. Mixing domains creates false proof or false disproof.

**Parent deferral line:**
> Laboratory methods measure bodies and behavior. Our teaching about the soul comes from śāstra. I will not claim science proves or disproves ātman.
""",
        "C1-W4": """## Empirical aids for priority / goal protection (not rarity proof)

### Goal Setting and Task Performance (Locke & Latham tradition)
- **Representative DOI:** https://doi.org/10.1037/0003-066X.57.9.705
- **Finding used:** Clear priorities and protected goals improve follow-through.
- **Limitation:** Supports time-protection pedagogy only; not proof of human-form rarity or transmigration.
- **Application:** Must / Should / Optional time-jar.
""",
        "C1-W5": """## Empirical aids illustrating fading contact pleasure / gratitude (not ontology proof)

### Hedonic adaptation tradition (Brickman & Campbell, 1971)
- **Record:** https://psycnet.apa.org/record/1972-24270-001
- **Finding used:** People adapt to rising material gains; lasting satisfaction is elusive from acquisition alone.
- **Limitation:** Illustrates temporary contact pleasure; does not prove BG 8.15 ontology.

### Counting Blessings Versus Burdens (Emmons & McCullough, 2003)
- **DOI:** https://doi.org/10.1037/0022-3514.84.2.377
- **Finding used:** Gratitude practices associate with well-being.
- **Limitation:** Supports gratitude application; not proof of Kṛṣṇa.
""",
        "C1-W6": """## Empirical aids for retrieval practice (not doctrinal proof)

### Test-Enhanced Learning (Roediger & Karpicke, 2006)
- **DOI:** https://doi.org/10.1111/j.1529-1006.2006.00027.x
- **Finding used:** Retrieval practice strengthens long-term retention.
- **Limitation:** Supports review stations; not doctrinal proof of the Cycle 1 metaphysical chain.
- **Application:** Non-exam retrieval stations; no ranking.
""",
    }[code]
    write(base / "SCIENCE-AND-APPLICATION.md", f"# {code} Science and Application\n\n{sci}\n")


def younger_older_activities(code: str, w: dict, v: dict) -> None:
    tdir = WEEKLY / w["slug"] / "teacher"
    adir = WEEKLY / w["slug"] / "activities"
    write(
        tdir / "YOUNGER-TEACHER-GUIDE.md",
        f"""# {code} Younger Teacher Guide (K–2) — 40-minute executable lesson

**Track window:** approx. 2:30–3:10 (40 minutes). Parents onsite elsewhere; reunite at 3:10.

## Objective

Children can say and show: **{w['memory']}**

## Exact memory phrase

> {w['memory']}

## Teacher background (2 minutes, before children arrive)

- Primary: {v['reference']} — {v['kutumba_teaching_meaning']}
- Block misconception: {w['misconception']}
- Do not teach adult debates or fear tactics.
- Snack later with whole group only; water okay if needed.

## Minute-by-minute lesson

| Minutes | Block | What you do |
|---|---|---|
| 0–3 | Welcome + seated circle | Soft voice; "kind words only"; show visual of the week |
| 3–8 | Memory phrase echo | You say half; they finish; two joyful rounds max |
| 8–16 | Story script | Read/tell the story below; ask one wonder question |
| 16–23 | Movement game | Freeze and Remember (rules below) |
| 23–33 | Hands-on + craft | Object lesson + take-home card |
| 33–37 | Coloring | `visuals/V12/line-art-younger.svg` |
| 37–40 | Cleanup + door handoff | Tell parent the memory phrase + home cue |

## Age-appropriate story script (paraphrase boundary)

{w['young_story']}

Rules: no invented deity dialogue; no frightening detail; stop at the moral: {w['conclusion']}

## Three wonder questions

1. What did you hear that was new?
2. Who can we serve with kindness this week?
3. When could our family practice for five minutes?

## Movement game (5–7 min) — Freeze and Remember — {code}

1. Children walk gently in a circle (or march in place).
2. When you say "Freeze!", they stop.
3. You say the first half of the memory phrase; they finish it.
4. Two rounds only; then sit. Redirect: "Feet on the floor. Kind words only."

## Hands-on object lesson (8–10 min)

**Object:** {w['young_object']}  
Children handle/see the object and finish: "This reminds me that…"  
Secure ending: point back to the memory phrase.

## Craft (8–10 min)

{w['young_craft']}

Fold or card format: outside picture; inside memory phrase.

## Coloring / line-art

Color `../visuals/V12/line-art-younger.svg`. Title the page with {code}.

## Sanskrit exposure (optional, 1 min)

Softly invite one name: **Kṛṣṇa** or **Hare** — never forced volume.

## Behavior redirects

- "Feet on the floor."
- "Kind words only."
- "That toy rests for now."
- Quiet reset in visible space if needed (parents onsite).

## Backup low-prep (if craft fails)

Sit in a circle; pass a soft object; each child says one kind word; end with memory phrase echo.

## Extension

Helper role: hand out crayons / collect papers.

## Materials

Printed line art; crayons; memory cards; soft toss object; card stock; tape; week object listed above.

## Cleanup / handoff

3 minutes cleanup. At door: tell parent the memory phrase and the home cue question: {w['question']}

## Home-practice explanation to parents

"Please say this phrase once at home and do one kind action. Five minutes is enough."
""",
    )

    terms = {
        "C1-W1": [("Hearing", "Regular Bhāgavata reception"), ("Saṅkalpa", "Specific practice intention"), ("Charter", "KUTUMBA purposes/boundaries"), ("Association", "Learning with devotees")],
        "C1-W2": [("Body", "Changes through stages"), ("Self", "Continues as conscious person"), ("Analogy", "Pedagogy with limits"), ("Respect", "Speech about every body")],
        "C1-W3": [("Jīva", "Eternal individual soul"), ("Fragmental part", "Related to Kṛṣṇa, not equal as Supreme"), ("Eternal", "Not created or destroyed"), ("Service", "Natural relationship")],
        "C1-W4": [("Human form", "Rare opportunity"), ("Priority", "What we protect in time"), ("Compassion", "Mercy without contempt"), ("Opportunity", "Chance for inquiry")],
        "C1-W5": [("Temporary", "Has beginning and end"), ("Lasting", "Shelter in Kṛṣṇa"), ("Gratitude", "Thanks before enjoyment"), ("Offering", "Turning acts toward Kṛṣṇa")],
        "C1-W6": [("Integration", "Weeks form one life"), ("Retrieval", "Remembering on purpose"), ("Presentation", "Share without ranking"), ("Review", "Extend C1 if unclear")],
    }[code]
    matching = "\n".join(f"| {a} | {b} |" for a, b in terms)
    answers = "\n".join(f"{i}. {a}" for i, (a, b) in enumerate(terms, 1))
    scrambled = "\n".join(f"{i}. {b} → ________" for i, (_, b) in enumerate(terms, 1))

    write(
        tdir / "OLDER-TEACHER-GUIDE.md",
        f"""# {code} Older Teacher Guide (Grades 4–5) — full track lesson

**Track window:** approx. 2:30–3:10 (40 minutes).

## Objective

Students explain **{w['conclusion']}** using {v['reference']}.

## Essential question

{w['question']}

## Minute-by-minute

| Minutes | Block | What you do |
|---|---|---|
| 0–5 | Hook | Read essential question; students write a one-line first answer |
| 5–15 | Text observation | Open {v['url']}; complete observation task below |
| 15–22 | Diagram | Label week concept diagram / board map |
| 22–30 | Scenario cards | Pairs work Case 1–3 from facilitator guide / activity pack |
| 30–36 | Worksheet / matching | `activities/OLDER-ACTIVITY-PACK.md` |
| 36–40 | Reflection + reunification sentence | Prepare one sentence for 3:10 share |

## Text-observation task (10 min)

Open {v['url']}. Students write:

1. Who is speaking / what is the setting (if known)?
2. One phrase that signals continuity, eternity, rarity, or lasting shelter (week-appropriate).
3. One sentence paraphrase in their own words (not a long dump).
4. One thing this verse does **not** say.

Target paraphrase: {v['kutumba_teaching_meaning']}

## Diagram task

Complete labels on `visuals/V12/` concept materials or board version. Week-specific conclusion arrow must appear.

## Scenario cards

Use the three constructed cases (inline in `MAIN-FACILITATOR-GUIDE-V12.md`). In pairs: mistaken conclusion + compassionate response + better family action.

## Worksheet + puzzle

See `activities/OLDER-ACTIVITY-PACK.md`; grade with `activities/OLDER-ANSWER-KEY.md`.

## Project contribution

Advance `project/CYCLE-CONTRIBUTION.md` layer for {code}.

## Reflection prompt

"Where did I confuse analogy with scripture today?"

## Extension

Prepare reunification share sentence answering: {w['question']}

## Boundaries

- Misconception to block: {w['misconception']}
- Science may illustrate habits only — never prove metaphysics.
- No ranking; no forced disclosure of private family struggles.
""",
    )

    write(
        adir / "YOUNGER-ACTIVITY-PACK.md",
        f"""# {code} Younger Activity Pack (K–2)

## Objective

Show and say: **{w['memory']}**

## 1. Core circle activity — {w['activity_core']} (5–8 min)

1. Teacher demonstrates once with the week object: {w['young_object']}
2. Children participate; every child gets one turn or partner turn.
3. End with memory phrase echo (two rounds max).

## 2. Story boundary

Use the story in `teacher/YOUNGER-TEACHER-GUIDE.md`.  
Paraphrase only. No invented deity dialogue. No graphic violence. No fear tactics.

## 3. Movement — Freeze and Remember — {code}

Walk/march → Freeze → finish memory phrase → sit.

## 4. Craft / object (actual)

{w['young_craft']}

Take-home: outside picture; inside memory phrase.

## 5. Memory card

- Front: simple icon for {code}
- Back: {w['memory']}

## 6. Printable coloring

Color `../visuals/V12/line-art-younger.svg` (US Letter). Prompt: color the scene that shows *this* week's idea.

## 7. Take-home family cue

Ask at home: {w['question']} (one sentence each)

## Backup low-prep

Pass soft object; each child says one kind word; echo memory phrase.

## Materials

Printed line art, crayons, card stock, soft toss object, tape, week object listed above.
""",
    )

    write(
        adir / "OLDER-ACTIVITY-PACK.md",
        f"""# {code} Older Activity Pack (Grades 4–5)

## A. Concept worksheet (write answers)

1. State this week's conclusion in one sentence.
2. Write the primary scripture reference: _______________
3. Paraphrase it in your words (no copying long text).
4. Name one misconception to avoid.
5. Write one family action for the next 7 days.
6. Essential question: {w['question']} — answer in 2–3 sentences.

## B. Matching puzzle

Match term → meaning:

| Term | Meaning |
|---|---|
{matching}

Print as two cut columns and match, **or** write letters.

## C. Scramble (optional)

{scrambled}

## D. Scenario response card

Pick Constructed case 1 from the facilitator guide (inline cases).  
Write: mistaken conclusion / better response / one sentence you would say at home.

## E. Diagram task

On the week diagram, label every node and draw one arrow that shows this week's primary conclusion: {w['conclusion']}

## F. Source observation

Open {v['url']}. Write a faithful paraphrase of {v['reference']} (not a long dump).

## G. Project / poster component

Produce one artifact for `project/CYCLE-CONTRIBUTION.md` ({code} layer).

## H. Optional reflection

Circle one: I confused analogy with scripture / I stayed in week scope / I need review.

## Low-prep backup

Pair-share essential question for 3 minutes; each writes one sentence for reunification.
""",
    )

    write(
        adir / "OLDER-ANSWER-KEY.md",
        f"""# {code} Older Answer Key

## Worksheet — secure answers

1. {w['conclusion']}
2. {v['reference']}
3. Accept any faithful paraphrase of: {v['kutumba_teaching_meaning']}
4. {w['misconception']} (or close equivalent)
5. Any concrete 5–15 minute cue tied to the week
6. Answers should connect identity/practice without ranking

## Matching key

{matching}

## Scramble key

{answers}

## Scenario grading

Secure = names mistaken conclusion + compassionate action + no shame language + no fear tactics.

## Do not accept

- Invented verse numbers
- "Science proves the soul"
- Mṛgāri cited from SB 6.x / SB 4.8 (must be CC Madhya 24.229–282)
- Importing another week's full ontology as if it were this week's only point
- Ranking language in presentations (especially W6)
""",
    )


def main() -> None:
    counts = {}
    for code, w in WEEKS.items():
        v = load_verse(code)
        path = WEEKLY / w["slug"] / "teacher" / "MAIN-FACILITATOR-GUIDE-V12.md"
        text = facilitator_md(code, w, v)
        # Guard forbidden shells
        if "Use week research ANALOGIES-AND-LIMITS" in text:
            raise SystemExit(f"Forbidden phrase slipped into {code}")
        write(path, text)
        words = len(text.split())
        counts[code] = (path, words)
        research_files(code, w, v)
        younger_older_activities(code, w, v)
        print(f"{code}: {words} words -> {path.relative_to(REPO)}")
    print("DONE", len(counts), "weeks")


if __name__ == "__main__":
    main()
