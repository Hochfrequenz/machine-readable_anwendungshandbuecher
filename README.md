# machine-readable_anwendungshandbuecher

> [!WARNING]  
> Dieses Repository wurde bis Ende 2024 [automatisch](https://github.com/Hochfrequenz/edi_energy_mirror/blob/1e42dffe7081d7bc2f0dee93e398300890d0e77c/.github/workflows/kohlrahbi.yml) (mittels [kohlrahbi](https://github.com/Hochfrequenz/kohlrahbi)) mit Informationen aus den `.docx`-Fassungen der Anwendunghandbücher befüllt.
> Wir sind mittlerweile Hochfrequenz-intern auf die (kostenpflichtigen<!-- 🙄 -->) XML-Versionen der Anwendungshandbücher umgestiegen und laden die Anwendungshandbücher, ihre Bedingungen, Pakete und UB-Bedingungen aus den XMLs in eine Datenbank, die wir dann in unsere Anwendungen einbinden.
> (Dazu verwenden wir [fundamend](https://github.com/Hochfrequenz/xml-fundamend-python/?tab=readme-ov-file#bef%C3%BCllen-einer-datenbank-mit-ahb-informationen)).
> Dieses Repository wird daher nicht mehr maintained.

Dieses Repository enthält Anwendungshandbücher (AHB) in einem maschinenlesbaren Format, das deutlich einfacher zu verarbeiten ist als `.docx` oder `.pdf`.
Wir pflegen analog zu den hier abgelegten Daten auch:

- [`edi_energy_ahb_conditions_and_packages`](https://github.com/Hochfrequenz/edi_energy_ahb_conditions_and_packages) für Bedingungen und Paket-Definitionen aus den AHBs
- [`machine-readable_message-implementation-guide`](https://github.com/Hochfrequenz/machine-readable_message-implementation-guide) für MIGs
- [`machine-readable_entscheidungsbaumdiagramme`](https://github.com/Hochfrequenz/machine-readable_entscheidungsbaumdiagramme/) für EBDs

## Unter der Haube

Zur Erstellung der hier veröffentlichten Daten nutzen wir [`kohlrahbi`](https://github.com/Hochfrequenz/kohlrahbi/), eine Open Source AHB Scraping Library.
Änderungen auf edi-energy.de werden mehrmals täglich automatisiert über unseren [edi_energy_mirror](https://github.com/Hochfrequenz/edi_energy_mirror) in dieses Repository synchronisiert.
Zur Weiterverarbeitung der Daten, z.B. einem automatischen Abgleich von AHBs in verschiedenen Versionen, eignet sich [`ahlbatross`](https://github.com/Hochfrequenz/ahlbatross/).

## Struktur & Datenformate

Zur Strukturierung nutzen wir nicht die Format- oder AHB-Versionen (z.B. UTILMD `5.2e` oder GPKE AHB `6.1e`), sondern lediglich den Zeitraum zu dem die Daten gültig sind.
Beispielsweise bezeichnet `FV2210` die Datenformate, die seit 2022-10-01 gültig sind oder `FV2304` die Datenformate, die seit 2023-04-01 gültig sind.

Die Anwendungshandbücher sind als je eine Datei pro Prüfidentifikator in jeweils drei Serialisierungs-Formaten verfügbar:

- CSV
- Excel
- JSON (mit [`FlatAnwendungshandbuch`](https://mig-ahb-utility-stack.readthedocs.io/en/stable/api/maus.models.html#maus.models.anwendungshandbuch.FlatAnwendungshandbuch) aus dem [MIG AHB Utility Stack](https://github.com/Hochfrequenz/mig_ahb_utility_stack/) (maus 🐭) als zugrunde liegendes Datenmodell)

Es macht wenig Sinn binäre Dateiformate wie bpsw. xlsx Dateien in git zu versionieren.
Daher verwenden wir in diesem Repoository Git LFS (Large File Storage) um die Excel-Dateien zu versionieren.
Was Git LFS ist und wie es funktioniert, ist [hier](https://git-lfs.github.com/) beschrieben.
Gitkraken hat auch eine [eigene Anleitung](https://help.gitkraken.com/gitkraken-client/git-lfs/) für Git LFS.

## Motivation

Wir freuen uns über jede durch dieses Repository ersparte Stunde Arbeit, in der wichtige Probleme gelöst werden können anstatt AHBs zu scrapen.

## Urheberrecht

Das Urheberrecht der hier versionierten Daten liegt bei EDI@energy bzw. den Autor\*innen der Anwendungshandbücher selbst.
Dieses Repository macht die Daten aus den AHBs lediglich leichter zugänglich.
Hochfrequenz garantiert weder für die Korrektheit noch die Vollständigkeit der hier bereitgestellten Daten.

## Rückmeldungen & Mitwirken

Es ist sehr wahrscheinlich, dass die hier bereitgestellten Daten nicht fehlerfrei sind.
Probleme oder Fehler können gerne als [Issue](https://github.com/Hochfrequenz/machine-readable_anwendungshandbuecher/issues/new) gemeldet werden.
Weil die Daten in diesem Repository aber maschinell erstellt und ggf. überschrieben werden, sind manuelle Anpassungen bzw Pull Requests nicht langfristig hilfreich.
Besser ist es, das Scraping in [`kohlrahbi`](https://github.com/Hochfrequenz/kohlrahbi/) zu fixen.

## Weiterführendes Tooling

Dieses Repository ist Teil der [Hochfrequenz Libraries und Tool für eine echte Digitalisierung der Marktkommunikation](https://github.com/Hochfrequenz/digital_market_communication/).
