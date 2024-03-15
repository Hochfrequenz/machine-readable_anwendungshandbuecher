"""
This module extracts ConditionKeyConditionTextMappings from all AHBs and dumps them into files
which are consistent with https://github.com/Hochfrequenz/edi_energy_ahb_conditions_and_packages
"""
# the requirements are installed in the GitHub Action: See .github/workflows/extract_conditions.yml
import json
import re
import sys
from csv import DictReader
from pathlib import Path

from ahbicht.mapping_results import (
    ConditionKeyConditionTextMapping,
    ConditionKeyConditionTextMappingSchema,
)
from maus.edifact import EdifactFormat, EdifactFormatVersion
from maus.models.anwendungshandbuch import FlatAnwendungshandbuchSchema
from maus.reader.flat_ahb_reader import FlatAhbCsvReader


_machine_readable_ahb_repo_root = Path(__file__).parent.parent
_edi_energy_conditions_repo_root = _machine_readable_ahb_repo_root.parent / Path(
    "edi_energy_ahb_conditions_and_packages"
)
_flat_ahb_schema = FlatAnwendungshandbuchSchema()
_known_formats = {str(x) for x in list(EdifactFormat)}
_fv_pattern = re.compile(r"^FV\d{4}$")
if __name__ == "__main__":
    if sys.version_info.major != 3 or sys.version_info.minor < 11:
        sys.exit("Python 3.11 is required to run this script")
    repo_root = Path(
        "C:/github/machine-readable_anwendungshandbuecher2/"
    )  # Path(__file__).parent.parent
    for directory_path in repo_root.iterdir():
        directory_name = directory_path.name
        if not _fv_pattern.match(directory_name):
            continue
        format_version = EdifactFormatVersion(directory_name)
        for format_path in directory_path.iterdir():
            if not format_path.is_dir() or not format_path.name in _known_formats:
                continue
            edifact_format = EdifactFormat(format_path.name)
            format_flat_ahbs_path = format_path / "csv"
            format_bedingungen: dict[str, str] = {}
            if not format_flat_ahbs_path.exists() or not format_flat_ahbs_path.is_dir():
                continue
            for ahb_csv_path in format_flat_ahbs_path.glob("*.csv"):
                pruefi = ahb_csv_path.stem
                with open(ahb_csv_path, "r", encoding="utf-8") as ahb_csv_file:
                    reader = DictReader(ahb_csv_file, delimiter=",")
                    ahb_bedingungen: dict[str, str] = {}
                    for row in reader:
                        if not "Bedingung" in row:
                            continue
                        row_bedingungen = FlatAhbCsvReader._extract_bedingungen(  # pylint:disable=protected-access
                            row["Bedingung"]
                        )
                        if any(row_bedingungen):
                            format_bedingungen.update(row_bedingungen)
            all_mappings_dict: dict[str, ConditionKeyConditionTextMapping] = {
                key: ConditionKeyConditionTextMapping(
                    edifact_format=edifact_format,
                    condition_key=key,
                    condition_text=value,
                )
                for key, value in format_bedingungen.items()
            }
            all_mappings_list = list(all_mappings_dict.values())
            all_mappings_list.sort(key=lambda x: x.condition_key.zfill(4))
            all_mappings_plain_dict_list: list[
                dict
            ] = ConditionKeyConditionTextMappingSchema().dump(
                all_mappings_list, many=True
            )
            file_path = _edi_energy_conditions_repo_root / Path(
                f"{format_version}/{edifact_format}/conditions.json"
            )
            Path.mkdir(file_path.parent, parents=True, exist_ok=True)
            with open(file_path, "w+", encoding="utf-8") as outfile:
                # the file name has to be the same as in the GitHub Action
                json.dump(
                    all_mappings_plain_dict_list,
                    outfile,
                    indent=2,
                    sort_keys=True,
                    ensure_ascii=True,
                )
