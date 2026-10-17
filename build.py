import os
EMAIL="wvihandu@gmail.com"; GH="https://github.com/vihandu-wan"; LI="https://www.linkedin.com/in/vihandu-wanniarachchi-964b32240"
NAV=[("Home","",""),("Projects","projects/","projects"),("About","about/","about"),("Oriax","oriax/","oriax")]
def page(path,title,desc,body,key=""):
    d=path.count("/"); r="../"*d
    nav="".join(f'<a href="{r}{h}"{" aria-current=page" if k==key else ""}>{n}</a>' for n,h,k in NAV)
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/style.css"></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap bar"><a class="brand" href="{r}">Vihandu Wanniarachchi</a><nav aria-label="Main">{nav}</nav></div></header>
<main id="main">{body.replace("{R}",r)}</main>
<footer><div class="wrap foot"><p>© 2026 Vihandu Wanniarachchi</p><p><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{GH}">GitHub</a> · <a href="{LI}">LinkedIn</a></p></div></footer>
</body></html>'''
    os.makedirs(os.path.dirname(path) or ".",exist_ok=True); open(path,"w").write(html)
def vid(n,cap,cls=""):
    return f'<figure class="media {cls}"><video controls preload="none" playsinline poster="{{R}}assets/img/{n}.jpg"><source src="{{R}}assets/video/{n}.mp4" type="video/mp4"></video><figcaption>{cap}</figcaption></figure>'
CTA=f'''<section class="wrap sec cta"><h2>Let’s discuss a problem</h2><p>Have a process that is difficult to manage, repetitive, or poorly supported by your existing software? I’d be happy to understand it and explore whether a software solution makes sense.</p>
<p><a class="btn" href="mailto:{EMAIL}">Email {EMAIL}</a></p></section>'''

# HOME
page("index.html","Vihandu Wanniarachchi — Software Engineer & Builder","I build practical software products and business systems.",f'''
<section class="wrap hero"><div class="hero-text"><h1>I build practical software products and business systems.</h1>
<p class="lead">I take a problem, work out how it really operates, and engineer something people can use. My work covers software engineering, backend systems, automation and AI-driven applications.</p>
<p>Through my projects and Oriax Technologies, I turn technical ideas into reliable solutions for real problems.</p>
<p class="actions"><a class="btn" href="{{R}}projects/">Explore my work</a><a class="btn ghost" href="mailto:{EMAIL}">Discuss a project</a></p></div>
<img class="portrait" src="{{R}}assets/img/vihandu.jpg" width="413" height="531" alt="Portrait of Vihandu Wanniarachchi"></section>

<section class="wrap sec"><h2>Selected work</h2><div class="list">
<article class="item"><div><h3>EveryRupee</h3><p class="status live">Active</p></div><div><p>A WhatsApp-based personal finance tracker that makes recording and reviewing expenses as easy as sending a message.</p><p class="meta">Backend engineering, API integrations, transaction processing, data management.</p><p><a href="{{R}}projects/everyrupee/">View case study</a> · <a href="{GH}">View source code</a></p></div></article>
<article class="item"><div><h3>Cold Chain Shipment Risk Predictor</h3><p class="status">Prototype built</p></div><div><p>A tool that scores a single shipment for cold chain risk from its carrier, packaging, route, product and handling details.</p><p class="meta">Data modelling, risk scoring, application development.</p><p><a href="{{R}}projects/#coldchain">View project</a></p></div></article>
<article class="item"><div><h3>Library website and digitalisation</h3><p class="status live">Delivered</p></div><div><p>A multilingual public website for Bandaranayake Public Library, Homagama, in English, Sinhala and Tamil, covering membership, services, events and announcements.</p><p class="meta">Information architecture, multilingual content, web development.</p><p><a href="{{R}}projects/#library">View project</a></p></div></article>
<article class="item"><div><h3>Tourism agency website</h3><p class="status live">Delivered</p></div><div><p>A website presenting a tourism agency’s services and making information easy for prospective customers to find.</p><p class="meta">Responsive design, web development, business requirements.</p><p><a href="{{R}}projects/#tourism">View project</a></p></div></article>
<article class="item"><div><h3>Research: post-harvest loss in Sri Lanka</h3><p class="status">Published</p></div><div><p>I studied why fruit and vegetables are lost in Sri Lanka’s traditional supply chain, through stakeholder discussions and a review of existing research. I proposed a cluster-based information-sharing system and an incremental way to implement it.</p><p><a href="https://lnkd.in/gGSwxPHp">Read the full paper</a></p></div></article>
</div></section>

<section class="wrap sec"><h2>What I build</h2><div class="cols">
<div><h3>Software products</h3><p>Web applications, backend services, APIs and data-driven tools.</p></div>
<div><h3>Business systems and automation</h3><p>Solutions that connect workflows, reduce repetitive work and make operational information easier to reach.</p></div>
<div><h3>AI-enabled applications</h3><p>Practical uses of AI and data processing, where they give a clear benefit.</p></div></div></section>

<section class="wrap sec"><h2>How I work</h2><ol class="steps">
<li><b>Understand the problem.</b> Learn how the current process works and what needs to improve.</li>
<li><b>Design the solution.</b> Define requirements, architecture, constraints and the simplest useful implementation.</li>
<li><b>Build and validate.</b> Implement the system, test its behaviour and demonstrate how it works.</li>
<li><b>Improve through evidence.</b> Use feedback, testing and real-world results to choose the next improvement.</li></ol></section>
{CTA}''')

# PROJECTS
page("projects/index.html","Projects — Vihandu Wanniarachchi","Software projects with status, contribution, technologies and demos.",f'''
<section class="wrap sec first"><h1>Projects</h1><p class="lead">Each project lists its status and my contribution. Recordings are of the working software.</p></section>

<section class="wrap sec proj" id="everyrupee"><div class="ph"><h2>EveryRupee</h2><p class="status live">Active</p></div>
<div class="pgrid"><div><p>Track expenses by chatting on WhatsApp. Send “Add 400 to bus”, get a confirmation, and ask for a monthly summary by category.</p>
<dl><dt>My contribution</dt><dd>Design and build of the backend, WhatsApp integration, transaction processing and data storage.</dd>
<dt>Focus</dt><dd>Backend engineering, API integrations, transaction processing, data management.</dd></dl>
<p><a class="btn" href="everyrupee/">Read the case study</a> <a class="btn ghost" href="{GH}">Source code</a></p></div>
{vid("everyrupee","Recorded demo: adding an expense, receiving a confirmation, and requesting a July summary.","tall")}</div></section>

<section class="wrap sec proj" id="coldchain"><div class="ph"><h2>Cold Chain Shipment Risk Predictor</h2><p class="status">Prototype built</p></div>
<div class="pgrid"><div><p>A shipment-scoring tool for cold chain logistics. You enter a shipment’s product category, packaging, carrier, route, transfer points, weight, value and cold chain requirements, and the tool returns a risk assessment for that shipment.</p>
<dl><dt>My contribution</dt><dd>Problem framing, input design, risk-scoring logic and the interactive interface.</dd>
<dt>Focus</dt><dd>Data modelling, risk scoring, application development.</dd></dl></div>
{vid("coldchain","Recorded demo: the “Score a single shipment” form.")}</div></section>

<section class="wrap sec proj" id="library"><div class="ph"><h2>Bandaranayake Public Library, Homagama</h2><p class="status live">Delivered</p></div>
<div class="pgrid"><div><p>A public website for the library in English, Sinhala and Tamil. It covers services, events, announcements, and a membership page with a downloadable application form.</p>
<dl><dt>My contribution</dt><dd>Site structure, multilingual content layout and front-end development.</dd>
<dt>Focus</dt><dd>Information management, multilingual web development, accessibility of public information.</dd></dl>
<p><a href="https://homagamabandaranayakalibrary.com">Visit the website</a></p></div>
{vid("web-b","Recorded walkthrough: language switcher and the membership page.")}</div>
{vid("web-a","Recorded: the live site found through search, with the library’s public listing.","wide")}</section>

<section class="wrap sec proj" id="tourism"><div class="ph"><h2>Tourism agency website</h2><p class="status live">Delivered</p></div>
<div class="pgrid"><div><p>A responsive website presenting a tourism agency’s services so prospective customers can find information quickly.</p>
<dl><dt>My contribution</dt><dd>Requirements, design and web development.</dd><dt>Focus</dt><dd>Web development, responsive design, business requirements.</dd></dl></div></div></section>

<section class="wrap sec proj" id="research"><div class="ph"><h2>Research: post-harvest loss</h2><p class="status">Published</p></div>
<div class="pgrid"><div><p>Why does produce get lost between farm and market in Sri Lanka? I spoke with stakeholders and reviewed existing research, then proposed a cluster-based information-sharing system and an incremental implementation framework. I’d welcome feedback on the approach.</p>
<p><a href="https://lnkd.in/gGSwxPHp">Read the full paper</a></p></div></div></section>
{CTA}''',"projects")

# CASE STUDY
svg='''<svg viewBox="0 0 760 120" role="img" aria-labelledby="dt dd" class="diagram"><title id="dt">EveryRupee message flow</title><desc id="dd">A WhatsApp message goes through the WhatsApp Business API to the backend, which parses it, records the transaction in the database, and replies to the user.</desc>
<g font-family="IBM Plex Sans,sans-serif" font-size="14" text-anchor="middle" fill="#e8e6e1"><g fill="none" stroke="#6fb3b8" stroke-width="1.5"><rect x="4" y="30" width="130" height="60" rx="4"/><rect x="164" y="30" width="130" height="60" rx="4"/><rect x="324" y="30" width="130" height="60" rx="4"/><rect x="484" y="30" width="130" height="60" rx="4"/><rect x="644" y="30" width="112" height="60" rx="4"/></g>
<text x="69" y="65">User on WhatsApp</text><text x="229" y="65">WhatsApp API</text><text x="389" y="65">Backend: parse</text><text x="549" y="65">Database</text><text x="700" y="65">Reply</text></g>
<g stroke="#a3a7ad" stroke-width="1.5"><path d="M134 60h30M294 60h30M454 60h30M614 60h30"/></g></svg>'''
page("projects/everyrupee/index.html","EveryRupee case study — Vihandu Wanniarachchi","How EveryRupee, a WhatsApp expense tracker, works.",f'''
<article class="wrap sec first prose"><p><a href="../">← All projects</a></p><h1>EveryRupee</h1><p class="status live">Active</p>
<p class="lead">A WhatsApp-based tool for recording and reviewing personal expenses.</p>
<h2>The problem</h2><p>Most people don’t keep an expense record because opening a separate app and filling in a form is too much effort for a Rs.400 bus fare. Chat is already open all day. EveryRupee brings expense tracking to the place people already are.</p>
<h2>What it does</h2><ul><li>Records an expense from a plain message such as “Add 400 to bus”.</li><li>Confirms what it recorded, so mistakes are visible straight away.</li><li>Produces a monthly summary with the total and a breakdown by category.</li><li>Lets the user undo the last entry.</li></ul>
<h2>Architecture</h2>{svg}<p>A message reaches the backend through the WhatsApp Business API. The backend interprets the text, stores the transaction, and sends back a confirmation or summary.</p>
<h2>Implementation</h2><p>The core work is in the backend: receiving messages reliably, turning free text into an amount and a category, storing transactions, and aggregating them for summaries. Keeping the commands short keeps the parsing predictable.</p>
<h2>Evidence</h2>{vid("everyrupee","Recording from a phone: add an expense, see the confirmation, request the July summary (Rs.407 total: bus Rs.400, domain Rs.7), then undo.","tall")}
<p>The recording shows the working product end to end on WhatsApp. <a href="{GH}">Source code on GitHub</a>.</p></article>
{CTA}''',"projects")

# ABOUT
page("about/index.html","About — Vihandu Wanniarachchi","Computer Science undergraduate and software builder.",f'''
<section class="wrap sec first pgrid"><div class="prose"><h1>About</h1>
<p class="lead">I’m a Computer Science undergraduate who builds working software and cares about the problem it solves.</p>
<p>I’m interested in backend systems, automation and applying AI where it genuinely helps. I like understanding how a process runs today before designing anything, then building the simplest version that works.</p>
<h2>How I approach building</h2><ul><li>Start from the real operational problem, not the technology.</li><li>Keep the first version small and demonstrable.</li><li>Explain engineering decisions, and show results with real recordings and tests.</li></ul>
<h2>Elsewhere</h2><p>I run Oriax Technologies to deliver software for businesses. I also research supply chain problems in Sri Lanka, including post-harvest loss.</p>
<p><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{GH}">GitHub</a> · <a href="{LI}">LinkedIn</a></p></div>
<img class="portrait" src="{{R}}assets/img/vihandu.jpg" width="413" height="531" alt="Vihandu Wanniarachchi in a suit and tie" loading="lazy"></section>''',"about")

# ORIAX
page("oriax/index.html","Oriax Technologies — Vihandu Wanniarachchi","Software and business systems for organisations with real operational problems.",f'''
<section class="wrap sec first prose"><h1>Oriax Technologies</h1>
<p class="lead">Practical software and business systems for organisations whose current tools don’t fit the way they work.</p>
<h2>Current offerings</h2><ul><li><b>Websites.</b> Responsive, multilingual public websites, such as the Bandaranayake Public Library site.</li><li><b>Business systems.</b> Tools that organise information and support day-to-day workflows.</li><li><b>Automation.</b> Chat-based and backend automation that removes repetitive work, such as EveryRupee on WhatsApp.</li></ul>
<h2>Delivery approach</h2><ol class="steps"><li><b>Discuss.</b> We talk through the process and what hurts today.</li><li><b>Scope.</b> I propose the simplest useful solution, with clear requirements.</li><li><b>Build.</b> You see working software early.</li><li><b>Review.</b> We test it together and decide what to improve next.</li></ol>
<h2>Business enquiries</h2><p>Describe the problem in a few lines and I’ll reply with whether and how software can help.</p><p><a class="btn" href="mailto:{EMAIL}">Email {EMAIL}</a></p></section>''',"oriax")
