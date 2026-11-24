"""
Génère le site à partir de python/contenu.py.

Utilisation (depuis le dossier « Mon Entreprise ») :
    python python/construire_site.py

Fichiers produits dans site/ :
    index.html       page principale (texte français par défaut, traduite par JavaScript)
    js/i18n.js       toutes les traductions (fr / en)
    js/config.js     contact, devises, liens de paiement
"""
import html
import json
import re
from pathlib import Path

import contenu as C

RACINE = Path(__file__).resolve().parent.parent
SITE = RACINE / "site"
FR = C.TEXTES["fr"]
E = C.ENTREPRISE

# --------------------------------------------------------------------------
# Outils
# --------------------------------------------------------------------------
ICONES = {
    "browser": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M7 13h6M7 16h4"/>',
    "pulse": '<path d="M3 12h4l3-8 4 16 3-8h4"/>',
    "monitor": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    "phone": '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
    "shield": '<path d="M12 3l8 3v6c0 5-3.5 8.5-8 9-4.5-.5-8-4-8-9V6l8-3z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "scale": '<path d="M4 20h16M7 16V9M12 16V5M17 16v-4"/><path d="M10 7l2-2 2 2"/>',
    "bag": '<path d="M5 8h14l-1 12H6L5 8z"/><path d="M9 8V6a3 3 0 016 0v2M10 12h4"/>',
    "code": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 8h18M9 12l-2 2 2 2M15 12l2 2-2 2M13 11l-2 6"/>',
    "portal": '<rect x="4" y="4" width="16" height="12" rx="1"/><path d="M8 8h5M8 11h8M3 20h18"/>',
    "plug": '<rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/><path d="M11 7h4a2 2 0 012 2v4M13 17H9a2 2 0 01-2-2v-4"/>',
    "app": '<rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><path d="M17.5 14v7M14 17.5h7"/>',
    "send": '<path d="M21 3L3 10.5l7 3 3 7L21 3z"/><path d="M10 13.5L21 3"/>',
    "layers": '<path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 012-2h2a2 2 0 012 2v2M3 12h18M12 11v2"/>',
    "cart": '<path d="M3 4h2l2.5 11h11L21 7H6.5"/><circle cx="9" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0114 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6L6 18"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9L12 3z"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "rocket": '<path d="M5 15c-1.5 1.5-2 4.5-2 6 1.5 0 4.5-.5 6-2M9 15l-3-3c1-4 4.5-9 12-9 0 7.5-5 11-9 12z"/><circle cx="15" cy="9" r="1.5"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    "moon": '<path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 010 18M12 3a14 14 0 000 18"/>',
    "card": '<rect x="2.5" y="5" width="19" height="14" rx="2"/><path d="M2.5 10h19M6 15h4"/>',
    "wallet": '<path d="M4 7h14a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V6a2 2 0 012-2h11"/><circle cx="16" cy="13.5" r="1.3"/>',
    "bank": '<path d="M3 10l9-6 9 6M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"/>',
    "exchange": '<path d="M4 8h13l-3-3M20 16H7l3 3"/>',
    "copy": '<rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V5a2 2 0 012-2h8"/>',
    "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 018 0v4"/>',
}
WHATSAPP_SVG = '<svg class="icon" width="{s}" height="{s}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 004.74 1.21c5.46 0 9.91-4.45 9.91-9.91C21.95 6.45 17.5 2 12.04 2zm0 18.15c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 01-1.26-4.38c0-4.54 3.7-8.24 8.25-8.24 4.54 0 8.24 3.7 8.24 8.24 0 4.55-3.7 8.24-8.24 8.24zm4.52-6.17c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.16.24-.64.8-.78.97-.14.16-.29.18-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.16.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.86.85-.86 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.15-1.18-.06-.1-.23-.16-.48-.28z"/></svg>'


def icon(name, size=24):
    return (f'<svg class="icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONES[name]}</svg>')


def wa_icon(size=24):
    return WHATSAPP_SVG.format(s=size)


def esc(text):
    return html.escape(str(text), quote=True)


def accent(text):
    """[[texte]] -> <span class="accent">texte</span> (texte échappé)."""
    return re.sub(r"\[\[(.+?)\]\]", r'<span class="accent">\1</span>', esc(text))


def get(lang_dict, key):
    node = lang_dict
    for part in key.split("."):
        node = node[int(part)] if isinstance(node, list) else node[part]
    return node


def t(key, tag="span", cls="", extra=""):
    """Élément traduisible (texte simple)."""
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} data-i18n="{key}"{extra}>{esc(get(FR, key))}</{tag}>'


def th(key, tag="h2", cls="", extra=""):
    """Élément traduisible contenant un passage mis en couleur ([[...]])."""
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} data-i18n-html="{key}"{extra}>{accent(get(FR, key))}</{tag}>'


def attr(**pairs):
    """Attributs traduisibles : attr(placeholder='quote.p_name')."""
    spec = ";".join(f"{name.replace('_', '-')}:{key}" for name, key in pairs.items())
    values = " ".join(f'{name.replace("_", "-")}="{esc(get(FR, key))}"' for name, key in pairs.items())
    return f' data-i18n-attr="{spec}" {values}'


def usd(amount):
    """Format français par défaut : 1 490 $."""
    return f"{amount:,}".replace(",", " ") + " $"


def usd_en(amount):
    return f"${amount:,}"


def money(amount):
    return f'<span class="money" data-usd="{amount}">{usd(amount)}</span>'


def wa_link(text=""):
    return f"https://wa.me/{E['whatsapp']}" + (f"?text={html.escape(text)}" if text else "")


# --------------------------------------------------------------------------
# Traductions générées (offres du formulaire)
# --------------------------------------------------------------------------
def offer_labels(lang):
    T = C.TEXTES[lang]
    q = T["quote"]
    fmt = usd if lang == "fr" else usd_en
    labels = {}
    for p in C.ABONNEMENTS:
        labels[p["slug"]] = q["offer_monthly"].format(name=T["pricing"]["plans"][p["slug"]]["name"], price=fmt(p["prix"]))
    for f in C.FORFAITS:
        name = T["pricing"]["packages"][f["slug"]]["name"]
        labels[f["slug"]] = (q["offer_custom"].format(name=name) if f["prix"] is None
                             else q["offer_oneoff"].format(name=name, price=fmt(f["prix"])))
    for a in C.APPLICATIONS:
        labels[a["slug"]] = q["offer_app"].format(name=T["apps"]["items"][a["slug"]]["name"])
    labels["conseil"] = q["conseil"]
    return labels


def flatten(node, prefix=""):
    out = {}
    if isinstance(node, dict):
        for k, v in node.items():
            out.update(flatten(v, f"{prefix}{k}."))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            out.update(flatten(v, f"{prefix}{i}."))
    else:
        out[prefix[:-1]] = node
    return out


def build_i18n():
    data = {}
    for lang, textes in C.TEXTES.items():
        flat = flatten(textes)
        for key, value in list(flat.items()):
            if "[[" in value:
                flat[key] = accent(value)
        for slug, label in offer_labels(lang).items():
            flat[f"offers.{slug}"] = label
        data[lang] = flat
    return ("/* Fichier généré par python/construire_site.py — modifiez python/contenu.py */\n"
            "window.I18N = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n")


def build_config():
    cfg = {
        "whatsapp": E["whatsapp"],
        "baseCurrency": C.DEVISE_BASE,
        "currencies": [{"code": c, "fr": fr, "en": en} for c, fr, en, _ in C.DEVISES],
        "fallbackRates": {c: rate for c, _, _, rate in C.DEVISES},
        "ratesUrl": "https://open.er-api.com/v6/latest/USD",
        "paymentLinks": C.LIENS_PAIEMENT,
    }
    return ("/* Fichier généré par python/construire_site.py — modifiez python/contenu.py */\n"
            "window.SITE_CONFIG = " + json.dumps(cfg, ensure_ascii=False, indent=1) + ";\n")


# --------------------------------------------------------------------------
# Sections HTML
# --------------------------------------------------------------------------
def section_head(prefix, center=True, with_lead=True, title_id=None):
    cls = "section-head section-head--center reveal" if center else "section-head reveal"
    tid = f' id="{title_id}"' if title_id else ""
    lead = t(f"{prefix}.lead", "p") if with_lead else ""
    return f'''<header class="{cls}">
                {t(f"{prefix}.eyebrow", "p", "eyebrow")}
                {th(f"{prefix}.title", "h2", extra=tid)}
                {lead}
            </header>'''


def currency_select(id_):
    options = "".join(
        f'<option value="{c}">{c} — {esc(fr)}</option>' for c, fr, _, _ in C.DEVISES
    )
    return f'''<div class="currency">
                    <label for="{id_}">{icon("globe", 18)}{t("ui.currency")}</label>
                    <select id="{id_}" class="currency__select" data-currency-select>{options}</select>
                </div>'''


def cards(prefix, icons_list, card_cls="card"):
    out = []
    for i, ic in enumerate(icons_list):
        out.append(f'''<article class="{card_cls} reveal">
                    <span class="card__icon">{icon(ic)}</span>
                    {t(f"{prefix}.items.{i}.title", "h3")}
                    {t(f"{prefix}.items.{i}.text", "p")}
                </article>''')
    return "\n                ".join(out)


def plans_html():
    out = []
    for p in C.ABONNEMENTS:
        s = p["slug"]
        k = f"pricing.plans.{s}"
        feats = "".join(f'<li>{icon("check", 18)}{t(f"{k}.features.{i}")}</li>'
                        for i in range(len(FR["pricing"]["plans"][s]["features"])))
        badge = f'<span class="badge">{icon("star", 14)}{t("pricing.popular")}</span>' if p["populaire"] else ""
        btn_cls = "btn--primary" if p["populaire"] else "btn--outline"
        out.append(f'''<article class="price-card{' price-card--popular' if p['populaire'] else ''}">
                            {badge}
                            {t("pricing.kicker", "p", "price-card__kicker")}
                            {t(f"{k}.name", "h3")}
                            {t(f"{k}.tagline", "p", "price-card__tagline")}
                            <p class="price"><span class="price__amount">{money(p["prix"])}</span>{t("ui.per_month", cls="price__unit")}</p>
                            <p class="price-card__setup">+ {money(p["installation"])} {t("pricing.setup")}</p>
                            <ul class="checklist">{feats}</ul>
                            <a class="btn {btn_cls} btn--block" href="?offre={s}#devis" data-offer="{s}"><span>{t("pricing.choose")} {t(f"{k}.name")}</span></a>
                        </article>''')
    return "\n                        ".join(out)


def packages_html():
    out = []
    for f in C.FORFAITS:
        s = f["slug"]
        k = f"pricing.packages.{s}"
        price = t("ui.quote_only") if f["prix"] is None else money(f["prix"])
        btn = t("pricing.ask_quote") if f["prix"] is None else t("pricing.order")
        out.append(f'''<li class="oneoff">
                            <span class="oneoff__icon">{icon(f["icone"])}</span>
                            <span class="oneoff__body">{t(f"{k}.name", "strong")}{t(f"{k}.detail", "small")}</span>
                            <span class="oneoff__price">{price}</span>
                            <a class="btn btn--outline btn--sm" href="?offre={s}#devis" data-offer="{s}">{btn}</a>
                        </li>''')
    return "\n                        ".join(out)


def apps_html():
    out = []
    for a in C.APPLICATIONS:
        s = a["slug"]
        k = f"apps.items.{s}"
        tags = "".join(t(f"{k}.features.{i}", "li") for i in range(len(FR["apps"]["items"][s]["features"])))
        bars = "".join(f'<i style="height:{h}%"></i>' for h in (40, 65, 50, 80, 60, 90))
        out.append(f'''<article class="app-card reveal">
                    <div class="app-card__preview" aria-hidden="true">
                        <span class="app-card__dots"><i></i><i></i><i></i></span>
                        <span class="app-card__bar"></span>
                        <span class="app-card__bar app-card__bar--short"></span>
                        <span class="app-card__chart">{bars}</span>
                    </div>
                    {t(f"{k}.category", "p", "app-card__category")}
                    {t(f"{k}.name", "h3")}
                    {t(f"{k}.text", "p")}
                    <ul class="tags">{tags}</ul>
                    <div class="app-card__footer">
                        <p class="price price--sm">{t("ui.from", cls="price__from")} <span class="price__amount">{money(a["prix"])}</span>{t("ui.per_month", cls="price__unit")}</p>
                        <a class="btn btn--primary btn--sm" href="?offre={s}#devis" data-offer="{s}">{t("apps.demo")}</a>
                    </div>
                </article>''')
    return "\n                ".join(out)


def steps_html():
    return "\n                ".join(
        f'''<li class="step reveal">
                    <span class="step__num">{i + 1:02d}</span>
                    {t(f"process.items.{i}.title", "h3")}
                    {t(f"process.items.{i}.text", "p")}
                </li>''' for i in range(len(FR["process"]["items"])))


PAY_METHODS = [
    # clé, icône, type d'action
    ("carte", "card", "link"),
    ("payshap", "pulse", "bank"),
    ("eft", "bank", "bank"),
    ("cash", "wallet", "bank"),
    ("mobile", "phone", "whatsapp"),
    ("swift", "globe", "bank"),
    ("paypal", "wallet", "optional"),   # affiché seulement si un lien est renseigné
    ("wise", "exchange", "optional"),   # affiché seulement si un lien est renseigné
]


def payment_html():
    methods = []
    for key, ic, kind in PAY_METHODS:
        k = f"payment.methods.{key}"
        if kind == "optional" and not C.LIENS_PAIEMENT.get(key):
            continue
        if kind == "bank":
            action = f'<a class="btn btn--outline btn--sm btn--block" href="#coordonnees">{t(f"{k}.button")}</a>'
        else:
            link = C.LIENS_PAIEMENT.get(key, "")
            href = esc(link) if link else wa_link()
            action = (f'<a class="btn btn--primary btn--sm btn--block" href="{href}" target="_blank" rel="noopener" '
                      f'data-pay="{key}" data-pay-link="{esc(link)}">{t(f"{k}.button")}</a>')
        methods.append(f'''<article class="pay-card reveal">
                    <span class="card__icon">{icon(ic)}</span>
                    {t(f"{k}.title", "h3")}
                    {t(f"{k}.text", "p")}
                    {action}
                </article>''')

    bank_rows = []
    for field in ["banque", "titulaire", "numero", "shapid", "type", "code_agence", "swift", "adresse_banque"]:
        value = C.COMPTE_FNB[field]
        bank_rows.append(f'''<div class="bank__row">
                            <dt>{t(f"payment.bank_fields.{field}")}</dt>
                            <dd><span class="bank__value">{esc(value)}</span><button class="copy-btn" type="button" data-copy="{esc(value)}"{attr(aria_label="ui.copy")}>{icon("copy", 16)}</button></dd>
                        </div>''')
    bank_rows.append(f'''<div class="bank__row">
                            <dt>{t("payment.bank_fields.reference")}</dt>
                            <dd>{t("payment.reference_value", cls="bank__value")}</dd>
                        </div>''')
    steps = "".join(f'<li>{t(f"payment.steps.{i}")}</li>' for i in range(len(FR["payment"]["steps"])))

    return f'''<section class="section" id="paiement" aria-labelledby="paiement-titre">
        <div class="container">
            {section_head("payment", title_id="paiement-titre")}
            <div class="currency-bar">{currency_select("devise-paiement")}{t("ui.currency_note", "p", "currency-bar__note")}</div>
            <div class="pay-grid">
                {"".join(methods)}
            </div>
            <div class="bank" id="coordonnees">
                <div class="bank__details">
                    <h3>{icon("bank", 22)}{t("payment.bank_title")}</h3>
                    {t("payment.bank_lead", "p", "bank__lead")}
                    <dl>
                        {"".join(bank_rows)}
                    </dl>
                </div>
                <div class="bank__steps">
                    {t("payment.steps_title", "h3")}
                    <ol class="pay-steps">{steps}</ol>
                    <p class="bank__safety">{icon("lock", 18)}{t("payment.safety")}</p>
                </div>
            </div>
        </div>
    </section>'''


def faq_html():
    return "\n                ".join(
        f'''<details class="faq__item"{" open" if i == 0 else ""}>
                    <summary>{t(f"faq.items.{i}.q")}<span class="faq__icon">{icon("plus", 20)}</span></summary>
                    {t(f"faq.items.{i}.a", "p")}
                </details>''' for i in range(len(FR["faq"]["items"])))


def field(name, kind="text", required=True, placeholder=True, autocomplete=None):
    label_opt = "" if required else " " + t("quote.optional", cls="field__optional")
    ac = f' autocomplete="{autocomplete}"' if autocomplete else ""
    ph = attr(placeholder=f"quote.p_{name}") if placeholder else ""
    if kind == "textarea":
        widget = f'<textarea id="{name}" name="{name}" rows="5"{ph}></textarea>'
    else:
        widget = f'<input type="{kind}" id="{name}" name="{name}"{ac}{ph}>'
    return f'<div class="field"><label for="{name}">{t(f"quote.f_{name}")}{label_opt}</label>{widget}</div>'


def form_html():
    fr_labels = offer_labels("fr")
    offers = f'<option value="" data-i18n="quote.o_offer">{esc(FR["quote"]["o_offer"])}</option>'
    offers += "".join(f'<option value="{s}" data-i18n="offers.{s}">{esc(label)}</option>' for s, label in fr_labels.items())
    budgets = f'<option value="" data-i18n="quote.o_budget">{esc(FR["quote"]["o_budget"])}</option>'
    budget_values = ["lt500", "500-1500", "1500-3000", "3000-10000", "gt10000"]
    budgets += "".join(f'<option value="{v}" data-i18n="quote.budgets.{i}">{esc(FR["quote"]["budgets"][i])}</option>'
                       for i, v in enumerate(budget_values))
    return f'''<div id="form-alert" role="status" hidden></div>
                <form id="form-devis" name="devis" method="POST" action="/" class="form" novalidate data-netlify="true" netlify-honeypot="website">
                    <input type="hidden" name="form-name" value="devis">
                    <input type="hidden" name="langue" id="langue" value="fr">
                    <input type="hidden" name="devise" id="devise" value="USD">
                    <div class="form__row">
                        {field("name", autocomplete="name")}
                        {field("email", "email", autocomplete="email")}
                    </div>
                    <div class="form__row">
                        {field("phone", "tel", required=False, autocomplete="tel")}
                        {field("company", required=False, autocomplete="organization")}
                    </div>
                    <div class="form__row">
                        {field("country", required=False, autocomplete="country-name")}
                        <div class="field"><label for="budget">{t("quote.f_budget")} {t("quote.optional", cls="field__optional")}</label><select id="budget" name="budget">{budgets}</select></div>
                    </div>
                    <div class="field"><label for="offer">{t("quote.f_offer")}</label><select id="offer" name="offer">{offers}</select></div>
                    {field("message", "textarea")}
                    <div class="field field--check"><label class="check"><input type="checkbox" id="consent" name="consent" value="oui">{t("quote.f_consent")}</label></div>
                    <div class="hp-field" aria-hidden="true"><label for="website">Ne pas remplir</label><input type="text" id="website" name="website" tabindex="-1" autocomplete="off"></div>
                    <button class="btn btn--primary btn--lg btn--block" type="submit">{t("quote.submit")} {icon("send", 18)}</button>
                    {t("quote.note", "p", "form__note")}
                </form>'''


def json_ld():
    data = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": E["nom"],
        "description": FR["brand"]["tagline"],
        "url": E["site_url"],
        "email": E["email"],
        "telephone": E["telephone"],
        "currenciesAccepted": ", ".join(c for c, *_ in C.DEVISES),
        "paymentAccepted": "Credit Card, PayShap, EFT, Cash, Bank Transfer, Mobile Money",
        "makesOffer": [{
            "@type": "Offer",
            "name": f'Website {C.TEXTES["en"]["pricing"]["plans"][p["slug"]]["name"]}',
            "priceSpecification": {"@type": "UnitPriceSpecification", "price": p["prix"],
                                   "priceCurrency": "USD", "unitText": "MONTH"},
        } for p in C.ABONNEMENTS],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


# --------------------------------------------------------------------------
# Éléments communs (accueil + pages légales)
# --------------------------------------------------------------------------
SOCIAL_SVG = {
    "facebook": '<path fill="currentColor" d="M13.5 22v-8.2h2.8l.4-3.2h-3.2V8.6c0-.9.3-1.6 1.6-1.6h1.7V4.1c-.3 0-1.3-.1-2.5-.1-2.5 0-4.2 1.5-4.2 4.3v2.4H7.3v3.2h2.8V22h3.4z"/>',
    "linkedin": '<path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 110 5 2.5 2.5 0 010-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.06c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.77 2.65 4.77 6.1V21h-4v-5.2c0-1.24-.02-2.84-1.73-2.84-1.73 0-2 1.35-2 2.75V21h-4z"/>',
    "instagram": '<rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/>',
    "tiktok": '<path fill="currentColor" d="M16.6 5.82A4.28 4.28 0 0115.54 3h-3.09v12.4a2.59 2.59 0 01-2.59 2.5c-1.42 0-2.6-1.16-2.6-2.6 0-1.72 1.66-3.01 3.37-2.48V9.66c-3.45-.46-6.47 2.22-6.47 5.64 0 3.33 2.76 5.7 5.69 5.7 3.14 0 5.69-2.55 5.69-5.7V9.01a7.35 7.35 0 004.3 1.38V7.3s-1.88.09-3.24-1.48z"/>',
}

# Pages légales : (fichier, clé dans TEXTES["legal"])
LEGAL_PAGES = [
    ("conditions.html", "terms"),
    ("remboursements.html", "refunds"),
    ("garantie.html", "warranty"),
    ("confidentialite.html", "privacy"),
]


def tel_link():
    return "tel:" + re.sub(r"[^\d+]", "", E["telephone"])


def logo_html():
    return f'''<span class="logo__mark">{esc(E["initiales"])}</span>
                <span class="logo__text"><strong>{esc(E["nom"])}</strong>{t("brand.tagline", "small")}</span>'''


def socials_html():
    links = []
    for name, svg in SOCIAL_SVG.items():
        url = E.get("reseaux", {}).get(name)
        if url:
            links.append(f'<a href="{esc(url)}" target="_blank" rel="noopener" aria-label="{name.capitalize()}">'
                         f'<svg class="icon" width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{svg}</svg></a>')
    links.append(f'<a href="{wa_link()}" target="_blank" rel="noopener" aria-label="WhatsApp" data-wa>{wa_icon(20)}</a>')
    return f'<div class="socials">{"".join(links)}</div>'


def header_html(p=""):
    """p = préfixe des liens : "" sur l'accueil, "index.html" sur les autres pages."""
    return f'''<header class="site-header">
    <div class="container site-header__inner">
        <a class="logo" href="{p or "#contenu"}" aria-label="{esc(E["nom"])}">
            {logo_html()}
        </a>
        <nav class="main-nav" id="main-nav">
            <a href="{p}#services">{t("nav.services")}</a>
            <a href="{p}#tarifs">{t("nav.pricing")}</a>
            <a href="{p}#applications">{t("nav.apps")}</a>
            <a href="{p}#paiement">{t("nav.payment")}</a>
            <a href="{p}#faq">{t("nav.faq")}</a>
            <a class="btn btn--primary btn--sm" href="{p}#devis">{t("nav.cta")}</a>
        </nav>
        <div class="header-tools">
            <button class="icon-btn lang-btn" type="button" id="lang-toggle"{attr(aria_label="ui.lang_switch", title="ui.lang_switch")}>{t("ui.lang_label")}</button>
            <button class="icon-btn theme-btn" type="button" id="theme-toggle" aria-label="{esc(FR["ui"]["theme_light"])}">
                <span class="theme-btn__sun">{icon("sun", 20)}</span><span class="theme-btn__moon">{icon("moon", 20)}</span>
            </button>
            <button class="icon-btn nav-toggle" type="button" aria-controls="main-nav" aria-expanded="false"{attr(aria_label="ui.menu_open")}>
                <span class="nav-toggle__open">{icon("menu")}</span>
                <span class="nav-toggle__close">{icon("close")}</span>
            </button>
        </div>
    </div>
</header>'''


def hours_trust_html():
    hours = "".join(f'<li>{t(f"hours.lines.{i}")}</li>' for i in range(len(FR["hours"]["lines"])))
    trust = [t(f"trust.items.{i}") for i in range(len(FR["trust"]["items"]))]
    if E.get("numero_enregistrement"):
        trust.append(t("trust.registered"))
    trust_li = "".join(f'<li>{icon("check", 18)}{x}</li>' for x in trust)
    return f'''<div class="info-card">
                    <h3>{icon("clock", 20)}{t("hours.title")}</h3>
                    <ul class="info-card__lines">{hours}</ul>
                    {t("hours.note", "p", "info-card__note")}
                </div>
                <ul class="trust-list">{trust_li}</ul>'''


def footer_html(p=""):
    wa = wa_link()
    services = "".join(f'<li><a href="{p}#services">{t(f"services.items.{i}.title")}</a></li>'
                       for i in range(len(FR["services"]["items"])))
    info_targets = [f"{p}#paiement", f"{p}#tarifs", f"{p}#faq"] + [f for f, _ in LEGAL_PAGES[:3]] + [LEGAL_PAGES[3][0]]
    info = "".join(f'<li><a href="{href}">{t(f"footer.info_links.{i}")}</a></li>' for i, href in enumerate(info_targets))
    company = esc(E.get("raison_sociale") or E["nom"])
    reg = (f'<br><span class="site-footer__muted">{t("footer.reg")} {esc(E["numero_enregistrement"])}</span>'
           if E.get("numero_enregistrement") else "")
    address = "".join(f"<br>{esc(line)}" for line in E.get("adresse", []))
    reg_bottom = f' {t("footer.reg")} {esc(E["numero_enregistrement"])}.' if E.get("numero_enregistrement") else ""
    legal_bottom = "".join(f'<a href="{f}">{t(f"legal.{k}.title")}</a>' for f, k in LEGAL_PAGES)
    return f'''<footer class="site-footer">
    <div class="container site-footer__grid">
        <div>
            <a class="logo" href="{p or "#contenu"}">
                {logo_html()}
            </a>
            {t("footer.about", "p", "site-footer__about")}
            {socials_html()}
        </div>
        <div>
            {t("footer.services", "h3")}
            <ul class="site-footer__links">{services}</ul>
        </div>
        <div>
            {t("footer.info", "h3")}
            <ul class="site-footer__links">{info}</ul>
        </div>
        <div>
            {t("footer.contact", "h3")}
            <ul class="footer-contact">
                <li><span class="footer-contact__icon">{icon("phone", 18)}</span><a href="{tel_link()}">{esc(E["telephone"])}</a></li>
                <li><span class="footer-contact__icon">{wa_icon(18)}</span><a href="{wa}" target="_blank" rel="noopener" data-wa>WhatsApp</a></li>
                <li><span class="footer-contact__icon">{icon("mail", 18)}</span><a href="mailto:{esc(E["email"])}">{esc(E["email"])}</a></li>
                <li><span class="footer-contact__icon">{icon("pin", 18)}</span><span><strong>{company}</strong>{reg}{address}</span></li>
            </ul>
        </div>
    </div>
    <div class="container site-footer__bottom">
        <p>© <span id="year">2026</span> {company}.{reg_bottom} {t("ui.rights")}</p>
        <nav class="site-footer__legal">{legal_bottom}</nav>
    </div>
</footer>

<a class="wa-float" href="{wa}" target="_blank" rel="noopener" data-wa{attr(aria_label="ui.whatsapp")}>{wa_icon(30)}</a>

<div class="mobile-bar">
    <a class="mobile-bar__brand" href="{tel_link()}"{attr(aria_label="footer.call")}>
        <span class="logo__mark">{esc(E["initiales"])}</span>
        <span class="mobile-bar__text"><strong>{esc(E["nom"])}</strong><small>{esc(E["telephone"])}</small></span>
    </a>
    <a class="btn btn--whatsapp mobile-bar__wa" href="{wa}" target="_blank" rel="noopener" data-wa>{wa_icon(20)} WhatsApp</a>
</div>'''


def page_head(title_key, description_key=None, path=""):
    desc = f'\n    <meta name="description"{attr(content=description_key)}>' if description_key else ""
    return f'''<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script>
        (function () {{
            var d = document.documentElement, theme, lang;
            try {{ theme = localStorage.getItem('theme'); lang = localStorage.getItem('lang'); }} catch (e) {{}}
            if (!theme) theme = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
            d.setAttribute('data-theme', theme);
            if (!lang) lang = (navigator.language || 'fr').slice(0, 2) === 'fr' ? 'fr' : 'en';
            d.setAttribute('lang', lang);
            d.classList.add('js');
        }})();
    </script>
    <meta name="theme-color" content="#070d1a">
    <title data-i18n="{title_key}">{esc(get(FR, title_key))}</title>{desc}
    <link rel="canonical" href="{esc(E["site_url"])}{path}">
    <link rel="icon" type="image/svg+xml" href="images/favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">'''


def build_legal(filename, key):
    sections = FR["legal"][key]["sections"]
    body = "".join(f'''
            <section class="legal__section">
                {t(f"legal.{key}.sections.{i}.h", "h2")}
                {t(f"legal.{key}.sections.{i}.p", "p")}
            </section>''' for i in range(len(sections)))
    return f'''<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    {page_head(f"legal.{key}.title", path=filename)}
</head>
<body data-whatsapp="{esc(E["whatsapp"])}">
<a class="skip-link" href="#contenu" data-i18n="ui.skip">{esc(FR["ui"]["skip"])}</a>

{header_html("index.html")}

<main id="contenu">
    <section class="section legal">
        <div class="container container--narrow">
            <a class="legal__back" href="index.html">{t("legal.back")}</a>
            {t(f"legal.{key}.title", "h1")}
            {t("legal.updated", "p", "legal__updated")}
            {body}
            <div class="legal__contact">
                {t("legal.contact_title", "h2")}
                {t("legal.contact_text", "p")}
                <div class="hero__actions">
                    <a class="btn btn--whatsapp" href="{wa_link()}" target="_blank" rel="noopener" data-wa>{wa_icon(20)} WhatsApp</a>
                    <a class="btn btn--ghost" href="mailto:{esc(E["email"])}">{icon("mail", 18)} {esc(E["email"])}</a>
                </div>
            </div>
        </div>
    </section>
</main>

{footer_html("index.html")}

<script src="js/config.js"></script>
<script src="js/i18n.js"></script>
<script src="js/main.js"></script>
</body>
</html>
'''


def build_index():
    wa = wa_link()
    first_price = C.ABONNEMENTS[0]["prix"]
    guarantees = "".join(f'<li>{icon("check", 16)}{t(f"pricing.guarantees.{i}")}</li>'
                         for i in range(len(FR["pricing"]["guarantees"])))
    strip_icons = ["monitor", "layers", "browser", "clock"]
    strip = "".join(f'<li>{icon(ic)}{t(f"strip.{i}")}</li>' for i, ic in enumerate(strip_icons))

    return f'''<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script>
        /* Thème et langue appliqués avant l'affichage (évite un flash) */
        (function () {{
            var d = document.documentElement, theme, lang;
            try {{ theme = localStorage.getItem('theme'); lang = localStorage.getItem('lang'); }} catch (e) {{}}
            if (!theme) theme = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
            d.setAttribute('data-theme', theme);
            if (!lang) lang = (navigator.language || 'fr').slice(0, 2) === 'fr' ? 'fr' : 'en';
            d.setAttribute('lang', lang);
            d.classList.add('js');
        }})();
    </script>
    <meta name="theme-color" content="#070d1a">
    <title data-i18n="meta.title">{esc(FR["meta"]["title"])}</title>
    <meta name="description"{attr(content="meta.description")}>
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="{esc(E["nom"])}">
    <meta property="og:title"{attr(content="meta.og_title")}>
    <meta property="og:description"{attr(content="meta.description")}>
    <meta property="og:url" content="{esc(E["site_url"])}">
    <meta property="og:image" content="{esc(E["site_url"])}images/og-image.png">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="canonical" href="{esc(E["site_url"])}">
    <link rel="icon" type="image/svg+xml" href="images/favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <script type="application/ld+json">
{json_ld()}
    </script>
</head>
<body data-whatsapp="{esc(E["whatsapp"])}">
<a class="skip-link" href="#contenu" data-i18n="ui.skip">{esc(FR["ui"]["skip"])}</a>

{header_html()}

<main id="contenu">
    <nav class="breadcrumb" aria-label="Breadcrumb">
        <div class="container">
            <ol>
                <li><a href="#contenu">{t("breadcrumb.home")}</a></li>
                <li><a href="#services">{t("breadcrumb.services")}</a></li>
                <li aria-current="page">{t("breadcrumb.current")}</li>
            </ol>
        </div>
    </nav>

    <section class="hero">
        <div class="container hero__grid">
            <div class="hero__content reveal">
                {t("hero.eyebrow", "p", "eyebrow")}
                {th("hero.title", "h1")}
                {t("hero.lead", "p", "lead")}
                <div class="hero__actions">
                    <a class="btn btn--primary btn--lg" href="#tarifs">{t("hero.cta_primary")} {icon("arrow", 18)}</a>
                    <a class="btn btn--ghost btn--lg" href="#devis">{t("hero.cta_secondary")}</a>
                </div>
                <ul class="hero__proof">
                    <li><strong>{t("ui.from")} {money(first_price)}</strong>{t("hero.proof1")}</li>
                    <li><strong>{t("hero.proof2_value")}</strong>{t("hero.proof2")}</li>
                    <li><strong>{t("hero.proof3_value")}</strong>{t("hero.proof3")}</li>
                </ul>
            </div>
            <div class="hero__visual reveal" aria-hidden="true">
                <div class="orbit">
                    <span class="orbit__ring orbit__ring--outer"></span>
                    <span class="orbit__ring orbit__ring--inner"></span>
                    <span class="orbit__node orbit__node--top">{icon("browser", 28)}</span>
                    <span class="orbit__node orbit__node--right">{icon("bag", 28)}</span>
                    <span class="orbit__node orbit__node--bottom">{icon("card", 28)}</span>
                    <span class="orbit__node orbit__node--left">{icon("globe", 28)}</span>
                    <span class="orbit__core">{icon("code", 56)}</span>
                </div>
            </div>
        </div>
        <div class="container">
            <ul class="feature-strip">{strip}</ul>
        </div>
    </section>

    <section class="section section--alt" aria-labelledby="defis-titre">
        <div class="container">
            {section_head("challenges", title_id="defis-titre")}
            <div class="card-grid">
                {cards("challenges", C.ICONES_DEFIS)}
            </div>
        </div>
    </section>

    <section class="section" id="services" aria-labelledby="services-titre">
        <div class="container">
            {section_head("services", title_id="services-titre")}
            <div class="card-grid">
                {cards("services", C.ICONES_SERVICES)}
            </div>
        </div>
    </section>

    <section class="section section--alt" id="tarifs" aria-labelledby="tarifs-titre">
        <div class="container">
            {section_head("pricing", center=False, title_id="tarifs-titre")}
            <div class="pricing-toolbar">
                <div class="tabs" role="tablist"{attr(aria_label="pricing.aria_tabs")}>
                    <button class="tabs__btn is-active" type="button" role="tab" id="tab-mensuel" aria-controls="panel-mensuel" aria-selected="true">{t("pricing.tab_monthly")}</button>
                    <button class="tabs__btn" type="button" role="tab" id="tab-unique" aria-controls="panel-unique" aria-selected="false" tabindex="-1">{t("pricing.tab_oneoff")}</button>
                </div>
                {currency_select("devise-tarifs")}
            </div>
            {t("ui.currency_note", "p", "currency-note")}
            <div class="tabs__panel" id="panel-mensuel" role="tabpanel" aria-labelledby="tab-mensuel">
                <p class="panel-intro">{icon("check", 18)}{t("pricing.intro_monthly")}</p>
                <div class="pricing-grid">
                        {plans_html()}
                </div>
            </div>
            <div class="tabs__panel" id="panel-unique" role="tabpanel" aria-labelledby="tab-unique" hidden>
                <p class="panel-intro">{icon("check", 18)}{t("pricing.intro_oneoff")}</p>
                <ul class="oneoff-list">
                        {packages_html()}
                </ul>
            </div>
            <ul class="guarantees">{guarantees}</ul>
        </div>
    </section>

    <section class="section" id="applications" aria-labelledby="apps-titre">
        <div class="container">
            {section_head("apps", title_id="apps-titre")}
            <div class="apps-grid">
                {apps_html()}
            </div>
        </div>
    </section>

    <section class="section section--alt" id="methode" aria-labelledby="methode-titre">
        <div class="container">
            {section_head("process", with_lead=False, title_id="methode-titre")}
            <ol class="steps">
                {steps_html()}
            </ol>
        </div>
    </section>

    {payment_html()}

    <section class="section section--alt" id="faq" aria-labelledby="faq-titre">
        <div class="container container--narrow">
            {section_head("faq", with_lead=False, title_id="faq-titre")}
            <div class="faq">
                {faq_html()}
            </div>
        </div>
    </section>

    <section class="section section--cta" id="devis" aria-labelledby="devis-titre">
        <div class="container quote">
            <div class="quote__intro">
                {t("quote.eyebrow", "p", "eyebrow")}
                {th("quote.title", "h2", extra=' id="devis-titre"')}
                {t("quote.lead", "p")}
                <ul class="contact-list">
                    <li><a href="{wa}" target="_blank" rel="noopener" data-wa>{wa_icon(22)}<span>{t("quote.contact_whatsapp", "small")}{esc(E["telephone"])}</span></a></li>
                    <li><a href="mailto:{esc(E["email"])}">{icon("mail", 22)}<span>{t("quote.contact_email", "small")}{esc(E["email"])}</span></a></li>
                    <li><span class="contact-list__static">{icon("pin", 22)}<span>{t("quote.contact_zone", "small")}{t("quote.zone")}</span></span></li>
                </ul>
                {hours_trust_html()}
            </div>
            <div class="quote__form">
                {form_html()}
            </div>
        </div>
    </section>

    <section class="final-cta">
        <div class="container final-cta__inner">
            <span class="final-cta__icon">{icon("rocket", 32)}</span>
            {t("final.title", "h2")}
            {t("final.lead", "p")}
            <div class="hero__actions hero__actions--center">
                <a class="btn btn--primary btn--lg" href="#devis">{t("final.cta")} {icon("arrow", 18)}</a>
                <a class="btn btn--whatsapp btn--lg" href="{wa}" target="_blank" rel="noopener" data-wa>{wa_icon(20)} {t("final.whatsapp")}</a>
            </div>
        </div>
    </section>
</main>

{footer_html()}

<script src="js/config.js"></script>
<script src="js/i18n.js"></script>
<script src="js/main.js"></script>
</body>
</html>
'''


def main():
    (SITE / "js").mkdir(parents=True, exist_ok=True)
    (SITE / "index.html").write_text(build_index(), encoding="utf-8")
    (SITE / "js" / "i18n.js").write_text(build_i18n(), encoding="utf-8")
    (SITE / "js" / "config.js").write_text(build_config(), encoding="utf-8")
    for filename, key in LEGAL_PAGES:
        (SITE / filename).write_text(build_legal(filename, key), encoding="utf-8")
    print("Site généré dans", SITE)
    print("  - index.html\n  - js/i18n.js\n  - js/config.js")
    for filename, _ in LEGAL_PAGES:
        print("  -", filename)


if __name__ == "__main__":
    main()
