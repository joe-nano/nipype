# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..convert import CFFConverter


def test_CFFConverter_inputs():
    input_map = dict(
        creator=dict(),
        data_files=dict(),
        description=dict(usedefault=True, ),
        email=dict(),
        gifti_labels=dict(),
        gifti_surfaces=dict(),
        gpickled_networks=dict(),
        graphml_networks=dict(),
        license=dict(),
        nifti_volumes=dict(),
        out_file=dict(usedefault=True, ),
        publisher=dict(),
        references=dict(),
        relation=dict(),
        rights=dict(),
        script_files=dict(),
        species=dict(usedefault=True, ),
        timeseries_files=dict(),
        title=dict(),
        tract_files=dict(),
    )
    inputs = CFFConverter.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_CFFConverter_outputs():
    output_map = dict(connectome_file=dict(), )
    outputs = CFFConverter.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
