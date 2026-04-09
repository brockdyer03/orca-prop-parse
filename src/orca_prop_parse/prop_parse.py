from warnings import warn
from io import StringIO
from typing import Any
import re
import json
import rtoml

_NESTED_PROP_MAP = {
    "AutoCI_Energies":                        {'super_type': 'Energy', 'key_name': 'AutoCI'},
    "AutoCI_Dipole_Moment":                   {'super_type': 'Dipole_Moment', 'key_name': 'AutoCI'},
    "AutoCI_Polarizability":                  {'super_type': 'Polarizability', 'key_name': 'AutoCI'},
    "AutoCI_Quadrupole_Moment":               {'super_type': 'Quadrupole_Moment', 'key_name': 'AutoCI'},
    "AutoCI_A_Tensor":                        {'super_type': 'A_Tensor', 'key_name': 'AutoCI'},
    "AUTOCI_Chemical_Shift":                  {'super_type': 'Chemical_Shift', 'key_name': 'AUTOCI'},
    "AutoCI_D_Tensor":                        {'super_type': 'D_Tensor', 'key_name': 'AutoCI'},
    "AutoCI_G_Tensor":                        {'super_type': 'G_Tensor', 'key_name': 'AutoCI'},
    "AutoCI_Spin_Spin_Coupling":              {'super_type': 'Spin_Spin_Coupling', 'key_name': 'AutoCI'},
    "AutoCI_Absorption_Spectrum":             {'super_type': 'Absorption_Spectrum', 'key_name': 'AutoCI'},
    "AutoCI_ECD_Spectrum":                    {'super_type': 'ECD_Spectrum', 'key_name': 'AutoCI'},
    "AutoCI_MRCI_Absorption_Spectrum":        {'super_type': 'Absorption_Spectrum', 'key_name': 'AutoCI_MRCI'},
    "AutoCI_MRCI_ECD_Spectrum":               {'super_type': 'ECD_Spectrum', 'key_name': 'AutoCI_MRCI'},
    "CAS_DCD_Energies":                       {'super_type': 'Energy', 'key_name': 'CAS_DCD'},
    "CAS_MSPT2_Energies":                     {'super_type': 'Energy', 'key_name': 'CAS_MSPT2'},
    "CAS_PT2_Energies":                       {'super_type': 'Energy', 'key_name': 'CAS_PT2'},
    "CAS_SCF_Energies":                       {'super_type': 'Energy', 'key_name': 'CAS_SCF'},
    "CASSCF_Dipole_Moment":                   {'super_type': 'Dipole_Moment', 'key_name': 'CASSCF'},
    "CASSCF_EFG_Tensor":                      {'super_type': 'EFG_Tensor', 'key_name': 'CASSCF'},
    "CASSCF_Polarizability":                  {'super_type': 'Polarizability', 'key_name': 'CASSCF'},
    "CASSCF_Quadrupole_Moment":               {'super_type': 'Quadrupole_Moment', 'key_name': 'CASSCF'},
    "CASSCF_A_Tensor":                        {'super_type': 'A_Tensor', 'key_name': 'CASSCF'},
    "CASSCF_Chemical_Shift":                  {'super_type': 'Chemical_Shift', 'key_name': 'CASSCF'},
    "CASSCF_D_Tensor":                        {'super_type': 'D_Tensor', 'key_name': 'CASSCF'},
    "CASSCF_G_Tensor":                        {'super_type': 'G_Tensor', 'key_name': 'CASSCF'},
    "CASSCF_Spin_Spin_Coupling":              {'super_type': 'Spin_Spin_Coupling', 'key_name': 'CASSCF'},
    "D_Tensor_CASSCF_2ndOrder":               {'super_type': 'D_Tensor', 'key_name': 'CASSCF_2ndOrder'},
    "D_Tensor_CASSCF_2ndOrder_ES":            {'super_type': 'D_Tensor', 'key_name': 'CASSCF_2ndOrder_ES'},
    "D_Tensor_CASSCF_Heff":                   {'super_type': 'D_Tensor', 'key_name': 'CASSCF_Heff'},
    "D_Tensor_CASSCF_Heff_ES":                {'super_type': 'D_Tensor', 'key_name': 'CASSCF_Heff_ES'},
    "D_Tensor_NEVPT2_2ndOrder":               {'super_type': 'D_Tensor', 'key_name': 'NEVPT2_2ndOrder'},
    "D_Tensor_NEVPT2_2ndOrder_ES":            {'super_type': 'D_Tensor', 'key_name': 'NEVPT2_2ndOrder_ES'},
    "D_Tensor_NEVPT2_Heff":                   {'super_type': 'D_Tensor', 'key_name': 'NEVPT2_Heff'},
    "D_Tensor_NEVPT2_Heff_ES":                {'super_type': 'D_Tensor', 'key_name': 'NEVPT2_Heff_ES'},
    "D_Tensor_CUSTOM_2ndOrder":               {'super_type': 'D_Tensor', 'key_name': 'CUSTOM_2ndOrder'},
    "D_Tensor_CUSTOM_2ndOrder_ES":            {'super_type': 'D_Tensor', 'key_name': 'CUSTOM_2ndOrder_ES'},
    "D_Tensor_CUSTOM_Heff":                   {'super_type': 'D_Tensor', 'key_name': 'CUSTOM_Heff'},
    "D_Tensor_CUSTOM_Heff_ES":                {'super_type': 'D_Tensor', 'key_name': 'CUSTOM_Heff_ES'},
    "G_Tensor_CASSCF_2ndOrder":               {'super_type': 'G_Tensor', 'key_name': 'CASSCF_2ndOrder'},
    "G_Tensor_CASSCF_Heff":                   {'super_type': 'G_Tensor', 'key_name': 'CASSCF_Heff'},
    "G_Tensor_NEVPT2_2ndOrder":               {'super_type': 'G_Tensor', 'key_name': 'NEVPT2_2ndOrder'},
    "G_Tensor_NEVPT2_Heff":                   {'super_type': 'G_Tensor', 'key_name': 'NEVPT2_Heff'},
    "G_Tensor_CUSTOM_2ndOrder":               {'super_type': 'G_Tensor', 'key_name': 'CUSTOM_2ndOrder'},
    "G_Tensor_CUSTOM_Heff":                   {'super_type': 'G_Tensor', 'key_name': 'CUSTOM_Heff'},
    "CASSCF_Absorption_Spectrum":             {'super_type': 'Absorption_Spectrum', 'key_name': 'CASSCF'},
    "CASSCF_PT_Absorption_Spectrum":          {'super_type': 'Absorption_Spectrum', 'key_name': 'CASSCF_PT'},
    "CASSCF_QDPT_Absorption_Spectrum":        {'super_type': 'Absorption_Spectrum', 'key_name': 'CASSCF_QDPT'},
    "CASSCF_DCD_Absorption_Spectrum":         {'super_type': 'Absorption_Spectrum', 'key_name': 'CASSCF_DCD'},
    "CASSCF_PT_Energies_Absorption_Spectrum": {'super_type': 'Absorption_Spectrum', 'key_name': 'CASSCF_PT_Energies'},
    "CASSCF_Custom_Absorption_Spectrum":      {'super_type': 'Absorption_Spectrum', 'key_name': 'CASSCF_Custom'},
    "CASSCF_ECD_Spectrum":                    {'super_type': 'ECD_Spectrum', 'key_name': 'CASSCF'},
    "CASSCF_PT_ECD_Spectrum":                 {'super_type': 'ECD_Spectrum', 'key_name': 'CASSCF_PT'},
    "CASSCF_QDPT_ECD_Spectrum":               {'super_type': 'ECD_Spectrum', 'key_name': 'CASSCF_QDPT'},
    "CASSCF_DCD_ECD_Spectrum":                {'super_type': 'ECD_Spectrum', 'key_name': 'CASSCF_DCD'},
    "CASSCF_Custom_ECD_Spectrum":             {'super_type': 'ECD_Spectrum', 'key_name': 'CASSCF_Custom'},
    "CIS_Energies":                           {'super_type': 'Energy', 'key_name': 'CIS'},
    "CIS_Nuc_Gradient":                       {'super_type': 'Nuclear_Gradient', 'key_name': 'CIS'},
    "CIS_Dipole_Moment":                      {'super_type': 'Dipole_Moment', 'key_name': 'CIS'},
    "CIS_EFG_Tensor":                         {'super_type': 'EFG_Tensor', 'key_name': 'CIS'},
    "CIS_Polarizability":                     {'super_type': 'Polarizability', 'key_name': 'CIS'},
    "CIS_Quadrupole_Moment":                  {'super_type': 'Quadrupole_Moment', 'key_name': 'CIS'},
    "CIS_A_Tensor":                           {'super_type': 'A_Tensor', 'key_name': 'CIS'},
    "CIS_Chemical_Shift":                     {'super_type': 'Chemical_Shift', 'key_name': 'CIS'},
    "CIS_D_Tensor":                           {'super_type': 'D_Tensor', 'key_name': 'CIS'},
    "CIS_G_Tensor":                           {'super_type': 'G_Tensor', 'key_name': 'CIS'},
    "CIS_Spin_Spin_Coupling":                 {'super_type': 'Spin_Spin_Coupling', 'key_name': 'CIS'},
    "CIS_Absorption_Spectrum":                {'super_type': 'Absorption_Spectrum', 'key_name': 'CIS'},
    "CIS_ECD_Spectrum":                       {'super_type': 'ECD_Spectrum', 'key_name': 'CIS'},
    "ICE_Dipole_Moment":                      {'super_type': 'Dipole_Moment', 'key_name': 'ICE'},
    "ICE_EFG_Tensor":                         {'super_type': 'EFG_Tensor', 'key_name': 'ICE'},
    "ICE_Polarizability":                     {'super_type': 'Polarizability', 'key_name': 'ICE'},
    "ICE_Quadrupole_Moment":                  {'super_type': 'Quadrupole_Moment', 'key_name': 'ICE'},
    "ICE_A_Tensor":                           {'super_type': 'A_Tensor', 'key_name': 'ICE'},
    "ICE_Chemical_Shift":                     {'super_type': 'Chemical_Shift', 'key_name': 'ICE'},
    "ICE_D_Tensor":                           {'super_type': 'D_Tensor', 'key_name': 'ICE'},
    "ICE_G_Tensor":                           {'super_type': 'G_Tensor', 'key_name': 'ICE'},
    "ICE_Spin_Spin_Coupling":                 {'super_type': 'Spin_Spin_Coupling', 'key_name': 'ICE'},
    "ICE_Absorption_Spectrum":                {'super_type': 'Absorption_Spectrum', 'key_name': 'ICE'},
    "ICE_ECD_Spectrum":                       {'super_type': 'ECD_Spectrum', 'key_name': 'ICE'},
    "LFT_Absorption_Spectrum":                {'super_type': 'Absorption_Spectrum', 'key_name': 'LFT'},
    "LFT_ECD_Spectrum":                       {'super_type': 'ECD_Spectrum', 'key_name': 'LFT'},
    "MCRPA_Dipole_Moment":                    {'super_type': 'Dipole_Moment', 'key_name': 'MCRPA'},
    "MCRPA_EFG_Tensor":                       {'super_type': 'EFG_Tensor', 'key_name': 'MCRPA'},
    "MCRPA_Polarizability":                   {'super_type': 'Polarizability', 'key_name': 'MCRPA'},
    "MCRPA_Quadrupole_Moment":                {'super_type': 'Quadrupole_Moment', 'key_name': 'MCRPA'},
    "MCRPA_A_Tensor":                         {'super_type': 'A_Tensor', 'key_name': 'MCRPA'},
    "MCRPA_Chemical_Shift":                   {'super_type': 'Chemical_Shift', 'key_name': 'MCRPA'},
    "MCRPA_D_Tensor":                         {'super_type': 'D_Tensor', 'key_name': 'MCRPA'},
    "MCRPA_G_Tensor":                         {'super_type': 'G_Tensor', 'key_name': 'MCRPA'},
    "MCRPA_Spin_Spin_Coupling":               {'super_type': 'Spin_Spin_Coupling', 'key_name': 'MCRPA'},
    "MCRPA_Absorption_Spectrum":              {'super_type': 'Absorption_Spectrum', 'key_name': 'MCRPA'},
    "MCRPA_ECD_Spectrum":                     {'super_type': 'ECD_Spectrum', 'key_name': 'MCRPA'},
    "MDCI_Energies":                          {'super_type': 'Energy', 'key_name': 'MDCI'},
    "MDCI_Nuc_Gradient":                      {'super_type': 'Nuclear_Gradient', 'key_name': 'MDCI'},
    "MDCI_Dipole_Moment":                     {'super_type': 'Dipole_Moment', 'key_name': 'MDCI'},
    "MDCI_EFG_Tensor":                        {'super_type': 'EFG_Tensor', 'key_name': 'MDCI'},
    "MDCI_Polarizability":                    {'super_type': 'Polarizability', 'key_name': 'MDCI'},
    "MDCI_Quadrupole_Moment":                 {'super_type': 'Quadrupole_Moment', 'key_name': 'MDCI'},
    "MDCI_A_Tensor":                          {'super_type': 'A_Tensor', 'key_name': 'MDCI'},
    "MDCI_Chemical_Shift":                    {'super_type': 'Chemical_Shift', 'key_name': 'MDCI'},
    "MDCI_D_Tensor":                          {'super_type': 'D_Tensor', 'key_name': 'MDCI'},
    "MDCI_G_Tensor":                          {'super_type': 'G_Tensor', 'key_name': 'MDCI'},
    "MDCI_Spin_Spin_Coupling":                {'super_type': 'Spin_Spin_Coupling', 'key_name': 'MDCI'},
    "MDCI_Absorption_Spectrum":               {'super_type': 'Absorption_Spectrum', 'key_name': 'MDCI'},
    "MDCI_ECD_Spectrum":                      {'super_type': 'ECD_Spectrum', 'key_name': 'MDCI'},
    "MP2_Energies":                           {'super_type': 'Energy', 'key_name': 'MP2'},
    "MP2_Nuc_Gradient":                       {'super_type': 'Nuclear_Gradient', 'key_name': 'MP2'},
    "MP2_Dipole_Moment":                      {'super_type': 'Dipole_Moment', 'key_name': 'MP2'},
    "MP2_EFG_Tensor":                         {'super_type': 'EFG_Tensor', 'key_name': 'MP2'},
    "MP2_Polarizability":                     {'super_type': 'Polarizability', 'key_name': 'MP2'},
    "MP2_Quadrupole_Moment":                  {'super_type': 'Quadrupole_Moment', 'key_name': 'MP2'},
    "MP2_A_Tensor":                           {'super_type': 'A_Tensor', 'key_name': 'MP2'},
    "MP2_Chemical_Shift":                     {'super_type': 'Chemical_Shift', 'key_name': 'MP2'},
    "MP2_D_Tensor":                           {'super_type': 'D_Tensor', 'key_name': 'MP2'},
    "MP2_G_Tensor":                           {'super_type': 'G_Tensor', 'key_name': 'MP2'},
    "MP2_Spin_Spin_Coupling":                 {'super_type': 'Spin_Spin_Coupling', 'key_name': 'MP2'},
    "MP2_Absorption_Spectrum":                {'super_type': 'Absorption_Spectrum', 'key_name': 'MP2'},
    "MP2_ECD_Spectrum":                       {'super_type': 'ECD_Spectrum', 'key_name': 'MP2'},
    "MRCI_Dipole_Moment":                     {'super_type': 'Dipole_Moment', 'key_name': 'MRCI'},
    "MRCI_EFG_Tensor":                        {'super_type': 'EFG_Tensor', 'key_name': 'MRCI'},
    "MRCI_Polarizability":                    {'super_type': 'Polarizability', 'key_name': 'MRCI'},
    "MRCI_Quadrupole_Moment":                 {'super_type': 'Quadrupole_Moment', 'key_name': 'MRCI'},
    "MRCI_A_Tensor":                          {'super_type': 'A_Tensor', 'key_name': 'MRCI'},
    "MRCI_Chemical_Shift":                    {'super_type': 'Chemical_Shift', 'key_name': 'MRCI'},
    "MRCI_D_Tensor":                          {'super_type': 'D_Tensor', 'key_name': 'MRCI'},
    "MRCI_G_Tensor":                          {'super_type': 'G_Tensor', 'key_name': 'MRCI'},
    "MRCI_Spin_Spin_Coupling":                {'super_type': 'Spin_Spin_Coupling', 'key_name': 'MRCI'},
    "D_Tensor_MRCI_2ndOrder":                 {'super_type': 'D_Tensor', 'key_name': 'MRCI_2ndOrder'},
    "D_Tensor_MRCI_2ndOrder_ES":              {'super_type': 'D_Tensor', 'key_name': 'MRCI_2ndOrder_ES'},
    "D_Tensor_MRCI_Heff":                     {'super_type': 'D_Tensor', 'key_name': 'MRCI_Heff'},
    "D_Tensor_MRCI_Heff_ES":                  {'super_type': 'D_Tensor', 'key_name': 'MRCI_Heff_ES'},
    "MRCI_Absorption_Spectrum":               {'super_type': 'Absorption_Spectrum', 'key_name': 'MRCI'},
    "MRCI_ECD_Spectrum":                      {'super_type': 'ECD_Spectrum', 'key_name': 'MRCI'},
    "RASCI_Nuc_Gradient":                     {'super_type': 'Nuclear_Gradient', 'key_name': 'RASCI'},
    "RASCI_Dipole_Moment":                    {'super_type': 'Dipole_Moment', 'key_name': 'RASCI'},
    "RASCI_EFG_Tensor":                       {'super_type': 'EFG_Tensor', 'key_name': 'RASCI'},
    "RASCI_Polarizability":                   {'super_type': 'Polarizability', 'key_name': 'RASCI'},
    "RASCI_Quadrupole_Moment":                {'super_type': 'Quadrupole_Moment', 'key_name': 'RASCI'},
    "RASCI_A_Tensor":                         {'super_type': 'A_Tensor', 'key_name': 'RASCI'},
    "RASCI_Chemical_Shift":                   {'super_type': 'Chemical_Shift', 'key_name': 'RASCI'},
    "RASCI_D_Tensor":                         {'super_type': 'D_Tensor', 'key_name': 'RASCI'},
    "RASCI_G_Tensor":                         {'super_type': 'G_Tensor', 'key_name': 'RASCI'},
    "RASCI_Spin_Spin_Coupling":               {'super_type': 'Spin_Spin_Coupling', 'key_name': 'RASCI'},
    "RASCI_Absorption_Spectrum":              {'super_type': 'Absorption_Spectrum', 'key_name': 'RASCI'},
    "RASCI_ECD_Spectrum":                     {'super_type': 'ECD_Spectrum', 'key_name': 'RASCI'},
    "ROCIS_Dipole_Moment":                    {'super_type': 'Dipole_Moment', 'key_name': 'ROCIS'},
    "ROCIS_EFG_Tensor":                       {'super_type': 'EFG_Tensor', 'key_name': 'ROCIS'},
    "ROCIS_Polarizability":                   {'super_type': 'Polarizability', 'key_name': 'ROCIS'},
    "ROCIS_Quadrupole_Moment":                {'super_type': 'Quadrupole_Moment', 'key_name': 'ROCIS'},
    "ROCIS_A_Tensor":                         {'super_type': 'A_Tensor', 'key_name': 'ROCIS'},
    "ROCIS_Chemical_Shift":                   {'super_type': 'Chemical_Shift', 'key_name': 'ROCIS'},
    "ROCIS_D_Tensor":                         {'super_type': 'D_Tensor', 'key_name': 'ROCIS'},
    "ROCIS_G_Tensor":                         {'super_type': 'G_Tensor', 'key_name': 'ROCIS'},
    "ROCIS_Spin_Spin_Coupling":               {'super_type': 'Spin_Spin_Coupling', 'key_name': 'ROCIS'},
    "ROCIS_Absorption_Spectrum":              {'super_type': 'Absorption_Spectrum', 'key_name': 'ROCIS'},
    "ROCIS_ECD_Spectrum":                     {'super_type': 'ECD_Spectrum', 'key_name': 'ROCIS'},
    "RPA_Dipole_Moment":                      {'super_type': 'Dipole_Moment', 'key_name': 'RPA'},
    "RPA_EFG_Tensor":                         {'super_type': 'EFG_Tensor', 'key_name': 'RPA'},
    "RPA_Polarizability":                     {'super_type': 'Polarizability', 'key_name': 'RPA'},
    "RPA_Quadrupole_Moment":                  {'super_type': 'Quadrupole_Moment', 'key_name': 'RPA'},
    "RPA_A_Tensor":                           {'super_type': 'A_Tensor', 'key_name': 'RPA'},
    "RPA_Chemical_Shift":                     {'super_type': 'Chemical_Shift', 'key_name': 'RPA'},
    "RPA_D_Tensor":                           {'super_type': 'D_Tensor', 'key_name': 'RPA'},
    "RPA_G_Tensor":                           {'super_type': 'G_Tensor', 'key_name': 'RPA'},
    "RPA_Spin_Spin_Coupling":                 {'super_type': 'Spin_Spin_Coupling', 'key_name': 'RPA'},
    "RPA_Absorption_Spectrum":                {'super_type': 'Absorption_Spectrum', 'key_name': 'RPA'},
    "RPA_ECD_Spectrum":                       {'super_type': 'ECD_Spectrum', 'key_name': 'RPA'},
    "SCF_Energy":                             {'super_type': 'Energy', 'key_name': 'SCF'},
    "SCF_Nuc_Gradient":                       {'super_type': 'Nuclear_Gradient', 'key_name': 'SCF'},
    "SCF_Dipole_Moment":                      {'super_type': 'Dipole_Moment', 'key_name': 'SCF'},
    "SCF_EFG_Tensor":                         {'super_type': 'EFG_Tensor', 'key_name': 'SCF'},
    "SCF_Polarizability":                     {'super_type': 'Polarizability', 'key_name': 'SCF'},
    "SCF_Quadrupole_Moment":                  {'super_type': 'Quadrupole_Moment', 'key_name': 'SCF'},
    "SCF_A_Tensor":                           {'super_type': 'A_Tensor', 'key_name': 'SCF'},
    "SCF_Chemical_Shift":                     {'super_type': 'Chemical_Shift', 'key_name': 'SCF'},
    "SCF_D_Tensor":                           {'super_type': 'D_Tensor', 'key_name': 'SCF'},
    "SCF_G_Tensor":                           {'super_type': 'G_Tensor', 'key_name': 'SCF'},
    "SCF_Spin_Spin_Coupling":                 {'super_type': 'Spin_Spin_Coupling', 'key_name': 'SCF'},
    "SCF_Absorption_Spectrum":                {'super_type': 'Absorption_Spectrum', 'key_name': 'SCF'},
    "SCF_ECD_Spectrum":                       {'super_type': 'ECD_Spectrum', 'key_name': 'SCF'},
    "CASPT2_Dipole_Moment":                   {'super_type': 'Dipole_Moment', 'key_name': 'CASPT2'},
    "CAS_CUSTOM_Dipole_Moment":               {'super_type': 'Dipole_Moment', 'key_name': 'CAS_CUSTOM'},
    "CASPT2_G_Tensor":                        {'super_type': 'G_Tensor', 'key_name': 'CASPT2'},
}

class OrcaPropParse:
    """Parsing and conversion for ORCA's ``.property.txt`` files"""

    @classmethod
    def _parse_props(cls, prop_io: StringIO, num_geoms: int) -> dict[str, Any]:
        prop_dict = {"Geometries": [{} for _ in range(num_geoms)]}
        while True:
            line = prop_io.readline()
            if line == "":
                break
            elif line.startswith("$Calculation_"):
                prop = line[1:].strip()
                prop_info, geom_number = cls._parse_prop(prop_io)
                prop_dict[prop] = prop_info
            elif line.startswith("$"):
                prop = line[1:].strip()
                prop_info, geom_number = cls._parse_prop(prop_io)
                if prop in _NESTED_PROP_MAP.keys():
                    super_type = _NESTED_PROP_MAP[prop]["super_type"]
                    prop_name = _NESTED_PROP_MAP[prop]["key_name"]
                    if super_type not in prop_dict["Geometries"][geom_number]:
                        prop_dict["Geometries"][geom_number][super_type] = {}

                    prop_dict["Geometries"][geom_number][super_type][prop_name] = prop_info
                else:
                    prop_dict["Geometries"][geom_number][prop] = prop_info
        return prop_dict

    @classmethod
    def loads(cls, prop_str: str) -> dict[str, Any]:
        num_geoms = max(map(int, re.findall(r"&GeometryIndex ([0-9]+)", prop_str)))
        prop_io = StringIO(prop_str)
        return cls._parse_props(prop_io, num_geoms)

    @classmethod
    def _parse_prop(cls, prop_io: StringIO) -> tuple[dict[str, Any], int]:
        prop_dict = {}
        geom_number = int(prop_io.readline().split()[-1]) - 1 # &GeometryIndex N
        line = prop_io.readline()
        while line.strip() != "$End":
            comp_name = line.split(maxsplit=1)[0].replace("&", "")

            dtype, dimensions, units = re.search(
                r'\[&Type "(\w+)"(?:, &Dim ?\(([0-9]+,[0-9]+)\)|, &Units "([-\.\w^]+)"){0,2}\]',
                line,
            ).groups()
            if dimensions is not None:
                dimensions = tuple(map(int, dimensions.split(",")))

            match dtype:
                case "Double":
                    prop_dict[comp_name] = float(re.search(r'\b([-\+]?[0-9]\.[0-9]+(?:[e][-\+]?[\.0-9]+)?)\b', line).group(1))
                case "Integer":
                    prop_dict[comp_name] = int(re.search(r'\b([0-9]+)\b', line).group(1))
                case "Boolean":
                    prop_dict[comp_name] = "true" in line
                case "Complex":
                    warn("Complex number parsing has not been tested!")
                    real, imag = re.search(
                        r'\b([-\+]?[0-9]\.[0-9]+(?:[e][-\+]?[\.0-9]+)?) ([-\+]?[0-9]\.[0-9]+(?:[e][-\+]?[\.0-9]+)?)\b',
                        line,
                    ).groups()
                    prop_dict[comp_name] = complex(float(real), float(imag))
                case "String":
                    prop_dict[comp_name] = line.split('] "', maxsplit=1)[-1].split('"', maxsplit=1)[0]
                case "ArrayOfDoubles" | "ArrayOfIntegers" | "ArrayOfBooleans":
                    prop_dict[comp_name] = cls._parse_array(prop_io, dtype, dimensions)
                case "Coordinates":
                    prop_dict[comp_name] = []
                    for _ in range(dimensions[0]):
                        atom = prop_io.readline().strip().split()
                        prop_dict[comp_name].append([
                            atom[0],        # Symbol
                            float(atom[1]), # x
                            float(atom[2]), # y
                            float(atom[3]), # z
                        ])
                case "ArrayOfComplex":
                    raise NotImplementedError(
                        "ArrayOfComplex parsing not yet implemented!\n"
                       f"ArrayOfComplex found at position {prop_io.tell()}!"
                    )
            line = prop_io.readline()

        return prop_dict, geom_number

    @staticmethod
    def _parse_array(
        prop_io: StringIO,
        array_type: str,
        dim: tuple[int, int],
    ) -> list[Any | list[Any]]:

        array = []
        if dim[1] == 1:
            for _ in range(2):
                prop_io.readline() # Skip over 2nd dimension index and comment line

            for _ in range(dim[0]):
                array.append(
                    prop_io.readline().strip().split()[-1]
                )

            match array_type:
                case "ArrayOfDoubles":
                    return list(map(float, array))
                case "ArrayOfIntegers":
                    return list(map(int, array))
                case "ArrayOfBooleans":
                    return list(map(lambda x: x.lower() == "true", array))
                case _:
                    raise ValueError(
                        f"Array type {array_type} not recognized!"
                    )
        else:
            for _ in range(dim[0]):
                array.append([])

            num_blocks = ((dim[1] - (dim[1] % 8)) / 8) + 1 if dim[1] > 8 else 1
            for b in range(num_blocks):
                for _ in range(2):
                    prop_io.readline() # Skip over 2nd dimension index and comment line

                for i in range(dim[0]):
                    line = prop_io.readline().strip().split()
                    arr_index = int(line[0])
                    array[arr_index].extend(line[1:])

            match array_type:
                case "ArrayOfDoubles":
                    return [list(map(float, row)) for row in array]
                case "ArrayOfIntegers":
                    return [list(map(int, row)) for row in array]
                case "ArrayOfBooleans":
                    return [list(map(lambda x: x.lower() == "true", row)) for row in array]
                case _:
                    raise ValueError(
                        f"Array type {array_type} not recognized!"
                    )
