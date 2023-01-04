# machine-readable_anwendungshandbuecher

Dieses Repository enthält Anwendungshandbücher (AHB) in einem maschinenlesbaren Format, das deutlich einfacher zu verarbeiten ist als `.docx` oder `.pdf`.

## Unter der Haube

Zur Erstellung der hier veröffentlichten Daten nutzen wir [`kohlrahbi`](https://github.com/Hochfrequenz/kohlrahbi/), eine Open Source AHB Scraping Library.

## Struktur

Zur Strukturierung nutzen wir nicht die Format- oder AHB-Versionen (z.B. UTILMD `5.2e` oder GPKE AHB `6.1e`), sondern lediglich den Zeitraum zu dem die Daten gültig sind.
Beispielsweise bezeichnet `FV2210` die Datenformate, die seit 2022-10-01 gültig sind oder `FV2304` die Datenformate, die seit 2023-04-01 gültig sind.

## Motivation

Wir freuen uns über jede durch dieses Repository ersparte Stunde Arbeit, in der wichtige Probleme gelöst werden können anstatt AHBs zu scrapen.

## Urheberrecht

Das Urheberrecht der hier versionierten Daten liegt bei EDI@energy bzw. den Autor\*innen der Anwendungshandbücher selbst.
Dieses Repository macht die Daten aus den AHBs lediglich leichter zugänglich.
Hochfrequenz garantiert weder für die Korrektheit noch die Vollständigkeit der hier bereitgestellten Daten, stellt aber selbst auch keine Bedingungen an deren Nutzung.

## Rückmeldungen & Mitwirken

Es ist sehr wahrscheinlich, dass die hier bereitgestellten Daten nicht fehlerfrei sind.
Probleme oder Fehler können gerne als [Issue](https://github.com/Hochfrequenz/machine-readable_anwendungshandbuecher/issues/new) gemeldet werden.
Weil die Daten in diesem Repository aber maschinell erstellt und ggf. überschrieben werden, sind manuelle Anpassungen bzw Pull Requests nicht langfristig hilfreich.
Besser ist es, das Scraping in [`kohlrahbi`](https://github.com/Hochfrequenz/kohlrahbi/) zu fixen.

## Weiterführendes Tooling

Dieses Repository ist Teil der [Hochfrequenz Libraries und Tool für eine echte Digitalisierung der Marktkommunikation](https://github.com/Hochfrequenz/digital_market_communication/).
Insbesondere die Daten aus unserem [Bedingungen- und Pakete-Repository](https://github.com/Hochfrequenz/edi_energy_ahb_conditions_and_packages) könnten ebenfalls relevant sein.
