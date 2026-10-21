"""Generates the static Sunstone site pages with a shared header and footer."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EMAIL = "contact@sunstonedatasystems.com"
SITE = "https://www.sunstonedatasystems.com"

ICONS = {
    "cabling": '<svg viewBox="0 0 24 24"><rect x="6" y="3" width="12" height="10" rx="1.5"/><path d="M9 3v3M12 3v3M15 3v3M12 13v8"/></svg>',
    "fiber": '<svg viewBox="0 0 24 24"><path d="M2 8c4 0 4 4 8 4s4-4 8-4h4"/><path d="M2 16c4 0 4-4 8-4s4 4 8 4h4"/><circle cx="2" cy="8" r=".6"/></svg>',
    "rack": '<svg viewBox="0 0 24 24"><rect x="4" y="2.5" width="16" height="19" rx="1.5"/><path d="M4 8h16M4 13.5h16M7 5.3h.01M7 10.8h.01M7 16.5h.01M11 5.3h6M11 10.8h6M11 16.5h6"/></svg>',
    "camera": '<svg viewBox="0 0 24 24"><path d="M3 6h13l3 4-3 4H3z"/><circle cx="9" cy="10" r="2"/><path d="M8 14v4H4M19 10h2"/></svg>',
    "access": '<svg viewBox="0 0 24 24"><rect x="5" y="2.5" width="14" height="19" rx="2"/><circle cx="12" cy="9" r="2.6"/><path d="M9 16h6"/></svg>',
    "wireless": '<svg viewBox="0 0 24 24"><path d="M2.5 9a14 14 0 0 1 19 0M5.5 12.5a9.5 9.5 0 0 1 13 0M8.6 15.8a5 5 0 0 1 6.8 0"/><circle cx="12" cy="19" r="1"/></svg>',
}
CHECK = '<span class="check"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'

SERVICES = [
    ("structured-cabling", "cabling", "Structured Cabling",
     "Cat-5e, Cat-6, and Cat-6A horizontal cabling, terminated, labeled, and certified with Fluke test reports.",
     "Every building system now rides on the horizontal cabling, from unit data to access points, cameras, and building controls. We pull, dress, terminate, and label it to the drawings, then certify every link and hand you the reports.",
     ["Cat-5e, Cat-6, and Cat-6A horizontal drops", "Jacks, faceplates, and patch panel termination", "Cable support, J-hooks, and firestop at penetrations", "Labeling to the drawing schedule", "Fluke certification of every link"],
     ["Conduit, sleeves, and backboxes by others", "Line voltage power", "Active network equipment", "Material, unless the bid is furnish-and-install"]),
    ("fiber-optic", "fiber", "Fiber Optic Installation and Splicing",
     "Single-mode backbone and fiber-to-the-unit, fusion splicing, splice closures, and OTDR and OLTS testing.",
     "Fiber now runs well past the MDF, out to every unit, every remote camera pole, and every gate too far for copper. We install single-mode feeder and drop cable, build splice closures, fusion-splice at the head end, the zone, and the unit, and test every fiber with OTDR plus OLTS loss testing. You get a test report for every strand.",
     ["OS2 feeder and drop pulls", "Handhole and pathway pass-through", "Zone splice closures", "Fusion splicing and splice-on connectors", "High-density MDF fiber panels", "OTDR and OLTS testing with reports"],
     ["Conduit, handholes, and trenching", "ONTs and ISP equipment", "Material, unless the bid is furnish-and-install"]),
    ("mdf-idf", "rack", "MDF / IDF Buildout",
     "Racks, ladder rack, patch panels, fiber enclosures, surge protection, and bonding, dressed and labeled.",
     "The network room is where inspectors, owners, and service providers judge the whole job. We build it to read cleanly: racks anchored and bonded, ladder rack and cable management set, copper and fiber terminated, and everything labeled to the drawings.",
     ["Two- and four-post racks and cabinets", "Ladder rack and vertical and horizontal management", "Copper patch panels and fiber enclosures", "Telecom bonding and grounding", "Surge protection at the entrance", "Labeling and rack elevations for closeout"],
     ["Room construction, HVAC, and dedicated power", "Backboard and TMGB if by electrical", "UPS and active equipment unless specified"]),
    ("security-cameras", "camera", "Security Cameras and Pole Systems",
     "Interior, exterior, and multi-sensor cameras, including remote pole sites with hardened switches.",
     "We mount, cable, and aim cameras to the security drawings, from interior domes to multi-sensor units covering parking and entries. For remote coverage we build out pole sites with NEMA enclosures, hardened switches, and fiber or copper back to the head end.",
     ["Interior and exterior dome cameras", "Multi-sensor and PTZ cameras", "Pole-mounted NEMA enclosures with hardened switches", "Camera cabling and terminations", "Aiming and field-of-view checkout with the owner"],
     ["Poles, bases, and foundations", "VMS licensing and server programming unless specified", "Power to remote poles"]),
    ("access-control", "access", "Access Control and Intercom",
     "Card and long-range readers, electric strikes, REX and door position, panels, and gate checkout.",
     "Access control is where low-voltage meets doors, hardware, and the fire alarm, and that's where projects slip. We coordinate with the door hardware and electrical trades, install the field devices and panels, and check out every opening with the owner.",
     ["Card and long-range vehicle readers", "Electric strikes and maglock connections", "REX and door position switches", "Control panels and power supplies", "Intercom and tele-entry stations", "Door and gate checkout"],
     ["Door hardware and frame prep", "Gate operators", "Fire alarm interface wiring by the FA contractor", "Software and credential programming unless specified"]),
    ("wireless", "wireless", "Wireless Access Points",
     "Access point installation for clubhouses, amenity spaces, common areas, and offices.",
     "We mount, cable, and label access points to the wireless drawings or a provided heat map, so the network team can light them up without chasing locations.",
     ["Ceiling and wall AP mounting", "AP cabling and termination", "Labeling to the AP schedule", "Exterior and weatherproof enclosures"],
     ["Wireless design and surveys", "Controllers, licensing, and configuration", "Access points, unless furnished by Sunstone"]),
]

PHOTOS = {
    "structured-cabling": [("cat6-termination", "Technician terminating Cat-6 cable bundles on a patch panel"), ("cable-testing", "Technician certifying a copper link with a handheld cable tester")],
    "fiber-optic": [("fiber-splicing", "Fusion splicing single-mode fiber beside a splice closure"), ("fiber-pulling", "Crew pulling fiber from a reel into a handhole on a multifamily site")],
    "mdf-idf": [("mdf-racks", "MDF racks with dressed Cat-6 patch panels, fiber enclosures, and overhead cable tray")],
    "security-cameras": [("pole-camera", "Technician installing a multi-sensor camera and NEMA enclosure on a pole")],
    "access-control": [("access-control", "Technician wiring a card reader at an amenity building entrance")],
    "wireless": [("wireless-ap", "Ceiling-mounted wireless access point in a clubhouse lounge")],
}


def img(name, alt, cls="", eager=False):
    return f'<img class="{cls}" src="/assets/img/photos/{name}.jpg" alt="{alt}" width="1200" height="805"{"" if eager else " loading=\"lazy\""} decoding="async">'


NAV = [("services.html", "Services"), ("index.html#markets", "Markets"), ("how-we-bid.html", "How We Bid"), ("about.html", "About")]


def header(active):
    links = "".join(
        f'<li><a href="/{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a></li>' for h, t in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <nav class="container nav" aria-label="Main">
    <a class="brand" href="/" aria-label="Sunstone Data Systems home"><img src="/assets/img/sunstone-logo-horizontal.svg" alt="Sunstone Data Systems" width="230" height="46"></a>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links"><span></span><span></span><span></span></button>
    <ul class="nav-links" id="nav-links">{links}<li><a class="btn btn--primary" href="/request-a-bid.html">Request a Bid</a></li></ul>
  </nav>
</header>'''


FOOTER = f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <img src="/assets/img/sunstone-logo-horizontal-white.svg" alt="Sunstone Data Systems" width="240" height="48">
        <p>Low-voltage infrastructure for commercial and multifamily construction. Fiber, structured cabling, security cameras, and access control.</p>
        <p>A wholly owned subsidiary of Southroad Holding Inc., Dallas, Texas.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{"".join(f'<li><a href="/services.html#{s[0]}">{s[2]}</a></li>' for s in SERVICES)}</ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Serving Dallas&ndash;Fort Worth and Texas</li>
          <li><a href="/request-a-bid.html">Request a Bid</a></li>
          <li><a href="/how-we-bid.html">How We Bid</a></li>
          <li><a href="/about.html">About</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> Sunstone Data Systems, a wholly owned subsidiary of Southroad Holding Inc., Dallas, Texas. All rights reserved.</span>
      <span>Photos are representative. <a href="/privacy.html">Privacy</a></span>
    </div>
  </div>
</footer>
<script src="/assets/js/main.js" defer></script>'''


def page(filename, title, desc, body, active=None):
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{'' if filename == 'index.html' else filename}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}/{'' if filename == 'index.html' else filename}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta name="theme-color" content="#061430">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/styles.css">
</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
'''
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(html)


def cta(title="Have a project out for bid?", text="Send the drawing set and bid date. An estimator will review the scope and confirm what we need to price it."):
    return f'''<section class="section"><div class="container"><div class="cta-band">
  <div><h2>{title}</h2><p>{text}</p></div>
  <a class="btn btn--primary" href="/request-a-bid.html">Request a Bid</a>
</div></div></section>'''


# ---------- Home ----------
service_cards = "".join(
    f'<a class="card card--photo" href="/services.html#{s[0]}">{img(*PHOTOS[s[0]][0], cls="card-img")}<div class="card-body"><div class="icon">{ICONS[s[1]]}</div><h3>{s[2]}</h3><p>{s[3]}</p><span class="more">Learn more &rarr;</span></div></a>'
    for s in SERVICES)

home = f'''<section class="hero hero--photo">
  <div class="container">
    <div>
      <span class="eyebrow" style="color:var(--cyan-400)">Low-voltage subcontractor</span>
      <h1>Low-voltage infrastructure for <span class="accent">large commercial and multifamily</span> builds.</h1>
      <p class="lead">Fiber, structured cabling, security cameras, and access control under one contract. Send us the drawings. We'll return a line-item bid tied to every sheet.</p>
      <div class="hero-actions">
        <a class="btn btn--primary" href="/request-a-bid.html">Request a Bid</a>
        <a class="btn btn--ghost" href="/services.html">Our Services</a>
      </div>
      <ul class="hero-tags"><li>Fiber-to-the-unit</li><li>Cat-6 / 6A</li><li>Cameras &amp; poles</li><li>Access control</li><li>Fluke &amp; OTDR tested</li></ul>
    </div>
    <div class="bid-card" aria-label="Illustration of a Sunstone line-item bid">
      <header><strong>Line-Item Bid</strong><span class="tag">Sample format</span></header>
      <table>
        <thead><tr><th>Sheet</th><th>Scope item</th><th class="num">Qty</th><th class="num hide-sm">Unit</th></tr></thead>
        <tbody>
          <tr><td class="sheet">T-201</td><td>Cat-6A horizontal drop</td><td class="num">&mdash;</td><td class="num hide-sm">EA</td></tr>
          <tr><td class="sheet">T-501</td><td>OS2 fiber drop, splice-on</td><td class="num">&mdash;</td><td class="num hide-sm">EA</td></tr>
          <tr><td class="sheet">T-601</td><td>Zone splice closure</td><td class="num">&mdash;</td><td class="num hide-sm">EA</td></tr>
          <tr><td class="sheet">TY-101</td><td>Multi-sensor camera</td><td class="num">&mdash;</td><td class="num hide-sm">EA</td></tr>
          <tr><td class="sheet">TY-301</td><td>Access-controlled opening</td><td class="num">&mdash;</td><td class="num hide-sm">EA</td></tr>
        </tbody>
      </table>
      <footer><span>Exclusions listed</span><span>RFIs flagged</span><span>Test reports at closeout</span></footer>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">One sub, whole scope</span>
      <h2>One contract for the whole low-voltage scope.</h2>
      <p class="lead">GCs and developers shouldn't have to coordinate four trades for one system. Sunstone takes the full low-voltage package, from the MDF to the last unit drop, gate reader, and pole camera. We staff it, schedule it, test it, and hand over the documentation.</p>
      <a class="btn btn--outline" href="/how-we-bid.html">See how we bid</a>
    </div>
    <ul class="scope-list">
      <li><span>MDF</span>Racks, fiber panels, bonding, surge</li>
      <li><span>FIBER</span>Feeder, zone splices, fiber-to-the-unit</li>
      <li><span>CAT-6</span>Horizontal cabling, certified and labeled</li>
      <li><span>CCTV</span>Interior, exterior, and pole cameras</li>
      <li><span>ACS</span>Readers, strikes, panels, gates, intercom</li>
      <li><span>WAP</span>Access points in amenity and common areas</li>
    </ul>
  </div>
</section>

<section class="section section--soft" id="services">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Services</span>
      <h2>The systems that connect and secure a building.</h2>
      <p class="lead">Bid and delivered as one coordinated low-voltage scope, or as individual packages.</p>
    </div>
    <div class="grid grid-3">{service_cards}</div>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Built for GCs</span>
      <h2>Built for the people who award the contract.</h2>
    </div>
    <div class="grid grid-4">
      <div class="card">{CHECK}<h3>Bids tied to the drawings</h3><p>Every line item cites the sheet it came from, so you can check our quantities.</p></div>
      <div class="card">{CHECK}<h3>Exclusions in writing</h3><p>What's in, what's out, and who furnishes what, stated before you sign.</p></div>
      <div class="card">{CHECK}<h3>RFIs before mobilization</h3><p>We flag drawing conflicts during takeoff, not on site.</p></div>
      <div class="card">{CHECK}<h3>Documentation at closeout</h3><p>Test reports, labeling, and as-builts come with the job.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">How we work</span>
      <h2>From IFC set to closeout package.</h2>
    </div>
    <div class="steps">
      <div class="step"><h3>Drawing review and takeoff</h3><p>We read the full IFC set and count every device, drop, and splice.</p></div>
      <div class="step"><h3>Line-item bid</h3><p>Hours, rates, assumptions, exclusions, and RFIs, all in one document.</p></div>
      <div class="step"><h3>Install</h3><p>Trained crews, coordinated with your schedule and the other trades.</p></div>
      <div class="step"><h3>Test and close out</h3><p>Certification, punch list, and as-builts.</p></div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">In the field</span>
      <h2>What the work looks like.</h2>
      <p class="lead">From the reel at the handhole to the last certified link in the MDF.</p>
    </div>
    <div class="gallery">
      <figure class="g-wide">{img("fiber-pulling", "Crew pulling fiber from a reel into a handhole on a multifamily site")}<figcaption>Fiber pulling: feeder and drops through handholes and conduit</figcaption></figure>
      <figure>{img("fiber-splicing", "Fusion splicing single-mode fiber beside a splice closure")}<figcaption>Fusion splicing and splice closures</figcaption></figure>
      <figure>{img("cat6-termination", "Technician terminating Cat-6 cable bundles on a patch panel")}<figcaption>Cat-5e / 6 / 6A termination</figcaption></figure>
      <figure>{img("cable-testing", "Technician certifying a copper link with a handheld cable tester")}<figcaption>Certification testing on every link</figcaption></figure>
      <figure>{img("mdf-racks", "MDF racks with dressed Cat-6 patch panels, fiber enclosures, and overhead cable tray")}<figcaption>MDF / IDF racks, patch panels, and fiber enclosures</figcaption></figure>
    </div>
  </div>
</section>

<section class="section" id="markets">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Markets</span>
      <h2>Where we work.</h2>
      <p class="lead">Serving general contractors, developers, owners' reps, and low-voltage contractors across Dallas&ndash;Fort Worth and Texas.</p>
    </div>
    <div class="grid grid-2">
      <div class="market"><span class="label">Multifamily</span><h3>Multifamily and Senior Living</h3><p>Fiber-to-the-unit, clubhouse networks, gate access control, and pool and amenity security across multi-building sites.</p></div>
      <div class="market"><span class="label">Commercial</span><h3>Commercial and Office</h3><p>Tenant buildouts, backbone and horizontal cabling, and MDF and IDF rooms built to inspect cleanly.</p></div>
    </div>
  </div>
</section>

{cta()}'''
page("index.html", "Sunstone Data Systems | Low-Voltage Contractor for Commercial & Multifamily",
     "Sunstone Data Systems installs fiber, structured cabling, security cameras, and access control for large commercial and multifamily construction. Send your drawings for a line-item bid.",
     home, "index.html")

# ---------- Services ----------
subnav = "".join(f'<a href="#{s[0]}">{s[2]}</a>' for s in SERVICES)
blocks = "".join(f'''<article class="service" id="{s[0]}">
  <aside><div class="icon">{ICONS[s[1]]}</div><h2>{s[2]}</h2></aside>
  <div>
    <div class="service-photos n{len(PHOTOS[s[0]])}">{"".join(img(n, a) for n, a in PHOTOS[s[0]])}</div>
    <p class="lead">{s[4]}</p>
    <div class="service-cols">
      <div><h4>What's included</h4><ul>{"".join(f"<li>{i}</li>" for i in s[5])}</ul></div>
      <div class="excl"><h4>Typically excluded</h4><ul>{"".join(f"<li>{i}</li>" for i in s[6])}</ul></div>
    </div>
  </div>
</article>''' for s in SERVICES)
services = f'''<section class="page-hero"><div class="container">
  <span class="eyebrow">Services</span>
  <h1>Low-voltage systems for commercial and multifamily construction.</h1>
  <p class="lead">Sunstone installs the systems that connect and secure a building: data, fiber, cameras, and access control. We bid and deliver them as one coordinated low-voltage scope, or as individual packages.</p>
  <nav class="subnav" aria-label="Services">{subnav}</nav>
</div></section>
<section class="section"><div class="container">{blocks}</div></section>
{cta("Need one scope priced, or all of them?", "Tell us which systems are in your package. We'll price them as one coordinated scope or as separate line items.")}'''
page("services.html", "Services | Sunstone Data Systems",
     "Structured cabling, fiber optic installation and splicing, MDF/IDF buildout, security cameras, access control, and wireless for commercial and multifamily projects.",
     services, "services.html")

# ---------- How We Bid ----------
bid = f'''<section class="page-hero"><div class="container">
  <span class="eyebrow">How we bid</span>
  <h1>Most bid disputes start with a vague number. Ours aren't vague.</h1>
  <p class="lead">We build every bid from the full drawing set, line by line, so you can check our quantities against the sheets and compare us fairly.</p>
</div></section>
<section class="section"><div class="container anatomy">
  <div>
    <span class="eyebrow">What you get</span>
    <h2>Every Sunstone bid includes:</h2>
    <ol>
      <li><strong>Summary by scope</strong><span>Hours and dollars for each system, so you can carry or cut scopes cleanly.</span></li>
      <li><strong>Rates and markups</strong><span>Labor classes, contingency, and overhead stated openly.</span></li>
      <li><strong>Line-item detail</strong><span>Quantity, unit, hours per unit, and the drawing sheet behind it.</span></li>
      <li><strong>Inclusions and exclusions</strong><span>Who furnishes material, conduit, power, programming, and lifts.</span></li>
      <li><strong>Assumptions</strong><span>Where drawings aren't to scale or counts conflict, we say what we carried.</span></li>
      <li><strong>RFIs</strong><span>Questions for the design team, listed and ready to send.</span></li>
    </ol>
  </div>
  <div>
    <div class="bid-card" style="transform:none">
      <header><strong>Bid Summary</strong><span class="tag">Sample format</span></header>
      <table>
        <thead><tr><th>Scope</th><th class="num">Hours</th><th class="num">Sheets</th></tr></thead>
        <tbody>
          <tr><td>MDF / IDF buildout</td><td class="num">&mdash;</td><td class="num sheet">T-401</td></tr>
          <tr><td>Fiber feeder and splicing</td><td class="num">&mdash;</td><td class="num sheet">T-501&ndash;503</td></tr>
          <tr><td>Fiber-to-the-unit drops</td><td class="num">&mdash;</td><td class="num sheet">T-201&ndash;212</td></tr>
          <tr><td>Security cameras</td><td class="num">&mdash;</td><td class="num sheet">TY-101</td></tr>
          <tr><td>Access control</td><td class="num">&mdash;</td><td class="num sheet">TY-301</td></tr>
          <tr><td>Testing and closeout</td><td class="num">&mdash;</td><td class="num sheet">All</td></tr>
        </tbody>
      </table>
      <footer><span>Exclusions</span><span>Assumptions</span><span>RFIs</span><span>Alternates</span></footer>
    </div>
    <p class="form-note">Illustration of our bid format. A full anonymized sample is available on request.</p>
  </div>
</div></section>
<section class="section section--soft"><div class="container">
  <div class="section-head"><span class="eyebrow">What we need</span><h2>Send us what you have.</h2>
  <p class="lead">A full IFC set gets the most accurate bid, but we can work from schematics for budgeting. The more of these you include, the faster we turn it around.</p></div>
  <div class="grid grid-3">
    <div class="card"><h3>Drawings</h3><p>Technology (T-series), security (TY-series), and site plans, plus any electrical sheets showing pathways.</p></div>
    <div class="card"><h3>Specifications</h3><p>Division 27 and 28 specs, approved manufacturers, and testing requirements.</p></div>
    <div class="card"><h3>Bid details</h3><p>Bid due date, schedule, labor-only or furnish-and-install, and who furnishes conduit and power.</p></div>
  </div>
</div></section>
{cta()}'''
page("how-we-bid.html", "How We Bid | Sunstone Data Systems",
     "Line-item low-voltage bids tied to drawing sheets, with rates, exclusions, assumptions, and RFIs stated up front.",
     bid, "how-we-bid.html")

# ---------- About ----------
about = f'''<section class="page-hero"><div class="container">
  <span class="eyebrow">About</span>
  <h1>A low-voltage contractor that talks like your estimator.</h1>
  <p class="lead">Sunstone Data Systems is a low-voltage contractor serving Dallas&ndash;Fort Worth and Texas. We take on the full communications and security scope for commercial and multifamily projects and manage it from takeoff to closeout.</p>
</div></section>
<section class="section"><div class="container split">
  <div>
    <span class="eyebrow">How we're set up</span>
    <h2>Subcontractor to the GC. Accountable for the whole scope.</h2>
    <p>We contract with the general contractor or developer for the low-voltage package, then staff the job with trained installation crews under our supervision. One point of contact for the estimate, the schedule, the installation, and the closeout documents.</p>
    <p>Sunstone Data Systems is a wholly owned subsidiary of <strong>Southroad Holding Inc.</strong>, headquartered in Dallas, Texas.</p>
    <p>We work best on large, multi-building projects where the low-voltage scope is broad: fiber backbone, unit cabling, network rooms, cameras, and access control all on the same site.</p>
  </div>
  <div class="facts">
    <div class="fact"><h3>Licensing</h3><p>Texas low-voltage licensing details available on request.</p></div>
    <div class="fact"><h3>Insurance</h3><p>Certificates of insurance provided with every bid.</p></div>
    <div class="fact"><h3>Testing</h3><p>Fluke copper certification, OTDR and OLTS fiber testing, with reports at closeout.</p></div>
    <div class="fact"><h3>Safety</h3><p>Site-specific safety coordination with every GC.</p></div>
  </div>
</div></section>
<section class="section section--soft"><div class="container">
  <div class="section-head"><span class="eyebrow">Who we work with</span><h2>Built for the people who award the contract.</h2></div>
  <div class="grid grid-4">
    <div class="card"><h3>General contractors</h3><p>Multifamily, senior living, affordable housing, and commercial builds.</p></div>
    <div class="card"><h3>Developers and owners' reps</h3><p>One accountable sub for the whole low-voltage package.</p></div>
    <div class="card"><h3>LV and ISP contractors</h3><p>Field labor and splicing crews for your awarded work.</p></div>
    <div class="card"><h3>Facility managers</h3><p>Adds, moves, and upgrades on commercial campuses.</p></div>
  </div>
</div></section>
{cta()}'''
page("about.html", "About | Sunstone Data Systems",
     "Sunstone Data Systems, a wholly owned subsidiary of Southroad Holding Inc. of Dallas, Texas, is a low-voltage subcontractor for commercial and multifamily construction.",
     about, "about.html")

# ---------- Request a Bid ----------
scopes = ["Structured cabling", "Fiber optic", "MDF / IDF", "Security cameras", "Access control", "Intercom", "Wireless", "Other"]
form = f'''<section class="page-hero"><div class="container">
  <span class="eyebrow">Request a bid</span>
  <h1>Send us the drawings.</h1>
  <p class="lead">A full IFC set gets the most accurate bid, but we can work from schematics for budgeting.</p>
</div></section>
<section class="section"><div class="container form-wrap">
  <form class="bid-form" id="bid-form" action="https://formsubmit.co/ajax/{EMAIL}" method="POST" data-email="{EMAIL}">
    <input type="hidden" name="_subject" value="New bid request: sunstonedatasystems.com">
    <input type="hidden" name="_template" value="table">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
    <div class="form-grid">
      <div class="field"><label for="name">Name <span class="req">*</span></label><input id="name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="company">Company <span class="req">*</span></label><input id="company" name="company" required autocomplete="organization"></div>
      <div class="field"><label for="email">Email <span class="req">*</span></label><input id="email" name="email" type="email" required autocomplete="email"></div>
      <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field"><label for="role">Your role</label><select id="role" name="role"><option>General contractor</option><option>Developer</option><option>Owner's rep</option><option>Low-voltage contractor</option><option>Other</option></select></div>
      <div class="field"><label for="due">Bid due date <span class="req">*</span></label><input id="due" name="bid_due_date" type="date" required></div>
      <div class="field"><label for="project">Project name <span class="req">*</span></label><input id="project" name="project_name" required></div>
      <div class="field"><label for="location">Project city / address <span class="req">*</span></label><input id="location" name="project_location" required></div>
      <fieldset class="field full"><legend>Scope</legend><div class="checks">{"".join(f'<label><input type="checkbox" name="scope" value="{s}"> {s}</label>' for s in scopes)}</div></fieldset>
      <div class="field full"><label for="contract">Contract type</label><select id="contract" name="contract_type"><option>Labor only</option><option>Furnish and install</option><option>Not sure</option></select></div>
      <div class="field full"><label for="drawings">Link to drawings or plan room</label><input id="drawings" name="drawings_link" type="url" placeholder="https:// (Dropbox, Google Drive, BuildingConnected, plan room)"></div>
      <div class="field full"><label for="notes">Notes</label><textarea id="notes" name="notes" placeholder="Scope boundaries, who furnishes material, schedule, anything we should know"></textarea></div>
    </div>
    <p class="form-note">Large drawing sets? Share a link above, or email them to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <button class="btn btn--primary" type="submit">Send bid request</button>
    <div class="form-status" role="status" aria-live="polite"></div>
  </form>
  <aside class="side-card">
    <h3>What happens next</h3>
    <ul>
      <li>An estimator reviews the set and confirms scope and bid date.</li>
      <li>We send RFIs early if the drawings conflict.</li>
      <li>You get a line-item bid with exclusions and assumptions stated.</li>
    </ul>
    <p>Prefer email? <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </aside>
</div></section>'''
page("request-a-bid.html", "Request a Bid | Sunstone Data Systems",
     "Send Sunstone Data Systems your drawing set and bid date for a line-item low-voltage bid.",
     form, "request-a-bid.html")

# ---------- Privacy ----------
privacy = f'''<section class="page-hero"><div class="container"><h1>Privacy</h1></div></section>
<section class="section"><div class="container" style="max-width:800px">
<p>Sunstone Data Systems collects the information you submit through our bid request form (name, company, contact details, and project information) only to respond to your request and prepare a bid.</p>
<p>We do not sell or share your information with third parties, except the form-processing service (FormSubmit) that delivers your submission to us by email.</p>
<p>To ask about or remove your information, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div></section>'''
page("privacy.html", "Privacy | Sunstone Data Systems", "Privacy policy for Sunstone Data Systems.", privacy)

# ---------- 404 ----------
nf = '''<section class="page-hero"><div class="container"><span class="eyebrow">404</span><h1>That page isn't on the drawings.</h1>
<p class="lead">The page you're looking for doesn't exist. Try the home page or send us a bid request.</p>
<div class="hero-actions"><a class="btn btn--primary" href="/">Home</a><a class="btn btn--ghost" href="/request-a-bid.html">Request a Bid</a></div></div></section>'''
page("404.html", "Page not found | Sunstone Data Systems", "Page not found.", nf)
print("built")
