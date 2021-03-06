# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..postproc import SplineFilter


def test_SplineFilter_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        output_file=dict(argstr="%s", extensions=None, position=2, usedefault=True,),
        step_length=dict(argstr="%f", mandatory=True, position=1,),
        track_file=dict(argstr="%s", extensions=None, mandatory=True, position=0,),
    )
    inputs = SplineFilter.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_SplineFilter_outputs():
    output_map = dict(smoothed_track_file=dict(extensions=None,),)
    outputs = SplineFilter.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
