from flask import Flask
import threading
import requests
import time
import json
from datetime import datetime, timedelta

app = Flask('')

@app.route('/')
def home():
    return "Bot läuft!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()

WEBHOOK_URL = "https://discord.com/api/webhooks/1391485113560203345/Ec9hNjJ2ySZoa2xp75XcB8dhWJ-0HnuFKsIbr0c_v10W8c5tx72zhNzg24qLvYpo2W8d"

START_DATETIME = datetime(2025, 7, 8, 16, 0, 0)  # 08.07.2025 16:00 Uhr

EVENT_INTERVAL_DAYS = 4

events = [
    {
        "title": "Sternenglut der Argo",
        "text": """**Wenn die Sterne der Argo hell über dem Firmament leuchten, erwacht der Schöpfungsgeist in den Hallen der Schmiede und Werkstätten.**
Es heißt, das legendäre Schiff der Helden durchquert in dieser Zeit die Himmelsbahnen, ein Omen für Erfindungsgeist, Meisterhandwerk und technische Inspiration. Werkzeuge folgen wie von selbst dem Willen ihres Trägers, und selbst das Unvollendete scheint zur Vollendung zu drängen.

Doch während Hammer, Feder und Nadel den Takt der Welt bestimmen, verlieren andere den Zugang zu den unsichtbaren Fäden. Die Magie stockt, wird starr – als müsse auch sie erst gehämmert, geschmiedet, gezirkelt werden.

__**Effekt:**__
- Die Arbeiten fliegen den Handwerkern nur so durch die Finger durch einen Würfelbonus von +1 auf alle relevanten Fähigkeiten
- Magier erhalten einen Würfelmalus von -1 auf magische Fähigkeiten (Zauber, magische Heilung/Angriffe etc.)
""",
        "image": "https://cdn.discordapp.com/attachments/1117849423158988840/1391840833640206406/Argo.png"
    },
    {
        "title": "Ruf des Orion",
        "text": """**Im Zeichen Orions beginnt die Zeit der Jagdfeuer.**
Die alten Geschichten erzählen von einem himmlischen Jäger, dessen Sternbild in regelmäßigen Abständen besonders hell leuchtet – ein Omen für all jene, die den Ruf der Wildnis vernehmen.

Wenn Orion am Himmel jagt, versammeln sich Streiter, Späher und Söldner, um sich auf gefährliche Pfade zu begeben: seltene Bestien, verfluchte Kreaturen oder Wesen aus vergessenen Schattenreichen werden zur Beute jener, die Mut und Waffe führen.

Ob zur Ehre Orions oder für Ruhm und Lohn – in diesen Nächten gilt: Wer nicht jagt, wird gejagt.

__**Effekt:**__
- Kämpfer und Jäger erhalten +1 auf alle für die Jagd und den Kampf relevanten Fähigkeiten.
- Der Jagdtrieb von Tierwandlern und Wehrwesen ist stärker ausgeprägt und bringt einen Würfelmalus auf geistige Fähigkeiten von -1
""",
        "image": "https://cdn.discordapp.com/attachments/1117849423158988840/1391840836089806970/Orion.png"
    },
    {
        "title": "Aquilas Ruf",
        "text": """**Wenn das Sternbild Aquila über den Himmelsbogen steigt, erklingt der Ruf des Himmels – klar, unmissverständlich, durchdringend.**
In dieser Zeit finden jene neue Kraft, die Licht, Wahrheit und Heilung in die Welt tragen. Engel, Lichtmagier und gute Naturwesen berichten von Visionen, innerer Klarheit und einer Schärfung ihres Wirkens. Ihre Magie leuchtet heller, ihre Worte tragen weiter, und ihre Berührungen heilen tiefer.

Doch wo Aquila wacht, wird nichts verborgen bleiben. Der Himmel duldet keine Lüge, keine Schattenflucht.

__**Effekt:**__
- Lichtwesen und gute Wesen erhalten einen Würfelbonus von +1 auf ALLE Werte 
- Schattenwesen und böse Wesen erhalten einen Würfelmalus von -1 auf ALLE Werte
""",
        "image": "https://cdn.discordapp.com/attachments/1117849423158988840/1391840832813797477/Aquila.png"
    },
    {
        "title": "Vollmond – Der Glanz des Ungefilterten",
        "text": """**Wenn der Vollmond wie ein glühendes Auge am Himmel steht, reißt die Welt ihre Schleier herunter.**
Es ist eine Zeit der Überfülle: Emotionen steigen, Magie flackert, Sinne überschlagen sich. Tierwandler spüren das Beben ihrer Gestalt, Blutmagie pulsiert lauter, und selbst gewöhnliche Worte brennen sich tiefer in die Herzen.

Doch wer sich auf Kontrolle stützt, wer Maß und Zurückhaltung lebt, der kämpft in dieser Zeit gegen den Sturm im eigenen Inneren.

__**Effekt:**__
- Tierwandler, leidenschaftliche Wesen +1 Würfelbonus auf Triebkräfte, instinkthafte Wahrnehmung und emotionale Magie
- Gelehrte, Taktiker, disziplinierte Zauberwirker verlieren Halt –1 Würfelmalus auf Willenskraft, rationale Entscheidungen und geistige Kontrolle 
""",
        "image": "https://cdn.discordapp.com/attachments/1117849423158988840/1391840829253091450/Vollmond.png"
    },
    {
        "title": "Andromedas Erwachen",
        "text": """**Wenn das Sternbild Andromeda in klarem Glanz über den Nachthimmel steigt, beginnen die arkanen Ströme zu singen.**
Die Welt wird durchlässiger, durchzogen von unsichtbaren Fäden. Zauber gleiten leichter durch das Gewebe der Wirklichkeit, Wissen offenbart sich in flüchtigen Momenten, und Visionen flackern selbst in nüchternen Köpfen auf. Es heißt, Andromeda selbst habe ihr kosmisches Schweigen gebrochen – und sende nun Zeichen an jene, die bereit sind zu lauschen.

Doch diese Offenheit verändert das Gleichgewicht: Für Wesen, die mit dem Körper denken – Jäger, Fährtenleser, Tierwesen – verliert die Welt an Klarheit. Orientierung, Instinkt und Wachsamkeit verschwimmen in einem leisen, sirrenden Rauschen.

__**Effekt:**__
- Magier erhalten einen Würfelbonus von +1 auf magische Fähigkeiten (Zauber, magische Heilung/Angriffe etc.)
- Jäger und Krieger fühlen sich durch die frei fließende Magie benebelt und erhalten einen Würfelmalus von -1 auf alle relevanten Fähigkeiten.
""",
        "image": "https://cdn.discordapp.com/attachments/1117849423158988840/1391840831840981154/Andromeda.png"
    },
    {
        "title": "Aequitas' Stunde des Gleichgewichts",
        "text": """**Wenn Aequitas ihre Waage erhebt, halten selbst Extreme den Atem an.**
In dieser Phase legt sich ein Gleichgewicht über die Welt – unausgesprochen, aber spürbar. Die Stimmen der Radikalen verhallen, die Urteile der Maßvollen tragen weiter. Für jene, die beobachten, beraten oder vermitteln, beginnt eine Zeit besonderer Klarheit.

Wissenshüter, Gelehrte, Diplomaten und Richter finden in sich eine ruhige Mitte. Gedanken ordnen sich, Entscheidungen wirken durchdachter, und selbst zwischen Licht und Schatten scheint kurz Frieden möglich.

Doch wo alles abgewogen wird, verliert das Herz an Gewicht. Wesen, die aus Leidenschaft handeln, deren Kraft aus Glaube, Wut oder Vision geboren ist, geraten ins Straucheln. Denn Aequitas fordert Vernunft, nicht Feuer.

__**Effekt:**__
- Neutrale Wesen erhalten einen Würfelbonus von +1 auf ALLE Werte
- Alle anderen erhalten einen Würfelmalus von -1, wenn sie ENTGEGEN dem Gleichgewicht handeln.
""",
        "image": "https://cdn.discordapp.com/attachments/1117849423158988840/1391840830188425376/Aequitas.png"
    },
    {
        "title": "Corvus' Flüstern",
        "text": """**Wenn das dunkle Sternbild Corvus seine Bahn über den Himmel zieht, wird der Schleier zwischen den Schatten dünner.**
In dieser Zeit erstarken jene, die im Verborgenen wirken: Schattenwesen, Nekromanten, Täuscher und Geisterflüsterer. Ihre Kräfte fließen leichter, Lügen klingen süßer, und das Unsichtbare gehorcht schneller.

Manche sagen, Corvus flüstert selbst, in den Ohren jener, die bereit sind zu hören. Und was er sagt, ist selten harmlos.

Doch Lichtwesen spüren diese Zeit wie ein Frösteln unter der Haut. Heilkräfte schwächen sich ab, Worte verfangen sich, und der moralische Kompass flackert, denn der Blick in den Abgrund verlangt mehr, als nur festen Willen.

__**Effekt:**__
- Schattenwesen und böse Wesen erhalten einen Würfelbonus von +1 auf ALLE Werte
- Lichtwesen und gute Wesen erhalten einen Würfelmalus von -1 auf ALLE Werte
""",
        "image": "https://cdn.discordapp.com/attachments/1117849423158988840/1391840834172748007/Corvus.png"
    },
    {
        "title": "Kassiopeias Versuchung",
        "text": """**Wenn Kassiopeia ihr Antlitz über den Nachthimmel legt, liegt ein flimmernder Reiz in der Luft.**
In dieser Zeit werden Blicke schwerer, Stimmen weicher, und selbst flüchtige Gesten laden sich mit Bedeutung. Wesen mit Schönheit, Charme oder feinem Gespür für Nähe finden sich plötzlich im Mittelpunkt. Nicht durch Absicht, sondern durch Wirkung.

Verführung fällt leichter, Hemmungen sinken schneller und selbst das Unausgesprochene beginnt zu wirken. Doch wo Nähe wächst, bröckelt auch der Schutz. Wer sonst mit Disziplin oder Willenskraft Grenzen wahrt, spürt sie nun verschwimmen.

__**Effekt:**__
- Charismawerte erhalten einen Würfelbonus von +1
- Willenskraft- und Intelligenzwerte erhalten einen Würfelmalus von -1
- Optional: Allgemein fühlt man sich körperlich wohl eher zu anderen hingezogen und die Lust ist gesteigert
""",
        "image": "https://cdn.discordapp.com/attachments/1117849423158988840/1391840834931920988/Kassiopeia.png"
    },
    {
        "title": "Neumond – Die Stunde des Schweigens",
        "text": """**Wenn der Mond vom Himmel verschwindet, beginnt die Zeit des Schweigens.**
Die Welt wirkt stiller, schwerer – als hätte selbst das Licht den Atem angehalten. Gedanken wandern tiefer, Worte klingen dumpfer, und Schatten fließen lautlos über den Boden. In dieser Nacht erwachen jene, die in der Tiefe horchen: Seher, Träumer, Schattenwesen.

Es ist eine Zeit der Rückkehr nach innen, der verborgenen Erkenntnisse – und der leisen Prüfungen.

__**Effekt:**__
- Für Wesen der Dunkelheit, des Inneren oder der Tiefe +1 Würfelbonus auf intuitive Wahrnehmung, Vorahnungen oder seelisches Erspüren
- Für Lichtwesen, Barden, charismatische Führer wirken matter –1 Würfelmalus auf Ausstrahlung, Charisma und lichtgebundene Präsenz
- Optional: Träume verdichten sich, Einsamkeit ruft, Entscheidungen wirken schwer. Viele ziehen sich zurück – aus Angst, aus Schutz, oder weil die Welt zu laut ist.
""",
        "image": "https://cdn.discordapp.com/attachments/1117849423158988840/1391840835485696050/Neumond.png"
    },
]

STATE_FILE = "event_state.json"

def load_state():
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f)

def post_event(event_idx, event_start, event_end):
    event = events[event_idx]
    embed = {
        "title": event["title"],
        "description": f"{event['text']}\n\n__**Start:**__ <t:{int(event_start.timestamp())}:f>\n__**Ende:**__ <t:{int(event_end.timestamp())}:f>",
        "image": {"url": event["image"]},
        "color": 0x7395A6
    }
    data = {"embeds": [embed]}
    requests.post(WEBHOOK_URL, json=data)

def main():
    keep_alive()
    while True:
        # --- NEU: immer den aktuellen State und Index laden ---
        state = load_state()
        event_idx = state.get("event_idx", 0)
        last_event_time_str = state.get("last_event_time")
        if last_event_time_str:
            last_event_time = datetime.fromisoformat(last_event_time_str)
        else:
            last_event_time = START_DATETIME - timedelta(days=EVENT_INTERVAL_DAYS)

        now = datetime.now()
        next_event_start = last_event_time + timedelta(days=EVENT_INTERVAL_DAYS)
        if now < next_event_start:
            to_wait = (next_event_start - now).total_seconds()
            print(f"Nächstes Event: {events[event_idx]['title']} am {next_event_start}. Warte {to_wait/3600:.1f} Stunden...")
            time.sleep(max(60, to_wait))
            continue

        next_event_end = next_event_start + timedelta(days=1)
        print(f"Poste Event {event_idx+1}: {events[event_idx]['title']}")
        post_event(event_idx, next_event_start, next_event_end)
        # --- State updaten & speichern ---
        state["event_idx"] = (event_idx + 1) % len(events)
        state["last_event_time"] = next_event_start.isoformat()
        save_state(state)
        time.sleep(EVENT_INTERVAL_DAYS * 24 * 60 * 60)

if __name__ == "__main__":
    main()
