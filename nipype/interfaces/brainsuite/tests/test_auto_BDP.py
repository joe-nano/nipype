# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..brainsuite import BDP


def test_BDP_inputs():
    input_map = dict(
        BVecBValPair=dict(
            argstr='--bvec %s --bval %s',
            mandatory=True,
            position=-1,
            xor=['bMatrixFile'],
        ),
        args=dict(argstr='%s', ),
        bMatrixFile=dict(
            argstr='--bmat %s',
            mandatory=True,
            position=-1,
            xor=['BVecBValPair'],
        ),
        bValRatioThreshold=dict(argstr='--bval-ratio-threshold %f', ),
        bfcFile=dict(
            argstr='%s',
            mandatory=True,
            position=0,
            xor=['noStructuralRegistration'],
        ),
        customDiffusionLabel=dict(argstr='--custom-diffusion-label %s', ),
        customLabelXML=dict(argstr='--custom-label-xml %s', ),
        customT1Label=dict(argstr='--custom-t1-label %s', ),
        dataSinkDelay=dict(argstr='%s', ),
        dcorrRegMeasure=dict(argstr='--dcorr-reg-method %s', ),
        dcorrWeight=dict(argstr='--dcorr-regularization-wt %f', ),
        dwiMask=dict(argstr='--dwi-mask %s', ),
        echoSpacing=dict(argstr='--echo-spacing=%f', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        estimateODF_3DShore=dict(argstr='--3dshore --diffusion_time_ms %f', ),
        estimateODF_FRACT=dict(argstr='--FRACT', ),
        estimateODF_FRT=dict(argstr='--FRT', ),
        estimateTensors=dict(argstr='--tensors', ),
        fieldmapCorrection=dict(
            argstr='--fieldmap-correction %s',
            requires=['echoSpacing'],
        ),
        fieldmapCorrectionMethod=dict(
            argstr='--fieldmap-correction-method %s',
            xor=['skipIntensityCorr'],
        ),
        fieldmapSmooth=dict(argstr='--fieldmap-smooth3=%f', ),
        flagConfigFile=dict(argstr='--flag-conf-file %s', ),
        forcePartialROIStats=dict(argstr='--force-partial-roi-stats', ),
        generateStats=dict(argstr='--generate-stats', ),
        ignoreFieldmapFOV=dict(argstr='--ignore-fieldmap-fov', ),
        ignoreMemory=dict(argstr='--ignore-memory', ),
        inputDiffusionData=dict(
            argstr='--nii %s',
            mandatory=True,
            position=-2,
        ),
        lowMemory=dict(argstr='--low-memory', ),
        noStructuralRegistration=dict(
            argstr='--no-structural-registration',
            mandatory=True,
            position=0,
            xor=['bfcFile'],
        ),
        odfLambta=dict(argstr='--odf-lambda <L>', ),
        onlyStats=dict(argstr='--generate-only-stats', ),
        outPrefix=dict(argstr='--output-fileprefix %s', ),
        outputDiffusionCoordinates=dict(
            argstr='--output-diffusion-coordinate', ),
        outputSubdir=dict(argstr='--output-subdir %s', ),
        phaseEncodingDirection=dict(argstr='--dir=%s', ),
        rigidRegMeasure=dict(argstr='--rigid-reg-measure %s', ),
        skipDistortionCorr=dict(argstr='--no-distortion-correction', ),
        skipIntensityCorr=dict(
            argstr='--no-intensity-correction',
            xor=['fieldmapCorrectionMethod'],
        ),
        skipNonuniformityCorr=dict(argstr='--no-nonuniformity-correction', ),
        t1Mask=dict(argstr='--t1-mask %s', ),
        threads=dict(argstr='--threads=%d', ),
        transformDataOnly=dict(argstr='--transform-data-only', ),
        transformDiffusionSurface=dict(
            argstr='--transform-diffusion-surface %s', ),
        transformDiffusionVolume=dict(
            argstr='--transform-diffusion-volume %s', ),
        transformInterpolation=dict(argstr='--transform-interpolation %s', ),
        transformT1Surface=dict(argstr='--transform-t1-surface %s', ),
        transformT1Volume=dict(argstr='--transform-t1-volume %s', ),
    )
    inputs = BDP.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
