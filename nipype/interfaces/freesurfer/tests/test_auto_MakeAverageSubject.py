# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import MakeAverageSubject


def test_MakeAverageSubject_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        out_name=dict(
            argstr='--out %s',
            usedefault=True,
        ),
        subjects_dir=dict(),
        subjects_ids=dict(
            argstr='--subjects %s',
            mandatory=True,
            sep=' ',
        ),
    )
    inputs = MakeAverageSubject.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_MakeAverageSubject_outputs():
    output_map = dict(average_subject_name=dict(), )
    outputs = MakeAverageSubject.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
