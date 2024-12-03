import os

from paraview.simple import *

def load_settings(setting_dir, sample_name):
    settings_fname = os.path.join(setting_dir, f"{sample_name}.json")
    with open(settings_fname, "r") as file:
        settings = json.load(file)
    return settings
def plot_fibers(fname, outname):
    # trace generated using paraview version 5.12.1
    #import paraview
    #paraview.compatibility.major = 5
    #paraview.compatibility.minor = 12

    #### import the simple module from the paraview
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # create a new 'Xdmf3 Reader T'
    microstructure_vizxdmf = Xdmf3ReaderT(registrationName='microstructure_viz.xdmf', FileName=[fname])
    microstructure_vizxdmf.PointArrays = []
    microstructure_vizxdmf.CellArrays = []
    microstructure_vizxdmf.Sets = []

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    microstructure_vizxdmfDisplay = Show(microstructure_vizxdmf, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    microstructure_vizxdmfDisplay.Selection = None
    microstructure_vizxdmfDisplay.Representation = 'Surface'
    microstructure_vizxdmfDisplay.ColorArrayName = [None, '']
    microstructure_vizxdmfDisplay.LookupTable = None
    microstructure_vizxdmfDisplay.MapScalars = 1
    microstructure_vizxdmfDisplay.MultiComponentsMapping = 0
    microstructure_vizxdmfDisplay.InterpolateScalarsBeforeMapping = 1
    microstructure_vizxdmfDisplay.UseNanColorForMissingArrays = 0
    microstructure_vizxdmfDisplay.Opacity = 1.0
    microstructure_vizxdmfDisplay.PointSize = 2.0
    microstructure_vizxdmfDisplay.LineWidth = 1.0
    microstructure_vizxdmfDisplay.RenderLinesAsTubes = 0
    microstructure_vizxdmfDisplay.RenderPointsAsSpheres = 0
    microstructure_vizxdmfDisplay.Interpolation = 'Gouraud'
    microstructure_vizxdmfDisplay.Specular = 0.0
    microstructure_vizxdmfDisplay.SpecularColor = [1.0, 1.0, 1.0]
    microstructure_vizxdmfDisplay.SpecularPower = 100.0
    microstructure_vizxdmfDisplay.Luminosity = 0.0
    microstructure_vizxdmfDisplay.Ambient = 0.0
    microstructure_vizxdmfDisplay.Diffuse = 1.0
    microstructure_vizxdmfDisplay.Roughness = 0.3
    microstructure_vizxdmfDisplay.Metallic = 0.0
    microstructure_vizxdmfDisplay.EdgeTint = [1.0, 1.0, 1.0]
    microstructure_vizxdmfDisplay.Anisotropy = 0.0
    microstructure_vizxdmfDisplay.AnisotropyRotation = 0.0
    microstructure_vizxdmfDisplay.BaseIOR = 1.5
    microstructure_vizxdmfDisplay.CoatStrength = 0.0
    microstructure_vizxdmfDisplay.CoatIOR = 2.0
    microstructure_vizxdmfDisplay.CoatRoughness = 0.0
    microstructure_vizxdmfDisplay.CoatColor = [1.0, 1.0, 1.0]
    microstructure_vizxdmfDisplay.SelectTCoordArray = 'None'
    microstructure_vizxdmfDisplay.SelectNormalArray = 'None'
    microstructure_vizxdmfDisplay.SelectTangentArray = 'None'
    microstructure_vizxdmfDisplay.Texture = None
    microstructure_vizxdmfDisplay.RepeatTextures = 1
    microstructure_vizxdmfDisplay.InterpolateTextures = 0
    microstructure_vizxdmfDisplay.SeamlessU = 0
    microstructure_vizxdmfDisplay.SeamlessV = 0
    microstructure_vizxdmfDisplay.UseMipmapTextures = 0
    microstructure_vizxdmfDisplay.ShowTexturesOnBackface = 1
    microstructure_vizxdmfDisplay.BaseColorTexture = None
    microstructure_vizxdmfDisplay.NormalTexture = None
    microstructure_vizxdmfDisplay.NormalScale = 1.0
    microstructure_vizxdmfDisplay.CoatNormalTexture = None
    microstructure_vizxdmfDisplay.CoatNormalScale = 1.0
    microstructure_vizxdmfDisplay.MaterialTexture = None
    microstructure_vizxdmfDisplay.OcclusionStrength = 1.0
    microstructure_vizxdmfDisplay.AnisotropyTexture = None
    microstructure_vizxdmfDisplay.EmissiveTexture = None
    microstructure_vizxdmfDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
    microstructure_vizxdmfDisplay.FlipTextures = 0
    microstructure_vizxdmfDisplay.EdgeOpacity = 1.0
    microstructure_vizxdmfDisplay.BackfaceRepresentation = 'Follow Frontface'
    microstructure_vizxdmfDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    microstructure_vizxdmfDisplay.BackfaceOpacity = 1.0
    microstructure_vizxdmfDisplay.Position = [0.0, 0.0, 0.0]
    microstructure_vizxdmfDisplay.Scale = [1.0, 1.0, 1.0]
    microstructure_vizxdmfDisplay.Orientation = [0.0, 0.0, 0.0]
    microstructure_vizxdmfDisplay.Origin = [0.0, 0.0, 0.0]
    microstructure_vizxdmfDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    microstructure_vizxdmfDisplay.Pickable = 1
    microstructure_vizxdmfDisplay.Triangulate = 0
    microstructure_vizxdmfDisplay.UseShaderReplacements = 0
    microstructure_vizxdmfDisplay.ShaderReplacements = ''
    microstructure_vizxdmfDisplay.NonlinearSubdivisionLevel = 1
    microstructure_vizxdmfDisplay.MatchBoundariesIgnoringCellOrder = 0
    microstructure_vizxdmfDisplay.UseDataPartitions = 0
    microstructure_vizxdmfDisplay.OSPRayUseScaleArray = 'All Approximate'
    microstructure_vizxdmfDisplay.OSPRayScaleArray = 'f0'
    microstructure_vizxdmfDisplay.OSPRayScaleFunction = 'Piecewise Function'
    microstructure_vizxdmfDisplay.OSPRayMaterial = 'None'
    microstructure_vizxdmfDisplay.Assembly = 'Hierarchy'
    microstructure_vizxdmfDisplay.BlockSelectors = ['/']
    microstructure_vizxdmfDisplay.BlockColors = []
    microstructure_vizxdmfDisplay.BlockOpacities = []
    microstructure_vizxdmfDisplay.Orient = 0
    microstructure_vizxdmfDisplay.OrientationMode = 'Direction'
    microstructure_vizxdmfDisplay.SelectOrientationVectors = 'n0'
    microstructure_vizxdmfDisplay.Scaling = 0
    microstructure_vizxdmfDisplay.ScaleMode = 'No Data Scaling Off'
    microstructure_vizxdmfDisplay.ScaleFactor = 0.7499993801116944
    microstructure_vizxdmfDisplay.SelectScaleArray = 'None'
    microstructure_vizxdmfDisplay.GlyphType = 'Arrow'
    microstructure_vizxdmfDisplay.UseGlyphTable = 0
    microstructure_vizxdmfDisplay.GlyphTableIndexArray = 'None'
    microstructure_vizxdmfDisplay.UseCompositeGlyphTable = 0
    microstructure_vizxdmfDisplay.UseGlyphCullingAndLOD = 0
    microstructure_vizxdmfDisplay.LODValues = []
    microstructure_vizxdmfDisplay.ColorByLODIndex = 0
    microstructure_vizxdmfDisplay.GaussianRadius = 0.037499969005584714
    microstructure_vizxdmfDisplay.ShaderPreset = 'Sphere'
    microstructure_vizxdmfDisplay.CustomTriangleScale = 3
    microstructure_vizxdmfDisplay.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
    float gaussian = exp(-0.5*dist2);
    opacity = opacity*gaussian;
    """
    microstructure_vizxdmfDisplay.Emissive = 0
    microstructure_vizxdmfDisplay.ScaleByArray = 0
    microstructure_vizxdmfDisplay.SetScaleArray = ['POINTS', 'f0']
    microstructure_vizxdmfDisplay.ScaleArrayComponent = 'X'
    microstructure_vizxdmfDisplay.UseScaleFunction = 1
    microstructure_vizxdmfDisplay.ScaleTransferFunction = 'Piecewise Function'
    microstructure_vizxdmfDisplay.OpacityByArray = 0
    microstructure_vizxdmfDisplay.OpacityArray = ['POINTS', 'f0']
    microstructure_vizxdmfDisplay.OpacityArrayComponent = 'X'
    microstructure_vizxdmfDisplay.OpacityTransferFunction = 'Piecewise Function'
    microstructure_vizxdmfDisplay.DataAxesGrid = 'Grid Axes Representation'
    microstructure_vizxdmfDisplay.SelectionCellLabelBold = 0
    microstructure_vizxdmfDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    microstructure_vizxdmfDisplay.SelectionCellLabelFontFamily = 'Arial'
    microstructure_vizxdmfDisplay.SelectionCellLabelFontFile = ''
    microstructure_vizxdmfDisplay.SelectionCellLabelFontSize = 18
    microstructure_vizxdmfDisplay.SelectionCellLabelItalic = 0
    microstructure_vizxdmfDisplay.SelectionCellLabelJustification = 'Left'
    microstructure_vizxdmfDisplay.SelectionCellLabelOpacity = 1.0
    microstructure_vizxdmfDisplay.SelectionCellLabelShadow = 0
    microstructure_vizxdmfDisplay.SelectionPointLabelBold = 0
    microstructure_vizxdmfDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    microstructure_vizxdmfDisplay.SelectionPointLabelFontFamily = 'Arial'
    microstructure_vizxdmfDisplay.SelectionPointLabelFontFile = ''
    microstructure_vizxdmfDisplay.SelectionPointLabelFontSize = 18
    microstructure_vizxdmfDisplay.SelectionPointLabelItalic = 0
    microstructure_vizxdmfDisplay.SelectionPointLabelJustification = 'Left'
    microstructure_vizxdmfDisplay.SelectionPointLabelOpacity = 1.0
    microstructure_vizxdmfDisplay.SelectionPointLabelShadow = 0
    microstructure_vizxdmfDisplay.PolarAxes = 'Polar Axes Representation'
    microstructure_vizxdmfDisplay.ScalarOpacityFunction = None
    microstructure_vizxdmfDisplay.ScalarOpacityUnitDistance = 0.3871410213004026
    microstructure_vizxdmfDisplay.UseSeparateOpacityArray = 0
    microstructure_vizxdmfDisplay.OpacityArrayName = ['POINTS', 'f0']
    microstructure_vizxdmfDisplay.OpacityComponent = 'X'
    microstructure_vizxdmfDisplay.SelectMapper = 'Projected tetra'
    microstructure_vizxdmfDisplay.SamplingDimensions = [128, 128, 128]
    microstructure_vizxdmfDisplay.UseFloatingPointFrameBuffer = 1
    microstructure_vizxdmfDisplay.SelectInputVectors = ['POINTS', 'n0']
    microstructure_vizxdmfDisplay.NumberOfSteps = 40
    microstructure_vizxdmfDisplay.StepSize = 0.25
    microstructure_vizxdmfDisplay.NormalizeVectors = 1
    microstructure_vizxdmfDisplay.EnhancedLIC = 1
    microstructure_vizxdmfDisplay.ColorMode = 'Blend'
    microstructure_vizxdmfDisplay.LICIntensity = 0.8
    microstructure_vizxdmfDisplay.MapModeBias = 0.0
    microstructure_vizxdmfDisplay.EnhanceContrast = 'Off'
    microstructure_vizxdmfDisplay.LowLICContrastEnhancementFactor = 0.0
    microstructure_vizxdmfDisplay.HighLICContrastEnhancementFactor = 0.0
    microstructure_vizxdmfDisplay.LowColorContrastEnhancementFactor = 0.0
    microstructure_vizxdmfDisplay.HighColorContrastEnhancementFactor = 0.0
    microstructure_vizxdmfDisplay.AntiAlias = 0
    microstructure_vizxdmfDisplay.MaskOnSurface = 1
    microstructure_vizxdmfDisplay.MaskThreshold = 0.0
    microstructure_vizxdmfDisplay.MaskIntensity = 0.0
    microstructure_vizxdmfDisplay.MaskColor = [0.5, 0.5, 0.5]
    microstructure_vizxdmfDisplay.GenerateNoiseTexture = 0
    microstructure_vizxdmfDisplay.NoiseType = 'Gaussian'
    microstructure_vizxdmfDisplay.NoiseTextureSize = 128
    microstructure_vizxdmfDisplay.NoiseGrainSize = 2
    microstructure_vizxdmfDisplay.MinNoiseValue = 0.0
    microstructure_vizxdmfDisplay.MaxNoiseValue = 0.8
    microstructure_vizxdmfDisplay.NumberOfNoiseLevels = 1024
    microstructure_vizxdmfDisplay.ImpulseNoiseProbability = 1.0
    microstructure_vizxdmfDisplay.ImpulseNoiseBackgroundValue = 0.0
    microstructure_vizxdmfDisplay.NoiseGeneratorSeed = 1
    microstructure_vizxdmfDisplay.CompositeStrategy = 'AUTO'
    microstructure_vizxdmfDisplay.UseLICForLOD = 0
    microstructure_vizxdmfDisplay.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    microstructure_vizxdmfDisplay.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]
    microstructure_vizxdmfDisplay.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    microstructure_vizxdmfDisplay.GlyphType.TipResolution = 6
    microstructure_vizxdmfDisplay.GlyphType.TipRadius = 0.1
    microstructure_vizxdmfDisplay.GlyphType.TipLength = 0.35
    microstructure_vizxdmfDisplay.GlyphType.ShaftResolution = 6
    microstructure_vizxdmfDisplay.GlyphType.ShaftRadius = 0.03
    microstructure_vizxdmfDisplay.GlyphType.Invert = 0

    # init the 'Piecewise Function' selected for 'ScaleTransferFunction'
    microstructure_vizxdmfDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    microstructure_vizxdmfDisplay.ScaleTransferFunction.UseLogScale = 0

    # init the 'Piecewise Function' selected for 'OpacityTransferFunction'
    microstructure_vizxdmfDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    microstructure_vizxdmfDisplay.OpacityTransferFunction.UseLogScale = 0

    # init the 'Grid Axes Representation' selected for 'DataAxesGrid'
    microstructure_vizxdmfDisplay.DataAxesGrid.XTitle = 'X Axis'
    microstructure_vizxdmfDisplay.DataAxesGrid.YTitle = 'Y Axis'
    microstructure_vizxdmfDisplay.DataAxesGrid.ZTitle = 'Z Axis'
    microstructure_vizxdmfDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
    microstructure_vizxdmfDisplay.DataAxesGrid.XTitleFontFile = ''
    microstructure_vizxdmfDisplay.DataAxesGrid.XTitleBold = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.XTitleItalic = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.XTitleFontSize = 12
    microstructure_vizxdmfDisplay.DataAxesGrid.XTitleShadow = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.XTitleOpacity = 1.0
    microstructure_vizxdmfDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
    microstructure_vizxdmfDisplay.DataAxesGrid.YTitleFontFile = ''
    microstructure_vizxdmfDisplay.DataAxesGrid.YTitleBold = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.YTitleItalic = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.YTitleFontSize = 12
    microstructure_vizxdmfDisplay.DataAxesGrid.YTitleShadow = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.YTitleOpacity = 1.0
    microstructure_vizxdmfDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
    microstructure_vizxdmfDisplay.DataAxesGrid.ZTitleFontFile = ''
    microstructure_vizxdmfDisplay.DataAxesGrid.ZTitleBold = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.ZTitleItalic = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.ZTitleFontSize = 12
    microstructure_vizxdmfDisplay.DataAxesGrid.ZTitleShadow = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.ZTitleOpacity = 1.0
    microstructure_vizxdmfDisplay.DataAxesGrid.FacesToRender = 63
    microstructure_vizxdmfDisplay.DataAxesGrid.CullBackface = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.CullFrontface = 1
    microstructure_vizxdmfDisplay.DataAxesGrid.ShowGrid = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.ShowEdges = 1
    microstructure_vizxdmfDisplay.DataAxesGrid.ShowTicks = 1
    microstructure_vizxdmfDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
    microstructure_vizxdmfDisplay.DataAxesGrid.AxesToLabel = 63
    microstructure_vizxdmfDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
    microstructure_vizxdmfDisplay.DataAxesGrid.XLabelFontFile = ''
    microstructure_vizxdmfDisplay.DataAxesGrid.XLabelBold = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.XLabelItalic = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.XLabelFontSize = 12
    microstructure_vizxdmfDisplay.DataAxesGrid.XLabelShadow = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.XLabelOpacity = 1.0
    microstructure_vizxdmfDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
    microstructure_vizxdmfDisplay.DataAxesGrid.YLabelFontFile = ''
    microstructure_vizxdmfDisplay.DataAxesGrid.YLabelBold = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.YLabelItalic = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.YLabelFontSize = 12
    microstructure_vizxdmfDisplay.DataAxesGrid.YLabelShadow = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.YLabelOpacity = 1.0
    microstructure_vizxdmfDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
    microstructure_vizxdmfDisplay.DataAxesGrid.ZLabelFontFile = ''
    microstructure_vizxdmfDisplay.DataAxesGrid.ZLabelBold = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.ZLabelItalic = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.ZLabelFontSize = 12
    microstructure_vizxdmfDisplay.DataAxesGrid.ZLabelShadow = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.ZLabelOpacity = 1.0
    microstructure_vizxdmfDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
    microstructure_vizxdmfDisplay.DataAxesGrid.XAxisPrecision = 2
    microstructure_vizxdmfDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.XAxisLabels = []
    microstructure_vizxdmfDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
    microstructure_vizxdmfDisplay.DataAxesGrid.YAxisPrecision = 2
    microstructure_vizxdmfDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.YAxisLabels = []
    microstructure_vizxdmfDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
    microstructure_vizxdmfDisplay.DataAxesGrid.ZAxisPrecision = 2
    microstructure_vizxdmfDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.ZAxisLabels = []
    microstructure_vizxdmfDisplay.DataAxesGrid.UseCustomBounds = 0
    microstructure_vizxdmfDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'Polar Axes Representation' selected for 'PolarAxes'
    microstructure_vizxdmfDisplay.PolarAxes.Visibility = 0
    microstructure_vizxdmfDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
    microstructure_vizxdmfDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
    microstructure_vizxdmfDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    microstructure_vizxdmfDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
    microstructure_vizxdmfDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    microstructure_vizxdmfDisplay.PolarAxes.EnableCustomRange = 0
    microstructure_vizxdmfDisplay.PolarAxes.CustomRange = [0.0, 1.0]
    microstructure_vizxdmfDisplay.PolarAxes.AutoPole = 1
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisVisibility = 1
    microstructure_vizxdmfDisplay.PolarAxes.RadialAxesVisibility = 1
    microstructure_vizxdmfDisplay.PolarAxes.DrawRadialGridlines = 1
    microstructure_vizxdmfDisplay.PolarAxes.PolarArcsVisibility = 1
    microstructure_vizxdmfDisplay.PolarAxes.DrawPolarArcsGridlines = 1
    microstructure_vizxdmfDisplay.PolarAxes.NumberOfRadialAxes = 0
    microstructure_vizxdmfDisplay.PolarAxes.DeltaAngleRadialAxes = 45.0
    microstructure_vizxdmfDisplay.PolarAxes.NumberOfPolarAxes = 5
    microstructure_vizxdmfDisplay.PolarAxes.DeltaRangePolarAxes = 0.0
    microstructure_vizxdmfDisplay.PolarAxes.CustomMinRadius = 1
    microstructure_vizxdmfDisplay.PolarAxes.MinimumRadius = 0.0
    microstructure_vizxdmfDisplay.PolarAxes.CustomAngles = 1
    microstructure_vizxdmfDisplay.PolarAxes.MinimumAngle = 0.0
    microstructure_vizxdmfDisplay.PolarAxes.MaximumAngle = 90.0
    microstructure_vizxdmfDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
    microstructure_vizxdmfDisplay.PolarAxes.PolarArcResolutionPerDegree = 0.2
    microstructure_vizxdmfDisplay.PolarAxes.Ratio = 1.0
    microstructure_vizxdmfDisplay.PolarAxes.EnableOverallColor = 1
    microstructure_vizxdmfDisplay.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    microstructure_vizxdmfDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    microstructure_vizxdmfDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    microstructure_vizxdmfDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    microstructure_vizxdmfDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisTitleVisibility = 1
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    microstructure_vizxdmfDisplay.PolarAxes.PolarTitleOffset = [20.0, 20.0]
    microstructure_vizxdmfDisplay.PolarAxes.PolarLabelVisibility = 1
    microstructure_vizxdmfDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
    microstructure_vizxdmfDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
    microstructure_vizxdmfDisplay.PolarAxes.PolarLabelOffset = 10.0
    microstructure_vizxdmfDisplay.PolarAxes.PolarExponentOffset = 5.0
    microstructure_vizxdmfDisplay.PolarAxes.RadialTitleVisibility = 1
    microstructure_vizxdmfDisplay.PolarAxes.RadialTitleFormat = '%-#3.1f'
    microstructure_vizxdmfDisplay.PolarAxes.RadialTitleLocation = 'Bottom'
    microstructure_vizxdmfDisplay.PolarAxes.RadialTitleOffset = [20.0, 0.0]
    microstructure_vizxdmfDisplay.PolarAxes.RadialUnitsVisibility = 1
    microstructure_vizxdmfDisplay.PolarAxes.ScreenSize = 10.0
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisTitleFontFile = ''
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisTitleBold = 0
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisTitleItalic = 0
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisTitleShadow = 0
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisTitleFontSize = 12
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisLabelFontFile = ''
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisLabelBold = 0
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisLabelItalic = 0
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisLabelShadow = 0
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisLabelFontSize = 12
    microstructure_vizxdmfDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
    microstructure_vizxdmfDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    microstructure_vizxdmfDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
    microstructure_vizxdmfDisplay.PolarAxes.LastRadialAxisTextBold = 0
    microstructure_vizxdmfDisplay.PolarAxes.LastRadialAxisTextItalic = 0
    microstructure_vizxdmfDisplay.PolarAxes.LastRadialAxisTextShadow = 0
    microstructure_vizxdmfDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
    microstructure_vizxdmfDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    microstructure_vizxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    microstructure_vizxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    microstructure_vizxdmfDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
    microstructure_vizxdmfDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
    microstructure_vizxdmfDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
    microstructure_vizxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    microstructure_vizxdmfDisplay.PolarAxes.EnableDistanceLOD = 1
    microstructure_vizxdmfDisplay.PolarAxes.DistanceLODThreshold = 0.7
    microstructure_vizxdmfDisplay.PolarAxes.EnableViewAngleLOD = 1
    microstructure_vizxdmfDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
    microstructure_vizxdmfDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
    microstructure_vizxdmfDisplay.PolarAxes.PolarTicksVisibility = 1
    microstructure_vizxdmfDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
    microstructure_vizxdmfDisplay.PolarAxes.TickLocation = 'Both'
    microstructure_vizxdmfDisplay.PolarAxes.AxisTickVisibility = 1
    microstructure_vizxdmfDisplay.PolarAxes.AxisMinorTickVisibility = 0
    microstructure_vizxdmfDisplay.PolarAxes.AxisTickMatchesPolarAxes = 1
    microstructure_vizxdmfDisplay.PolarAxes.DeltaRangeMajor = 1.0
    microstructure_vizxdmfDisplay.PolarAxes.DeltaRangeMinor = 0.5
    microstructure_vizxdmfDisplay.PolarAxes.ArcTickVisibility = 1
    microstructure_vizxdmfDisplay.PolarAxes.ArcMinorTickVisibility = 0
    microstructure_vizxdmfDisplay.PolarAxes.ArcTickMatchesRadialAxes = 1
    microstructure_vizxdmfDisplay.PolarAxes.DeltaAngleMajor = 10.0
    microstructure_vizxdmfDisplay.PolarAxes.DeltaAngleMinor = 5.0
    microstructure_vizxdmfDisplay.PolarAxes.TickRatioRadiusSize = 0.02
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
    microstructure_vizxdmfDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
    microstructure_vizxdmfDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    microstructure_vizxdmfDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    microstructure_vizxdmfDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    microstructure_vizxdmfDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    microstructure_vizxdmfDisplay.PolarAxes.ArcMajorTickSize = 0.0
    microstructure_vizxdmfDisplay.PolarAxes.ArcTickRatioSize = 0.3
    microstructure_vizxdmfDisplay.PolarAxes.ArcMajorTickThickness = 1.0
    microstructure_vizxdmfDisplay.PolarAxes.ArcTickRatioThickness = 0.5
    microstructure_vizxdmfDisplay.PolarAxes.Use2DMode = 0
    microstructure_vizxdmfDisplay.PolarAxes.UseLogAxis = 0

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # update the view to ensure updated data information
    renderView1.Update()

    # set scalar coloring
    ColorBy(microstructure_vizxdmfDisplay, ('FIELD', 'vtkBlockColors'))

    # show color bar/color legend
    microstructure_vizxdmfDisplay.SetScalarBarVisibility(renderView1, True)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932

    # get 2D transfer function for 'vtkBlockColors'
    vtkBlockColorsTF2D = GetTransferFunction2D('vtkBlockColors')
    vtkBlockColorsTF2D.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
    vtkBlockColorsTF2D.Boxes = []
    vtkBlockColorsTF2D.ScalarRangeInitialized = 0
    vtkBlockColorsTF2D.Range = [0.0, 1.0, 0.0, 1.0]
    vtkBlockColorsTF2D.OutputDimensions = [10, 10]

    # get color transfer function/color map for 'vtkBlockColors'
    vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
    vtkBlockColorsLUT.InterpretValuesAsCategories = 1
    vtkBlockColorsLUT.AnnotationsInitialized = 1
    vtkBlockColorsLUT.ShowCategoricalColorsinDataRangeOnly = 0
    vtkBlockColorsLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
    vtkBlockColorsLUT.RescaleOnVisibilityChange = 0
    vtkBlockColorsLUT.TransferFunction2D = vtkBlockColorsTF2D
    vtkBlockColorsLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.5, 0.865003, 0.865003, 0.865003, 1.0, 0.705882, 0.0156863, 0.14902]
    vtkBlockColorsLUT.UseLogScale = 0
    vtkBlockColorsLUT.UseOpacityControlPointsFreehandDrawing = 0
    vtkBlockColorsLUT.ShowDataHistogram = 0
    vtkBlockColorsLUT.AutomaticDataHistogramComputation = 0
    vtkBlockColorsLUT.DataHistogramNumberOfBins = 10
    vtkBlockColorsLUT.ColorSpace = 'Diverging'
    vtkBlockColorsLUT.UseBelowRangeColor = 0
    vtkBlockColorsLUT.BelowRangeColor = [0.0, 0.0, 0.0]
    vtkBlockColorsLUT.UseAboveRangeColor = 0
    vtkBlockColorsLUT.AboveRangeColor = [0.5, 0.5, 0.5]
    vtkBlockColorsLUT.NanColor = [1.0, 1.0, 0.0]
    vtkBlockColorsLUT.NanOpacity = 1.0
    vtkBlockColorsLUT.Discretize = 1
    vtkBlockColorsLUT.NumberOfTableValues = 256
    vtkBlockColorsLUT.ScalarRangeInitialized = 0.0
    vtkBlockColorsLUT.HSVWrap = 0
    vtkBlockColorsLUT.VectorComponent = 0
    vtkBlockColorsLUT.VectorMode = 'Magnitude'
    vtkBlockColorsLUT.AllowDuplicateScalars = 1
    vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
    vtkBlockColorsLUT.ActiveAnnotatedValues = ['0', '1', '2']
    vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.63, 0.63, 1.0, 0.67, 0.5, 0.33, 1.0, 0.5, 0.75, 0.53, 0.35, 0.7, 1.0, 0.75, 0.5]
    vtkBlockColorsLUT.IndexedOpacities = []
    vtkBlockColorsLUT.EnableOpacityMapping = 0

    # get opacity transfer function/opacity map for 'vtkBlockColors'
    vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')
    vtkBlockColorsPWF.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]
    vtkBlockColorsPWF.AllowDuplicateScalars = 1
    vtkBlockColorsPWF.UseLogScale = 0
    vtkBlockColorsPWF.ScalarRangeInitialized = 0
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932

    # create a new 'Extract Block'
    extractBlock1 = ExtractBlock(registrationName='ExtractBlock1', Input=microstructure_vizxdmf)
    extractBlock1.Assembly = 'Hierarchy'
    extractBlock1.Selectors = []

    # Properties modified on extractBlock1
    extractBlock1.Selectors = ['/Root/Block0']

    # show data in view
    extractBlock1Display = Show(extractBlock1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    extractBlock1Display.Selection = None
    extractBlock1Display.Representation = 'Surface'
    extractBlock1Display.ColorArrayName = [None, '']
    extractBlock1Display.LookupTable = None
    extractBlock1Display.MapScalars = 1
    extractBlock1Display.MultiComponentsMapping = 0
    extractBlock1Display.InterpolateScalarsBeforeMapping = 1
    extractBlock1Display.UseNanColorForMissingArrays = 0
    extractBlock1Display.Opacity = 1.0
    extractBlock1Display.PointSize = 2.0
    extractBlock1Display.LineWidth = 1.0
    extractBlock1Display.RenderLinesAsTubes = 0
    extractBlock1Display.RenderPointsAsSpheres = 0
    extractBlock1Display.Interpolation = 'Gouraud'
    extractBlock1Display.Specular = 0.0
    extractBlock1Display.SpecularColor = [1.0, 1.0, 1.0]
    extractBlock1Display.SpecularPower = 100.0
    extractBlock1Display.Luminosity = 0.0
    extractBlock1Display.Ambient = 0.0
    extractBlock1Display.Diffuse = 1.0
    extractBlock1Display.Roughness = 0.3
    extractBlock1Display.Metallic = 0.0
    extractBlock1Display.EdgeTint = [1.0, 1.0, 1.0]
    extractBlock1Display.Anisotropy = 0.0
    extractBlock1Display.AnisotropyRotation = 0.0
    extractBlock1Display.BaseIOR = 1.5
    extractBlock1Display.CoatStrength = 0.0
    extractBlock1Display.CoatIOR = 2.0
    extractBlock1Display.CoatRoughness = 0.0
    extractBlock1Display.CoatColor = [1.0, 1.0, 1.0]
    extractBlock1Display.SelectTCoordArray = 'None'
    extractBlock1Display.SelectNormalArray = 'None'
    extractBlock1Display.SelectTangentArray = 'None'
    extractBlock1Display.Texture = None
    extractBlock1Display.RepeatTextures = 1
    extractBlock1Display.InterpolateTextures = 0
    extractBlock1Display.SeamlessU = 0
    extractBlock1Display.SeamlessV = 0
    extractBlock1Display.UseMipmapTextures = 0
    extractBlock1Display.ShowTexturesOnBackface = 1
    extractBlock1Display.BaseColorTexture = None
    extractBlock1Display.NormalTexture = None
    extractBlock1Display.NormalScale = 1.0
    extractBlock1Display.CoatNormalTexture = None
    extractBlock1Display.CoatNormalScale = 1.0
    extractBlock1Display.MaterialTexture = None
    extractBlock1Display.OcclusionStrength = 1.0
    extractBlock1Display.AnisotropyTexture = None
    extractBlock1Display.EmissiveTexture = None
    extractBlock1Display.EmissiveFactor = [1.0, 1.0, 1.0]
    extractBlock1Display.FlipTextures = 0
    extractBlock1Display.EdgeOpacity = 1.0
    extractBlock1Display.BackfaceRepresentation = 'Follow Frontface'
    extractBlock1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    extractBlock1Display.BackfaceOpacity = 1.0
    extractBlock1Display.Position = [0.0, 0.0, 0.0]
    extractBlock1Display.Scale = [1.0, 1.0, 1.0]
    extractBlock1Display.Orientation = [0.0, 0.0, 0.0]
    extractBlock1Display.Origin = [0.0, 0.0, 0.0]
    extractBlock1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    extractBlock1Display.Pickable = 1
    extractBlock1Display.Triangulate = 0
    extractBlock1Display.UseShaderReplacements = 0
    extractBlock1Display.ShaderReplacements = ''
    extractBlock1Display.NonlinearSubdivisionLevel = 1
    extractBlock1Display.MatchBoundariesIgnoringCellOrder = 0
    extractBlock1Display.UseDataPartitions = 0
    extractBlock1Display.OSPRayUseScaleArray = 'All Approximate'
    extractBlock1Display.OSPRayScaleArray = 'f0'
    extractBlock1Display.OSPRayScaleFunction = 'Piecewise Function'
    extractBlock1Display.OSPRayMaterial = 'None'
    extractBlock1Display.Assembly = 'Hierarchy'
    extractBlock1Display.BlockSelectors = ['/']
    extractBlock1Display.BlockColors = []
    extractBlock1Display.BlockOpacities = []
    extractBlock1Display.Orient = 0
    extractBlock1Display.OrientationMode = 'Direction'
    extractBlock1Display.SelectOrientationVectors = 'f0'
    extractBlock1Display.Scaling = 0
    extractBlock1Display.ScaleMode = 'No Data Scaling Off'
    extractBlock1Display.ScaleFactor = 0.7499993801116944
    extractBlock1Display.SelectScaleArray = 'None'
    extractBlock1Display.GlyphType = 'Arrow'
    extractBlock1Display.UseGlyphTable = 0
    extractBlock1Display.GlyphTableIndexArray = 'None'
    extractBlock1Display.UseCompositeGlyphTable = 0
    extractBlock1Display.UseGlyphCullingAndLOD = 0
    extractBlock1Display.LODValues = []
    extractBlock1Display.ColorByLODIndex = 0
    extractBlock1Display.GaussianRadius = 0.037499969005584714
    extractBlock1Display.ShaderPreset = 'Sphere'
    extractBlock1Display.CustomTriangleScale = 3
    extractBlock1Display.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
    float gaussian = exp(-0.5*dist2);
    opacity = opacity*gaussian;
    """
    extractBlock1Display.Emissive = 0
    extractBlock1Display.ScaleByArray = 0
    extractBlock1Display.SetScaleArray = ['POINTS', 'f0']
    extractBlock1Display.ScaleArrayComponent = 'X'
    extractBlock1Display.UseScaleFunction = 1
    extractBlock1Display.ScaleTransferFunction = 'Piecewise Function'
    extractBlock1Display.OpacityByArray = 0
    extractBlock1Display.OpacityArray = ['POINTS', 'f0']
    extractBlock1Display.OpacityArrayComponent = 'X'
    extractBlock1Display.OpacityTransferFunction = 'Piecewise Function'
    extractBlock1Display.DataAxesGrid = 'Grid Axes Representation'
    extractBlock1Display.SelectionCellLabelBold = 0
    extractBlock1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    extractBlock1Display.SelectionCellLabelFontFamily = 'Arial'
    extractBlock1Display.SelectionCellLabelFontFile = ''
    extractBlock1Display.SelectionCellLabelFontSize = 18
    extractBlock1Display.SelectionCellLabelItalic = 0
    extractBlock1Display.SelectionCellLabelJustification = 'Left'
    extractBlock1Display.SelectionCellLabelOpacity = 1.0
    extractBlock1Display.SelectionCellLabelShadow = 0
    extractBlock1Display.SelectionPointLabelBold = 0
    extractBlock1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    extractBlock1Display.SelectionPointLabelFontFamily = 'Arial'
    extractBlock1Display.SelectionPointLabelFontFile = ''
    extractBlock1Display.SelectionPointLabelFontSize = 18
    extractBlock1Display.SelectionPointLabelItalic = 0
    extractBlock1Display.SelectionPointLabelJustification = 'Left'
    extractBlock1Display.SelectionPointLabelOpacity = 1.0
    extractBlock1Display.SelectionPointLabelShadow = 0
    extractBlock1Display.PolarAxes = 'Polar Axes Representation'
    extractBlock1Display.ScalarOpacityFunction = None
    extractBlock1Display.ScalarOpacityUnitDistance = 0.5583539716188769
    extractBlock1Display.UseSeparateOpacityArray = 0
    extractBlock1Display.OpacityArrayName = ['POINTS', 'f0']
    extractBlock1Display.OpacityComponent = 'X'
    extractBlock1Display.SelectMapper = 'Projected tetra'
    extractBlock1Display.SamplingDimensions = [128, 128, 128]
    extractBlock1Display.UseFloatingPointFrameBuffer = 1
    extractBlock1Display.SelectInputVectors = ['POINTS', 'f0']
    extractBlock1Display.NumberOfSteps = 40
    extractBlock1Display.StepSize = 0.25
    extractBlock1Display.NormalizeVectors = 1
    extractBlock1Display.EnhancedLIC = 1
    extractBlock1Display.ColorMode = 'Blend'
    extractBlock1Display.LICIntensity = 0.8
    extractBlock1Display.MapModeBias = 0.0
    extractBlock1Display.EnhanceContrast = 'Off'
    extractBlock1Display.LowLICContrastEnhancementFactor = 0.0
    extractBlock1Display.HighLICContrastEnhancementFactor = 0.0
    extractBlock1Display.LowColorContrastEnhancementFactor = 0.0
    extractBlock1Display.HighColorContrastEnhancementFactor = 0.0
    extractBlock1Display.AntiAlias = 0
    extractBlock1Display.MaskOnSurface = 1
    extractBlock1Display.MaskThreshold = 0.0
    extractBlock1Display.MaskIntensity = 0.0
    extractBlock1Display.MaskColor = [0.5, 0.5, 0.5]
    extractBlock1Display.GenerateNoiseTexture = 0
    extractBlock1Display.NoiseType = 'Gaussian'
    extractBlock1Display.NoiseTextureSize = 128
    extractBlock1Display.NoiseGrainSize = 2
    extractBlock1Display.MinNoiseValue = 0.0
    extractBlock1Display.MaxNoiseValue = 0.8
    extractBlock1Display.NumberOfNoiseLevels = 1024
    extractBlock1Display.ImpulseNoiseProbability = 1.0
    extractBlock1Display.ImpulseNoiseBackgroundValue = 0.0
    extractBlock1Display.NoiseGeneratorSeed = 1
    extractBlock1Display.CompositeStrategy = 'AUTO'
    extractBlock1Display.UseLICForLOD = 0
    extractBlock1Display.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    extractBlock1Display.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]
    extractBlock1Display.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    extractBlock1Display.GlyphType.TipResolution = 6
    extractBlock1Display.GlyphType.TipRadius = 0.1
    extractBlock1Display.GlyphType.TipLength = 0.35
    extractBlock1Display.GlyphType.ShaftResolution = 6
    extractBlock1Display.GlyphType.ShaftRadius = 0.03
    extractBlock1Display.GlyphType.Invert = 0

    # init the 'Piecewise Function' selected for 'ScaleTransferFunction'
    extractBlock1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    extractBlock1Display.ScaleTransferFunction.UseLogScale = 0

    # init the 'Piecewise Function' selected for 'OpacityTransferFunction'
    extractBlock1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    extractBlock1Display.OpacityTransferFunction.UseLogScale = 0

    # init the 'Grid Axes Representation' selected for 'DataAxesGrid'
    extractBlock1Display.DataAxesGrid.XTitle = 'X Axis'
    extractBlock1Display.DataAxesGrid.YTitle = 'Y Axis'
    extractBlock1Display.DataAxesGrid.ZTitle = 'Z Axis'
    extractBlock1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
    extractBlock1Display.DataAxesGrid.XTitleFontFile = ''
    extractBlock1Display.DataAxesGrid.XTitleBold = 0
    extractBlock1Display.DataAxesGrid.XTitleItalic = 0
    extractBlock1Display.DataAxesGrid.XTitleFontSize = 12
    extractBlock1Display.DataAxesGrid.XTitleShadow = 0
    extractBlock1Display.DataAxesGrid.XTitleOpacity = 1.0
    extractBlock1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
    extractBlock1Display.DataAxesGrid.YTitleFontFile = ''
    extractBlock1Display.DataAxesGrid.YTitleBold = 0
    extractBlock1Display.DataAxesGrid.YTitleItalic = 0
    extractBlock1Display.DataAxesGrid.YTitleFontSize = 12
    extractBlock1Display.DataAxesGrid.YTitleShadow = 0
    extractBlock1Display.DataAxesGrid.YTitleOpacity = 1.0
    extractBlock1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
    extractBlock1Display.DataAxesGrid.ZTitleFontFile = ''
    extractBlock1Display.DataAxesGrid.ZTitleBold = 0
    extractBlock1Display.DataAxesGrid.ZTitleItalic = 0
    extractBlock1Display.DataAxesGrid.ZTitleFontSize = 12
    extractBlock1Display.DataAxesGrid.ZTitleShadow = 0
    extractBlock1Display.DataAxesGrid.ZTitleOpacity = 1.0
    extractBlock1Display.DataAxesGrid.FacesToRender = 63
    extractBlock1Display.DataAxesGrid.CullBackface = 0
    extractBlock1Display.DataAxesGrid.CullFrontface = 1
    extractBlock1Display.DataAxesGrid.ShowGrid = 0
    extractBlock1Display.DataAxesGrid.ShowEdges = 1
    extractBlock1Display.DataAxesGrid.ShowTicks = 1
    extractBlock1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
    extractBlock1Display.DataAxesGrid.AxesToLabel = 63
    extractBlock1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
    extractBlock1Display.DataAxesGrid.XLabelFontFile = ''
    extractBlock1Display.DataAxesGrid.XLabelBold = 0
    extractBlock1Display.DataAxesGrid.XLabelItalic = 0
    extractBlock1Display.DataAxesGrid.XLabelFontSize = 12
    extractBlock1Display.DataAxesGrid.XLabelShadow = 0
    extractBlock1Display.DataAxesGrid.XLabelOpacity = 1.0
    extractBlock1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
    extractBlock1Display.DataAxesGrid.YLabelFontFile = ''
    extractBlock1Display.DataAxesGrid.YLabelBold = 0
    extractBlock1Display.DataAxesGrid.YLabelItalic = 0
    extractBlock1Display.DataAxesGrid.YLabelFontSize = 12
    extractBlock1Display.DataAxesGrid.YLabelShadow = 0
    extractBlock1Display.DataAxesGrid.YLabelOpacity = 1.0
    extractBlock1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
    extractBlock1Display.DataAxesGrid.ZLabelFontFile = ''
    extractBlock1Display.DataAxesGrid.ZLabelBold = 0
    extractBlock1Display.DataAxesGrid.ZLabelItalic = 0
    extractBlock1Display.DataAxesGrid.ZLabelFontSize = 12
    extractBlock1Display.DataAxesGrid.ZLabelShadow = 0
    extractBlock1Display.DataAxesGrid.ZLabelOpacity = 1.0
    extractBlock1Display.DataAxesGrid.XAxisNotation = 'Mixed'
    extractBlock1Display.DataAxesGrid.XAxisPrecision = 2
    extractBlock1Display.DataAxesGrid.XAxisUseCustomLabels = 0
    extractBlock1Display.DataAxesGrid.XAxisLabels = []
    extractBlock1Display.DataAxesGrid.YAxisNotation = 'Mixed'
    extractBlock1Display.DataAxesGrid.YAxisPrecision = 2
    extractBlock1Display.DataAxesGrid.YAxisUseCustomLabels = 0
    extractBlock1Display.DataAxesGrid.YAxisLabels = []
    extractBlock1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
    extractBlock1Display.DataAxesGrid.ZAxisPrecision = 2
    extractBlock1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
    extractBlock1Display.DataAxesGrid.ZAxisLabels = []
    extractBlock1Display.DataAxesGrid.UseCustomBounds = 0
    extractBlock1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'Polar Axes Representation' selected for 'PolarAxes'
    extractBlock1Display.PolarAxes.Visibility = 0
    extractBlock1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
    extractBlock1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
    extractBlock1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    extractBlock1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
    extractBlock1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    extractBlock1Display.PolarAxes.EnableCustomRange = 0
    extractBlock1Display.PolarAxes.CustomRange = [0.0, 1.0]
    extractBlock1Display.PolarAxes.AutoPole = 1
    extractBlock1Display.PolarAxes.PolarAxisVisibility = 1
    extractBlock1Display.PolarAxes.RadialAxesVisibility = 1
    extractBlock1Display.PolarAxes.DrawRadialGridlines = 1
    extractBlock1Display.PolarAxes.PolarArcsVisibility = 1
    extractBlock1Display.PolarAxes.DrawPolarArcsGridlines = 1
    extractBlock1Display.PolarAxes.NumberOfRadialAxes = 0
    extractBlock1Display.PolarAxes.DeltaAngleRadialAxes = 45.0
    extractBlock1Display.PolarAxes.NumberOfPolarAxes = 5
    extractBlock1Display.PolarAxes.DeltaRangePolarAxes = 0.0
    extractBlock1Display.PolarAxes.CustomMinRadius = 1
    extractBlock1Display.PolarAxes.MinimumRadius = 0.0
    extractBlock1Display.PolarAxes.CustomAngles = 1
    extractBlock1Display.PolarAxes.MinimumAngle = 0.0
    extractBlock1Display.PolarAxes.MaximumAngle = 90.0
    extractBlock1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
    extractBlock1Display.PolarAxes.PolarArcResolutionPerDegree = 0.2
    extractBlock1Display.PolarAxes.Ratio = 1.0
    extractBlock1Display.PolarAxes.EnableOverallColor = 1
    extractBlock1Display.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
    extractBlock1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    extractBlock1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    extractBlock1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    extractBlock1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    extractBlock1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    extractBlock1Display.PolarAxes.PolarAxisTitleVisibility = 1
    extractBlock1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
    extractBlock1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    extractBlock1Display.PolarAxes.PolarTitleOffset = [20.0, 20.0]
    extractBlock1Display.PolarAxes.PolarLabelVisibility = 1
    extractBlock1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
    extractBlock1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
    extractBlock1Display.PolarAxes.PolarLabelOffset = 10.0
    extractBlock1Display.PolarAxes.PolarExponentOffset = 5.0
    extractBlock1Display.PolarAxes.RadialTitleVisibility = 1
    extractBlock1Display.PolarAxes.RadialTitleFormat = '%-#3.1f'
    extractBlock1Display.PolarAxes.RadialTitleLocation = 'Bottom'
    extractBlock1Display.PolarAxes.RadialTitleOffset = [20.0, 0.0]
    extractBlock1Display.PolarAxes.RadialUnitsVisibility = 1
    extractBlock1Display.PolarAxes.ScreenSize = 10.0
    extractBlock1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
    extractBlock1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    extractBlock1Display.PolarAxes.PolarAxisTitleFontFile = ''
    extractBlock1Display.PolarAxes.PolarAxisTitleBold = 0
    extractBlock1Display.PolarAxes.PolarAxisTitleItalic = 0
    extractBlock1Display.PolarAxes.PolarAxisTitleShadow = 0
    extractBlock1Display.PolarAxes.PolarAxisTitleFontSize = 12
    extractBlock1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
    extractBlock1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    extractBlock1Display.PolarAxes.PolarAxisLabelFontFile = ''
    extractBlock1Display.PolarAxes.PolarAxisLabelBold = 0
    extractBlock1Display.PolarAxes.PolarAxisLabelItalic = 0
    extractBlock1Display.PolarAxes.PolarAxisLabelShadow = 0
    extractBlock1Display.PolarAxes.PolarAxisLabelFontSize = 12
    extractBlock1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
    extractBlock1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    extractBlock1Display.PolarAxes.LastRadialAxisTextFontFile = ''
    extractBlock1Display.PolarAxes.LastRadialAxisTextBold = 0
    extractBlock1Display.PolarAxes.LastRadialAxisTextItalic = 0
    extractBlock1Display.PolarAxes.LastRadialAxisTextShadow = 0
    extractBlock1Display.PolarAxes.LastRadialAxisTextFontSize = 12
    extractBlock1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    extractBlock1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    extractBlock1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    extractBlock1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
    extractBlock1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
    extractBlock1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
    extractBlock1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    extractBlock1Display.PolarAxes.EnableDistanceLOD = 1
    extractBlock1Display.PolarAxes.DistanceLODThreshold = 0.7
    extractBlock1Display.PolarAxes.EnableViewAngleLOD = 1
    extractBlock1Display.PolarAxes.ViewAngleLODThreshold = 0.7
    extractBlock1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
    extractBlock1Display.PolarAxes.PolarTicksVisibility = 1
    extractBlock1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
    extractBlock1Display.PolarAxes.TickLocation = 'Both'
    extractBlock1Display.PolarAxes.AxisTickVisibility = 1
    extractBlock1Display.PolarAxes.AxisMinorTickVisibility = 0
    extractBlock1Display.PolarAxes.AxisTickMatchesPolarAxes = 1
    extractBlock1Display.PolarAxes.DeltaRangeMajor = 1.0
    extractBlock1Display.PolarAxes.DeltaRangeMinor = 0.5
    extractBlock1Display.PolarAxes.ArcTickVisibility = 1
    extractBlock1Display.PolarAxes.ArcMinorTickVisibility = 0
    extractBlock1Display.PolarAxes.ArcTickMatchesRadialAxes = 1
    extractBlock1Display.PolarAxes.DeltaAngleMajor = 10.0
    extractBlock1Display.PolarAxes.DeltaAngleMinor = 5.0
    extractBlock1Display.PolarAxes.TickRatioRadiusSize = 0.02
    extractBlock1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
    extractBlock1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
    extractBlock1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
    extractBlock1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
    extractBlock1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    extractBlock1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    extractBlock1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    extractBlock1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    extractBlock1Display.PolarAxes.ArcMajorTickSize = 0.0
    extractBlock1Display.PolarAxes.ArcTickRatioSize = 0.3
    extractBlock1Display.PolarAxes.ArcMajorTickThickness = 1.0
    extractBlock1Display.PolarAxes.ArcTickRatioThickness = 0.5
    extractBlock1Display.PolarAxes.Use2DMode = 0
    extractBlock1Display.PolarAxes.UseLogAxis = 0

    # hide data in view
    Hide(microstructure_vizxdmf, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932

    # create a new 'Glyph'
    glyph1 = Glyph(registrationName='Glyph1', Input=extractBlock1,
        GlyphType='Arrow')
    glyph1.OrientationArray = ['POINTS', 'f0']
    glyph1.ScaleArray = ['POINTS', 'No scale array']
    glyph1.VectorScaleMode = 'Scale by Magnitude'
    glyph1.ScaleFactor = 0.7499993801116944
    glyph1.GlyphTransform = 'Transform2'
    glyph1.GlyphMode = 'Uniform Spatial Distribution (Bounds Based)'
    glyph1.MaximumNumberOfSamplePoints = 5000
    glyph1.Seed = 10339
    glyph1.Stride = 1

    # init the 'Arrow' selected for 'GlyphType'
    glyph1.GlyphType.TipResolution = 6
    glyph1.GlyphType.TipRadius = 0.1
    glyph1.GlyphType.TipLength = 0.35
    glyph1.GlyphType.ShaftResolution = 6
    glyph1.GlyphType.ShaftRadius = 0.03
    glyph1.GlyphType.Invert = 0

    # init the 'Transform2' selected for 'GlyphTransform'
    glyph1.GlyphTransform.Translate = [0.0, 0.0, 0.0]
    glyph1.GlyphTransform.Rotate = [0.0, 0.0, 0.0]
    glyph1.GlyphTransform.Scale = [1.0, 1.0, 1.0]

    # show data in view
    glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    glyph1Display.Selection = None
    glyph1Display.Representation = 'Surface'
    glyph1Display.ColorArrayName = [None, '']
    glyph1Display.LookupTable = None
    glyph1Display.MapScalars = 1
    glyph1Display.MultiComponentsMapping = 0
    glyph1Display.InterpolateScalarsBeforeMapping = 1
    glyph1Display.UseNanColorForMissingArrays = 0
    glyph1Display.Opacity = 1.0
    glyph1Display.PointSize = 2.0
    glyph1Display.LineWidth = 1.0
    glyph1Display.RenderLinesAsTubes = 0
    glyph1Display.RenderPointsAsSpheres = 0
    glyph1Display.Interpolation = 'Gouraud'
    glyph1Display.Specular = 0.0
    glyph1Display.SpecularColor = [1.0, 1.0, 1.0]
    glyph1Display.SpecularPower = 100.0
    glyph1Display.Luminosity = 0.0
    glyph1Display.Ambient = 0.0
    glyph1Display.Diffuse = 1.0
    glyph1Display.Roughness = 0.3
    glyph1Display.Metallic = 0.0
    glyph1Display.EdgeTint = [1.0, 1.0, 1.0]
    glyph1Display.Anisotropy = 0.0
    glyph1Display.AnisotropyRotation = 0.0
    glyph1Display.BaseIOR = 1.5
    glyph1Display.CoatStrength = 0.0
    glyph1Display.CoatIOR = 2.0
    glyph1Display.CoatRoughness = 0.0
    glyph1Display.CoatColor = [1.0, 1.0, 1.0]
    glyph1Display.SelectTCoordArray = 'None'
    glyph1Display.SelectNormalArray = 'None'
    glyph1Display.SelectTangentArray = 'None'
    glyph1Display.Texture = None
    glyph1Display.RepeatTextures = 1
    glyph1Display.InterpolateTextures = 0
    glyph1Display.SeamlessU = 0
    glyph1Display.SeamlessV = 0
    glyph1Display.UseMipmapTextures = 0
    glyph1Display.ShowTexturesOnBackface = 1
    glyph1Display.BaseColorTexture = None
    glyph1Display.NormalTexture = None
    glyph1Display.NormalScale = 1.0
    glyph1Display.CoatNormalTexture = None
    glyph1Display.CoatNormalScale = 1.0
    glyph1Display.MaterialTexture = None
    glyph1Display.OcclusionStrength = 1.0
    glyph1Display.AnisotropyTexture = None
    glyph1Display.EmissiveTexture = None
    glyph1Display.EmissiveFactor = [1.0, 1.0, 1.0]
    glyph1Display.FlipTextures = 0
    glyph1Display.EdgeOpacity = 1.0
    glyph1Display.BackfaceRepresentation = 'Follow Frontface'
    glyph1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    glyph1Display.BackfaceOpacity = 1.0
    glyph1Display.Position = [0.0, 0.0, 0.0]
    glyph1Display.Scale = [1.0, 1.0, 1.0]
    glyph1Display.Orientation = [0.0, 0.0, 0.0]
    glyph1Display.Origin = [0.0, 0.0, 0.0]
    glyph1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    glyph1Display.Pickable = 1
    glyph1Display.Triangulate = 0
    glyph1Display.UseShaderReplacements = 0
    glyph1Display.ShaderReplacements = ''
    glyph1Display.NonlinearSubdivisionLevel = 1
    glyph1Display.MatchBoundariesIgnoringCellOrder = 0
    glyph1Display.UseDataPartitions = 0
    glyph1Display.OSPRayUseScaleArray = 'All Approximate'
    glyph1Display.OSPRayScaleArray = 'f0'
    glyph1Display.OSPRayScaleFunction = 'Piecewise Function'
    glyph1Display.OSPRayMaterial = 'None'
    glyph1Display.Assembly = 'Hierarchy'
    glyph1Display.BlockSelectors = ['/']
    glyph1Display.BlockColors = []
    glyph1Display.BlockOpacities = []
    glyph1Display.Orient = 0
    glyph1Display.OrientationMode = 'Direction'
    glyph1Display.SelectOrientationVectors = 'f0'
    glyph1Display.Scaling = 0
    glyph1Display.ScaleMode = 'No Data Scaling Off'
    glyph1Display.ScaleFactor = 0.7701293468475342
    glyph1Display.SelectScaleArray = 'None'
    glyph1Display.GlyphType = 'Arrow'
    glyph1Display.UseGlyphTable = 0
    glyph1Display.GlyphTableIndexArray = 'None'
    glyph1Display.UseCompositeGlyphTable = 0
    glyph1Display.UseGlyphCullingAndLOD = 0
    glyph1Display.LODValues = []
    glyph1Display.ColorByLODIndex = 0
    glyph1Display.GaussianRadius = 0.03850646734237671
    glyph1Display.ShaderPreset = 'Sphere'
    glyph1Display.CustomTriangleScale = 3
    glyph1Display.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
    float gaussian = exp(-0.5*dist2);
    opacity = opacity*gaussian;
    """
    glyph1Display.Emissive = 0
    glyph1Display.ScaleByArray = 0
    glyph1Display.SetScaleArray = ['POINTS', 'f0']
    glyph1Display.ScaleArrayComponent = 'X'
    glyph1Display.UseScaleFunction = 1
    glyph1Display.ScaleTransferFunction = 'Piecewise Function'
    glyph1Display.OpacityByArray = 0
    glyph1Display.OpacityArray = ['POINTS', 'f0']
    glyph1Display.OpacityArrayComponent = 'X'
    glyph1Display.OpacityTransferFunction = 'Piecewise Function'
    glyph1Display.DataAxesGrid = 'Grid Axes Representation'
    glyph1Display.SelectionCellLabelBold = 0
    glyph1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    glyph1Display.SelectionCellLabelFontFamily = 'Arial'
    glyph1Display.SelectionCellLabelFontFile = ''
    glyph1Display.SelectionCellLabelFontSize = 18
    glyph1Display.SelectionCellLabelItalic = 0
    glyph1Display.SelectionCellLabelJustification = 'Left'
    glyph1Display.SelectionCellLabelOpacity = 1.0
    glyph1Display.SelectionCellLabelShadow = 0
    glyph1Display.SelectionPointLabelBold = 0
    glyph1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    glyph1Display.SelectionPointLabelFontFamily = 'Arial'
    glyph1Display.SelectionPointLabelFontFile = ''
    glyph1Display.SelectionPointLabelFontSize = 18
    glyph1Display.SelectionPointLabelItalic = 0
    glyph1Display.SelectionPointLabelJustification = 'Left'
    glyph1Display.SelectionPointLabelOpacity = 1.0
    glyph1Display.SelectionPointLabelShadow = 0
    glyph1Display.PolarAxes = 'Polar Axes Representation'
    glyph1Display.SelectInputVectors = ['POINTS', 'f0']
    glyph1Display.NumberOfSteps = 40
    glyph1Display.StepSize = 0.25
    glyph1Display.NormalizeVectors = 1
    glyph1Display.EnhancedLIC = 1
    glyph1Display.ColorMode = 'Blend'
    glyph1Display.LICIntensity = 0.8
    glyph1Display.MapModeBias = 0.0
    glyph1Display.EnhanceContrast = 'Off'
    glyph1Display.LowLICContrastEnhancementFactor = 0.0
    glyph1Display.HighLICContrastEnhancementFactor = 0.0
    glyph1Display.LowColorContrastEnhancementFactor = 0.0
    glyph1Display.HighColorContrastEnhancementFactor = 0.0
    glyph1Display.AntiAlias = 0
    glyph1Display.MaskOnSurface = 1
    glyph1Display.MaskThreshold = 0.0
    glyph1Display.MaskIntensity = 0.0
    glyph1Display.MaskColor = [0.5, 0.5, 0.5]
    glyph1Display.GenerateNoiseTexture = 0
    glyph1Display.NoiseType = 'Gaussian'
    glyph1Display.NoiseTextureSize = 128
    glyph1Display.NoiseGrainSize = 2
    glyph1Display.MinNoiseValue = 0.0
    glyph1Display.MaxNoiseValue = 0.8
    glyph1Display.NumberOfNoiseLevels = 1024
    glyph1Display.ImpulseNoiseProbability = 1.0
    glyph1Display.ImpulseNoiseBackgroundValue = 0.0
    glyph1Display.NoiseGeneratorSeed = 1
    glyph1Display.CompositeStrategy = 'AUTO'
    glyph1Display.UseLICForLOD = 0
    glyph1Display.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    glyph1Display.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]
    glyph1Display.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    glyph1Display.GlyphType.TipResolution = 6
    glyph1Display.GlyphType.TipRadius = 0.1
    glyph1Display.GlyphType.TipLength = 0.35
    glyph1Display.GlyphType.ShaftResolution = 6
    glyph1Display.GlyphType.ShaftRadius = 0.03
    glyph1Display.GlyphType.Invert = 0

    # init the 'Piecewise Function' selected for 'ScaleTransferFunction'
    glyph1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    glyph1Display.ScaleTransferFunction.UseLogScale = 0

    # init the 'Piecewise Function' selected for 'OpacityTransferFunction'
    glyph1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    glyph1Display.OpacityTransferFunction.UseLogScale = 0

    # init the 'Grid Axes Representation' selected for 'DataAxesGrid'
    glyph1Display.DataAxesGrid.XTitle = 'X Axis'
    glyph1Display.DataAxesGrid.YTitle = 'Y Axis'
    glyph1Display.DataAxesGrid.ZTitle = 'Z Axis'
    glyph1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.XTitleFontFile = ''
    glyph1Display.DataAxesGrid.XTitleBold = 0
    glyph1Display.DataAxesGrid.XTitleItalic = 0
    glyph1Display.DataAxesGrid.XTitleFontSize = 12
    glyph1Display.DataAxesGrid.XTitleShadow = 0
    glyph1Display.DataAxesGrid.XTitleOpacity = 1.0
    glyph1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.YTitleFontFile = ''
    glyph1Display.DataAxesGrid.YTitleBold = 0
    glyph1Display.DataAxesGrid.YTitleItalic = 0
    glyph1Display.DataAxesGrid.YTitleFontSize = 12
    glyph1Display.DataAxesGrid.YTitleShadow = 0
    glyph1Display.DataAxesGrid.YTitleOpacity = 1.0
    glyph1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.ZTitleFontFile = ''
    glyph1Display.DataAxesGrid.ZTitleBold = 0
    glyph1Display.DataAxesGrid.ZTitleItalic = 0
    glyph1Display.DataAxesGrid.ZTitleFontSize = 12
    glyph1Display.DataAxesGrid.ZTitleShadow = 0
    glyph1Display.DataAxesGrid.ZTitleOpacity = 1.0
    glyph1Display.DataAxesGrid.FacesToRender = 63
    glyph1Display.DataAxesGrid.CullBackface = 0
    glyph1Display.DataAxesGrid.CullFrontface = 1
    glyph1Display.DataAxesGrid.ShowGrid = 0
    glyph1Display.DataAxesGrid.ShowEdges = 1
    glyph1Display.DataAxesGrid.ShowTicks = 1
    glyph1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
    glyph1Display.DataAxesGrid.AxesToLabel = 63
    glyph1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.XLabelFontFile = ''
    glyph1Display.DataAxesGrid.XLabelBold = 0
    glyph1Display.DataAxesGrid.XLabelItalic = 0
    glyph1Display.DataAxesGrid.XLabelFontSize = 12
    glyph1Display.DataAxesGrid.XLabelShadow = 0
    glyph1Display.DataAxesGrid.XLabelOpacity = 1.0
    glyph1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.YLabelFontFile = ''
    glyph1Display.DataAxesGrid.YLabelBold = 0
    glyph1Display.DataAxesGrid.YLabelItalic = 0
    glyph1Display.DataAxesGrid.YLabelFontSize = 12
    glyph1Display.DataAxesGrid.YLabelShadow = 0
    glyph1Display.DataAxesGrid.YLabelOpacity = 1.0
    glyph1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
    glyph1Display.DataAxesGrid.ZLabelFontFile = ''
    glyph1Display.DataAxesGrid.ZLabelBold = 0
    glyph1Display.DataAxesGrid.ZLabelItalic = 0
    glyph1Display.DataAxesGrid.ZLabelFontSize = 12
    glyph1Display.DataAxesGrid.ZLabelShadow = 0
    glyph1Display.DataAxesGrid.ZLabelOpacity = 1.0
    glyph1Display.DataAxesGrid.XAxisNotation = 'Mixed'
    glyph1Display.DataAxesGrid.XAxisPrecision = 2
    glyph1Display.DataAxesGrid.XAxisUseCustomLabels = 0
    glyph1Display.DataAxesGrid.XAxisLabels = []
    glyph1Display.DataAxesGrid.YAxisNotation = 'Mixed'
    glyph1Display.DataAxesGrid.YAxisPrecision = 2
    glyph1Display.DataAxesGrid.YAxisUseCustomLabels = 0
    glyph1Display.DataAxesGrid.YAxisLabels = []
    glyph1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
    glyph1Display.DataAxesGrid.ZAxisPrecision = 2
    glyph1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
    glyph1Display.DataAxesGrid.ZAxisLabels = []
    glyph1Display.DataAxesGrid.UseCustomBounds = 0
    glyph1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'Polar Axes Representation' selected for 'PolarAxes'
    glyph1Display.PolarAxes.Visibility = 0
    glyph1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
    glyph1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    glyph1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
    glyph1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    glyph1Display.PolarAxes.EnableCustomRange = 0
    glyph1Display.PolarAxes.CustomRange = [0.0, 1.0]
    glyph1Display.PolarAxes.AutoPole = 1
    glyph1Display.PolarAxes.PolarAxisVisibility = 1
    glyph1Display.PolarAxes.RadialAxesVisibility = 1
    glyph1Display.PolarAxes.DrawRadialGridlines = 1
    glyph1Display.PolarAxes.PolarArcsVisibility = 1
    glyph1Display.PolarAxes.DrawPolarArcsGridlines = 1
    glyph1Display.PolarAxes.NumberOfRadialAxes = 0
    glyph1Display.PolarAxes.DeltaAngleRadialAxes = 45.0
    glyph1Display.PolarAxes.NumberOfPolarAxes = 5
    glyph1Display.PolarAxes.DeltaRangePolarAxes = 0.0
    glyph1Display.PolarAxes.CustomMinRadius = 1
    glyph1Display.PolarAxes.MinimumRadius = 0.0
    glyph1Display.PolarAxes.CustomAngles = 1
    glyph1Display.PolarAxes.MinimumAngle = 0.0
    glyph1Display.PolarAxes.MaximumAngle = 90.0
    glyph1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
    glyph1Display.PolarAxes.PolarArcResolutionPerDegree = 0.2
    glyph1Display.PolarAxes.Ratio = 1.0
    glyph1Display.PolarAxes.EnableOverallColor = 1
    glyph1Display.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    glyph1Display.PolarAxes.PolarAxisTitleVisibility = 1
    glyph1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
    glyph1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    glyph1Display.PolarAxes.PolarTitleOffset = [20.0, 20.0]
    glyph1Display.PolarAxes.PolarLabelVisibility = 1
    glyph1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
    glyph1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
    glyph1Display.PolarAxes.PolarLabelOffset = 10.0
    glyph1Display.PolarAxes.PolarExponentOffset = 5.0
    glyph1Display.PolarAxes.RadialTitleVisibility = 1
    glyph1Display.PolarAxes.RadialTitleFormat = '%-#3.1f'
    glyph1Display.PolarAxes.RadialTitleLocation = 'Bottom'
    glyph1Display.PolarAxes.RadialTitleOffset = [20.0, 0.0]
    glyph1Display.PolarAxes.RadialUnitsVisibility = 1
    glyph1Display.PolarAxes.ScreenSize = 10.0
    glyph1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
    glyph1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    glyph1Display.PolarAxes.PolarAxisTitleFontFile = ''
    glyph1Display.PolarAxes.PolarAxisTitleBold = 0
    glyph1Display.PolarAxes.PolarAxisTitleItalic = 0
    glyph1Display.PolarAxes.PolarAxisTitleShadow = 0
    glyph1Display.PolarAxes.PolarAxisTitleFontSize = 12
    glyph1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
    glyph1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    glyph1Display.PolarAxes.PolarAxisLabelFontFile = ''
    glyph1Display.PolarAxes.PolarAxisLabelBold = 0
    glyph1Display.PolarAxes.PolarAxisLabelItalic = 0
    glyph1Display.PolarAxes.PolarAxisLabelShadow = 0
    glyph1Display.PolarAxes.PolarAxisLabelFontSize = 12
    glyph1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
    glyph1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    glyph1Display.PolarAxes.LastRadialAxisTextFontFile = ''
    glyph1Display.PolarAxes.LastRadialAxisTextBold = 0
    glyph1Display.PolarAxes.LastRadialAxisTextItalic = 0
    glyph1Display.PolarAxes.LastRadialAxisTextShadow = 0
    glyph1Display.PolarAxes.LastRadialAxisTextFontSize = 12
    glyph1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    glyph1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
    glyph1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
    glyph1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
    glyph1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    glyph1Display.PolarAxes.EnableDistanceLOD = 1
    glyph1Display.PolarAxes.DistanceLODThreshold = 0.7
    glyph1Display.PolarAxes.EnableViewAngleLOD = 1
    glyph1Display.PolarAxes.ViewAngleLODThreshold = 0.7
    glyph1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
    glyph1Display.PolarAxes.PolarTicksVisibility = 1
    glyph1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
    glyph1Display.PolarAxes.TickLocation = 'Both'
    glyph1Display.PolarAxes.AxisTickVisibility = 1
    glyph1Display.PolarAxes.AxisMinorTickVisibility = 0
    glyph1Display.PolarAxes.AxisTickMatchesPolarAxes = 1
    glyph1Display.PolarAxes.DeltaRangeMajor = 1.0
    glyph1Display.PolarAxes.DeltaRangeMinor = 0.5
    glyph1Display.PolarAxes.ArcTickVisibility = 1
    glyph1Display.PolarAxes.ArcMinorTickVisibility = 0
    glyph1Display.PolarAxes.ArcTickMatchesRadialAxes = 1
    glyph1Display.PolarAxes.DeltaAngleMajor = 10.0
    glyph1Display.PolarAxes.DeltaAngleMinor = 5.0
    glyph1Display.PolarAxes.TickRatioRadiusSize = 0.02
    glyph1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
    glyph1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
    glyph1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
    glyph1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
    glyph1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    glyph1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    glyph1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    glyph1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    glyph1Display.PolarAxes.ArcMajorTickSize = 0.0
    glyph1Display.PolarAxes.ArcTickRatioSize = 0.3
    glyph1Display.PolarAxes.ArcMajorTickThickness = 1.0
    glyph1Display.PolarAxes.ArcTickRatioThickness = 0.5
    glyph1Display.PolarAxes.Use2DMode = 0
    glyph1Display.PolarAxes.UseLogAxis = 0

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932

    # hide data in view
    Hide(extractBlock1, renderView1)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932

    # set active source
    SetActiveSource(extractBlock1)

    # show data in view
    extractBlock1Display = Show(extractBlock1, renderView1, 'UnstructuredGridRepresentation')

    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932

    # create a new 'Clip'
    clip1 = Clip(registrationName='Clip1', Input=extractBlock1)
    clip1.ClipType = 'Plane'
    clip1.HyperTreeGridClipper = 'Plane'
    clip1.Scalars = [None, '']
    clip1.Value = 0.0
    clip1.Invert = 1
    clip1.Crinkleclip = 0
    clip1.Exact = 0

    # init the 'Plane' selected for 'ClipType'
    clip1.ClipType.Origin = [-1.5625, 0.0, 0.0]
    clip1.ClipType.Normal = [1.0, 0.0, 0.0]
    clip1.ClipType.Offset = 0.0

    # init the 'Plane' selected for 'HyperTreeGridClipper'
    clip1.HyperTreeGridClipper.Origin = [-1.5625, 0.0, 0.0]
    clip1.HyperTreeGridClipper.Normal = [1.0, 0.0, 0.0]
    clip1.HyperTreeGridClipper.Offset = 0.0
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932

    # toggle interactive widget visibility (only when running from the GUI)
    HideInteractiveWidgets(proxy=clip1.ClipType)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932

    # toggle interactive widget visibility (only when running from the GUI)
    ShowInteractiveWidgets(proxy=clip1.ClipType)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932

    # Properties modified on clip1
    clip1.Scalars = ['POINTS', '']

    # Properties modified on clip1.ClipType
    clip1.ClipType.Normal = [0.0, 1.0, 0.0]

    # show data in view
    clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    clip1Display.Selection = None
    clip1Display.Representation = 'Surface'
    clip1Display.ColorArrayName = [None, '']
    clip1Display.LookupTable = None
    clip1Display.MapScalars = 1
    clip1Display.MultiComponentsMapping = 0
    clip1Display.InterpolateScalarsBeforeMapping = 1
    clip1Display.UseNanColorForMissingArrays = 0
    clip1Display.Opacity = 1.0
    clip1Display.PointSize = 2.0
    clip1Display.LineWidth = 1.0
    clip1Display.RenderLinesAsTubes = 0
    clip1Display.RenderPointsAsSpheres = 0
    clip1Display.Interpolation = 'Gouraud'
    clip1Display.Specular = 0.0
    clip1Display.SpecularColor = [1.0, 1.0, 1.0]
    clip1Display.SpecularPower = 100.0
    clip1Display.Luminosity = 0.0
    clip1Display.Ambient = 0.0
    clip1Display.Diffuse = 1.0
    clip1Display.Roughness = 0.3
    clip1Display.Metallic = 0.0
    clip1Display.EdgeTint = [1.0, 1.0, 1.0]
    clip1Display.Anisotropy = 0.0
    clip1Display.AnisotropyRotation = 0.0
    clip1Display.BaseIOR = 1.5
    clip1Display.CoatStrength = 0.0
    clip1Display.CoatIOR = 2.0
    clip1Display.CoatRoughness = 0.0
    clip1Display.CoatColor = [1.0, 1.0, 1.0]
    clip1Display.SelectTCoordArray = 'None'
    clip1Display.SelectNormalArray = 'None'
    clip1Display.SelectTangentArray = 'None'
    clip1Display.Texture = None
    clip1Display.RepeatTextures = 1
    clip1Display.InterpolateTextures = 0
    clip1Display.SeamlessU = 0
    clip1Display.SeamlessV = 0
    clip1Display.UseMipmapTextures = 0
    clip1Display.ShowTexturesOnBackface = 1
    clip1Display.BaseColorTexture = None
    clip1Display.NormalTexture = None
    clip1Display.NormalScale = 1.0
    clip1Display.CoatNormalTexture = None
    clip1Display.CoatNormalScale = 1.0
    clip1Display.MaterialTexture = None
    clip1Display.OcclusionStrength = 1.0
    clip1Display.AnisotropyTexture = None
    clip1Display.EmissiveTexture = None
    clip1Display.EmissiveFactor = [1.0, 1.0, 1.0]
    clip1Display.FlipTextures = 0
    clip1Display.EdgeOpacity = 1.0
    clip1Display.BackfaceRepresentation = 'Follow Frontface'
    clip1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    clip1Display.BackfaceOpacity = 1.0
    clip1Display.Position = [0.0, 0.0, 0.0]
    clip1Display.Scale = [1.0, 1.0, 1.0]
    clip1Display.Orientation = [0.0, 0.0, 0.0]
    clip1Display.Origin = [0.0, 0.0, 0.0]
    clip1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    clip1Display.Pickable = 1
    clip1Display.Triangulate = 0
    clip1Display.UseShaderReplacements = 0
    clip1Display.ShaderReplacements = ''
    clip1Display.NonlinearSubdivisionLevel = 1
    clip1Display.MatchBoundariesIgnoringCellOrder = 0
    clip1Display.UseDataPartitions = 0
    clip1Display.OSPRayUseScaleArray = 'All Approximate'
    clip1Display.OSPRayScaleArray = 'f0'
    clip1Display.OSPRayScaleFunction = 'Piecewise Function'
    clip1Display.OSPRayMaterial = 'None'
    clip1Display.Assembly = 'Hierarchy'
    clip1Display.BlockSelectors = ['/']
    clip1Display.BlockColors = []
    clip1Display.BlockOpacities = []
    clip1Display.Orient = 0
    clip1Display.OrientationMode = 'Direction'
    clip1Display.SelectOrientationVectors = 'f0'
    clip1Display.Scaling = 0
    clip1Display.ScaleMode = 'No Data Scaling Off'
    clip1Display.ScaleFactor = 0.7499993801116944
    clip1Display.SelectScaleArray = 'None'
    clip1Display.GlyphType = 'Arrow'
    clip1Display.UseGlyphTable = 0
    clip1Display.GlyphTableIndexArray = 'None'
    clip1Display.UseCompositeGlyphTable = 0
    clip1Display.UseGlyphCullingAndLOD = 0
    clip1Display.LODValues = []
    clip1Display.ColorByLODIndex = 0
    clip1Display.GaussianRadius = 0.037499969005584714
    clip1Display.ShaderPreset = 'Sphere'
    clip1Display.CustomTriangleScale = 3
    clip1Display.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
    float gaussian = exp(-0.5*dist2);
    opacity = opacity*gaussian;
    """
    clip1Display.Emissive = 0
    clip1Display.ScaleByArray = 0
    clip1Display.SetScaleArray = ['POINTS', 'f0']
    clip1Display.ScaleArrayComponent = 'X'
    clip1Display.UseScaleFunction = 1
    clip1Display.ScaleTransferFunction = 'Piecewise Function'
    clip1Display.OpacityByArray = 0
    clip1Display.OpacityArray = ['POINTS', 'f0']
    clip1Display.OpacityArrayComponent = 'X'
    clip1Display.OpacityTransferFunction = 'Piecewise Function'
    clip1Display.DataAxesGrid = 'Grid Axes Representation'
    clip1Display.SelectionCellLabelBold = 0
    clip1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    clip1Display.SelectionCellLabelFontFamily = 'Arial'
    clip1Display.SelectionCellLabelFontFile = ''
    clip1Display.SelectionCellLabelFontSize = 18
    clip1Display.SelectionCellLabelItalic = 0
    clip1Display.SelectionCellLabelJustification = 'Left'
    clip1Display.SelectionCellLabelOpacity = 1.0
    clip1Display.SelectionCellLabelShadow = 0
    clip1Display.SelectionPointLabelBold = 0
    clip1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    clip1Display.SelectionPointLabelFontFamily = 'Arial'
    clip1Display.SelectionPointLabelFontFile = ''
    clip1Display.SelectionPointLabelFontSize = 18
    clip1Display.SelectionPointLabelItalic = 0
    clip1Display.SelectionPointLabelJustification = 'Left'
    clip1Display.SelectionPointLabelOpacity = 1.0
    clip1Display.SelectionPointLabelShadow = 0
    clip1Display.PolarAxes = 'Polar Axes Representation'
    clip1Display.ScalarOpacityFunction = None
    clip1Display.ScalarOpacityUnitDistance = 0.584580221109436
    clip1Display.UseSeparateOpacityArray = 0
    clip1Display.OpacityArrayName = ['POINTS', 'f0']
    clip1Display.OpacityComponent = 'X'
    clip1Display.SelectMapper = 'Projected tetra'
    clip1Display.SamplingDimensions = [128, 128, 128]
    clip1Display.UseFloatingPointFrameBuffer = 1
    clip1Display.SelectInputVectors = ['POINTS', 'f0']
    clip1Display.NumberOfSteps = 40
    clip1Display.StepSize = 0.25
    clip1Display.NormalizeVectors = 1
    clip1Display.EnhancedLIC = 1
    clip1Display.ColorMode = 'Blend'
    clip1Display.LICIntensity = 0.8
    clip1Display.MapModeBias = 0.0
    clip1Display.EnhanceContrast = 'Off'
    clip1Display.LowLICContrastEnhancementFactor = 0.0
    clip1Display.HighLICContrastEnhancementFactor = 0.0
    clip1Display.LowColorContrastEnhancementFactor = 0.0
    clip1Display.HighColorContrastEnhancementFactor = 0.0
    clip1Display.AntiAlias = 0
    clip1Display.MaskOnSurface = 1
    clip1Display.MaskThreshold = 0.0
    clip1Display.MaskIntensity = 0.0
    clip1Display.MaskColor = [0.5, 0.5, 0.5]
    clip1Display.GenerateNoiseTexture = 0
    clip1Display.NoiseType = 'Gaussian'
    clip1Display.NoiseTextureSize = 128
    clip1Display.NoiseGrainSize = 2
    clip1Display.MinNoiseValue = 0.0
    clip1Display.MaxNoiseValue = 0.8
    clip1Display.NumberOfNoiseLevels = 1024
    clip1Display.ImpulseNoiseProbability = 1.0
    clip1Display.ImpulseNoiseBackgroundValue = 0.0
    clip1Display.NoiseGeneratorSeed = 1
    clip1Display.CompositeStrategy = 'AUTO'
    clip1Display.UseLICForLOD = 0
    clip1Display.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    clip1Display.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]
    clip1Display.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    clip1Display.GlyphType.TipResolution = 6
    clip1Display.GlyphType.TipRadius = 0.1
    clip1Display.GlyphType.TipLength = 0.35
    clip1Display.GlyphType.ShaftResolution = 6
    clip1Display.GlyphType.ShaftRadius = 0.03
    clip1Display.GlyphType.Invert = 0

    # init the 'Piecewise Function' selected for 'ScaleTransferFunction'
    clip1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    clip1Display.ScaleTransferFunction.UseLogScale = 0

    # init the 'Piecewise Function' selected for 'OpacityTransferFunction'
    clip1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    clip1Display.OpacityTransferFunction.UseLogScale = 0

    # init the 'Grid Axes Representation' selected for 'DataAxesGrid'
    clip1Display.DataAxesGrid.XTitle = 'X Axis'
    clip1Display.DataAxesGrid.YTitle = 'Y Axis'
    clip1Display.DataAxesGrid.ZTitle = 'Z Axis'
    clip1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
    clip1Display.DataAxesGrid.XTitleFontFile = ''
    clip1Display.DataAxesGrid.XTitleBold = 0
    clip1Display.DataAxesGrid.XTitleItalic = 0
    clip1Display.DataAxesGrid.XTitleFontSize = 12
    clip1Display.DataAxesGrid.XTitleShadow = 0
    clip1Display.DataAxesGrid.XTitleOpacity = 1.0
    clip1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
    clip1Display.DataAxesGrid.YTitleFontFile = ''
    clip1Display.DataAxesGrid.YTitleBold = 0
    clip1Display.DataAxesGrid.YTitleItalic = 0
    clip1Display.DataAxesGrid.YTitleFontSize = 12
    clip1Display.DataAxesGrid.YTitleShadow = 0
    clip1Display.DataAxesGrid.YTitleOpacity = 1.0
    clip1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
    clip1Display.DataAxesGrid.ZTitleFontFile = ''
    clip1Display.DataAxesGrid.ZTitleBold = 0
    clip1Display.DataAxesGrid.ZTitleItalic = 0
    clip1Display.DataAxesGrid.ZTitleFontSize = 12
    clip1Display.DataAxesGrid.ZTitleShadow = 0
    clip1Display.DataAxesGrid.ZTitleOpacity = 1.0
    clip1Display.DataAxesGrid.FacesToRender = 63
    clip1Display.DataAxesGrid.CullBackface = 0
    clip1Display.DataAxesGrid.CullFrontface = 1
    clip1Display.DataAxesGrid.ShowGrid = 0
    clip1Display.DataAxesGrid.ShowEdges = 1
    clip1Display.DataAxesGrid.ShowTicks = 1
    clip1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
    clip1Display.DataAxesGrid.AxesToLabel = 63
    clip1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
    clip1Display.DataAxesGrid.XLabelFontFile = ''
    clip1Display.DataAxesGrid.XLabelBold = 0
    clip1Display.DataAxesGrid.XLabelItalic = 0
    clip1Display.DataAxesGrid.XLabelFontSize = 12
    clip1Display.DataAxesGrid.XLabelShadow = 0
    clip1Display.DataAxesGrid.XLabelOpacity = 1.0
    clip1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
    clip1Display.DataAxesGrid.YLabelFontFile = ''
    clip1Display.DataAxesGrid.YLabelBold = 0
    clip1Display.DataAxesGrid.YLabelItalic = 0
    clip1Display.DataAxesGrid.YLabelFontSize = 12
    clip1Display.DataAxesGrid.YLabelShadow = 0
    clip1Display.DataAxesGrid.YLabelOpacity = 1.0
    clip1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
    clip1Display.DataAxesGrid.ZLabelFontFile = ''
    clip1Display.DataAxesGrid.ZLabelBold = 0
    clip1Display.DataAxesGrid.ZLabelItalic = 0
    clip1Display.DataAxesGrid.ZLabelFontSize = 12
    clip1Display.DataAxesGrid.ZLabelShadow = 0
    clip1Display.DataAxesGrid.ZLabelOpacity = 1.0
    clip1Display.DataAxesGrid.XAxisNotation = 'Mixed'
    clip1Display.DataAxesGrid.XAxisPrecision = 2
    clip1Display.DataAxesGrid.XAxisUseCustomLabels = 0
    clip1Display.DataAxesGrid.XAxisLabels = []
    clip1Display.DataAxesGrid.YAxisNotation = 'Mixed'
    clip1Display.DataAxesGrid.YAxisPrecision = 2
    clip1Display.DataAxesGrid.YAxisUseCustomLabels = 0
    clip1Display.DataAxesGrid.YAxisLabels = []
    clip1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
    clip1Display.DataAxesGrid.ZAxisPrecision = 2
    clip1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
    clip1Display.DataAxesGrid.ZAxisLabels = []
    clip1Display.DataAxesGrid.UseCustomBounds = 0
    clip1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'Polar Axes Representation' selected for 'PolarAxes'
    clip1Display.PolarAxes.Visibility = 0
    clip1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
    clip1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
    clip1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    clip1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
    clip1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    clip1Display.PolarAxes.EnableCustomRange = 0
    clip1Display.PolarAxes.CustomRange = [0.0, 1.0]
    clip1Display.PolarAxes.AutoPole = 1
    clip1Display.PolarAxes.PolarAxisVisibility = 1
    clip1Display.PolarAxes.RadialAxesVisibility = 1
    clip1Display.PolarAxes.DrawRadialGridlines = 1
    clip1Display.PolarAxes.PolarArcsVisibility = 1
    clip1Display.PolarAxes.DrawPolarArcsGridlines = 1
    clip1Display.PolarAxes.NumberOfRadialAxes = 0
    clip1Display.PolarAxes.DeltaAngleRadialAxes = 45.0
    clip1Display.PolarAxes.NumberOfPolarAxes = 5
    clip1Display.PolarAxes.DeltaRangePolarAxes = 0.0
    clip1Display.PolarAxes.CustomMinRadius = 1
    clip1Display.PolarAxes.MinimumRadius = 0.0
    clip1Display.PolarAxes.CustomAngles = 1
    clip1Display.PolarAxes.MinimumAngle = 0.0
    clip1Display.PolarAxes.MaximumAngle = 90.0
    clip1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
    clip1Display.PolarAxes.PolarArcResolutionPerDegree = 0.2
    clip1Display.PolarAxes.Ratio = 1.0
    clip1Display.PolarAxes.EnableOverallColor = 1
    clip1Display.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
    clip1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    clip1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    clip1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    clip1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    clip1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    clip1Display.PolarAxes.PolarAxisTitleVisibility = 1
    clip1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
    clip1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    clip1Display.PolarAxes.PolarTitleOffset = [20.0, 20.0]
    clip1Display.PolarAxes.PolarLabelVisibility = 1
    clip1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
    clip1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
    clip1Display.PolarAxes.PolarLabelOffset = 10.0
    clip1Display.PolarAxes.PolarExponentOffset = 5.0
    clip1Display.PolarAxes.RadialTitleVisibility = 1
    clip1Display.PolarAxes.RadialTitleFormat = '%-#3.1f'
    clip1Display.PolarAxes.RadialTitleLocation = 'Bottom'
    clip1Display.PolarAxes.RadialTitleOffset = [20.0, 0.0]
    clip1Display.PolarAxes.RadialUnitsVisibility = 1
    clip1Display.PolarAxes.ScreenSize = 10.0
    clip1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
    clip1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
    clip1Display.PolarAxes.PolarAxisTitleBold = 0
    clip1Display.PolarAxes.PolarAxisTitleItalic = 0
    clip1Display.PolarAxes.PolarAxisTitleShadow = 0
    clip1Display.PolarAxes.PolarAxisTitleFontSize = 12
    clip1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
    clip1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
    clip1Display.PolarAxes.PolarAxisLabelBold = 0
    clip1Display.PolarAxes.PolarAxisLabelItalic = 0
    clip1Display.PolarAxes.PolarAxisLabelShadow = 0
    clip1Display.PolarAxes.PolarAxisLabelFontSize = 12
    clip1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
    clip1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
    clip1Display.PolarAxes.LastRadialAxisTextBold = 0
    clip1Display.PolarAxes.LastRadialAxisTextItalic = 0
    clip1Display.PolarAxes.LastRadialAxisTextShadow = 0
    clip1Display.PolarAxes.LastRadialAxisTextFontSize = 12
    clip1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    clip1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    clip1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
    clip1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
    clip1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
    clip1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    clip1Display.PolarAxes.EnableDistanceLOD = 1
    clip1Display.PolarAxes.DistanceLODThreshold = 0.7
    clip1Display.PolarAxes.EnableViewAngleLOD = 1
    clip1Display.PolarAxes.ViewAngleLODThreshold = 0.7
    clip1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
    clip1Display.PolarAxes.PolarTicksVisibility = 1
    clip1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
    clip1Display.PolarAxes.TickLocation = 'Both'
    clip1Display.PolarAxes.AxisTickVisibility = 1
    clip1Display.PolarAxes.AxisMinorTickVisibility = 0
    clip1Display.PolarAxes.AxisTickMatchesPolarAxes = 1
    clip1Display.PolarAxes.DeltaRangeMajor = 1.0
    clip1Display.PolarAxes.DeltaRangeMinor = 0.5
    clip1Display.PolarAxes.ArcTickVisibility = 1
    clip1Display.PolarAxes.ArcMinorTickVisibility = 0
    clip1Display.PolarAxes.ArcTickMatchesRadialAxes = 1
    clip1Display.PolarAxes.DeltaAngleMajor = 10.0
    clip1Display.PolarAxes.DeltaAngleMinor = 5.0
    clip1Display.PolarAxes.TickRatioRadiusSize = 0.02
    clip1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
    clip1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
    clip1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
    clip1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
    clip1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    clip1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    clip1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    clip1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    clip1Display.PolarAxes.ArcMajorTickSize = 0.0
    clip1Display.PolarAxes.ArcTickRatioSize = 0.3
    clip1Display.PolarAxes.ArcMajorTickThickness = 1.0
    clip1Display.PolarAxes.ArcTickRatioThickness = 0.5
    clip1Display.PolarAxes.Use2DMode = 0
    clip1Display.PolarAxes.UseLogAxis = 0

    # hide data in view
    Hide(extractBlock1, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932

    # Properties modified on renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    # toggle interactive widget visibility (only when running from the GUI)
    HideInteractiveWidgets(proxy=clip1.ClipType)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    # set active source
    SetActiveSource(glyph1)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    # set scalar coloring
    ColorBy(glyph1Display, ('POINTS', 'f0', 'Magnitude'))

    # rescale color and/or opacity maps used to include current data range
    glyph1Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    glyph1Display.SetScalarBarVisibility(renderView1, True)

    # get 2D transfer function for 'f0'
    f0TF2D = GetTransferFunction2D('f0')
    f0TF2D.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
    f0TF2D.Boxes = []
    f0TF2D.ScalarRangeInitialized = 0
    f0TF2D.Range = [0.0, 1.0, 0.0, 1.0]
    f0TF2D.OutputDimensions = [10, 10]

    # get color transfer function/color map for 'f0'
    f0LUT = GetColorTransferFunction('f0')
    f0LUT.InterpretValuesAsCategories = 0
    f0LUT.AnnotationsInitialized = 0
    f0LUT.ShowCategoricalColorsinDataRangeOnly = 0
    f0LUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
    f0LUT.RescaleOnVisibilityChange = 0
    f0LUT.TransferFunction2D = f0TF2D
    f0LUT.RGBPoints = [0.9999999622881017, 0.231373, 0.298039, 0.752941, 1.0000000015474786, 0.865003, 0.865003, 0.865003, 1.0000000408068557, 0.705882, 0.0156863, 0.14902]
    f0LUT.UseLogScale = 0
    f0LUT.UseOpacityControlPointsFreehandDrawing = 0
    f0LUT.ShowDataHistogram = 0
    f0LUT.AutomaticDataHistogramComputation = 0
    f0LUT.DataHistogramNumberOfBins = 10
    f0LUT.ColorSpace = 'Diverging'
    f0LUT.UseBelowRangeColor = 0
    f0LUT.BelowRangeColor = [0.0, 0.0, 0.0]
    f0LUT.UseAboveRangeColor = 0
    f0LUT.AboveRangeColor = [0.5, 0.5, 0.5]
    f0LUT.NanColor = [1.0, 1.0, 0.0]
    f0LUT.NanOpacity = 1.0
    f0LUT.Discretize = 1
    f0LUT.NumberOfTableValues = 256
    f0LUT.ScalarRangeInitialized = 1.0
    f0LUT.HSVWrap = 0
    f0LUT.VectorComponent = 0
    f0LUT.VectorMode = 'Magnitude'
    f0LUT.AllowDuplicateScalars = 1
    f0LUT.Annotations = []
    f0LUT.ActiveAnnotatedValues = []
    f0LUT.IndexedColors = []
    f0LUT.IndexedOpacities = []
    f0LUT.EnableOpacityMapping = 0

    # get opacity transfer function/opacity map for 'f0'
    f0PWF = GetOpacityTransferFunction('f0')
    f0PWF.Points = [0.9999999622881017, 0.0, 0.5, 0.0, 1.0000000408068557, 1.0, 0.5, 0.0]
    f0PWF.AllowDuplicateScalars = 1
    f0PWF.UseLogScale = 0
    f0PWF.ScalarRangeInitialized = 1
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    # set scalar coloring
    ColorBy(glyph1Display, ('POINTS', 'f0', 'Y'))

    # rescale color and/or opacity maps used to exactly fit the current data range
    glyph1Display.RescaleTransferFunctionToDataRange(False, False)

    # Update a scalar bar component title.
    UpdateScalarBarsComponentTitle(f0LUT, glyph1Display)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    # set active source
    SetActiveSource(clip1)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    # change representation type
    clip1Display.SetRepresentationType('Surface With Edges')
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    # Properties modified on renderView1
    renderView1.UseColorPaletteForBackground = 0
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    # Properties modified on renderView1
    renderView1.Background = [1.0, 1.0, 1.0]
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    # set active source
    SetActiveSource(glyph1)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    # Properties modified on glyph1
    glyph1.MaximumNumberOfSamplePoints = 10000

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    # Properties modified on glyph1
    glyph1.GlyphMode = 'All Points'

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    # get layout
    layout1 = GetLayout()

    # layout/tab size in pixels
    layout1.SetSize(2893, 1215)

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    # save screenshot
    SaveScreenshot(filename=outname, viewOrLayout=renderView1, location=16, ImageResolution=[2893, 1215],
        FontScaling='Scale fonts proportionally',
        OverrideColorPalette='',
        StereoMode='No change',
        TransparentBackground=1,
        SaveInBackground=0,
        EmbedParaViewState=0, 
        # PNG options
        CompressionLevel='3',
        MetaData=['Application', 'ParaView'])
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    #================================================================
    # addendum: following script captures some of the application
    # state to faithfully reproduce the visualization during playback
    #================================================================

    #--------------------------------
    # saving layout sizes for layouts

    # layout/tab size in pixels
    layout1.SetSize(2893, 1215)

    #-----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
    renderView1.CameraPosition = [17.39973890545381, 0.3221369373642374, 15.381237247145213]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraViewUp = [0.6298529936308681, 0.008400773694759368, -0.7766689342413299]
    renderView1.CameraParallelScale = 6.319917701868932

    # destroy glyph1
    Delete(clip1)
    del clip1
    
    # destroy glyph1
    Delete(glyph1)
    del glyph1

        
        # destroy extractBlock1
    Delete(extractBlock1)
    del extractBlock1

    # destroy microstructure_vizxdmf
    Delete(microstructure_vizxdmf)
    del microstructure_vizxdmf
        
    ##--------------------------------------------
    ## You may need to add some code at the end of this python script depending on your usage, eg:
    #
    ## Render all views to see them appears
    # RenderAllViews()
    #
    ## Interact with the view, usefull when running from pvpython
    # Interact()
    #
    ## Save a screenshot of the active view
    # SaveScreenshot("path/to/screenshot.png")
    #
    ## Save a screenshot of a layout (multiple splitted view)
    # SaveScreenshot("path/to/screenshot.png", GetLayout())
    #
    ## Save all "Extractors" from the pipeline browser
    # SaveExtracts()
    #
    ## Save a animation of the current active view
    # SaveAnimation()
    #
    ## Please refer to the documentation of paraview.simple
    ## https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html
    ##--------------------------------------------
    

def save_ani_deformed_activation(fname_act, fname_disp, outname):
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # Properties modified on renderView1
    renderView1.UseColorPaletteForBackground = 0

    # get the material library
    materialLibrary1 = GetMaterialLibrary()
    # Adjust camera

    # Properties modified on renderView1
    renderView1.Background = [1.0, 1.0, 1.0]
    # Adjust camera

    # create a new 'Xdmf3 Reader T'
    displacementxdmf = Xdmf3ReaderT(registrationName='displacement.xdmf', FileName=[fname_disp])
    # Adjust camera

    # get animation scene
    animationScene1 = GetAnimationScene()

    # update animation scene based on data timesteps
    animationScene1.UpdateAnimationUsingDataTimeSteps()

    # create a new 'Xdmf3 Reader T'
    activation_resultsxdmf = Xdmf3ReaderT(registrationName='Activation_results.xdmf', FileName=[fname_act])

    # show data in view
    activation_resultsxdmfDisplay = Show(activation_resultsxdmf, renderView1, 'UnstructuredGridRepresentation')

    # get 2D transfer function for 'Activation'
    activationTF2D = GetTransferFunction2D('Activation')

    # get color transfer function/color map for 'Activation'
    activationLUT = GetColorTransferFunction('Activation')
    activationLUT.TransferFunction2D = activationTF2D
    activationLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 5.878906683738906e-39, 0.865003, 0.865003, 0.865003, 1.1757813367477812e-38, 0.705882, 0.0156863, 0.14902]
    activationLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'Activation'
    activationPWF = GetOpacityTransferFunction('Activation')
    activationPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    activationPWF.ScalarRangeInitialized = 1

    # trace defaults for the display properties.
    activation_resultsxdmfDisplay.Representation = 'Surface'
    activation_resultsxdmfDisplay.ColorArrayName = ['CELLS', 'Activation']
    activation_resultsxdmfDisplay.LookupTable = activationLUT
    activation_resultsxdmfDisplay.SelectTCoordArray = 'None'
    activation_resultsxdmfDisplay.SelectNormalArray = 'None'
    activation_resultsxdmfDisplay.SelectTangentArray = 'None'
    activation_resultsxdmfDisplay.OSPRayScaleFunction = 'Piecewise Function'
    activation_resultsxdmfDisplay.Assembly = ''
    activation_resultsxdmfDisplay.SelectOrientationVectors = 'None'
    activation_resultsxdmfDisplay.ScaleFactor = 0.7499993801116944
    activation_resultsxdmfDisplay.SelectScaleArray = 'Activation'
    activation_resultsxdmfDisplay.GlyphType = 'Arrow'
    activation_resultsxdmfDisplay.GlyphTableIndexArray = 'Activation'
    activation_resultsxdmfDisplay.GaussianRadius = 0.037499969005584714
    activation_resultsxdmfDisplay.SetScaleArray = [None, '']
    activation_resultsxdmfDisplay.ScaleTransferFunction = 'Piecewise Function'
    activation_resultsxdmfDisplay.OpacityArray = [None, '']
    activation_resultsxdmfDisplay.OpacityTransferFunction = 'Piecewise Function'
    activation_resultsxdmfDisplay.DataAxesGrid = 'Grid Axes Representation'
    activation_resultsxdmfDisplay.PolarAxes = 'Polar Axes Representation'
    activation_resultsxdmfDisplay.ScalarOpacityFunction = activationPWF
    activation_resultsxdmfDisplay.ScalarOpacityUnitDistance = 0.5583539716188769
    activation_resultsxdmfDisplay.OpacityArrayName = ['CELLS', 'Activation']
    activation_resultsxdmfDisplay.SelectInputVectors = [None, '']
    activation_resultsxdmfDisplay.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    activation_resultsxdmfDisplay.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    # show color bar/color legend
    activation_resultsxdmfDisplay.SetScalarBarVisibility(renderView1, True)

    # show data in view
    displacementxdmfDisplay = Show(displacementxdmf, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    displacementxdmfDisplay.Representation = 'Surface'
    displacementxdmfDisplay.ColorArrayName = [None, '']
    displacementxdmfDisplay.SelectTCoordArray = 'None'
    displacementxdmfDisplay.SelectNormalArray = 'None'
    displacementxdmfDisplay.SelectTangentArray = 'None'
    displacementxdmfDisplay.OSPRayScaleArray = 'Displacement'
    displacementxdmfDisplay.OSPRayScaleFunction = 'Piecewise Function'
    displacementxdmfDisplay.Assembly = ''
    displacementxdmfDisplay.SelectOrientationVectors = 'Displacement'
    displacementxdmfDisplay.ScaleFactor = 0.7499993801116944
    displacementxdmfDisplay.SelectScaleArray = 'Displacement'
    displacementxdmfDisplay.GlyphType = 'Arrow'
    displacementxdmfDisplay.GlyphTableIndexArray = 'Displacement'
    displacementxdmfDisplay.GaussianRadius = 0.037499969005584714
    displacementxdmfDisplay.SetScaleArray = ['POINTS', 'Displacement']
    displacementxdmfDisplay.ScaleTransferFunction = 'Piecewise Function'
    displacementxdmfDisplay.OpacityArray = ['POINTS', 'Displacement']
    displacementxdmfDisplay.OpacityTransferFunction = 'Piecewise Function'
    displacementxdmfDisplay.DataAxesGrid = 'Grid Axes Representation'
    displacementxdmfDisplay.PolarAxes = 'Polar Axes Representation'
    displacementxdmfDisplay.ScalarOpacityUnitDistance = 0.5583539716188769
    displacementxdmfDisplay.OpacityArrayName = ['POINTS', 'Displacement']
    displacementxdmfDisplay.SelectInputVectors = ['POINTS', 'Displacement']
    displacementxdmfDisplay.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    displacementxdmfDisplay.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]

    # init the 'Piecewise Function' selected for 'ScaleTransferFunction'
    displacementxdmfDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

    # init the 'Piecewise Function' selected for 'OpacityTransferFunction'
    displacementxdmfDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.0, 0.0, 6.6921304299024635]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 1.7320508075688772

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    # create a new 'Append Attributes'
    appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=activation_resultsxdmf)

    # set active source
    SetActiveSource(activation_resultsxdmf)

    # destroy appendAttributes1
    Delete(appendAttributes1)
    del appendAttributes1

    # set active source
    SetActiveSource(displacementxdmf)

    # set active source
    SetActiveSource(activation_resultsxdmf)

    # create a new 'Append Attributes'
    appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[displacementxdmf, activation_resultsxdmf])

    # show data in view
    appendAttributes1Display = Show(appendAttributes1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    appendAttributes1Display.Representation = 'Surface'
    appendAttributes1Display.ColorArrayName = [None, '']
    appendAttributes1Display.SelectTCoordArray = 'None'
    appendAttributes1Display.SelectNormalArray = 'None'
    appendAttributes1Display.SelectTangentArray = 'None'
    appendAttributes1Display.OSPRayScaleArray = 'Displacement'
    appendAttributes1Display.OSPRayScaleFunction = 'Piecewise Function'
    appendAttributes1Display.Assembly = ''
    appendAttributes1Display.SelectOrientationVectors = 'Displacement'
    appendAttributes1Display.ScaleFactor = 0.7499993801116944
    appendAttributes1Display.SelectScaleArray = 'Displacement'
    appendAttributes1Display.GlyphType = 'Arrow'
    appendAttributes1Display.GlyphTableIndexArray = 'Displacement'
    appendAttributes1Display.GaussianRadius = 0.037499969005584714
    appendAttributes1Display.SetScaleArray = ['POINTS', 'Displacement']
    appendAttributes1Display.ScaleTransferFunction = 'Piecewise Function'
    appendAttributes1Display.OpacityArray = ['POINTS', 'Displacement']
    appendAttributes1Display.OpacityTransferFunction = 'Piecewise Function'
    appendAttributes1Display.DataAxesGrid = 'Grid Axes Representation'
    appendAttributes1Display.PolarAxes = 'Polar Axes Representation'
    appendAttributes1Display.ScalarOpacityUnitDistance = 0.5583539716188769
    appendAttributes1Display.OpacityArrayName = ['POINTS', 'Displacement']
    appendAttributes1Display.SelectInputVectors = ['POINTS', 'Displacement']
    appendAttributes1Display.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    appendAttributes1Display.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]

    # init the 'Piecewise Function' selected for 'ScaleTransferFunction'
    appendAttributes1Display.ScaleTransferFunction.Points = [-0.28369444608688354, 0.0, 0.5, 0.0, 0.0175445768982172, 1.0, 0.5, 0.0]

    # init the 'Piecewise Function' selected for 'OpacityTransferFunction'
    appendAttributes1Display.OpacityTransferFunction.Points = [-0.28369444608688354, 0.0, 0.5, 0.0, 0.0175445768982172, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(displacementxdmf, renderView1)

    # hide data in view
    Hide(activation_resultsxdmf, renderView1)

    # create a new 'Warp By Vector'
    warpByVector1 = WarpByVector(registrationName='WarpByVector1', Input=appendAttributes1)
    warpByVector1.Vectors = ['POINTS', 'Displacement']

    # show data in view
    warpByVector1Display = Show(warpByVector1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    warpByVector1Display.Representation = 'Surface'
    warpByVector1Display.ColorArrayName = [None, '']
    warpByVector1Display.SelectTCoordArray = 'None'
    warpByVector1Display.SelectNormalArray = 'None'
    warpByVector1Display.SelectTangentArray = 'None'
    warpByVector1Display.OSPRayScaleArray = 'Displacement'
    warpByVector1Display.OSPRayScaleFunction = 'Piecewise Function'
    warpByVector1Display.Assembly = ''
    warpByVector1Display.SelectOrientationVectors = 'Displacement'
    warpByVector1Display.ScaleFactor = 0.8380639553070068
    warpByVector1Display.SelectScaleArray = 'Displacement'
    warpByVector1Display.GlyphType = 'Arrow'
    warpByVector1Display.GlyphTableIndexArray = 'Displacement'
    warpByVector1Display.GaussianRadius = 0.04190319776535034
    warpByVector1Display.SetScaleArray = ['POINTS', 'Displacement']
    warpByVector1Display.ScaleTransferFunction = 'Piecewise Function'
    warpByVector1Display.OpacityArray = ['POINTS', 'Displacement']
    warpByVector1Display.OpacityTransferFunction = 'Piecewise Function'
    warpByVector1Display.DataAxesGrid = 'Grid Axes Representation'
    warpByVector1Display.PolarAxes = 'Polar Axes Representation'
    warpByVector1Display.ScalarOpacityUnitDistance = 0.6092618537762925
    warpByVector1Display.OpacityArrayName = ['POINTS', 'Displacement']
    warpByVector1Display.SelectInputVectors = ['POINTS', 'Displacement']
    warpByVector1Display.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    warpByVector1Display.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]

    # init the 'Piecewise Function' selected for 'ScaleTransferFunction'
    warpByVector1Display.ScaleTransferFunction.Points = [-0.28369444608688354, 0.0, 0.5, 0.0, 0.0175445768982172, 1.0, 0.5, 0.0]

    # init the 'Piecewise Function' selected for 'OpacityTransferFunction'
    warpByVector1Display.OpacityTransferFunction.Points = [-0.28369444608688354, 0.0, 0.5, 0.0, 0.0175445768982172, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(appendAttributes1, renderView1)

    # set scalar coloring
    ColorBy(warpByVector1Display, ('CELLS', 'Activation'))

    # rescale color and/or opacity maps used to exactly fit the current data range
    warpByVector1Display.RescaleTransferFunctionToDataRange(False, True)

    # rescale color and/or opacity maps used to include current data range
    warpByVector1Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    warpByVector1Display.SetScalarBarVisibility(renderView1, True)

    # Rescale transfer function
    activationLUT.RescaleTransferFunction(0.0, 196.83546447753906)

    # Rescale transfer function
    activationPWF.RescaleTransferFunction(0.0, 196.83546447753906)

    renderView1.ResetActiveCameraToNegativeY()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    renderView1.ResetActiveCameraToNegativeZ()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    renderView1.ResetActiveCameraToPositiveX()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    renderView1.ResetActiveCameraToNegativeX()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    # change representation type
    warpByVector1Display.SetRepresentationType('Surface With Edges')
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588

    renderView1.ResetActiveCameraToPositiveX()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-28.296888207446326, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 6.8961357319448755

    renderView1.ResetActiveCameraToNegativeX()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [24.99235663319706, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 6.8961357319448755

    # create a new 'Clip'
    clip1 = Clip(registrationName='Clip1', Input=warpByVector1)
    clip1.ClipType = 'Plane'
    clip1.HyperTreeGridClipper = 'Plane'
    clip1.Scalars = ['CELLS', 'Activation']

    # init the 'Plane' selected for 'ClipType'
    clip1.ClipType.Origin = [-1.6522657871246338, 0.00021028518676757812, -0.0002200603485107422]

    # init the 'Plane' selected for 'HyperTreeGridClipper'
    clip1.HyperTreeGridClipper.Origin = [-1.6522657871246338, 0.00021028518676757812, -0.0002200603485107422]
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [24.99235663319706, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 6.8961357319448755
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [24.99235663319706, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 6.8961357319448755
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [24.99235663319706, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 6.8961357319448755
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [24.99235663319706, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 6.8961357319448755

    # toggle interactive widget visibility (only when running from the GUI)
    HideInteractiveWidgets(proxy=clip1.ClipType)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [24.99235663319706, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 6.8961357319448755

    # Properties modified on clip1
    clip1.Invert = 0

    # Properties modified on clip1.ClipType
    clip1.ClipType.Normal = [0.0, 0.0, 1.0]

    # show data in view
    clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    clip1Display.Representation = 'Surface'
    clip1Display.ColorArrayName = ['CELLS', 'Activation']
    clip1Display.LookupTable = activationLUT
    clip1Display.SelectTCoordArray = 'None'
    clip1Display.SelectNormalArray = 'None'
    clip1Display.SelectTangentArray = 'None'
    clip1Display.OSPRayScaleArray = 'Displacement'
    clip1Display.OSPRayScaleFunction = 'Piecewise Function'
    clip1Display.Assembly = ''
    clip1Display.SelectOrientationVectors = 'Displacement'
    clip1Display.ScaleFactor = 0.8380036354064941
    clip1Display.SelectScaleArray = 'Displacement'
    clip1Display.GlyphType = 'Arrow'
    clip1Display.GlyphTableIndexArray = 'Displacement'
    clip1Display.GaussianRadius = 0.04190018177032471
    clip1Display.SetScaleArray = ['POINTS', 'Displacement']
    clip1Display.ScaleTransferFunction = 'Piecewise Function'
    clip1Display.OpacityArray = ['POINTS', 'Displacement']
    clip1Display.OpacityTransferFunction = 'Piecewise Function'
    clip1Display.DataAxesGrid = 'Grid Axes Representation'
    clip1Display.PolarAxes = 'Polar Axes Representation'
    clip1Display.ScalarOpacityFunction = activationPWF
    clip1Display.ScalarOpacityUnitDistance = 0.5307337713109331
    clip1Display.OpacityArrayName = ['POINTS', 'Displacement']
    clip1Display.SelectInputVectors = ['POINTS', 'Displacement']
    clip1Display.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    clip1Display.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]

    # init the 'Piecewise Function' selected for 'ScaleTransferFunction'
    clip1Display.ScaleTransferFunction.Points = [-0.28357866406440735, 0.0, 0.5, 0.0, 0.0175445768982172, 1.0, 0.5, 0.0]

    # init the 'Piecewise Function' selected for 'OpacityTransferFunction'
    clip1Display.OpacityTransferFunction.Points = [-0.28357866406440735, 0.0, 0.5, 0.0, 0.0175445768982172, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(warpByVector1, renderView1)

    # show color bar/color legend
    clip1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [24.99235663319706, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 6.8961357319448755
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [24.99235663319706, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 6.8961357319448755
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [24.99235663319706, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.00021028518676757812, -0.0002200603485107422]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 6.8961357319448755

    renderView1.ResetActiveCameraToPositiveZ()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraParallelScale = 5.864089973284469
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraParallelScale = 5.864089973284469

    renderView1.AdjustRoll(-90.0)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469

    # get color legend/bar for activationLUT in view renderView1
    activationLUTColorBar = GetScalarBar(activationLUT, renderView1)
    activationLUTColorBar.WindowLocation = 'Any Location'
    activationLUTColorBar.Title = 'Activation'
    activationLUTColorBar.ComponentTitle = ''
    activationLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    activationLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
    activationLUTColorBar.ScalarBarLength = 0.32999999999999996
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469

    # change scalar bar placement
    activationLUTColorBar.Position = [0.6642827514690632, 0.5661215932914047]
    activationLUTColorBar.ScalarBarLength = 0.3300000000000003
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469

    # Rescale transfer function
    activationLUT.RescaleTransferFunction(-0.004698578733950853, 242.50637817382812)

    # Rescale transfer function
    activationPWF.RescaleTransferFunction(-0.004698578733950853, 242.50637817382812)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469

    # change scalar bar placement
    activationLUTColorBar.Position = [0.6604804701002419, 0.5891823899371069]
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469

    # Properties modified on renderView1
    renderView1.OrientationAxesVisibility = 0
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469

    # get layout
    layout1 = GetLayout()

    # layout/tab size in pixels
    layout1.SetSize(2893, 954)

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469

    # save animation
    SaveAnimation(filename=outname, viewOrLayout=renderView1, location=16, ImageResolution=[2892, 952],
        FontScaling='Scale fonts proportionally',
        OverrideColorPalette='',
        StereoMode='No change',
        TransparentBackground=0,
        FrameRate=30,
        FrameStride=1,
        # FrameWindow=[0, 279], 
        # FFMPEG options
        Compression=1,
        Quality='2'
    )
    # Adjust camera
    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469

    #================================================================
    # addendum: following script captures some of the application
    # state to faithfully reproduce the visualization during playback
    #================================================================

    #--------------------------------
    # saving layout sizes for layouts

    # layout/tab size in pixels
    layout1.SetSize(2893, 954)

    #-----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.6522657871246338, 0.0002040863037109375, -20.562163983710374]
    renderView1.CameraFocalPoint = [-1.6522657871246338, 0.0002040863037109375, 2.094939827802591]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.864089973284469



    # destroy clip1
    Delete(clip1)
    del clip1
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 19.763005504233327]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, -1.590216487646103]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.5266205258003795

    # set active source
    SetActiveSource(appendAttributes1)

    # hide data in view
    Hide(warpByVector1, renderView1)

    # show data in view
    appendAttributes1Display = Show(appendAttributes1, renderView1, 'UnstructuredGridRepresentation')

    # destroy warpByVector1
    Delete(warpByVector1)
    del warpByVector1
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 19.763005504233327]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, -1.590216487646103]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.5266205258003795

    # set active source
    SetActiveSource(displacementxdmf)

    # hide data in view
    Hide(appendAttributes1, renderView1)

    # show data in view
    displacementxdmfDisplay = Show(displacementxdmf, renderView1, 'UnstructuredGridRepresentation')

    # destroy appendAttributes1
    Delete(appendAttributes1)
    del appendAttributes1
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 19.763005504233327]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, -1.590216487646103]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.5266205258003795

    # destroy displacementxdmf
    Delete(displacementxdmf)
    del displacementxdmf
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 19.763005504233327]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, -1.590216487646103]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.5266205258003795

    # destroy activation_resultsxdmf
    Delete(activation_resultsxdmf)
    del activation_resultsxdmf
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 19.763005504233327]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, -1.590216487646103]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.5266205258003795

    # update animation scene based on data timesteps
    animationScene1.UpdateAnimationUsingDataTimeSteps()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 19.763005504233327]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, -1.590216487646103]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.5266205258003795

    #================================================================
    # addendum: following script captures some of the application
    # state to faithfully reproduce the visualization during playback
    #================================================================

    #--------------------------------
    # saving layout sizes for layouts

    # layout/tab size in pixels
    layout1.SetSize(2893, 954)

    #-----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 19.763005504233327]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, -1.590216487646103]
    renderView1.CameraViewUp = [1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 5.5266205258003795


    ##--------------------------------------------
    ## You may need to add some code at the end of this python script depending on your usage, eg:
    #
    ## Render all views to see them appears
    # RenderAllViews()
    #
    ## Interact with the view, usefull when running from pvpython
    # Interact()
    #
    ## Save a screenshot of the active view
    # SaveScreenshot("path/to/screenshot.png")
    #
    ## Save a screenshot of a layout (multiple splitted view)
    # SaveScreenshot("path/to/screenshot.png", GetLayout())
    #
    ## Save all "Extractors" from the pipeline browser
    # SaveExtracts()
    #
    ## Save a animation of the current active view
    # SaveAnimation()
    #
    ## Please refer to the documentation of paraview.simple
    ## https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html
    ##--------------------------------------------
  
def save_ani_deformed_activation_cross(fname_act, fname_disp, outname, clip_origin = -1.47839):
    # trace generated using paraview version 5.12.1
    #import paraview
    #paraview.compatibility.major = 5
    #paraview.compatibility.minor = 12

    #### import the simple module from the paraview
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # create a new 'Xdmf3 Reader T'
    activation_resultsxdmf = Xdmf3ReaderT(registrationName='Activation_results.xdmf', FileName=[fname_act])
    activation_resultsxdmf.PointArrays = []
    activation_resultsxdmf.CellArrays = []
    activation_resultsxdmf.Sets = []

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    # Adjust camera

    # get animation scene
    animationScene1 = GetAnimationScene()

    # update animation scene based on data timesteps
    animationScene1.UpdateAnimationUsingDataTimeSteps()

    # create a new 'Xdmf3 Reader T'
    displacementxdmf = Xdmf3ReaderT(registrationName='displacement.xdmf', FileName=[fname_disp])
    displacementxdmf.PointArrays = []
    displacementxdmf.CellArrays = []
    displacementxdmf.Sets = []

    # show data in view
    displacementxdmfDisplay = Show(displacementxdmf, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    displacementxdmfDisplay.Selection = None
    displacementxdmfDisplay.Representation = 'Surface'
    displacementxdmfDisplay.ColorArrayName = [None, '']
    displacementxdmfDisplay.LookupTable = None
    displacementxdmfDisplay.MapScalars = 1
    displacementxdmfDisplay.MultiComponentsMapping = 0
    displacementxdmfDisplay.InterpolateScalarsBeforeMapping = 1
    displacementxdmfDisplay.UseNanColorForMissingArrays = 0
    displacementxdmfDisplay.Opacity = 1.0
    displacementxdmfDisplay.PointSize = 2.0
    displacementxdmfDisplay.LineWidth = 1.0
    displacementxdmfDisplay.RenderLinesAsTubes = 0
    displacementxdmfDisplay.RenderPointsAsSpheres = 0
    displacementxdmfDisplay.Interpolation = 'Gouraud'
    displacementxdmfDisplay.Specular = 0.0
    displacementxdmfDisplay.SpecularColor = [1.0, 1.0, 1.0]
    displacementxdmfDisplay.SpecularPower = 100.0
    displacementxdmfDisplay.Luminosity = 0.0
    displacementxdmfDisplay.Ambient = 0.0
    displacementxdmfDisplay.Diffuse = 1.0
    displacementxdmfDisplay.Roughness = 0.3
    displacementxdmfDisplay.Metallic = 0.0
    displacementxdmfDisplay.EdgeTint = [1.0, 1.0, 1.0]
    displacementxdmfDisplay.Anisotropy = 0.0
    displacementxdmfDisplay.AnisotropyRotation = 0.0
    displacementxdmfDisplay.BaseIOR = 1.5
    displacementxdmfDisplay.CoatStrength = 0.0
    displacementxdmfDisplay.CoatIOR = 2.0
    displacementxdmfDisplay.CoatRoughness = 0.0
    displacementxdmfDisplay.CoatColor = [1.0, 1.0, 1.0]
    displacementxdmfDisplay.SelectTCoordArray = 'None'
    displacementxdmfDisplay.SelectNormalArray = 'None'
    displacementxdmfDisplay.SelectTangentArray = 'None'
    displacementxdmfDisplay.Texture = None
    displacementxdmfDisplay.RepeatTextures = 1
    displacementxdmfDisplay.InterpolateTextures = 0
    displacementxdmfDisplay.SeamlessU = 0
    displacementxdmfDisplay.SeamlessV = 0
    displacementxdmfDisplay.UseMipmapTextures = 0
    displacementxdmfDisplay.ShowTexturesOnBackface = 1
    displacementxdmfDisplay.BaseColorTexture = None
    displacementxdmfDisplay.NormalTexture = None
    displacementxdmfDisplay.NormalScale = 1.0
    displacementxdmfDisplay.CoatNormalTexture = None
    displacementxdmfDisplay.CoatNormalScale = 1.0
    displacementxdmfDisplay.MaterialTexture = None
    displacementxdmfDisplay.OcclusionStrength = 1.0
    displacementxdmfDisplay.AnisotropyTexture = None
    displacementxdmfDisplay.EmissiveTexture = None
    displacementxdmfDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
    displacementxdmfDisplay.FlipTextures = 0
    displacementxdmfDisplay.EdgeOpacity = 1.0
    displacementxdmfDisplay.BackfaceRepresentation = 'Follow Frontface'
    displacementxdmfDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    displacementxdmfDisplay.BackfaceOpacity = 1.0
    displacementxdmfDisplay.Position = [0.0, 0.0, 0.0]
    displacementxdmfDisplay.Scale = [1.0, 1.0, 1.0]
    displacementxdmfDisplay.Orientation = [0.0, 0.0, 0.0]
    displacementxdmfDisplay.Origin = [0.0, 0.0, 0.0]
    displacementxdmfDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    displacementxdmfDisplay.Pickable = 1
    displacementxdmfDisplay.Triangulate = 0
    displacementxdmfDisplay.UseShaderReplacements = 0
    displacementxdmfDisplay.ShaderReplacements = ''
    displacementxdmfDisplay.NonlinearSubdivisionLevel = 1
    displacementxdmfDisplay.MatchBoundariesIgnoringCellOrder = 0
    displacementxdmfDisplay.UseDataPartitions = 0
    displacementxdmfDisplay.OSPRayUseScaleArray = 'All Approximate'
    displacementxdmfDisplay.OSPRayScaleArray = 'Displacement'
    displacementxdmfDisplay.OSPRayScaleFunction = 'Piecewise Function'
    displacementxdmfDisplay.OSPRayMaterial = 'None'
    displacementxdmfDisplay.Assembly = ''
    displacementxdmfDisplay.BlockSelectors = ['/']
    displacementxdmfDisplay.BlockColors = []
    displacementxdmfDisplay.BlockOpacities = []
    displacementxdmfDisplay.Orient = 0
    displacementxdmfDisplay.OrientationMode = 'Direction'
    displacementxdmfDisplay.SelectOrientationVectors = 'Displacement'
    displacementxdmfDisplay.Scaling = 0
    displacementxdmfDisplay.ScaleMode = 'No Data Scaling Off'
    displacementxdmfDisplay.ScaleFactor = 0.7499993801116944
    displacementxdmfDisplay.SelectScaleArray = 'Displacement'
    displacementxdmfDisplay.GlyphType = 'Arrow'
    displacementxdmfDisplay.UseGlyphTable = 0
    displacementxdmfDisplay.GlyphTableIndexArray = 'Displacement'
    displacementxdmfDisplay.UseCompositeGlyphTable = 0
    displacementxdmfDisplay.UseGlyphCullingAndLOD = 0
    displacementxdmfDisplay.LODValues = []
    displacementxdmfDisplay.ColorByLODIndex = 0
    displacementxdmfDisplay.GaussianRadius = 0.037499969005584714
    displacementxdmfDisplay.ShaderPreset = 'Sphere'
    displacementxdmfDisplay.CustomTriangleScale = 3
    displacementxdmfDisplay.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
    float gaussian = exp(-0.5*dist2);
    opacity = opacity*gaussian;
    """
    displacementxdmfDisplay.Emissive = 0
    displacementxdmfDisplay.ScaleByArray = 0
    displacementxdmfDisplay.SetScaleArray = ['POINTS', 'Displacement']
    displacementxdmfDisplay.ScaleArrayComponent = 'X'
    displacementxdmfDisplay.UseScaleFunction = 1
    displacementxdmfDisplay.ScaleTransferFunction = 'Piecewise Function'
    displacementxdmfDisplay.OpacityByArray = 0
    displacementxdmfDisplay.OpacityArray = ['POINTS', 'Displacement']
    displacementxdmfDisplay.OpacityArrayComponent = 'X'
    displacementxdmfDisplay.OpacityTransferFunction = 'Piecewise Function'
    displacementxdmfDisplay.DataAxesGrid = 'Grid Axes Representation'
    displacementxdmfDisplay.SelectionCellLabelBold = 0
    displacementxdmfDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    displacementxdmfDisplay.SelectionCellLabelFontFamily = 'Arial'
    displacementxdmfDisplay.SelectionCellLabelFontFile = ''
    displacementxdmfDisplay.SelectionCellLabelFontSize = 18
    displacementxdmfDisplay.SelectionCellLabelItalic = 0
    displacementxdmfDisplay.SelectionCellLabelJustification = 'Left'
    displacementxdmfDisplay.SelectionCellLabelOpacity = 1.0
    displacementxdmfDisplay.SelectionCellLabelShadow = 0
    displacementxdmfDisplay.SelectionPointLabelBold = 0
    displacementxdmfDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    displacementxdmfDisplay.SelectionPointLabelFontFamily = 'Arial'
    displacementxdmfDisplay.SelectionPointLabelFontFile = ''
    displacementxdmfDisplay.SelectionPointLabelFontSize = 18
    displacementxdmfDisplay.SelectionPointLabelItalic = 0
    displacementxdmfDisplay.SelectionPointLabelJustification = 'Left'
    displacementxdmfDisplay.SelectionPointLabelOpacity = 1.0
    displacementxdmfDisplay.SelectionPointLabelShadow = 0
    displacementxdmfDisplay.PolarAxes = 'Polar Axes Representation'
    displacementxdmfDisplay.ScalarOpacityFunction = None
    displacementxdmfDisplay.ScalarOpacityUnitDistance = 0.5583539716188769
    displacementxdmfDisplay.UseSeparateOpacityArray = 0
    displacementxdmfDisplay.OpacityArrayName = ['POINTS', 'Displacement']
    displacementxdmfDisplay.OpacityComponent = 'X'
    displacementxdmfDisplay.SelectMapper = 'Projected tetra'
    displacementxdmfDisplay.SamplingDimensions = [128, 128, 128]
    displacementxdmfDisplay.UseFloatingPointFrameBuffer = 1
    displacementxdmfDisplay.SelectInputVectors = ['POINTS', 'Displacement']
    displacementxdmfDisplay.NumberOfSteps = 40
    displacementxdmfDisplay.StepSize = 0.25
    displacementxdmfDisplay.NormalizeVectors = 1
    displacementxdmfDisplay.EnhancedLIC = 1
    displacementxdmfDisplay.ColorMode = 'Blend'
    displacementxdmfDisplay.LICIntensity = 0.8
    displacementxdmfDisplay.MapModeBias = 0.0
    displacementxdmfDisplay.EnhanceContrast = 'Off'
    displacementxdmfDisplay.LowLICContrastEnhancementFactor = 0.0
    displacementxdmfDisplay.HighLICContrastEnhancementFactor = 0.0
    displacementxdmfDisplay.LowColorContrastEnhancementFactor = 0.0
    displacementxdmfDisplay.HighColorContrastEnhancementFactor = 0.0
    displacementxdmfDisplay.AntiAlias = 0
    displacementxdmfDisplay.MaskOnSurface = 1
    displacementxdmfDisplay.MaskThreshold = 0.0
    displacementxdmfDisplay.MaskIntensity = 0.0
    displacementxdmfDisplay.MaskColor = [0.5, 0.5, 0.5]
    displacementxdmfDisplay.GenerateNoiseTexture = 0
    displacementxdmfDisplay.NoiseType = 'Gaussian'
    displacementxdmfDisplay.NoiseTextureSize = 128
    displacementxdmfDisplay.NoiseGrainSize = 2
    displacementxdmfDisplay.MinNoiseValue = 0.0
    displacementxdmfDisplay.MaxNoiseValue = 0.8
    displacementxdmfDisplay.NumberOfNoiseLevels = 1024
    displacementxdmfDisplay.ImpulseNoiseProbability = 1.0
    displacementxdmfDisplay.ImpulseNoiseBackgroundValue = 0.0
    displacementxdmfDisplay.NoiseGeneratorSeed = 1
    displacementxdmfDisplay.CompositeStrategy = 'AUTO'
    displacementxdmfDisplay.UseLICForLOD = 0
    displacementxdmfDisplay.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    displacementxdmfDisplay.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]
    displacementxdmfDisplay.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    displacementxdmfDisplay.GlyphType.TipResolution = 6
    displacementxdmfDisplay.GlyphType.TipRadius = 0.1
    displacementxdmfDisplay.GlyphType.TipLength = 0.35
    displacementxdmfDisplay.GlyphType.ShaftResolution = 6
    displacementxdmfDisplay.GlyphType.ShaftRadius = 0.03
    displacementxdmfDisplay.GlyphType.Invert = 0

    # init the 'Piecewise Function' selected for 'ScaleTransferFunction'
    displacementxdmfDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    displacementxdmfDisplay.ScaleTransferFunction.UseLogScale = 0

    # init the 'Piecewise Function' selected for 'OpacityTransferFunction'
    displacementxdmfDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    displacementxdmfDisplay.OpacityTransferFunction.UseLogScale = 0

    # init the 'Grid Axes Representation' selected for 'DataAxesGrid'
    displacementxdmfDisplay.DataAxesGrid.XTitle = 'X Axis'
    displacementxdmfDisplay.DataAxesGrid.YTitle = 'Y Axis'
    displacementxdmfDisplay.DataAxesGrid.ZTitle = 'Z Axis'
    displacementxdmfDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
    displacementxdmfDisplay.DataAxesGrid.XTitleFontFile = ''
    displacementxdmfDisplay.DataAxesGrid.XTitleBold = 0
    displacementxdmfDisplay.DataAxesGrid.XTitleItalic = 0
    displacementxdmfDisplay.DataAxesGrid.XTitleFontSize = 12
    displacementxdmfDisplay.DataAxesGrid.XTitleShadow = 0
    displacementxdmfDisplay.DataAxesGrid.XTitleOpacity = 1.0
    displacementxdmfDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
    displacementxdmfDisplay.DataAxesGrid.YTitleFontFile = ''
    displacementxdmfDisplay.DataAxesGrid.YTitleBold = 0
    displacementxdmfDisplay.DataAxesGrid.YTitleItalic = 0
    displacementxdmfDisplay.DataAxesGrid.YTitleFontSize = 12
    displacementxdmfDisplay.DataAxesGrid.YTitleShadow = 0
    displacementxdmfDisplay.DataAxesGrid.YTitleOpacity = 1.0
    displacementxdmfDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
    displacementxdmfDisplay.DataAxesGrid.ZTitleFontFile = ''
    displacementxdmfDisplay.DataAxesGrid.ZTitleBold = 0
    displacementxdmfDisplay.DataAxesGrid.ZTitleItalic = 0
    displacementxdmfDisplay.DataAxesGrid.ZTitleFontSize = 12
    displacementxdmfDisplay.DataAxesGrid.ZTitleShadow = 0
    displacementxdmfDisplay.DataAxesGrid.ZTitleOpacity = 1.0
    displacementxdmfDisplay.DataAxesGrid.FacesToRender = 63
    displacementxdmfDisplay.DataAxesGrid.CullBackface = 0
    displacementxdmfDisplay.DataAxesGrid.CullFrontface = 1
    displacementxdmfDisplay.DataAxesGrid.ShowGrid = 0
    displacementxdmfDisplay.DataAxesGrid.ShowEdges = 1
    displacementxdmfDisplay.DataAxesGrid.ShowTicks = 1
    displacementxdmfDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
    displacementxdmfDisplay.DataAxesGrid.AxesToLabel = 63
    displacementxdmfDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
    displacementxdmfDisplay.DataAxesGrid.XLabelFontFile = ''
    displacementxdmfDisplay.DataAxesGrid.XLabelBold = 0
    displacementxdmfDisplay.DataAxesGrid.XLabelItalic = 0
    displacementxdmfDisplay.DataAxesGrid.XLabelFontSize = 12
    displacementxdmfDisplay.DataAxesGrid.XLabelShadow = 0
    displacementxdmfDisplay.DataAxesGrid.XLabelOpacity = 1.0
    displacementxdmfDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
    displacementxdmfDisplay.DataAxesGrid.YLabelFontFile = ''
    displacementxdmfDisplay.DataAxesGrid.YLabelBold = 0
    displacementxdmfDisplay.DataAxesGrid.YLabelItalic = 0
    displacementxdmfDisplay.DataAxesGrid.YLabelFontSize = 12
    displacementxdmfDisplay.DataAxesGrid.YLabelShadow = 0
    displacementxdmfDisplay.DataAxesGrid.YLabelOpacity = 1.0
    displacementxdmfDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
    displacementxdmfDisplay.DataAxesGrid.ZLabelFontFile = ''
    displacementxdmfDisplay.DataAxesGrid.ZLabelBold = 0
    displacementxdmfDisplay.DataAxesGrid.ZLabelItalic = 0
    displacementxdmfDisplay.DataAxesGrid.ZLabelFontSize = 12
    displacementxdmfDisplay.DataAxesGrid.ZLabelShadow = 0
    displacementxdmfDisplay.DataAxesGrid.ZLabelOpacity = 1.0
    displacementxdmfDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
    displacementxdmfDisplay.DataAxesGrid.XAxisPrecision = 2
    displacementxdmfDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
    displacementxdmfDisplay.DataAxesGrid.XAxisLabels = []
    displacementxdmfDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
    displacementxdmfDisplay.DataAxesGrid.YAxisPrecision = 2
    displacementxdmfDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
    displacementxdmfDisplay.DataAxesGrid.YAxisLabels = []
    displacementxdmfDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
    displacementxdmfDisplay.DataAxesGrid.ZAxisPrecision = 2
    displacementxdmfDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
    displacementxdmfDisplay.DataAxesGrid.ZAxisLabels = []
    displacementxdmfDisplay.DataAxesGrid.UseCustomBounds = 0
    displacementxdmfDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'Polar Axes Representation' selected for 'PolarAxes'
    displacementxdmfDisplay.PolarAxes.Visibility = 0
    displacementxdmfDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
    displacementxdmfDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
    displacementxdmfDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    displacementxdmfDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
    displacementxdmfDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    displacementxdmfDisplay.PolarAxes.EnableCustomRange = 0
    displacementxdmfDisplay.PolarAxes.CustomRange = [0.0, 1.0]
    displacementxdmfDisplay.PolarAxes.AutoPole = 1
    displacementxdmfDisplay.PolarAxes.PolarAxisVisibility = 1
    displacementxdmfDisplay.PolarAxes.RadialAxesVisibility = 1
    displacementxdmfDisplay.PolarAxes.DrawRadialGridlines = 1
    displacementxdmfDisplay.PolarAxes.PolarArcsVisibility = 1
    displacementxdmfDisplay.PolarAxes.DrawPolarArcsGridlines = 1
    displacementxdmfDisplay.PolarAxes.NumberOfRadialAxes = 0
    displacementxdmfDisplay.PolarAxes.DeltaAngleRadialAxes = 45.0
    displacementxdmfDisplay.PolarAxes.NumberOfPolarAxes = 5
    displacementxdmfDisplay.PolarAxes.DeltaRangePolarAxes = 0.0
    displacementxdmfDisplay.PolarAxes.CustomMinRadius = 1
    displacementxdmfDisplay.PolarAxes.MinimumRadius = 0.0
    displacementxdmfDisplay.PolarAxes.CustomAngles = 1
    displacementxdmfDisplay.PolarAxes.MinimumAngle = 0.0
    displacementxdmfDisplay.PolarAxes.MaximumAngle = 90.0
    displacementxdmfDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
    displacementxdmfDisplay.PolarAxes.PolarArcResolutionPerDegree = 0.2
    displacementxdmfDisplay.PolarAxes.Ratio = 1.0
    displacementxdmfDisplay.PolarAxes.EnableOverallColor = 1
    displacementxdmfDisplay.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
    displacementxdmfDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    displacementxdmfDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    displacementxdmfDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    displacementxdmfDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    displacementxdmfDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    displacementxdmfDisplay.PolarAxes.PolarAxisTitleVisibility = 1
    displacementxdmfDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
    displacementxdmfDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    displacementxdmfDisplay.PolarAxes.PolarTitleOffset = [20.0, 20.0]
    displacementxdmfDisplay.PolarAxes.PolarLabelVisibility = 1
    displacementxdmfDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
    displacementxdmfDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
    displacementxdmfDisplay.PolarAxes.PolarLabelOffset = 10.0
    displacementxdmfDisplay.PolarAxes.PolarExponentOffset = 5.0
    displacementxdmfDisplay.PolarAxes.RadialTitleVisibility = 1
    displacementxdmfDisplay.PolarAxes.RadialTitleFormat = '%-#3.1f'
    displacementxdmfDisplay.PolarAxes.RadialTitleLocation = 'Bottom'
    displacementxdmfDisplay.PolarAxes.RadialTitleOffset = [20.0, 0.0]
    displacementxdmfDisplay.PolarAxes.RadialUnitsVisibility = 1
    displacementxdmfDisplay.PolarAxes.ScreenSize = 10.0
    displacementxdmfDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
    displacementxdmfDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    displacementxdmfDisplay.PolarAxes.PolarAxisTitleFontFile = ''
    displacementxdmfDisplay.PolarAxes.PolarAxisTitleBold = 0
    displacementxdmfDisplay.PolarAxes.PolarAxisTitleItalic = 0
    displacementxdmfDisplay.PolarAxes.PolarAxisTitleShadow = 0
    displacementxdmfDisplay.PolarAxes.PolarAxisTitleFontSize = 12
    displacementxdmfDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
    displacementxdmfDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    displacementxdmfDisplay.PolarAxes.PolarAxisLabelFontFile = ''
    displacementxdmfDisplay.PolarAxes.PolarAxisLabelBold = 0
    displacementxdmfDisplay.PolarAxes.PolarAxisLabelItalic = 0
    displacementxdmfDisplay.PolarAxes.PolarAxisLabelShadow = 0
    displacementxdmfDisplay.PolarAxes.PolarAxisLabelFontSize = 12
    displacementxdmfDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
    displacementxdmfDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    displacementxdmfDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
    displacementxdmfDisplay.PolarAxes.LastRadialAxisTextBold = 0
    displacementxdmfDisplay.PolarAxes.LastRadialAxisTextItalic = 0
    displacementxdmfDisplay.PolarAxes.LastRadialAxisTextShadow = 0
    displacementxdmfDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
    displacementxdmfDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    displacementxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    displacementxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    displacementxdmfDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
    displacementxdmfDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
    displacementxdmfDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
    displacementxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    displacementxdmfDisplay.PolarAxes.EnableDistanceLOD = 1
    displacementxdmfDisplay.PolarAxes.DistanceLODThreshold = 0.7
    displacementxdmfDisplay.PolarAxes.EnableViewAngleLOD = 1
    displacementxdmfDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
    displacementxdmfDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
    displacementxdmfDisplay.PolarAxes.PolarTicksVisibility = 1
    displacementxdmfDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
    displacementxdmfDisplay.PolarAxes.TickLocation = 'Both'
    displacementxdmfDisplay.PolarAxes.AxisTickVisibility = 1
    displacementxdmfDisplay.PolarAxes.AxisMinorTickVisibility = 0
    displacementxdmfDisplay.PolarAxes.AxisTickMatchesPolarAxes = 1
    displacementxdmfDisplay.PolarAxes.DeltaRangeMajor = 1.0
    displacementxdmfDisplay.PolarAxes.DeltaRangeMinor = 0.5
    displacementxdmfDisplay.PolarAxes.ArcTickVisibility = 1
    displacementxdmfDisplay.PolarAxes.ArcMinorTickVisibility = 0
    displacementxdmfDisplay.PolarAxes.ArcTickMatchesRadialAxes = 1
    displacementxdmfDisplay.PolarAxes.DeltaAngleMajor = 10.0
    displacementxdmfDisplay.PolarAxes.DeltaAngleMinor = 5.0
    displacementxdmfDisplay.PolarAxes.TickRatioRadiusSize = 0.02
    displacementxdmfDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
    displacementxdmfDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
    displacementxdmfDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
    displacementxdmfDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
    displacementxdmfDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    displacementxdmfDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    displacementxdmfDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    displacementxdmfDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    displacementxdmfDisplay.PolarAxes.ArcMajorTickSize = 0.0
    displacementxdmfDisplay.PolarAxes.ArcTickRatioSize = 0.3
    displacementxdmfDisplay.PolarAxes.ArcMajorTickThickness = 1.0
    displacementxdmfDisplay.PolarAxes.ArcTickRatioThickness = 0.5
    displacementxdmfDisplay.PolarAxes.Use2DMode = 0
    displacementxdmfDisplay.PolarAxes.UseLogAxis = 0

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # show data in view
    activation_resultsxdmfDisplay = Show(activation_resultsxdmf, renderView1, 'UnstructuredGridRepresentation')

    # get 2D transfer function for 'Activation'
    activationTF2D = GetTransferFunction2D('Activation')
    activationTF2D.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
    activationTF2D.Boxes = []
    activationTF2D.ScalarRangeInitialized = 0
    activationTF2D.Range = [0.0, 1.0, 0.0, 1.0]
    activationTF2D.OutputDimensions = [10, 10]

    # get color transfer function/color map for 'Activation'
    activationLUT = GetColorTransferFunction('Activation')
    activationLUT.InterpretValuesAsCategories = 0
    activationLUT.AnnotationsInitialized = 0
    activationLUT.ShowCategoricalColorsinDataRangeOnly = 0
    activationLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
    activationLUT.RescaleOnVisibilityChange = 0
    activationLUT.TransferFunction2D = activationTF2D
    activationLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 5.878906683738906e-39, 0.865003, 0.865003, 0.865003, 1.1757813367477812e-38, 0.705882, 0.0156863, 0.14902]
    activationLUT.UseLogScale = 0
    activationLUT.UseOpacityControlPointsFreehandDrawing = 0
    activationLUT.ShowDataHistogram = 0
    activationLUT.AutomaticDataHistogramComputation = 0
    activationLUT.DataHistogramNumberOfBins = 10
    activationLUT.ColorSpace = 'Diverging'
    activationLUT.UseBelowRangeColor = 0
    activationLUT.BelowRangeColor = [0.0, 0.0, 0.0]
    activationLUT.UseAboveRangeColor = 0
    activationLUT.AboveRangeColor = [0.5, 0.5, 0.5]
    activationLUT.NanColor = [1.0, 1.0, 0.0]
    activationLUT.NanOpacity = 1.0
    activationLUT.Discretize = 1
    activationLUT.NumberOfTableValues = 256
    activationLUT.ScalarRangeInitialized = 1.0
    activationLUT.HSVWrap = 0
    activationLUT.VectorComponent = 0
    activationLUT.VectorMode = 'Magnitude'
    activationLUT.AllowDuplicateScalars = 1
    activationLUT.Annotations = []
    activationLUT.ActiveAnnotatedValues = []
    activationLUT.IndexedColors = []
    activationLUT.IndexedOpacities = []
    activationLUT.EnableOpacityMapping = 0

    # get opacity transfer function/opacity map for 'Activation'
    activationPWF = GetOpacityTransferFunction('Activation')
    activationPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    activationPWF.AllowDuplicateScalars = 1
    activationPWF.UseLogScale = 0
    activationPWF.ScalarRangeInitialized = 1

    # trace defaults for the display properties.
    activation_resultsxdmfDisplay.Selection = None
    activation_resultsxdmfDisplay.Representation = 'Surface'
    activation_resultsxdmfDisplay.ColorArrayName = ['CELLS', 'Activation']
    activation_resultsxdmfDisplay.LookupTable = activationLUT
    activation_resultsxdmfDisplay.MapScalars = 1
    activation_resultsxdmfDisplay.MultiComponentsMapping = 0
    activation_resultsxdmfDisplay.InterpolateScalarsBeforeMapping = 1
    activation_resultsxdmfDisplay.UseNanColorForMissingArrays = 0
    activation_resultsxdmfDisplay.Opacity = 1.0
    activation_resultsxdmfDisplay.PointSize = 2.0
    activation_resultsxdmfDisplay.LineWidth = 1.0
    activation_resultsxdmfDisplay.RenderLinesAsTubes = 0
    activation_resultsxdmfDisplay.RenderPointsAsSpheres = 0
    activation_resultsxdmfDisplay.Interpolation = 'Gouraud'
    activation_resultsxdmfDisplay.Specular = 0.0
    activation_resultsxdmfDisplay.SpecularColor = [1.0, 1.0, 1.0]
    activation_resultsxdmfDisplay.SpecularPower = 100.0
    activation_resultsxdmfDisplay.Luminosity = 0.0
    activation_resultsxdmfDisplay.Ambient = 0.0
    activation_resultsxdmfDisplay.Diffuse = 1.0
    activation_resultsxdmfDisplay.Roughness = 0.3
    activation_resultsxdmfDisplay.Metallic = 0.0
    activation_resultsxdmfDisplay.EdgeTint = [1.0, 1.0, 1.0]
    activation_resultsxdmfDisplay.Anisotropy = 0.0
    activation_resultsxdmfDisplay.AnisotropyRotation = 0.0
    activation_resultsxdmfDisplay.BaseIOR = 1.5
    activation_resultsxdmfDisplay.CoatStrength = 0.0
    activation_resultsxdmfDisplay.CoatIOR = 2.0
    activation_resultsxdmfDisplay.CoatRoughness = 0.0
    activation_resultsxdmfDisplay.CoatColor = [1.0, 1.0, 1.0]
    activation_resultsxdmfDisplay.SelectTCoordArray = 'None'
    activation_resultsxdmfDisplay.SelectNormalArray = 'None'
    activation_resultsxdmfDisplay.SelectTangentArray = 'None'
    activation_resultsxdmfDisplay.Texture = None
    activation_resultsxdmfDisplay.RepeatTextures = 1
    activation_resultsxdmfDisplay.InterpolateTextures = 0
    activation_resultsxdmfDisplay.SeamlessU = 0
    activation_resultsxdmfDisplay.SeamlessV = 0
    activation_resultsxdmfDisplay.UseMipmapTextures = 0
    activation_resultsxdmfDisplay.ShowTexturesOnBackface = 1
    activation_resultsxdmfDisplay.BaseColorTexture = None
    activation_resultsxdmfDisplay.NormalTexture = None
    activation_resultsxdmfDisplay.NormalScale = 1.0
    activation_resultsxdmfDisplay.CoatNormalTexture = None
    activation_resultsxdmfDisplay.CoatNormalScale = 1.0
    activation_resultsxdmfDisplay.MaterialTexture = None
    activation_resultsxdmfDisplay.OcclusionStrength = 1.0
    activation_resultsxdmfDisplay.AnisotropyTexture = None
    activation_resultsxdmfDisplay.EmissiveTexture = None
    activation_resultsxdmfDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
    activation_resultsxdmfDisplay.FlipTextures = 0
    activation_resultsxdmfDisplay.EdgeOpacity = 1.0
    activation_resultsxdmfDisplay.BackfaceRepresentation = 'Follow Frontface'
    activation_resultsxdmfDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    activation_resultsxdmfDisplay.BackfaceOpacity = 1.0
    activation_resultsxdmfDisplay.Position = [0.0, 0.0, 0.0]
    activation_resultsxdmfDisplay.Scale = [1.0, 1.0, 1.0]
    activation_resultsxdmfDisplay.Orientation = [0.0, 0.0, 0.0]
    activation_resultsxdmfDisplay.Origin = [0.0, 0.0, 0.0]
    activation_resultsxdmfDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    activation_resultsxdmfDisplay.Pickable = 1
    activation_resultsxdmfDisplay.Triangulate = 0
    activation_resultsxdmfDisplay.UseShaderReplacements = 0
    activation_resultsxdmfDisplay.ShaderReplacements = ''
    activation_resultsxdmfDisplay.NonlinearSubdivisionLevel = 1
    activation_resultsxdmfDisplay.MatchBoundariesIgnoringCellOrder = 0
    activation_resultsxdmfDisplay.UseDataPartitions = 0
    activation_resultsxdmfDisplay.OSPRayUseScaleArray = 'All Approximate'
    activation_resultsxdmfDisplay.OSPRayScaleArray = ''
    activation_resultsxdmfDisplay.OSPRayScaleFunction = 'Piecewise Function'
    activation_resultsxdmfDisplay.OSPRayMaterial = 'None'
    activation_resultsxdmfDisplay.Assembly = ''
    activation_resultsxdmfDisplay.BlockSelectors = ['/']
    activation_resultsxdmfDisplay.BlockColors = []
    activation_resultsxdmfDisplay.BlockOpacities = []
    activation_resultsxdmfDisplay.Orient = 0
    activation_resultsxdmfDisplay.OrientationMode = 'Direction'
    activation_resultsxdmfDisplay.SelectOrientationVectors = 'None'
    activation_resultsxdmfDisplay.Scaling = 0
    activation_resultsxdmfDisplay.ScaleMode = 'No Data Scaling Off'
    activation_resultsxdmfDisplay.ScaleFactor = 0.7499993801116944
    activation_resultsxdmfDisplay.SelectScaleArray = 'Activation'
    activation_resultsxdmfDisplay.GlyphType = 'Arrow'
    activation_resultsxdmfDisplay.UseGlyphTable = 0
    activation_resultsxdmfDisplay.GlyphTableIndexArray = 'Activation'
    activation_resultsxdmfDisplay.UseCompositeGlyphTable = 0
    activation_resultsxdmfDisplay.UseGlyphCullingAndLOD = 0
    activation_resultsxdmfDisplay.LODValues = []
    activation_resultsxdmfDisplay.ColorByLODIndex = 0
    activation_resultsxdmfDisplay.GaussianRadius = 0.037499969005584714
    activation_resultsxdmfDisplay.ShaderPreset = 'Sphere'
    activation_resultsxdmfDisplay.CustomTriangleScale = 3
    activation_resultsxdmfDisplay.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
    float gaussian = exp(-0.5*dist2);
    opacity = opacity*gaussian;
    """
    activation_resultsxdmfDisplay.Emissive = 0
    activation_resultsxdmfDisplay.ScaleByArray = 0
    activation_resultsxdmfDisplay.SetScaleArray = [None, '']
    activation_resultsxdmfDisplay.ScaleArrayComponent = 0
    activation_resultsxdmfDisplay.UseScaleFunction = 1
    activation_resultsxdmfDisplay.ScaleTransferFunction = 'Piecewise Function'
    activation_resultsxdmfDisplay.OpacityByArray = 0
    activation_resultsxdmfDisplay.OpacityArray = [None, '']
    activation_resultsxdmfDisplay.OpacityArrayComponent = 0
    activation_resultsxdmfDisplay.OpacityTransferFunction = 'Piecewise Function'
    activation_resultsxdmfDisplay.DataAxesGrid = 'Grid Axes Representation'
    activation_resultsxdmfDisplay.SelectionCellLabelBold = 0
    activation_resultsxdmfDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    activation_resultsxdmfDisplay.SelectionCellLabelFontFamily = 'Arial'
    activation_resultsxdmfDisplay.SelectionCellLabelFontFile = ''
    activation_resultsxdmfDisplay.SelectionCellLabelFontSize = 18
    activation_resultsxdmfDisplay.SelectionCellLabelItalic = 0
    activation_resultsxdmfDisplay.SelectionCellLabelJustification = 'Left'
    activation_resultsxdmfDisplay.SelectionCellLabelOpacity = 1.0
    activation_resultsxdmfDisplay.SelectionCellLabelShadow = 0
    activation_resultsxdmfDisplay.SelectionPointLabelBold = 0
    activation_resultsxdmfDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    activation_resultsxdmfDisplay.SelectionPointLabelFontFamily = 'Arial'
    activation_resultsxdmfDisplay.SelectionPointLabelFontFile = ''
    activation_resultsxdmfDisplay.SelectionPointLabelFontSize = 18
    activation_resultsxdmfDisplay.SelectionPointLabelItalic = 0
    activation_resultsxdmfDisplay.SelectionPointLabelJustification = 'Left'
    activation_resultsxdmfDisplay.SelectionPointLabelOpacity = 1.0
    activation_resultsxdmfDisplay.SelectionPointLabelShadow = 0
    activation_resultsxdmfDisplay.PolarAxes = 'Polar Axes Representation'
    activation_resultsxdmfDisplay.ScalarOpacityFunction = activationPWF
    activation_resultsxdmfDisplay.ScalarOpacityUnitDistance = 0.5583539716188769
    activation_resultsxdmfDisplay.UseSeparateOpacityArray = 0
    activation_resultsxdmfDisplay.OpacityArrayName = ['CELLS', 'Activation']
    activation_resultsxdmfDisplay.OpacityComponent = ''
    activation_resultsxdmfDisplay.SelectMapper = 'Projected tetra'
    activation_resultsxdmfDisplay.SamplingDimensions = [128, 128, 128]
    activation_resultsxdmfDisplay.UseFloatingPointFrameBuffer = 1
    activation_resultsxdmfDisplay.SelectInputVectors = [None, '']
    activation_resultsxdmfDisplay.NumberOfSteps = 40
    activation_resultsxdmfDisplay.StepSize = 0.25
    activation_resultsxdmfDisplay.NormalizeVectors = 1
    activation_resultsxdmfDisplay.EnhancedLIC = 1
    activation_resultsxdmfDisplay.ColorMode = 'Blend'
    activation_resultsxdmfDisplay.LICIntensity = 0.8
    activation_resultsxdmfDisplay.MapModeBias = 0.0
    activation_resultsxdmfDisplay.EnhanceContrast = 'Off'
    activation_resultsxdmfDisplay.LowLICContrastEnhancementFactor = 0.0
    activation_resultsxdmfDisplay.HighLICContrastEnhancementFactor = 0.0
    activation_resultsxdmfDisplay.LowColorContrastEnhancementFactor = 0.0
    activation_resultsxdmfDisplay.HighColorContrastEnhancementFactor = 0.0
    activation_resultsxdmfDisplay.AntiAlias = 0
    activation_resultsxdmfDisplay.MaskOnSurface = 1
    activation_resultsxdmfDisplay.MaskThreshold = 0.0
    activation_resultsxdmfDisplay.MaskIntensity = 0.0
    activation_resultsxdmfDisplay.MaskColor = [0.5, 0.5, 0.5]
    activation_resultsxdmfDisplay.GenerateNoiseTexture = 0
    activation_resultsxdmfDisplay.NoiseType = 'Gaussian'
    activation_resultsxdmfDisplay.NoiseTextureSize = 128
    activation_resultsxdmfDisplay.NoiseGrainSize = 2
    activation_resultsxdmfDisplay.MinNoiseValue = 0.0
    activation_resultsxdmfDisplay.MaxNoiseValue = 0.8
    activation_resultsxdmfDisplay.NumberOfNoiseLevels = 1024
    activation_resultsxdmfDisplay.ImpulseNoiseProbability = 1.0
    activation_resultsxdmfDisplay.ImpulseNoiseBackgroundValue = 0.0
    activation_resultsxdmfDisplay.NoiseGeneratorSeed = 1
    activation_resultsxdmfDisplay.CompositeStrategy = 'AUTO'
    activation_resultsxdmfDisplay.UseLICForLOD = 0
    activation_resultsxdmfDisplay.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    activation_resultsxdmfDisplay.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]
    activation_resultsxdmfDisplay.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    activation_resultsxdmfDisplay.GlyphType.TipResolution = 6
    activation_resultsxdmfDisplay.GlyphType.TipRadius = 0.1
    activation_resultsxdmfDisplay.GlyphType.TipLength = 0.35
    activation_resultsxdmfDisplay.GlyphType.ShaftResolution = 6
    activation_resultsxdmfDisplay.GlyphType.ShaftRadius = 0.03
    activation_resultsxdmfDisplay.GlyphType.Invert = 0

    # init the 'Piecewise Function' selected for 'ScaleTransferFunction'
    activation_resultsxdmfDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
    activation_resultsxdmfDisplay.ScaleTransferFunction.UseLogScale = 0

    # init the 'Piecewise Function' selected for 'OpacityTransferFunction'
    activation_resultsxdmfDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
    activation_resultsxdmfDisplay.OpacityTransferFunction.UseLogScale = 0

    # init the 'Grid Axes Representation' selected for 'DataAxesGrid'
    activation_resultsxdmfDisplay.DataAxesGrid.XTitle = 'X Axis'
    activation_resultsxdmfDisplay.DataAxesGrid.YTitle = 'Y Axis'
    activation_resultsxdmfDisplay.DataAxesGrid.ZTitle = 'Z Axis'
    activation_resultsxdmfDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
    activation_resultsxdmfDisplay.DataAxesGrid.XTitleFontFile = ''
    activation_resultsxdmfDisplay.DataAxesGrid.XTitleBold = 0
    activation_resultsxdmfDisplay.DataAxesGrid.XTitleItalic = 0
    activation_resultsxdmfDisplay.DataAxesGrid.XTitleFontSize = 12
    activation_resultsxdmfDisplay.DataAxesGrid.XTitleShadow = 0
    activation_resultsxdmfDisplay.DataAxesGrid.XTitleOpacity = 1.0
    activation_resultsxdmfDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
    activation_resultsxdmfDisplay.DataAxesGrid.YTitleFontFile = ''
    activation_resultsxdmfDisplay.DataAxesGrid.YTitleBold = 0
    activation_resultsxdmfDisplay.DataAxesGrid.YTitleItalic = 0
    activation_resultsxdmfDisplay.DataAxesGrid.YTitleFontSize = 12
    activation_resultsxdmfDisplay.DataAxesGrid.YTitleShadow = 0
    activation_resultsxdmfDisplay.DataAxesGrid.YTitleOpacity = 1.0
    activation_resultsxdmfDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
    activation_resultsxdmfDisplay.DataAxesGrid.ZTitleFontFile = ''
    activation_resultsxdmfDisplay.DataAxesGrid.ZTitleBold = 0
    activation_resultsxdmfDisplay.DataAxesGrid.ZTitleItalic = 0
    activation_resultsxdmfDisplay.DataAxesGrid.ZTitleFontSize = 12
    activation_resultsxdmfDisplay.DataAxesGrid.ZTitleShadow = 0
    activation_resultsxdmfDisplay.DataAxesGrid.ZTitleOpacity = 1.0
    activation_resultsxdmfDisplay.DataAxesGrid.FacesToRender = 63
    activation_resultsxdmfDisplay.DataAxesGrid.CullBackface = 0
    activation_resultsxdmfDisplay.DataAxesGrid.CullFrontface = 1
    activation_resultsxdmfDisplay.DataAxesGrid.ShowGrid = 0
    activation_resultsxdmfDisplay.DataAxesGrid.ShowEdges = 1
    activation_resultsxdmfDisplay.DataAxesGrid.ShowTicks = 1
    activation_resultsxdmfDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
    activation_resultsxdmfDisplay.DataAxesGrid.AxesToLabel = 63
    activation_resultsxdmfDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
    activation_resultsxdmfDisplay.DataAxesGrid.XLabelFontFile = ''
    activation_resultsxdmfDisplay.DataAxesGrid.XLabelBold = 0
    activation_resultsxdmfDisplay.DataAxesGrid.XLabelItalic = 0
    activation_resultsxdmfDisplay.DataAxesGrid.XLabelFontSize = 12
    activation_resultsxdmfDisplay.DataAxesGrid.XLabelShadow = 0
    activation_resultsxdmfDisplay.DataAxesGrid.XLabelOpacity = 1.0
    activation_resultsxdmfDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
    activation_resultsxdmfDisplay.DataAxesGrid.YLabelFontFile = ''
    activation_resultsxdmfDisplay.DataAxesGrid.YLabelBold = 0
    activation_resultsxdmfDisplay.DataAxesGrid.YLabelItalic = 0
    activation_resultsxdmfDisplay.DataAxesGrid.YLabelFontSize = 12
    activation_resultsxdmfDisplay.DataAxesGrid.YLabelShadow = 0
    activation_resultsxdmfDisplay.DataAxesGrid.YLabelOpacity = 1.0
    activation_resultsxdmfDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
    activation_resultsxdmfDisplay.DataAxesGrid.ZLabelFontFile = ''
    activation_resultsxdmfDisplay.DataAxesGrid.ZLabelBold = 0
    activation_resultsxdmfDisplay.DataAxesGrid.ZLabelItalic = 0
    activation_resultsxdmfDisplay.DataAxesGrid.ZLabelFontSize = 12
    activation_resultsxdmfDisplay.DataAxesGrid.ZLabelShadow = 0
    activation_resultsxdmfDisplay.DataAxesGrid.ZLabelOpacity = 1.0
    activation_resultsxdmfDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
    activation_resultsxdmfDisplay.DataAxesGrid.XAxisPrecision = 2
    activation_resultsxdmfDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
    activation_resultsxdmfDisplay.DataAxesGrid.XAxisLabels = []
    activation_resultsxdmfDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
    activation_resultsxdmfDisplay.DataAxesGrid.YAxisPrecision = 2
    activation_resultsxdmfDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
    activation_resultsxdmfDisplay.DataAxesGrid.YAxisLabels = []
    activation_resultsxdmfDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
    activation_resultsxdmfDisplay.DataAxesGrid.ZAxisPrecision = 2
    activation_resultsxdmfDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
    activation_resultsxdmfDisplay.DataAxesGrid.ZAxisLabels = []
    activation_resultsxdmfDisplay.DataAxesGrid.UseCustomBounds = 0
    activation_resultsxdmfDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'Polar Axes Representation' selected for 'PolarAxes'
    activation_resultsxdmfDisplay.PolarAxes.Visibility = 0
    activation_resultsxdmfDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
    activation_resultsxdmfDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
    activation_resultsxdmfDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    activation_resultsxdmfDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
    activation_resultsxdmfDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    activation_resultsxdmfDisplay.PolarAxes.EnableCustomRange = 0
    activation_resultsxdmfDisplay.PolarAxes.CustomRange = [0.0, 1.0]
    activation_resultsxdmfDisplay.PolarAxes.AutoPole = 1
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisVisibility = 1
    activation_resultsxdmfDisplay.PolarAxes.RadialAxesVisibility = 1
    activation_resultsxdmfDisplay.PolarAxes.DrawRadialGridlines = 1
    activation_resultsxdmfDisplay.PolarAxes.PolarArcsVisibility = 1
    activation_resultsxdmfDisplay.PolarAxes.DrawPolarArcsGridlines = 1
    activation_resultsxdmfDisplay.PolarAxes.NumberOfRadialAxes = 0
    activation_resultsxdmfDisplay.PolarAxes.DeltaAngleRadialAxes = 45.0
    activation_resultsxdmfDisplay.PolarAxes.NumberOfPolarAxes = 5
    activation_resultsxdmfDisplay.PolarAxes.DeltaRangePolarAxes = 0.0
    activation_resultsxdmfDisplay.PolarAxes.CustomMinRadius = 1
    activation_resultsxdmfDisplay.PolarAxes.MinimumRadius = 0.0
    activation_resultsxdmfDisplay.PolarAxes.CustomAngles = 1
    activation_resultsxdmfDisplay.PolarAxes.MinimumAngle = 0.0
    activation_resultsxdmfDisplay.PolarAxes.MaximumAngle = 90.0
    activation_resultsxdmfDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
    activation_resultsxdmfDisplay.PolarAxes.PolarArcResolutionPerDegree = 0.2
    activation_resultsxdmfDisplay.PolarAxes.Ratio = 1.0
    activation_resultsxdmfDisplay.PolarAxes.EnableOverallColor = 1
    activation_resultsxdmfDisplay.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    activation_resultsxdmfDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    activation_resultsxdmfDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    activation_resultsxdmfDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    activation_resultsxdmfDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisTitleVisibility = 1
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    activation_resultsxdmfDisplay.PolarAxes.PolarTitleOffset = [20.0, 20.0]
    activation_resultsxdmfDisplay.PolarAxes.PolarLabelVisibility = 1
    activation_resultsxdmfDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
    activation_resultsxdmfDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
    activation_resultsxdmfDisplay.PolarAxes.PolarLabelOffset = 10.0
    activation_resultsxdmfDisplay.PolarAxes.PolarExponentOffset = 5.0
    activation_resultsxdmfDisplay.PolarAxes.RadialTitleVisibility = 1
    activation_resultsxdmfDisplay.PolarAxes.RadialTitleFormat = '%-#3.1f'
    activation_resultsxdmfDisplay.PolarAxes.RadialTitleLocation = 'Bottom'
    activation_resultsxdmfDisplay.PolarAxes.RadialTitleOffset = [20.0, 0.0]
    activation_resultsxdmfDisplay.PolarAxes.RadialUnitsVisibility = 1
    activation_resultsxdmfDisplay.PolarAxes.ScreenSize = 10.0
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisTitleFontFile = ''
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisTitleBold = 0
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisTitleItalic = 0
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisTitleShadow = 0
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisTitleFontSize = 12
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisLabelFontFile = ''
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisLabelBold = 0
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisLabelItalic = 0
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisLabelShadow = 0
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisLabelFontSize = 12
    activation_resultsxdmfDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
    activation_resultsxdmfDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    activation_resultsxdmfDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
    activation_resultsxdmfDisplay.PolarAxes.LastRadialAxisTextBold = 0
    activation_resultsxdmfDisplay.PolarAxes.LastRadialAxisTextItalic = 0
    activation_resultsxdmfDisplay.PolarAxes.LastRadialAxisTextShadow = 0
    activation_resultsxdmfDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
    activation_resultsxdmfDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    activation_resultsxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    activation_resultsxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    activation_resultsxdmfDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
    activation_resultsxdmfDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
    activation_resultsxdmfDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
    activation_resultsxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    activation_resultsxdmfDisplay.PolarAxes.EnableDistanceLOD = 1
    activation_resultsxdmfDisplay.PolarAxes.DistanceLODThreshold = 0.7
    activation_resultsxdmfDisplay.PolarAxes.EnableViewAngleLOD = 1
    activation_resultsxdmfDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
    activation_resultsxdmfDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
    activation_resultsxdmfDisplay.PolarAxes.PolarTicksVisibility = 1
    activation_resultsxdmfDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
    activation_resultsxdmfDisplay.PolarAxes.TickLocation = 'Both'
    activation_resultsxdmfDisplay.PolarAxes.AxisTickVisibility = 1
    activation_resultsxdmfDisplay.PolarAxes.AxisMinorTickVisibility = 0
    activation_resultsxdmfDisplay.PolarAxes.AxisTickMatchesPolarAxes = 1
    activation_resultsxdmfDisplay.PolarAxes.DeltaRangeMajor = 1.0
    activation_resultsxdmfDisplay.PolarAxes.DeltaRangeMinor = 0.5
    activation_resultsxdmfDisplay.PolarAxes.ArcTickVisibility = 1
    activation_resultsxdmfDisplay.PolarAxes.ArcMinorTickVisibility = 0
    activation_resultsxdmfDisplay.PolarAxes.ArcTickMatchesRadialAxes = 1
    activation_resultsxdmfDisplay.PolarAxes.DeltaAngleMajor = 10.0
    activation_resultsxdmfDisplay.PolarAxes.DeltaAngleMinor = 5.0
    activation_resultsxdmfDisplay.PolarAxes.TickRatioRadiusSize = 0.02
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
    activation_resultsxdmfDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
    activation_resultsxdmfDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    activation_resultsxdmfDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    activation_resultsxdmfDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    activation_resultsxdmfDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    activation_resultsxdmfDisplay.PolarAxes.ArcMajorTickSize = 0.0
    activation_resultsxdmfDisplay.PolarAxes.ArcTickRatioSize = 0.3
    activation_resultsxdmfDisplay.PolarAxes.ArcMajorTickThickness = 1.0
    activation_resultsxdmfDisplay.PolarAxes.ArcTickRatioThickness = 0.5
    activation_resultsxdmfDisplay.PolarAxes.Use2DMode = 0
    activation_resultsxdmfDisplay.PolarAxes.UseLogAxis = 0

    # show color bar/color legend
    activation_resultsxdmfDisplay.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.5625, 0.0, 24.418286913026634]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 6.319917701868932
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.0, 0.0, 6.6921304299024635]
    renderView1.CameraFocalPoint = [-1.5625, 0.0, 0.0]
    renderView1.CameraParallelScale = 1.7320508075688772

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    # create a new 'Append Attributes'
    appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=activation_resultsxdmf)

    # set active source
    SetActiveSource(activation_resultsxdmf)

    # destroy appendAttributes1
    Delete(appendAttributes1)
    del appendAttributes1

    # set active source
    SetActiveSource(displacementxdmf)

    # set active source
    SetActiveSource(activation_resultsxdmf)

    # create a new 'Append Attributes'
    appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[displacementxdmf, activation_resultsxdmf])

    # show data in view
    appendAttributes1Display = Show(appendAttributes1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    appendAttributes1Display.Selection = None
    appendAttributes1Display.Representation = 'Surface'
    appendAttributes1Display.ColorArrayName = [None, '']
    appendAttributes1Display.LookupTable = None
    appendAttributes1Display.MapScalars = 1
    appendAttributes1Display.MultiComponentsMapping = 0
    appendAttributes1Display.InterpolateScalarsBeforeMapping = 1
    appendAttributes1Display.UseNanColorForMissingArrays = 0
    appendAttributes1Display.Opacity = 1.0
    appendAttributes1Display.PointSize = 2.0
    appendAttributes1Display.LineWidth = 1.0
    appendAttributes1Display.RenderLinesAsTubes = 0
    appendAttributes1Display.RenderPointsAsSpheres = 0
    appendAttributes1Display.Interpolation = 'Gouraud'
    appendAttributes1Display.Specular = 0.0
    appendAttributes1Display.SpecularColor = [1.0, 1.0, 1.0]
    appendAttributes1Display.SpecularPower = 100.0
    appendAttributes1Display.Luminosity = 0.0
    appendAttributes1Display.Ambient = 0.0
    appendAttributes1Display.Diffuse = 1.0
    appendAttributes1Display.Roughness = 0.3
    appendAttributes1Display.Metallic = 0.0
    appendAttributes1Display.EdgeTint = [1.0, 1.0, 1.0]
    appendAttributes1Display.Anisotropy = 0.0
    appendAttributes1Display.AnisotropyRotation = 0.0
    appendAttributes1Display.BaseIOR = 1.5
    appendAttributes1Display.CoatStrength = 0.0
    appendAttributes1Display.CoatIOR = 2.0
    appendAttributes1Display.CoatRoughness = 0.0
    appendAttributes1Display.CoatColor = [1.0, 1.0, 1.0]
    appendAttributes1Display.SelectTCoordArray = 'None'
    appendAttributes1Display.SelectNormalArray = 'None'
    appendAttributes1Display.SelectTangentArray = 'None'
    appendAttributes1Display.Texture = None
    appendAttributes1Display.RepeatTextures = 1
    appendAttributes1Display.InterpolateTextures = 0
    appendAttributes1Display.SeamlessU = 0
    appendAttributes1Display.SeamlessV = 0
    appendAttributes1Display.UseMipmapTextures = 0
    appendAttributes1Display.ShowTexturesOnBackface = 1
    appendAttributes1Display.BaseColorTexture = None
    appendAttributes1Display.NormalTexture = None
    appendAttributes1Display.NormalScale = 1.0
    appendAttributes1Display.CoatNormalTexture = None
    appendAttributes1Display.CoatNormalScale = 1.0
    appendAttributes1Display.MaterialTexture = None
    appendAttributes1Display.OcclusionStrength = 1.0
    appendAttributes1Display.AnisotropyTexture = None
    appendAttributes1Display.EmissiveTexture = None
    appendAttributes1Display.EmissiveFactor = [1.0, 1.0, 1.0]
    appendAttributes1Display.FlipTextures = 0
    appendAttributes1Display.EdgeOpacity = 1.0
    appendAttributes1Display.BackfaceRepresentation = 'Follow Frontface'
    appendAttributes1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    appendAttributes1Display.BackfaceOpacity = 1.0
    appendAttributes1Display.Position = [0.0, 0.0, 0.0]
    appendAttributes1Display.Scale = [1.0, 1.0, 1.0]
    appendAttributes1Display.Orientation = [0.0, 0.0, 0.0]
    appendAttributes1Display.Origin = [0.0, 0.0, 0.0]
    appendAttributes1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    appendAttributes1Display.Pickable = 1
    appendAttributes1Display.Triangulate = 0
    appendAttributes1Display.UseShaderReplacements = 0
    appendAttributes1Display.ShaderReplacements = ''
    appendAttributes1Display.NonlinearSubdivisionLevel = 1
    appendAttributes1Display.MatchBoundariesIgnoringCellOrder = 0
    appendAttributes1Display.UseDataPartitions = 0
    appendAttributes1Display.OSPRayUseScaleArray = 'All Approximate'
    appendAttributes1Display.OSPRayScaleArray = 'Displacement'
    appendAttributes1Display.OSPRayScaleFunction = 'Piecewise Function'
    appendAttributes1Display.OSPRayMaterial = 'None'
    appendAttributes1Display.Assembly = ''
    appendAttributes1Display.BlockSelectors = ['/']
    appendAttributes1Display.BlockColors = []
    appendAttributes1Display.BlockOpacities = []
    appendAttributes1Display.Orient = 0
    appendAttributes1Display.OrientationMode = 'Direction'
    appendAttributes1Display.SelectOrientationVectors = 'Displacement'
    appendAttributes1Display.Scaling = 0
    appendAttributes1Display.ScaleMode = 'No Data Scaling Off'
    appendAttributes1Display.ScaleFactor = 0.7499993801116944
    appendAttributes1Display.SelectScaleArray = 'Displacement'
    appendAttributes1Display.GlyphType = 'Arrow'
    appendAttributes1Display.UseGlyphTable = 0
    appendAttributes1Display.GlyphTableIndexArray = 'Displacement'
    appendAttributes1Display.UseCompositeGlyphTable = 0
    appendAttributes1Display.UseGlyphCullingAndLOD = 0
    appendAttributes1Display.LODValues = []
    appendAttributes1Display.ColorByLODIndex = 0
    appendAttributes1Display.GaussianRadius = 0.037499969005584714
    appendAttributes1Display.ShaderPreset = 'Sphere'
    appendAttributes1Display.CustomTriangleScale = 3
    appendAttributes1Display.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
    float gaussian = exp(-0.5*dist2);
    opacity = opacity*gaussian;
    """
    appendAttributes1Display.Emissive = 0
    appendAttributes1Display.ScaleByArray = 0
    appendAttributes1Display.SetScaleArray = ['POINTS', 'Displacement']
    appendAttributes1Display.ScaleArrayComponent = 'X'
    appendAttributes1Display.UseScaleFunction = 1
    appendAttributes1Display.ScaleTransferFunction = 'Piecewise Function'
    appendAttributes1Display.OpacityByArray = 0
    appendAttributes1Display.OpacityArray = ['POINTS', 'Displacement']
    appendAttributes1Display.OpacityArrayComponent = 'X'
    appendAttributes1Display.OpacityTransferFunction = 'Piecewise Function'
    appendAttributes1Display.DataAxesGrid = 'Grid Axes Representation'
    appendAttributes1Display.SelectionCellLabelBold = 0
    appendAttributes1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    appendAttributes1Display.SelectionCellLabelFontFamily = 'Arial'
    appendAttributes1Display.SelectionCellLabelFontFile = ''
    appendAttributes1Display.SelectionCellLabelFontSize = 18
    appendAttributes1Display.SelectionCellLabelItalic = 0
    appendAttributes1Display.SelectionCellLabelJustification = 'Left'
    appendAttributes1Display.SelectionCellLabelOpacity = 1.0
    appendAttributes1Display.SelectionCellLabelShadow = 0
    appendAttributes1Display.SelectionPointLabelBold = 0
    appendAttributes1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    appendAttributes1Display.SelectionPointLabelFontFamily = 'Arial'
    appendAttributes1Display.SelectionPointLabelFontFile = ''
    appendAttributes1Display.SelectionPointLabelFontSize = 18
    appendAttributes1Display.SelectionPointLabelItalic = 0
    appendAttributes1Display.SelectionPointLabelJustification = 'Left'
    appendAttributes1Display.SelectionPointLabelOpacity = 1.0
    appendAttributes1Display.SelectionPointLabelShadow = 0
    appendAttributes1Display.PolarAxes = 'Polar Axes Representation'
    appendAttributes1Display.ScalarOpacityFunction = None
    appendAttributes1Display.ScalarOpacityUnitDistance = 0.5583539716188769
    appendAttributes1Display.UseSeparateOpacityArray = 0
    appendAttributes1Display.OpacityArrayName = ['POINTS', 'Displacement']
    appendAttributes1Display.OpacityComponent = 'X'
    appendAttributes1Display.SelectMapper = 'Projected tetra'
    appendAttributes1Display.SamplingDimensions = [128, 128, 128]
    appendAttributes1Display.UseFloatingPointFrameBuffer = 1
    appendAttributes1Display.SelectInputVectors = ['POINTS', 'Displacement']
    appendAttributes1Display.NumberOfSteps = 40
    appendAttributes1Display.StepSize = 0.25
    appendAttributes1Display.NormalizeVectors = 1
    appendAttributes1Display.EnhancedLIC = 1
    appendAttributes1Display.ColorMode = 'Blend'
    appendAttributes1Display.LICIntensity = 0.8
    appendAttributes1Display.MapModeBias = 0.0
    appendAttributes1Display.EnhanceContrast = 'Off'
    appendAttributes1Display.LowLICContrastEnhancementFactor = 0.0
    appendAttributes1Display.HighLICContrastEnhancementFactor = 0.0
    appendAttributes1Display.LowColorContrastEnhancementFactor = 0.0
    appendAttributes1Display.HighColorContrastEnhancementFactor = 0.0
    appendAttributes1Display.AntiAlias = 0
    appendAttributes1Display.MaskOnSurface = 1
    appendAttributes1Display.MaskThreshold = 0.0
    appendAttributes1Display.MaskIntensity = 0.0
    appendAttributes1Display.MaskColor = [0.5, 0.5, 0.5]
    appendAttributes1Display.GenerateNoiseTexture = 0
    appendAttributes1Display.NoiseType = 'Gaussian'
    appendAttributes1Display.NoiseTextureSize = 128
    appendAttributes1Display.NoiseGrainSize = 2
    appendAttributes1Display.MinNoiseValue = 0.0
    appendAttributes1Display.MaxNoiseValue = 0.8
    appendAttributes1Display.NumberOfNoiseLevels = 1024
    appendAttributes1Display.ImpulseNoiseProbability = 1.0
    appendAttributes1Display.ImpulseNoiseBackgroundValue = 0.0
    appendAttributes1Display.NoiseGeneratorSeed = 1
    appendAttributes1Display.CompositeStrategy = 'AUTO'
    appendAttributes1Display.UseLICForLOD = 0
    appendAttributes1Display.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    appendAttributes1Display.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]
    appendAttributes1Display.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    appendAttributes1Display.GlyphType.TipResolution = 6
    appendAttributes1Display.GlyphType.TipRadius = 0.1
    appendAttributes1Display.GlyphType.TipLength = 0.35
    appendAttributes1Display.GlyphType.ShaftResolution = 6
    appendAttributes1Display.GlyphType.ShaftRadius = 0.03
    appendAttributes1Display.GlyphType.Invert = 0

    # init the 'Piecewise Function' selected for 'ScaleTransferFunction'
    appendAttributes1Display.ScaleTransferFunction.Points = [-0.28369444608688354, 0.0, 0.5, 0.0, 0.0175445768982172, 1.0, 0.5, 0.0]
    appendAttributes1Display.ScaleTransferFunction.UseLogScale = 0

    # init the 'Piecewise Function' selected for 'OpacityTransferFunction'
    appendAttributes1Display.OpacityTransferFunction.Points = [-0.28369444608688354, 0.0, 0.5, 0.0, 0.0175445768982172, 1.0, 0.5, 0.0]
    appendAttributes1Display.OpacityTransferFunction.UseLogScale = 0

    # init the 'Grid Axes Representation' selected for 'DataAxesGrid'
    appendAttributes1Display.DataAxesGrid.XTitle = 'X Axis'
    appendAttributes1Display.DataAxesGrid.YTitle = 'Y Axis'
    appendAttributes1Display.DataAxesGrid.ZTitle = 'Z Axis'
    appendAttributes1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
    appendAttributes1Display.DataAxesGrid.XTitleFontFile = ''
    appendAttributes1Display.DataAxesGrid.XTitleBold = 0
    appendAttributes1Display.DataAxesGrid.XTitleItalic = 0
    appendAttributes1Display.DataAxesGrid.XTitleFontSize = 12
    appendAttributes1Display.DataAxesGrid.XTitleShadow = 0
    appendAttributes1Display.DataAxesGrid.XTitleOpacity = 1.0
    appendAttributes1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
    appendAttributes1Display.DataAxesGrid.YTitleFontFile = ''
    appendAttributes1Display.DataAxesGrid.YTitleBold = 0
    appendAttributes1Display.DataAxesGrid.YTitleItalic = 0
    appendAttributes1Display.DataAxesGrid.YTitleFontSize = 12
    appendAttributes1Display.DataAxesGrid.YTitleShadow = 0
    appendAttributes1Display.DataAxesGrid.YTitleOpacity = 1.0
    appendAttributes1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
    appendAttributes1Display.DataAxesGrid.ZTitleFontFile = ''
    appendAttributes1Display.DataAxesGrid.ZTitleBold = 0
    appendAttributes1Display.DataAxesGrid.ZTitleItalic = 0
    appendAttributes1Display.DataAxesGrid.ZTitleFontSize = 12
    appendAttributes1Display.DataAxesGrid.ZTitleShadow = 0
    appendAttributes1Display.DataAxesGrid.ZTitleOpacity = 1.0
    appendAttributes1Display.DataAxesGrid.FacesToRender = 63
    appendAttributes1Display.DataAxesGrid.CullBackface = 0
    appendAttributes1Display.DataAxesGrid.CullFrontface = 1
    appendAttributes1Display.DataAxesGrid.ShowGrid = 0
    appendAttributes1Display.DataAxesGrid.ShowEdges = 1
    appendAttributes1Display.DataAxesGrid.ShowTicks = 1
    appendAttributes1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
    appendAttributes1Display.DataAxesGrid.AxesToLabel = 63
    appendAttributes1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
    appendAttributes1Display.DataAxesGrid.XLabelFontFile = ''
    appendAttributes1Display.DataAxesGrid.XLabelBold = 0
    appendAttributes1Display.DataAxesGrid.XLabelItalic = 0
    appendAttributes1Display.DataAxesGrid.XLabelFontSize = 12
    appendAttributes1Display.DataAxesGrid.XLabelShadow = 0
    appendAttributes1Display.DataAxesGrid.XLabelOpacity = 1.0
    appendAttributes1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
    appendAttributes1Display.DataAxesGrid.YLabelFontFile = ''
    appendAttributes1Display.DataAxesGrid.YLabelBold = 0
    appendAttributes1Display.DataAxesGrid.YLabelItalic = 0
    appendAttributes1Display.DataAxesGrid.YLabelFontSize = 12
    appendAttributes1Display.DataAxesGrid.YLabelShadow = 0
    appendAttributes1Display.DataAxesGrid.YLabelOpacity = 1.0
    appendAttributes1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
    appendAttributes1Display.DataAxesGrid.ZLabelFontFile = ''
    appendAttributes1Display.DataAxesGrid.ZLabelBold = 0
    appendAttributes1Display.DataAxesGrid.ZLabelItalic = 0
    appendAttributes1Display.DataAxesGrid.ZLabelFontSize = 12
    appendAttributes1Display.DataAxesGrid.ZLabelShadow = 0
    appendAttributes1Display.DataAxesGrid.ZLabelOpacity = 1.0
    appendAttributes1Display.DataAxesGrid.XAxisNotation = 'Mixed'
    appendAttributes1Display.DataAxesGrid.XAxisPrecision = 2
    appendAttributes1Display.DataAxesGrid.XAxisUseCustomLabels = 0
    appendAttributes1Display.DataAxesGrid.XAxisLabels = []
    appendAttributes1Display.DataAxesGrid.YAxisNotation = 'Mixed'
    appendAttributes1Display.DataAxesGrid.YAxisPrecision = 2
    appendAttributes1Display.DataAxesGrid.YAxisUseCustomLabels = 0
    appendAttributes1Display.DataAxesGrid.YAxisLabels = []
    appendAttributes1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
    appendAttributes1Display.DataAxesGrid.ZAxisPrecision = 2
    appendAttributes1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
    appendAttributes1Display.DataAxesGrid.ZAxisLabels = []
    appendAttributes1Display.DataAxesGrid.UseCustomBounds = 0
    appendAttributes1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'Polar Axes Representation' selected for 'PolarAxes'
    appendAttributes1Display.PolarAxes.Visibility = 0
    appendAttributes1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
    appendAttributes1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
    appendAttributes1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    appendAttributes1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
    appendAttributes1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    appendAttributes1Display.PolarAxes.EnableCustomRange = 0
    appendAttributes1Display.PolarAxes.CustomRange = [0.0, 1.0]
    appendAttributes1Display.PolarAxes.AutoPole = 1
    appendAttributes1Display.PolarAxes.PolarAxisVisibility = 1
    appendAttributes1Display.PolarAxes.RadialAxesVisibility = 1
    appendAttributes1Display.PolarAxes.DrawRadialGridlines = 1
    appendAttributes1Display.PolarAxes.PolarArcsVisibility = 1
    appendAttributes1Display.PolarAxes.DrawPolarArcsGridlines = 1
    appendAttributes1Display.PolarAxes.NumberOfRadialAxes = 0
    appendAttributes1Display.PolarAxes.DeltaAngleRadialAxes = 45.0
    appendAttributes1Display.PolarAxes.NumberOfPolarAxes = 5
    appendAttributes1Display.PolarAxes.DeltaRangePolarAxes = 0.0
    appendAttributes1Display.PolarAxes.CustomMinRadius = 1
    appendAttributes1Display.PolarAxes.MinimumRadius = 0.0
    appendAttributes1Display.PolarAxes.CustomAngles = 1
    appendAttributes1Display.PolarAxes.MinimumAngle = 0.0
    appendAttributes1Display.PolarAxes.MaximumAngle = 90.0
    appendAttributes1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
    appendAttributes1Display.PolarAxes.PolarArcResolutionPerDegree = 0.2
    appendAttributes1Display.PolarAxes.Ratio = 1.0
    appendAttributes1Display.PolarAxes.EnableOverallColor = 1
    appendAttributes1Display.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
    appendAttributes1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    appendAttributes1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    appendAttributes1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    appendAttributes1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    appendAttributes1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    appendAttributes1Display.PolarAxes.PolarAxisTitleVisibility = 1
    appendAttributes1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
    appendAttributes1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    appendAttributes1Display.PolarAxes.PolarTitleOffset = [20.0, 20.0]
    appendAttributes1Display.PolarAxes.PolarLabelVisibility = 1
    appendAttributes1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
    appendAttributes1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
    appendAttributes1Display.PolarAxes.PolarLabelOffset = 10.0
    appendAttributes1Display.PolarAxes.PolarExponentOffset = 5.0
    appendAttributes1Display.PolarAxes.RadialTitleVisibility = 1
    appendAttributes1Display.PolarAxes.RadialTitleFormat = '%-#3.1f'
    appendAttributes1Display.PolarAxes.RadialTitleLocation = 'Bottom'
    appendAttributes1Display.PolarAxes.RadialTitleOffset = [20.0, 0.0]
    appendAttributes1Display.PolarAxes.RadialUnitsVisibility = 1
    appendAttributes1Display.PolarAxes.ScreenSize = 10.0
    appendAttributes1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
    appendAttributes1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    appendAttributes1Display.PolarAxes.PolarAxisTitleFontFile = ''
    appendAttributes1Display.PolarAxes.PolarAxisTitleBold = 0
    appendAttributes1Display.PolarAxes.PolarAxisTitleItalic = 0
    appendAttributes1Display.PolarAxes.PolarAxisTitleShadow = 0
    appendAttributes1Display.PolarAxes.PolarAxisTitleFontSize = 12
    appendAttributes1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
    appendAttributes1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    appendAttributes1Display.PolarAxes.PolarAxisLabelFontFile = ''
    appendAttributes1Display.PolarAxes.PolarAxisLabelBold = 0
    appendAttributes1Display.PolarAxes.PolarAxisLabelItalic = 0
    appendAttributes1Display.PolarAxes.PolarAxisLabelShadow = 0
    appendAttributes1Display.PolarAxes.PolarAxisLabelFontSize = 12
    appendAttributes1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
    appendAttributes1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    appendAttributes1Display.PolarAxes.LastRadialAxisTextFontFile = ''
    appendAttributes1Display.PolarAxes.LastRadialAxisTextBold = 0
    appendAttributes1Display.PolarAxes.LastRadialAxisTextItalic = 0
    appendAttributes1Display.PolarAxes.LastRadialAxisTextShadow = 0
    appendAttributes1Display.PolarAxes.LastRadialAxisTextFontSize = 12
    appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
    appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
    appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
    appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    appendAttributes1Display.PolarAxes.EnableDistanceLOD = 1
    appendAttributes1Display.PolarAxes.DistanceLODThreshold = 0.7
    appendAttributes1Display.PolarAxes.EnableViewAngleLOD = 1
    appendAttributes1Display.PolarAxes.ViewAngleLODThreshold = 0.7
    appendAttributes1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
    appendAttributes1Display.PolarAxes.PolarTicksVisibility = 1
    appendAttributes1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
    appendAttributes1Display.PolarAxes.TickLocation = 'Both'
    appendAttributes1Display.PolarAxes.AxisTickVisibility = 1
    appendAttributes1Display.PolarAxes.AxisMinorTickVisibility = 0
    appendAttributes1Display.PolarAxes.AxisTickMatchesPolarAxes = 1
    appendAttributes1Display.PolarAxes.DeltaRangeMajor = 1.0
    appendAttributes1Display.PolarAxes.DeltaRangeMinor = 0.5
    appendAttributes1Display.PolarAxes.ArcTickVisibility = 1
    appendAttributes1Display.PolarAxes.ArcMinorTickVisibility = 0
    appendAttributes1Display.PolarAxes.ArcTickMatchesRadialAxes = 1
    appendAttributes1Display.PolarAxes.DeltaAngleMajor = 10.0
    appendAttributes1Display.PolarAxes.DeltaAngleMinor = 5.0
    appendAttributes1Display.PolarAxes.TickRatioRadiusSize = 0.02
    appendAttributes1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
    appendAttributes1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
    appendAttributes1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
    appendAttributes1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
    appendAttributes1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    appendAttributes1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    appendAttributes1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    appendAttributes1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    appendAttributes1Display.PolarAxes.ArcMajorTickSize = 0.0
    appendAttributes1Display.PolarAxes.ArcTickRatioSize = 0.3
    appendAttributes1Display.PolarAxes.ArcMajorTickThickness = 1.0
    appendAttributes1Display.PolarAxes.ArcTickRatioThickness = 0.5
    appendAttributes1Display.PolarAxes.Use2DMode = 0
    appendAttributes1Display.PolarAxes.UseLogAxis = 0

    # hide data in view
    Hide(displacementxdmf, renderView1)

    # hide data in view
    Hide(activation_resultsxdmf, renderView1)

    # create a new 'Warp By Vector'
    warpByVector1 = WarpByVector(registrationName='WarpByVector1', Input=appendAttributes1)
    warpByVector1.Vectors = ['POINTS', 'Displacement']
    warpByVector1.ScaleFactor = 1.0

    # show data in view
    warpByVector1Display = Show(warpByVector1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    warpByVector1Display.Selection = None
    warpByVector1Display.Representation = 'Surface'
    warpByVector1Display.ColorArrayName = [None, '']
    warpByVector1Display.LookupTable = None
    warpByVector1Display.MapScalars = 1
    warpByVector1Display.MultiComponentsMapping = 0
    warpByVector1Display.InterpolateScalarsBeforeMapping = 1
    warpByVector1Display.UseNanColorForMissingArrays = 0
    warpByVector1Display.Opacity = 1.0
    warpByVector1Display.PointSize = 2.0
    warpByVector1Display.LineWidth = 1.0
    warpByVector1Display.RenderLinesAsTubes = 0
    warpByVector1Display.RenderPointsAsSpheres = 0
    warpByVector1Display.Interpolation = 'Gouraud'
    warpByVector1Display.Specular = 0.0
    warpByVector1Display.SpecularColor = [1.0, 1.0, 1.0]
    warpByVector1Display.SpecularPower = 100.0
    warpByVector1Display.Luminosity = 0.0
    warpByVector1Display.Ambient = 0.0
    warpByVector1Display.Diffuse = 1.0
    warpByVector1Display.Roughness = 0.3
    warpByVector1Display.Metallic = 0.0
    warpByVector1Display.EdgeTint = [1.0, 1.0, 1.0]
    warpByVector1Display.Anisotropy = 0.0
    warpByVector1Display.AnisotropyRotation = 0.0
    warpByVector1Display.BaseIOR = 1.5
    warpByVector1Display.CoatStrength = 0.0
    warpByVector1Display.CoatIOR = 2.0
    warpByVector1Display.CoatRoughness = 0.0
    warpByVector1Display.CoatColor = [1.0, 1.0, 1.0]
    warpByVector1Display.SelectTCoordArray = 'None'
    warpByVector1Display.SelectNormalArray = 'None'
    warpByVector1Display.SelectTangentArray = 'None'
    warpByVector1Display.Texture = None
    warpByVector1Display.RepeatTextures = 1
    warpByVector1Display.InterpolateTextures = 0
    warpByVector1Display.SeamlessU = 0
    warpByVector1Display.SeamlessV = 0
    warpByVector1Display.UseMipmapTextures = 0
    warpByVector1Display.ShowTexturesOnBackface = 1
    warpByVector1Display.BaseColorTexture = None
    warpByVector1Display.NormalTexture = None
    warpByVector1Display.NormalScale = 1.0
    warpByVector1Display.CoatNormalTexture = None
    warpByVector1Display.CoatNormalScale = 1.0
    warpByVector1Display.MaterialTexture = None
    warpByVector1Display.OcclusionStrength = 1.0
    warpByVector1Display.AnisotropyTexture = None
    warpByVector1Display.EmissiveTexture = None
    warpByVector1Display.EmissiveFactor = [1.0, 1.0, 1.0]
    warpByVector1Display.FlipTextures = 0
    warpByVector1Display.EdgeOpacity = 1.0
    warpByVector1Display.BackfaceRepresentation = 'Follow Frontface'
    warpByVector1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    warpByVector1Display.BackfaceOpacity = 1.0
    warpByVector1Display.Position = [0.0, 0.0, 0.0]
    warpByVector1Display.Scale = [1.0, 1.0, 1.0]
    warpByVector1Display.Orientation = [0.0, 0.0, 0.0]
    warpByVector1Display.Origin = [0.0, 0.0, 0.0]
    warpByVector1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    warpByVector1Display.Pickable = 1
    warpByVector1Display.Triangulate = 0
    warpByVector1Display.UseShaderReplacements = 0
    warpByVector1Display.ShaderReplacements = ''
    warpByVector1Display.NonlinearSubdivisionLevel = 1
    warpByVector1Display.MatchBoundariesIgnoringCellOrder = 0
    warpByVector1Display.UseDataPartitions = 0
    warpByVector1Display.OSPRayUseScaleArray = 'All Approximate'
    warpByVector1Display.OSPRayScaleArray = 'Displacement'
    warpByVector1Display.OSPRayScaleFunction = 'Piecewise Function'
    warpByVector1Display.OSPRayMaterial = 'None'
    warpByVector1Display.Assembly = ''
    warpByVector1Display.BlockSelectors = ['/']
    warpByVector1Display.BlockColors = []
    warpByVector1Display.BlockOpacities = []
    warpByVector1Display.Orient = 0
    warpByVector1Display.OrientationMode = 'Direction'
    warpByVector1Display.SelectOrientationVectors = 'Displacement'
    warpByVector1Display.Scaling = 0
    warpByVector1Display.ScaleMode = 'No Data Scaling Off'
    warpByVector1Display.ScaleFactor = 0.8380639553070068
    warpByVector1Display.SelectScaleArray = 'Displacement'
    warpByVector1Display.GlyphType = 'Arrow'
    warpByVector1Display.UseGlyphTable = 0
    warpByVector1Display.GlyphTableIndexArray = 'Displacement'
    warpByVector1Display.UseCompositeGlyphTable = 0
    warpByVector1Display.UseGlyphCullingAndLOD = 0
    warpByVector1Display.LODValues = []
    warpByVector1Display.ColorByLODIndex = 0
    warpByVector1Display.GaussianRadius = 0.04190319776535034
    warpByVector1Display.ShaderPreset = 'Sphere'
    warpByVector1Display.CustomTriangleScale = 3
    warpByVector1Display.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
    float gaussian = exp(-0.5*dist2);
    opacity = opacity*gaussian;
    """
    warpByVector1Display.Emissive = 0
    warpByVector1Display.ScaleByArray = 0
    warpByVector1Display.SetScaleArray = ['POINTS', 'Displacement']
    warpByVector1Display.ScaleArrayComponent = 'X'
    warpByVector1Display.UseScaleFunction = 1
    warpByVector1Display.ScaleTransferFunction = 'Piecewise Function'
    warpByVector1Display.OpacityByArray = 0
    warpByVector1Display.OpacityArray = ['POINTS', 'Displacement']
    warpByVector1Display.OpacityArrayComponent = 'X'
    warpByVector1Display.OpacityTransferFunction = 'Piecewise Function'
    warpByVector1Display.DataAxesGrid = 'Grid Axes Representation'
    warpByVector1Display.SelectionCellLabelBold = 0
    warpByVector1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    warpByVector1Display.SelectionCellLabelFontFamily = 'Arial'
    warpByVector1Display.SelectionCellLabelFontFile = ''
    warpByVector1Display.SelectionCellLabelFontSize = 18
    warpByVector1Display.SelectionCellLabelItalic = 0
    warpByVector1Display.SelectionCellLabelJustification = 'Left'
    warpByVector1Display.SelectionCellLabelOpacity = 1.0
    warpByVector1Display.SelectionCellLabelShadow = 0
    warpByVector1Display.SelectionPointLabelBold = 0
    warpByVector1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    warpByVector1Display.SelectionPointLabelFontFamily = 'Arial'
    warpByVector1Display.SelectionPointLabelFontFile = ''
    warpByVector1Display.SelectionPointLabelFontSize = 18
    warpByVector1Display.SelectionPointLabelItalic = 0
    warpByVector1Display.SelectionPointLabelJustification = 'Left'
    warpByVector1Display.SelectionPointLabelOpacity = 1.0
    warpByVector1Display.SelectionPointLabelShadow = 0
    warpByVector1Display.PolarAxes = 'Polar Axes Representation'
    warpByVector1Display.ScalarOpacityFunction = None
    warpByVector1Display.ScalarOpacityUnitDistance = 0.6092618537762925
    warpByVector1Display.UseSeparateOpacityArray = 0
    warpByVector1Display.OpacityArrayName = ['POINTS', 'Displacement']
    warpByVector1Display.OpacityComponent = 'X'
    warpByVector1Display.SelectMapper = 'Projected tetra'
    warpByVector1Display.SamplingDimensions = [128, 128, 128]
    warpByVector1Display.UseFloatingPointFrameBuffer = 1
    warpByVector1Display.SelectInputVectors = ['POINTS', 'Displacement']
    warpByVector1Display.NumberOfSteps = 40
    warpByVector1Display.StepSize = 0.25
    warpByVector1Display.NormalizeVectors = 1
    warpByVector1Display.EnhancedLIC = 1
    warpByVector1Display.ColorMode = 'Blend'
    warpByVector1Display.LICIntensity = 0.8
    warpByVector1Display.MapModeBias = 0.0
    warpByVector1Display.EnhanceContrast = 'Off'
    warpByVector1Display.LowLICContrastEnhancementFactor = 0.0
    warpByVector1Display.HighLICContrastEnhancementFactor = 0.0
    warpByVector1Display.LowColorContrastEnhancementFactor = 0.0
    warpByVector1Display.HighColorContrastEnhancementFactor = 0.0
    warpByVector1Display.AntiAlias = 0
    warpByVector1Display.MaskOnSurface = 1
    warpByVector1Display.MaskThreshold = 0.0
    warpByVector1Display.MaskIntensity = 0.0
    warpByVector1Display.MaskColor = [0.5, 0.5, 0.5]
    warpByVector1Display.GenerateNoiseTexture = 0
    warpByVector1Display.NoiseType = 'Gaussian'
    warpByVector1Display.NoiseTextureSize = 128
    warpByVector1Display.NoiseGrainSize = 2
    warpByVector1Display.MinNoiseValue = 0.0
    warpByVector1Display.MaxNoiseValue = 0.8
    warpByVector1Display.NumberOfNoiseLevels = 1024
    warpByVector1Display.ImpulseNoiseProbability = 1.0
    warpByVector1Display.ImpulseNoiseBackgroundValue = 0.0
    warpByVector1Display.NoiseGeneratorSeed = 1
    warpByVector1Display.CompositeStrategy = 'AUTO'
    warpByVector1Display.UseLICForLOD = 0
    warpByVector1Display.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    warpByVector1Display.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]
    warpByVector1Display.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    warpByVector1Display.GlyphType.TipResolution = 6
    warpByVector1Display.GlyphType.TipRadius = 0.1
    warpByVector1Display.GlyphType.TipLength = 0.35
    warpByVector1Display.GlyphType.ShaftResolution = 6
    warpByVector1Display.GlyphType.ShaftRadius = 0.03
    warpByVector1Display.GlyphType.Invert = 0

    # init the 'Piecewise Function' selected for 'ScaleTransferFunction'
    warpByVector1Display.ScaleTransferFunction.Points = [-0.28369444608688354, 0.0, 0.5, 0.0, 0.0175445768982172, 1.0, 0.5, 0.0]
    warpByVector1Display.ScaleTransferFunction.UseLogScale = 0

    # init the 'Piecewise Function' selected for 'OpacityTransferFunction'
    warpByVector1Display.OpacityTransferFunction.Points = [-0.28369444608688354, 0.0, 0.5, 0.0, 0.0175445768982172, 1.0, 0.5, 0.0]
    warpByVector1Display.OpacityTransferFunction.UseLogScale = 0

    # init the 'Grid Axes Representation' selected for 'DataAxesGrid'
    warpByVector1Display.DataAxesGrid.XTitle = 'X Axis'
    warpByVector1Display.DataAxesGrid.YTitle = 'Y Axis'
    warpByVector1Display.DataAxesGrid.ZTitle = 'Z Axis'
    warpByVector1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
    warpByVector1Display.DataAxesGrid.XTitleFontFile = ''
    warpByVector1Display.DataAxesGrid.XTitleBold = 0
    warpByVector1Display.DataAxesGrid.XTitleItalic = 0
    warpByVector1Display.DataAxesGrid.XTitleFontSize = 12
    warpByVector1Display.DataAxesGrid.XTitleShadow = 0
    warpByVector1Display.DataAxesGrid.XTitleOpacity = 1.0
    warpByVector1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
    warpByVector1Display.DataAxesGrid.YTitleFontFile = ''
    warpByVector1Display.DataAxesGrid.YTitleBold = 0
    warpByVector1Display.DataAxesGrid.YTitleItalic = 0
    warpByVector1Display.DataAxesGrid.YTitleFontSize = 12
    warpByVector1Display.DataAxesGrid.YTitleShadow = 0
    warpByVector1Display.DataAxesGrid.YTitleOpacity = 1.0
    warpByVector1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
    warpByVector1Display.DataAxesGrid.ZTitleFontFile = ''
    warpByVector1Display.DataAxesGrid.ZTitleBold = 0
    warpByVector1Display.DataAxesGrid.ZTitleItalic = 0
    warpByVector1Display.DataAxesGrid.ZTitleFontSize = 12
    warpByVector1Display.DataAxesGrid.ZTitleShadow = 0
    warpByVector1Display.DataAxesGrid.ZTitleOpacity = 1.0
    warpByVector1Display.DataAxesGrid.FacesToRender = 63
    warpByVector1Display.DataAxesGrid.CullBackface = 0
    warpByVector1Display.DataAxesGrid.CullFrontface = 1
    warpByVector1Display.DataAxesGrid.ShowGrid = 0
    warpByVector1Display.DataAxesGrid.ShowEdges = 1
    warpByVector1Display.DataAxesGrid.ShowTicks = 1
    warpByVector1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
    warpByVector1Display.DataAxesGrid.AxesToLabel = 63
    warpByVector1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
    warpByVector1Display.DataAxesGrid.XLabelFontFile = ''
    warpByVector1Display.DataAxesGrid.XLabelBold = 0
    warpByVector1Display.DataAxesGrid.XLabelItalic = 0
    warpByVector1Display.DataAxesGrid.XLabelFontSize = 12
    warpByVector1Display.DataAxesGrid.XLabelShadow = 0
    warpByVector1Display.DataAxesGrid.XLabelOpacity = 1.0
    warpByVector1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
    warpByVector1Display.DataAxesGrid.YLabelFontFile = ''
    warpByVector1Display.DataAxesGrid.YLabelBold = 0
    warpByVector1Display.DataAxesGrid.YLabelItalic = 0
    warpByVector1Display.DataAxesGrid.YLabelFontSize = 12
    warpByVector1Display.DataAxesGrid.YLabelShadow = 0
    warpByVector1Display.DataAxesGrid.YLabelOpacity = 1.0
    warpByVector1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
    warpByVector1Display.DataAxesGrid.ZLabelFontFile = ''
    warpByVector1Display.DataAxesGrid.ZLabelBold = 0
    warpByVector1Display.DataAxesGrid.ZLabelItalic = 0
    warpByVector1Display.DataAxesGrid.ZLabelFontSize = 12
    warpByVector1Display.DataAxesGrid.ZLabelShadow = 0
    warpByVector1Display.DataAxesGrid.ZLabelOpacity = 1.0
    warpByVector1Display.DataAxesGrid.XAxisNotation = 'Mixed'
    warpByVector1Display.DataAxesGrid.XAxisPrecision = 2
    warpByVector1Display.DataAxesGrid.XAxisUseCustomLabels = 0
    warpByVector1Display.DataAxesGrid.XAxisLabels = []
    warpByVector1Display.DataAxesGrid.YAxisNotation = 'Mixed'
    warpByVector1Display.DataAxesGrid.YAxisPrecision = 2
    warpByVector1Display.DataAxesGrid.YAxisUseCustomLabels = 0
    warpByVector1Display.DataAxesGrid.YAxisLabels = []
    warpByVector1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
    warpByVector1Display.DataAxesGrid.ZAxisPrecision = 2
    warpByVector1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
    warpByVector1Display.DataAxesGrid.ZAxisLabels = []
    warpByVector1Display.DataAxesGrid.UseCustomBounds = 0
    warpByVector1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'Polar Axes Representation' selected for 'PolarAxes'
    warpByVector1Display.PolarAxes.Visibility = 0
    warpByVector1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
    warpByVector1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
    warpByVector1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    warpByVector1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
    warpByVector1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    warpByVector1Display.PolarAxes.EnableCustomRange = 0
    warpByVector1Display.PolarAxes.CustomRange = [0.0, 1.0]
    warpByVector1Display.PolarAxes.AutoPole = 1
    warpByVector1Display.PolarAxes.PolarAxisVisibility = 1
    warpByVector1Display.PolarAxes.RadialAxesVisibility = 1
    warpByVector1Display.PolarAxes.DrawRadialGridlines = 1
    warpByVector1Display.PolarAxes.PolarArcsVisibility = 1
    warpByVector1Display.PolarAxes.DrawPolarArcsGridlines = 1
    warpByVector1Display.PolarAxes.NumberOfRadialAxes = 0
    warpByVector1Display.PolarAxes.DeltaAngleRadialAxes = 45.0
    warpByVector1Display.PolarAxes.NumberOfPolarAxes = 5
    warpByVector1Display.PolarAxes.DeltaRangePolarAxes = 0.0
    warpByVector1Display.PolarAxes.CustomMinRadius = 1
    warpByVector1Display.PolarAxes.MinimumRadius = 0.0
    warpByVector1Display.PolarAxes.CustomAngles = 1
    warpByVector1Display.PolarAxes.MinimumAngle = 0.0
    warpByVector1Display.PolarAxes.MaximumAngle = 90.0
    warpByVector1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
    warpByVector1Display.PolarAxes.PolarArcResolutionPerDegree = 0.2
    warpByVector1Display.PolarAxes.Ratio = 1.0
    warpByVector1Display.PolarAxes.EnableOverallColor = 1
    warpByVector1Display.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
    warpByVector1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    warpByVector1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    warpByVector1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    warpByVector1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    warpByVector1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    warpByVector1Display.PolarAxes.PolarAxisTitleVisibility = 1
    warpByVector1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
    warpByVector1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    warpByVector1Display.PolarAxes.PolarTitleOffset = [20.0, 20.0]
    warpByVector1Display.PolarAxes.PolarLabelVisibility = 1
    warpByVector1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
    warpByVector1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
    warpByVector1Display.PolarAxes.PolarLabelOffset = 10.0
    warpByVector1Display.PolarAxes.PolarExponentOffset = 5.0
    warpByVector1Display.PolarAxes.RadialTitleVisibility = 1
    warpByVector1Display.PolarAxes.RadialTitleFormat = '%-#3.1f'
    warpByVector1Display.PolarAxes.RadialTitleLocation = 'Bottom'
    warpByVector1Display.PolarAxes.RadialTitleOffset = [20.0, 0.0]
    warpByVector1Display.PolarAxes.RadialUnitsVisibility = 1
    warpByVector1Display.PolarAxes.ScreenSize = 10.0
    warpByVector1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
    warpByVector1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    warpByVector1Display.PolarAxes.PolarAxisTitleFontFile = ''
    warpByVector1Display.PolarAxes.PolarAxisTitleBold = 0
    warpByVector1Display.PolarAxes.PolarAxisTitleItalic = 0
    warpByVector1Display.PolarAxes.PolarAxisTitleShadow = 0
    warpByVector1Display.PolarAxes.PolarAxisTitleFontSize = 12
    warpByVector1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
    warpByVector1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    warpByVector1Display.PolarAxes.PolarAxisLabelFontFile = ''
    warpByVector1Display.PolarAxes.PolarAxisLabelBold = 0
    warpByVector1Display.PolarAxes.PolarAxisLabelItalic = 0
    warpByVector1Display.PolarAxes.PolarAxisLabelShadow = 0
    warpByVector1Display.PolarAxes.PolarAxisLabelFontSize = 12
    warpByVector1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
    warpByVector1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    warpByVector1Display.PolarAxes.LastRadialAxisTextFontFile = ''
    warpByVector1Display.PolarAxes.LastRadialAxisTextBold = 0
    warpByVector1Display.PolarAxes.LastRadialAxisTextItalic = 0
    warpByVector1Display.PolarAxes.LastRadialAxisTextShadow = 0
    warpByVector1Display.PolarAxes.LastRadialAxisTextFontSize = 12
    warpByVector1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    warpByVector1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    warpByVector1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    warpByVector1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
    warpByVector1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
    warpByVector1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
    warpByVector1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    warpByVector1Display.PolarAxes.EnableDistanceLOD = 1
    warpByVector1Display.PolarAxes.DistanceLODThreshold = 0.7
    warpByVector1Display.PolarAxes.EnableViewAngleLOD = 1
    warpByVector1Display.PolarAxes.ViewAngleLODThreshold = 0.7
    warpByVector1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
    warpByVector1Display.PolarAxes.PolarTicksVisibility = 1
    warpByVector1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
    warpByVector1Display.PolarAxes.TickLocation = 'Both'
    warpByVector1Display.PolarAxes.AxisTickVisibility = 1
    warpByVector1Display.PolarAxes.AxisMinorTickVisibility = 0
    warpByVector1Display.PolarAxes.AxisTickMatchesPolarAxes = 1
    warpByVector1Display.PolarAxes.DeltaRangeMajor = 1.0
    warpByVector1Display.PolarAxes.DeltaRangeMinor = 0.5
    warpByVector1Display.PolarAxes.ArcTickVisibility = 1
    warpByVector1Display.PolarAxes.ArcMinorTickVisibility = 0
    warpByVector1Display.PolarAxes.ArcTickMatchesRadialAxes = 1
    warpByVector1Display.PolarAxes.DeltaAngleMajor = 10.0
    warpByVector1Display.PolarAxes.DeltaAngleMinor = 5.0
    warpByVector1Display.PolarAxes.TickRatioRadiusSize = 0.02
    warpByVector1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
    warpByVector1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
    warpByVector1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
    warpByVector1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
    warpByVector1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    warpByVector1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    warpByVector1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    warpByVector1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    warpByVector1Display.PolarAxes.ArcMajorTickSize = 0.0
    warpByVector1Display.PolarAxes.ArcTickRatioSize = 0.3
    warpByVector1Display.PolarAxes.ArcMajorTickThickness = 1.0
    warpByVector1Display.PolarAxes.ArcTickRatioThickness = 0.5
    warpByVector1Display.PolarAxes.Use2DMode = 0
    warpByVector1Display.PolarAxes.UseLogAxis = 0

    # hide data in view
    Hide(appendAttributes1, renderView1)

    # set scalar coloring
    ColorBy(warpByVector1Display, ('CELLS', 'Activation'))

    # rescale color and/or opacity maps used to exactly fit the current data range
    warpByVector1Display.RescaleTransferFunctionToDataRange(False, True)

    # rescale color and/or opacity maps used to include current data range
    warpByVector1Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    warpByVector1Display.SetScalarBarVisibility(renderView1, True)

    # Rescale transfer function
    activationLUT.RescaleTransferFunction(0.0, 196.83546447753906)

    # Rescale transfer function
    activationPWF.RescaleTransferFunction(0.0, 196.83546447753906)

    renderView1.ResetActiveCameraToNegativeY()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    renderView1.ResetActiveCameraToNegativeZ()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    renderView1.ResetActiveCameraToPositiveX()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    renderView1.ResetActiveCameraToNegativeX()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    # change representation type
    warpByVector1Display.SetRepresentationType('Surface With Edges')
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588

    # Properties modified on renderView1
    renderView1.UseColorPaletteForBackground = 0
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588

    # Properties modified on renderView1
    renderView1.Background = [1.0, 1.0, 1.0]
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588

    # Properties modified on renderView1
    renderView1.OrientationAxesVisibility = 0
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588

    # Rescale transfer function
    activationLUT.RescaleTransferFunction(-0.004698578733950853, 242.50637817382812)

    # Rescale transfer function
    activationPWF.RescaleTransferFunction(-0.004698578733950853, 242.50637817382812)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588

    # get color legend/bar for activationLUT in view renderView1
    activationLUTColorBar = GetScalarBar(activationLUT, renderView1)
    activationLUTColorBar.AutoOrient = 1
    activationLUTColorBar.Orientation = 'Vertical'
    activationLUTColorBar.WindowLocation = 'Any Location'
    activationLUTColorBar.Position = [0.89, 0.02]
    activationLUTColorBar.Title = 'Activation'
    activationLUTColorBar.ComponentTitle = ''
    activationLUTColorBar.TitleJustification = 'Centered'
    activationLUTColorBar.HorizontalTitle = 0
    activationLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    activationLUTColorBar.TitleOpacity = 1.0
    activationLUTColorBar.TitleFontFamily = 'Arial'
    activationLUTColorBar.TitleFontFile = ''
    activationLUTColorBar.TitleBold = 0
    activationLUTColorBar.TitleItalic = 0
    activationLUTColorBar.TitleShadow = 0
    activationLUTColorBar.TitleFontSize = 16
    activationLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
    activationLUTColorBar.LabelOpacity = 1.0
    activationLUTColorBar.LabelFontFamily = 'Arial'
    activationLUTColorBar.LabelFontFile = ''
    activationLUTColorBar.LabelBold = 0
    activationLUTColorBar.LabelItalic = 0
    activationLUTColorBar.LabelShadow = 0
    activationLUTColorBar.LabelFontSize = 16
    activationLUTColorBar.ScalarBarThickness = 16
    activationLUTColorBar.ScalarBarLength = 0.32999999999999996
    activationLUTColorBar.DrawBackground = 0
    activationLUTColorBar.BackgroundColor = [1.0, 1.0, 1.0, 0.5]
    activationLUTColorBar.BackgroundPadding = 2.0
    activationLUTColorBar.DrawScalarBarOutline = 0
    activationLUTColorBar.ScalarBarOutlineColor = [1.0, 1.0, 1.0]
    activationLUTColorBar.ScalarBarOutlineThickness = 1
    activationLUTColorBar.AutomaticLabelFormat = 1
    activationLUTColorBar.LabelFormat = '%-#6.3g'
    activationLUTColorBar.DrawTickMarks = 1
    activationLUTColorBar.DrawTickLabels = 1
    activationLUTColorBar.UseCustomLabels = 0
    activationLUTColorBar.CustomLabels = []
    activationLUTColorBar.AddRangeLabels = 1
    activationLUTColorBar.RangeLabelFormat = '%-#6.1e'
    activationLUTColorBar.DrawDataRange = 0
    activationLUTColorBar.DataRangeLabelFormat = '%-#6.1e'
    activationLUTColorBar.DrawAnnotations = 1
    activationLUTColorBar.AddRangeAnnotations = 0
    activationLUTColorBar.AutomaticAnnotations = 0
    activationLUTColorBar.DrawNanAnnotation = 0
    activationLUTColorBar.NanAnnotation = 'NaN'
    activationLUTColorBar.TextPosition = 'Ticks right/top, annotations left/bottom'
    activationLUTColorBar.ReverseLegend = 0
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588

    # change scalar bar placement
    activationLUTColorBar.Position = [0.6387037677151746, 0.6227253668763103]
    activationLUTColorBar.ScalarBarLength = 0.32999999999999996
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588

    # create a new 'Clip'
    clip1 = Clip(registrationName='Clip1', Input=warpByVector1)
    clip1.ClipType = 'Plane'
    clip1.HyperTreeGridClipper = 'Plane'
    clip1.Scalars = ['CELLS', 'Activation']
    clip1.Value = 0.0
    clip1.Invert = 1
    clip1.Crinkleclip = 0
    clip1.Exact = 0

    # init the 'Plane' selected for 'ClipType'
    clip1.ClipType.Origin = [-1.6522657871246338, 0.00021028518676757812, -0.0002200603485107422]
    clip1.ClipType.Normal = [1.0, 0.0, 0.0]
    clip1.ClipType.Offset = 0.0

    # init the 'Plane' selected for 'HyperTreeGridClipper'
    clip1.HyperTreeGridClipper.Origin = [-1.6522657871246338, 0.00021028518676757812, -0.0002200603485107422]
    clip1.HyperTreeGridClipper.Normal = [1.0, 0.0, 0.0]
    clip1.HyperTreeGridClipper.Offset = 0.0
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588

    # toggle interactive widget visibility (only when running from the GUI)
    HideInteractiveWidgets(proxy=clip1.ClipType)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588

    # Properties modified on clip1.ClipType
    clip1.ClipType.Origin = [clip_origin, 0.00021028518676757812, -0.0002200603485107422]

    # show data in view
    clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    clip1Display.Selection = None
    clip1Display.Representation = 'Surface'
    clip1Display.ColorArrayName = ['CELLS', 'Activation']
    clip1Display.LookupTable = activationLUT
    clip1Display.MapScalars = 1
    clip1Display.MultiComponentsMapping = 0
    clip1Display.InterpolateScalarsBeforeMapping = 1
    clip1Display.UseNanColorForMissingArrays = 0
    clip1Display.Opacity = 1.0
    clip1Display.PointSize = 2.0
    clip1Display.LineWidth = 1.0
    clip1Display.RenderLinesAsTubes = 0
    clip1Display.RenderPointsAsSpheres = 0
    clip1Display.Interpolation = 'Gouraud'
    clip1Display.Specular = 0.0
    clip1Display.SpecularColor = [1.0, 1.0, 1.0]
    clip1Display.SpecularPower = 100.0
    clip1Display.Luminosity = 0.0
    clip1Display.Ambient = 0.0
    clip1Display.Diffuse = 1.0
    clip1Display.Roughness = 0.3
    clip1Display.Metallic = 0.0
    clip1Display.EdgeTint = [1.0, 1.0, 1.0]
    clip1Display.Anisotropy = 0.0
    clip1Display.AnisotropyRotation = 0.0
    clip1Display.BaseIOR = 1.5
    clip1Display.CoatStrength = 0.0
    clip1Display.CoatIOR = 2.0
    clip1Display.CoatRoughness = 0.0
    clip1Display.CoatColor = [1.0, 1.0, 1.0]
    clip1Display.SelectTCoordArray = 'None'
    clip1Display.SelectNormalArray = 'None'
    clip1Display.SelectTangentArray = 'None'
    clip1Display.Texture = None
    clip1Display.RepeatTextures = 1
    clip1Display.InterpolateTextures = 0
    clip1Display.SeamlessU = 0
    clip1Display.SeamlessV = 0
    clip1Display.UseMipmapTextures = 0
    clip1Display.ShowTexturesOnBackface = 1
    clip1Display.BaseColorTexture = None
    clip1Display.NormalTexture = None
    clip1Display.NormalScale = 1.0
    clip1Display.CoatNormalTexture = None
    clip1Display.CoatNormalScale = 1.0
    clip1Display.MaterialTexture = None
    clip1Display.OcclusionStrength = 1.0
    clip1Display.AnisotropyTexture = None
    clip1Display.EmissiveTexture = None
    clip1Display.EmissiveFactor = [1.0, 1.0, 1.0]
    clip1Display.FlipTextures = 0
    clip1Display.EdgeOpacity = 1.0
    clip1Display.BackfaceRepresentation = 'Follow Frontface'
    clip1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    clip1Display.BackfaceOpacity = 1.0
    clip1Display.Position = [0.0, 0.0, 0.0]
    clip1Display.Scale = [1.0, 1.0, 1.0]
    clip1Display.Orientation = [0.0, 0.0, 0.0]
    clip1Display.Origin = [0.0, 0.0, 0.0]
    clip1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    clip1Display.Pickable = 1
    clip1Display.Triangulate = 0
    clip1Display.UseShaderReplacements = 0
    clip1Display.ShaderReplacements = ''
    clip1Display.NonlinearSubdivisionLevel = 1
    clip1Display.MatchBoundariesIgnoringCellOrder = 0
    clip1Display.UseDataPartitions = 0
    clip1Display.OSPRayUseScaleArray = 'All Approximate'
    clip1Display.OSPRayScaleArray = 'Displacement'
    clip1Display.OSPRayScaleFunction = 'Piecewise Function'
    clip1Display.OSPRayMaterial = 'None'
    clip1Display.Assembly = ''
    clip1Display.BlockSelectors = ['/']
    clip1Display.BlockColors = []
    clip1Display.BlockOpacities = []
    clip1Display.Orient = 0
    clip1Display.OrientationMode = 'Direction'
    clip1Display.SelectOrientationVectors = 'Displacement'
    clip1Display.Scaling = 0
    clip1Display.ScaleMode = 'No Data Scaling Off'
    clip1Display.ScaleFactor = 0.7941803932189941
    clip1Display.SelectScaleArray = 'Displacement'
    clip1Display.GlyphType = 'Arrow'
    clip1Display.UseGlyphTable = 0
    clip1Display.GlyphTableIndexArray = 'Displacement'
    clip1Display.UseCompositeGlyphTable = 0
    clip1Display.UseGlyphCullingAndLOD = 0
    clip1Display.LODValues = []
    clip1Display.ColorByLODIndex = 0
    clip1Display.GaussianRadius = 0.03970901966094971
    clip1Display.ShaderPreset = 'Sphere'
    clip1Display.CustomTriangleScale = 3
    clip1Display.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
    float gaussian = exp(-0.5*dist2);
    opacity = opacity*gaussian;
    """
    clip1Display.Emissive = 0
    clip1Display.ScaleByArray = 0
    clip1Display.SetScaleArray = ['POINTS', 'Displacement']
    clip1Display.ScaleArrayComponent = 'X'
    clip1Display.UseScaleFunction = 1
    clip1Display.ScaleTransferFunction = 'Piecewise Function'
    clip1Display.OpacityByArray = 0
    clip1Display.OpacityArray = ['POINTS', 'Displacement']
    clip1Display.OpacityArrayComponent = 'X'
    clip1Display.OpacityTransferFunction = 'Piecewise Function'
    clip1Display.DataAxesGrid = 'Grid Axes Representation'
    clip1Display.SelectionCellLabelBold = 0
    clip1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    clip1Display.SelectionCellLabelFontFamily = 'Arial'
    clip1Display.SelectionCellLabelFontFile = ''
    clip1Display.SelectionCellLabelFontSize = 18
    clip1Display.SelectionCellLabelItalic = 0
    clip1Display.SelectionCellLabelJustification = 'Left'
    clip1Display.SelectionCellLabelOpacity = 1.0
    clip1Display.SelectionCellLabelShadow = 0
    clip1Display.SelectionPointLabelBold = 0
    clip1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    clip1Display.SelectionPointLabelFontFamily = 'Arial'
    clip1Display.SelectionPointLabelFontFile = ''
    clip1Display.SelectionPointLabelFontSize = 18
    clip1Display.SelectionPointLabelItalic = 0
    clip1Display.SelectionPointLabelJustification = 'Left'
    clip1Display.SelectionPointLabelOpacity = 1.0
    clip1Display.SelectionPointLabelShadow = 0
    clip1Display.PolarAxes = 'Polar Axes Representation'
    clip1Display.ScalarOpacityFunction = activationPWF
    clip1Display.ScalarOpacityUnitDistance = 0.5317323227970959
    clip1Display.UseSeparateOpacityArray = 0
    clip1Display.OpacityArrayName = ['POINTS', 'Displacement']
    clip1Display.OpacityComponent = 'X'
    clip1Display.SelectMapper = 'Projected tetra'
    clip1Display.SamplingDimensions = [128, 128, 128]
    clip1Display.UseFloatingPointFrameBuffer = 1
    clip1Display.SelectInputVectors = ['POINTS', 'Displacement']
    clip1Display.NumberOfSteps = 40
    clip1Display.StepSize = 0.25
    clip1Display.NormalizeVectors = 1
    clip1Display.EnhancedLIC = 1
    clip1Display.ColorMode = 'Blend'
    clip1Display.LICIntensity = 0.8
    clip1Display.MapModeBias = 0.0
    clip1Display.EnhanceContrast = 'Off'
    clip1Display.LowLICContrastEnhancementFactor = 0.0
    clip1Display.HighLICContrastEnhancementFactor = 0.0
    clip1Display.LowColorContrastEnhancementFactor = 0.0
    clip1Display.HighColorContrastEnhancementFactor = 0.0
    clip1Display.AntiAlias = 0
    clip1Display.MaskOnSurface = 1
    clip1Display.MaskThreshold = 0.0
    clip1Display.MaskIntensity = 0.0
    clip1Display.MaskColor = [0.5, 0.5, 0.5]
    clip1Display.GenerateNoiseTexture = 0
    clip1Display.NoiseType = 'Gaussian'
    clip1Display.NoiseTextureSize = 128
    clip1Display.NoiseGrainSize = 2
    clip1Display.MinNoiseValue = 0.0
    clip1Display.MaxNoiseValue = 0.8
    clip1Display.NumberOfNoiseLevels = 1024
    clip1Display.ImpulseNoiseProbability = 1.0
    clip1Display.ImpulseNoiseBackgroundValue = 0.0
    clip1Display.NoiseGeneratorSeed = 1
    clip1Display.CompositeStrategy = 'AUTO'
    clip1Display.UseLICForLOD = 0
    clip1Display.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    clip1Display.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]
    clip1Display.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    clip1Display.GlyphType.TipResolution = 6
    clip1Display.GlyphType.TipRadius = 0.1
    clip1Display.GlyphType.TipLength = 0.35
    clip1Display.GlyphType.ShaftResolution = 6
    clip1Display.GlyphType.ShaftRadius = 0.03
    clip1Display.GlyphType.Invert = 0

    # init the 'Piecewise Function' selected for 'ScaleTransferFunction'
    clip1Display.ScaleTransferFunction.Points = [-0.28369444608688354, 0.0, 0.5, 0.0, -0.1369963138351956, 1.0, 0.5, 0.0]
    clip1Display.ScaleTransferFunction.UseLogScale = 0

    # init the 'Piecewise Function' selected for 'OpacityTransferFunction'
    clip1Display.OpacityTransferFunction.Points = [-0.28369444608688354, 0.0, 0.5, 0.0, -0.1369963138351956, 1.0, 0.5, 0.0]
    clip1Display.OpacityTransferFunction.UseLogScale = 0

    # init the 'Grid Axes Representation' selected for 'DataAxesGrid'
    clip1Display.DataAxesGrid.XTitle = 'X Axis'
    clip1Display.DataAxesGrid.YTitle = 'Y Axis'
    clip1Display.DataAxesGrid.ZTitle = 'Z Axis'
    clip1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
    clip1Display.DataAxesGrid.XTitleFontFile = ''
    clip1Display.DataAxesGrid.XTitleBold = 0
    clip1Display.DataAxesGrid.XTitleItalic = 0
    clip1Display.DataAxesGrid.XTitleFontSize = 12
    clip1Display.DataAxesGrid.XTitleShadow = 0
    clip1Display.DataAxesGrid.XTitleOpacity = 1.0
    clip1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
    clip1Display.DataAxesGrid.YTitleFontFile = ''
    clip1Display.DataAxesGrid.YTitleBold = 0
    clip1Display.DataAxesGrid.YTitleItalic = 0
    clip1Display.DataAxesGrid.YTitleFontSize = 12
    clip1Display.DataAxesGrid.YTitleShadow = 0
    clip1Display.DataAxesGrid.YTitleOpacity = 1.0
    clip1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
    clip1Display.DataAxesGrid.ZTitleFontFile = ''
    clip1Display.DataAxesGrid.ZTitleBold = 0
    clip1Display.DataAxesGrid.ZTitleItalic = 0
    clip1Display.DataAxesGrid.ZTitleFontSize = 12
    clip1Display.DataAxesGrid.ZTitleShadow = 0
    clip1Display.DataAxesGrid.ZTitleOpacity = 1.0
    clip1Display.DataAxesGrid.FacesToRender = 63
    clip1Display.DataAxesGrid.CullBackface = 0
    clip1Display.DataAxesGrid.CullFrontface = 1
    clip1Display.DataAxesGrid.ShowGrid = 0
    clip1Display.DataAxesGrid.ShowEdges = 1
    clip1Display.DataAxesGrid.ShowTicks = 1
    clip1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
    clip1Display.DataAxesGrid.AxesToLabel = 63
    clip1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
    clip1Display.DataAxesGrid.XLabelFontFile = ''
    clip1Display.DataAxesGrid.XLabelBold = 0
    clip1Display.DataAxesGrid.XLabelItalic = 0
    clip1Display.DataAxesGrid.XLabelFontSize = 12
    clip1Display.DataAxesGrid.XLabelShadow = 0
    clip1Display.DataAxesGrid.XLabelOpacity = 1.0
    clip1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
    clip1Display.DataAxesGrid.YLabelFontFile = ''
    clip1Display.DataAxesGrid.YLabelBold = 0
    clip1Display.DataAxesGrid.YLabelItalic = 0
    clip1Display.DataAxesGrid.YLabelFontSize = 12
    clip1Display.DataAxesGrid.YLabelShadow = 0
    clip1Display.DataAxesGrid.YLabelOpacity = 1.0
    clip1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
    clip1Display.DataAxesGrid.ZLabelFontFile = ''
    clip1Display.DataAxesGrid.ZLabelBold = 0
    clip1Display.DataAxesGrid.ZLabelItalic = 0
    clip1Display.DataAxesGrid.ZLabelFontSize = 12
    clip1Display.DataAxesGrid.ZLabelShadow = 0
    clip1Display.DataAxesGrid.ZLabelOpacity = 1.0
    clip1Display.DataAxesGrid.XAxisNotation = 'Mixed'
    clip1Display.DataAxesGrid.XAxisPrecision = 2
    clip1Display.DataAxesGrid.XAxisUseCustomLabels = 0
    clip1Display.DataAxesGrid.XAxisLabels = []
    clip1Display.DataAxesGrid.YAxisNotation = 'Mixed'
    clip1Display.DataAxesGrid.YAxisPrecision = 2
    clip1Display.DataAxesGrid.YAxisUseCustomLabels = 0
    clip1Display.DataAxesGrid.YAxisLabels = []
    clip1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
    clip1Display.DataAxesGrid.ZAxisPrecision = 2
    clip1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
    clip1Display.DataAxesGrid.ZAxisLabels = []
    clip1Display.DataAxesGrid.UseCustomBounds = 0
    clip1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'Polar Axes Representation' selected for 'PolarAxes'
    clip1Display.PolarAxes.Visibility = 0
    clip1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
    clip1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
    clip1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    clip1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
    clip1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    clip1Display.PolarAxes.EnableCustomRange = 0
    clip1Display.PolarAxes.CustomRange = [0.0, 1.0]
    clip1Display.PolarAxes.AutoPole = 1
    clip1Display.PolarAxes.PolarAxisVisibility = 1
    clip1Display.PolarAxes.RadialAxesVisibility = 1
    clip1Display.PolarAxes.DrawRadialGridlines = 1
    clip1Display.PolarAxes.PolarArcsVisibility = 1
    clip1Display.PolarAxes.DrawPolarArcsGridlines = 1
    clip1Display.PolarAxes.NumberOfRadialAxes = 0
    clip1Display.PolarAxes.DeltaAngleRadialAxes = 45.0
    clip1Display.PolarAxes.NumberOfPolarAxes = 5
    clip1Display.PolarAxes.DeltaRangePolarAxes = 0.0
    clip1Display.PolarAxes.CustomMinRadius = 1
    clip1Display.PolarAxes.MinimumRadius = 0.0
    clip1Display.PolarAxes.CustomAngles = 1
    clip1Display.PolarAxes.MinimumAngle = 0.0
    clip1Display.PolarAxes.MaximumAngle = 90.0
    clip1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
    clip1Display.PolarAxes.PolarArcResolutionPerDegree = 0.2
    clip1Display.PolarAxes.Ratio = 1.0
    clip1Display.PolarAxes.EnableOverallColor = 1
    clip1Display.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
    clip1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    clip1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    clip1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    clip1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    clip1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    clip1Display.PolarAxes.PolarAxisTitleVisibility = 1
    clip1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
    clip1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    clip1Display.PolarAxes.PolarTitleOffset = [20.0, 20.0]
    clip1Display.PolarAxes.PolarLabelVisibility = 1
    clip1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
    clip1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
    clip1Display.PolarAxes.PolarLabelOffset = 10.0
    clip1Display.PolarAxes.PolarExponentOffset = 5.0
    clip1Display.PolarAxes.RadialTitleVisibility = 1
    clip1Display.PolarAxes.RadialTitleFormat = '%-#3.1f'
    clip1Display.PolarAxes.RadialTitleLocation = 'Bottom'
    clip1Display.PolarAxes.RadialTitleOffset = [20.0, 0.0]
    clip1Display.PolarAxes.RadialUnitsVisibility = 1
    clip1Display.PolarAxes.ScreenSize = 10.0
    clip1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
    clip1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
    clip1Display.PolarAxes.PolarAxisTitleBold = 0
    clip1Display.PolarAxes.PolarAxisTitleItalic = 0
    clip1Display.PolarAxes.PolarAxisTitleShadow = 0
    clip1Display.PolarAxes.PolarAxisTitleFontSize = 12
    clip1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
    clip1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
    clip1Display.PolarAxes.PolarAxisLabelBold = 0
    clip1Display.PolarAxes.PolarAxisLabelItalic = 0
    clip1Display.PolarAxes.PolarAxisLabelShadow = 0
    clip1Display.PolarAxes.PolarAxisLabelFontSize = 12
    clip1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
    clip1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
    clip1Display.PolarAxes.LastRadialAxisTextBold = 0
    clip1Display.PolarAxes.LastRadialAxisTextItalic = 0
    clip1Display.PolarAxes.LastRadialAxisTextShadow = 0
    clip1Display.PolarAxes.LastRadialAxisTextFontSize = 12
    clip1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    clip1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    clip1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
    clip1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
    clip1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
    clip1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    clip1Display.PolarAxes.EnableDistanceLOD = 1
    clip1Display.PolarAxes.DistanceLODThreshold = 0.7
    clip1Display.PolarAxes.EnableViewAngleLOD = 1
    clip1Display.PolarAxes.ViewAngleLODThreshold = 0.7
    clip1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
    clip1Display.PolarAxes.PolarTicksVisibility = 1
    clip1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
    clip1Display.PolarAxes.TickLocation = 'Both'
    clip1Display.PolarAxes.AxisTickVisibility = 1
    clip1Display.PolarAxes.AxisMinorTickVisibility = 0
    clip1Display.PolarAxes.AxisTickMatchesPolarAxes = 1
    clip1Display.PolarAxes.DeltaRangeMajor = 1.0
    clip1Display.PolarAxes.DeltaRangeMinor = 0.5
    clip1Display.PolarAxes.ArcTickVisibility = 1
    clip1Display.PolarAxes.ArcMinorTickVisibility = 0
    clip1Display.PolarAxes.ArcTickMatchesRadialAxes = 1
    clip1Display.PolarAxes.DeltaAngleMajor = 10.0
    clip1Display.PolarAxes.DeltaAngleMinor = 5.0
    clip1Display.PolarAxes.TickRatioRadiusSize = 0.02
    clip1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
    clip1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
    clip1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
    clip1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
    clip1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    clip1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    clip1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    clip1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    clip1Display.PolarAxes.ArcMajorTickSize = 0.0
    clip1Display.PolarAxes.ArcTickRatioSize = 0.3
    clip1Display.PolarAxes.ArcMajorTickThickness = 1.0
    clip1Display.PolarAxes.ArcTickRatioThickness = 0.5
    clip1Display.PolarAxes.Use2DMode = 0
    clip1Display.PolarAxes.UseLogAxis = 0

    # hide data in view
    Hide(warpByVector1, renderView1)

    # show color bar/color legend
    clip1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [13.609066213065542, -0.4531025349827244, -21.12491736285597]
    renderView1.CameraFocalPoint = [-1.8397653102874754, -0.0002174377441406233, 0.00017523765563968354]
    renderView1.CameraViewUp = [0.8071906614968228, 0.00046011853910021307, 0.5902906269654395]
    renderView1.CameraParallelScale = 6.774639986020588

    renderView1.ResetActiveCameraToNegativeX()

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976

    # create a new 'Cell Data to Point Data'
    cellDatatoPointData1 = CellDatatoPointData(registrationName='CellDatatoPointData1', Input=clip1)
    cellDatatoPointData1.ProcessAllArrays = 1
    cellDatatoPointData1.CellDataArraytoprocess = ['Activation']
    cellDatatoPointData1.PassCellData = 0
    cellDatatoPointData1.PieceInvariant = 0
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976

    # show data in view
    cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    cellDatatoPointData1Display.Selection = None
    cellDatatoPointData1Display.Representation = 'Surface'
    cellDatatoPointData1Display.ColorArrayName = [None, '']
    cellDatatoPointData1Display.LookupTable = None
    cellDatatoPointData1Display.MapScalars = 1
    cellDatatoPointData1Display.MultiComponentsMapping = 0
    cellDatatoPointData1Display.InterpolateScalarsBeforeMapping = 1
    cellDatatoPointData1Display.UseNanColorForMissingArrays = 0
    cellDatatoPointData1Display.Opacity = 1.0
    cellDatatoPointData1Display.PointSize = 2.0
    cellDatatoPointData1Display.LineWidth = 1.0
    cellDatatoPointData1Display.RenderLinesAsTubes = 0
    cellDatatoPointData1Display.RenderPointsAsSpheres = 0
    cellDatatoPointData1Display.Interpolation = 'Gouraud'
    cellDatatoPointData1Display.Specular = 0.0
    cellDatatoPointData1Display.SpecularColor = [1.0, 1.0, 1.0]
    cellDatatoPointData1Display.SpecularPower = 100.0
    cellDatatoPointData1Display.Luminosity = 0.0
    cellDatatoPointData1Display.Ambient = 0.0
    cellDatatoPointData1Display.Diffuse = 1.0
    cellDatatoPointData1Display.Roughness = 0.3
    cellDatatoPointData1Display.Metallic = 0.0
    cellDatatoPointData1Display.EdgeTint = [1.0, 1.0, 1.0]
    cellDatatoPointData1Display.Anisotropy = 0.0
    cellDatatoPointData1Display.AnisotropyRotation = 0.0
    cellDatatoPointData1Display.BaseIOR = 1.5
    cellDatatoPointData1Display.CoatStrength = 0.0
    cellDatatoPointData1Display.CoatIOR = 2.0
    cellDatatoPointData1Display.CoatRoughness = 0.0
    cellDatatoPointData1Display.CoatColor = [1.0, 1.0, 1.0]
    cellDatatoPointData1Display.SelectTCoordArray = 'None'
    cellDatatoPointData1Display.SelectNormalArray = 'None'
    cellDatatoPointData1Display.SelectTangentArray = 'None'
    cellDatatoPointData1Display.Texture = None
    cellDatatoPointData1Display.RepeatTextures = 1
    cellDatatoPointData1Display.InterpolateTextures = 0
    cellDatatoPointData1Display.SeamlessU = 0
    cellDatatoPointData1Display.SeamlessV = 0
    cellDatatoPointData1Display.UseMipmapTextures = 0
    cellDatatoPointData1Display.ShowTexturesOnBackface = 1
    cellDatatoPointData1Display.BaseColorTexture = None
    cellDatatoPointData1Display.NormalTexture = None
    cellDatatoPointData1Display.NormalScale = 1.0
    cellDatatoPointData1Display.CoatNormalTexture = None
    cellDatatoPointData1Display.CoatNormalScale = 1.0
    cellDatatoPointData1Display.MaterialTexture = None
    cellDatatoPointData1Display.OcclusionStrength = 1.0
    cellDatatoPointData1Display.AnisotropyTexture = None
    cellDatatoPointData1Display.EmissiveTexture = None
    cellDatatoPointData1Display.EmissiveFactor = [1.0, 1.0, 1.0]
    cellDatatoPointData1Display.FlipTextures = 0
    cellDatatoPointData1Display.EdgeOpacity = 1.0
    cellDatatoPointData1Display.BackfaceRepresentation = 'Follow Frontface'
    cellDatatoPointData1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    cellDatatoPointData1Display.BackfaceOpacity = 1.0
    cellDatatoPointData1Display.Position = [0.0, 0.0, 0.0]
    cellDatatoPointData1Display.Scale = [1.0, 1.0, 1.0]
    cellDatatoPointData1Display.Orientation = [0.0, 0.0, 0.0]
    cellDatatoPointData1Display.Origin = [0.0, 0.0, 0.0]
    cellDatatoPointData1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
    cellDatatoPointData1Display.Pickable = 1
    cellDatatoPointData1Display.Triangulate = 0
    cellDatatoPointData1Display.UseShaderReplacements = 0
    cellDatatoPointData1Display.ShaderReplacements = ''
    cellDatatoPointData1Display.NonlinearSubdivisionLevel = 1
    cellDatatoPointData1Display.MatchBoundariesIgnoringCellOrder = 0
    cellDatatoPointData1Display.UseDataPartitions = 0
    cellDatatoPointData1Display.OSPRayUseScaleArray = 'All Approximate'
    cellDatatoPointData1Display.OSPRayScaleArray = 'Activation'
    cellDatatoPointData1Display.OSPRayScaleFunction = 'Piecewise Function'
    cellDatatoPointData1Display.OSPRayMaterial = 'None'
    cellDatatoPointData1Display.Assembly = ''
    cellDatatoPointData1Display.BlockSelectors = ['/']
    cellDatatoPointData1Display.BlockColors = []
    cellDatatoPointData1Display.BlockOpacities = []
    cellDatatoPointData1Display.Orient = 0
    cellDatatoPointData1Display.OrientationMode = 'Direction'
    cellDatatoPointData1Display.SelectOrientationVectors = 'Displacement'
    cellDatatoPointData1Display.Scaling = 0
    cellDatatoPointData1Display.ScaleMode = 'No Data Scaling Off'
    cellDatatoPointData1Display.ScaleFactor = 0.7941803932189941
    cellDatatoPointData1Display.SelectScaleArray = 'Activation'
    cellDatatoPointData1Display.GlyphType = 'Arrow'
    cellDatatoPointData1Display.UseGlyphTable = 0
    cellDatatoPointData1Display.GlyphTableIndexArray = 'Activation'
    cellDatatoPointData1Display.UseCompositeGlyphTable = 0
    cellDatatoPointData1Display.UseGlyphCullingAndLOD = 0
    cellDatatoPointData1Display.LODValues = []
    cellDatatoPointData1Display.ColorByLODIndex = 0
    cellDatatoPointData1Display.GaussianRadius = 0.03970901966094971
    cellDatatoPointData1Display.ShaderPreset = 'Sphere'
    cellDatatoPointData1Display.CustomTriangleScale = 3
    cellDatatoPointData1Display.CustomShader = """ // This custom shader code define a gaussian blur
    // Please take a look into vtkSMPointGaussianRepresentation.cxx
    // for other custom shader examples
    //VTK::Color::Impl
    float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
    float gaussian = exp(-0.5*dist2);
    opacity = opacity*gaussian;
    """
    cellDatatoPointData1Display.Emissive = 0
    cellDatatoPointData1Display.ScaleByArray = 0
    cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'Activation']
    cellDatatoPointData1Display.ScaleArrayComponent = ''
    cellDatatoPointData1Display.UseScaleFunction = 1
    cellDatatoPointData1Display.ScaleTransferFunction = 'Piecewise Function'
    cellDatatoPointData1Display.OpacityByArray = 0
    cellDatatoPointData1Display.OpacityArray = ['POINTS', 'Activation']
    cellDatatoPointData1Display.OpacityArrayComponent = ''
    cellDatatoPointData1Display.OpacityTransferFunction = 'Piecewise Function'
    cellDatatoPointData1Display.DataAxesGrid = 'Grid Axes Representation'
    cellDatatoPointData1Display.SelectionCellLabelBold = 0
    cellDatatoPointData1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    cellDatatoPointData1Display.SelectionCellLabelFontFamily = 'Arial'
    cellDatatoPointData1Display.SelectionCellLabelFontFile = ''
    cellDatatoPointData1Display.SelectionCellLabelFontSize = 18
    cellDatatoPointData1Display.SelectionCellLabelItalic = 0
    cellDatatoPointData1Display.SelectionCellLabelJustification = 'Left'
    cellDatatoPointData1Display.SelectionCellLabelOpacity = 1.0
    cellDatatoPointData1Display.SelectionCellLabelShadow = 0
    cellDatatoPointData1Display.SelectionPointLabelBold = 0
    cellDatatoPointData1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    cellDatatoPointData1Display.SelectionPointLabelFontFamily = 'Arial'
    cellDatatoPointData1Display.SelectionPointLabelFontFile = ''
    cellDatatoPointData1Display.SelectionPointLabelFontSize = 18
    cellDatatoPointData1Display.SelectionPointLabelItalic = 0
    cellDatatoPointData1Display.SelectionPointLabelJustification = 'Left'
    cellDatatoPointData1Display.SelectionPointLabelOpacity = 1.0
    cellDatatoPointData1Display.SelectionPointLabelShadow = 0
    cellDatatoPointData1Display.PolarAxes = 'Polar Axes Representation'
    cellDatatoPointData1Display.ScalarOpacityFunction = None
    cellDatatoPointData1Display.ScalarOpacityUnitDistance = 0.5317323227970959
    cellDatatoPointData1Display.UseSeparateOpacityArray = 0
    cellDatatoPointData1Display.OpacityArrayName = ['POINTS', 'Activation']
    cellDatatoPointData1Display.OpacityComponent = ''
    cellDatatoPointData1Display.SelectMapper = 'Projected tetra'
    cellDatatoPointData1Display.SamplingDimensions = [128, 128, 128]
    cellDatatoPointData1Display.UseFloatingPointFrameBuffer = 1
    cellDatatoPointData1Display.SelectInputVectors = ['POINTS', 'Displacement']
    cellDatatoPointData1Display.NumberOfSteps = 40
    cellDatatoPointData1Display.StepSize = 0.25
    cellDatatoPointData1Display.NormalizeVectors = 1
    cellDatatoPointData1Display.EnhancedLIC = 1
    cellDatatoPointData1Display.ColorMode = 'Blend'
    cellDatatoPointData1Display.LICIntensity = 0.8
    cellDatatoPointData1Display.MapModeBias = 0.0
    cellDatatoPointData1Display.EnhanceContrast = 'Off'
    cellDatatoPointData1Display.LowLICContrastEnhancementFactor = 0.0
    cellDatatoPointData1Display.HighLICContrastEnhancementFactor = 0.0
    cellDatatoPointData1Display.LowColorContrastEnhancementFactor = 0.0
    cellDatatoPointData1Display.HighColorContrastEnhancementFactor = 0.0
    cellDatatoPointData1Display.AntiAlias = 0
    cellDatatoPointData1Display.MaskOnSurface = 1
    cellDatatoPointData1Display.MaskThreshold = 0.0
    cellDatatoPointData1Display.MaskIntensity = 0.0
    cellDatatoPointData1Display.MaskColor = [0.5, 0.5, 0.5]
    cellDatatoPointData1Display.GenerateNoiseTexture = 0
    cellDatatoPointData1Display.NoiseType = 'Gaussian'
    cellDatatoPointData1Display.NoiseTextureSize = 128
    cellDatatoPointData1Display.NoiseGrainSize = 2
    cellDatatoPointData1Display.MinNoiseValue = 0.0
    cellDatatoPointData1Display.MaxNoiseValue = 0.8
    cellDatatoPointData1Display.NumberOfNoiseLevels = 1024
    cellDatatoPointData1Display.ImpulseNoiseProbability = 1.0
    cellDatatoPointData1Display.ImpulseNoiseBackgroundValue = 0.0
    cellDatatoPointData1Display.NoiseGeneratorSeed = 1
    cellDatatoPointData1Display.CompositeStrategy = 'AUTO'
    cellDatatoPointData1Display.UseLICForLOD = 0
    cellDatatoPointData1Display.WriteLog = ''

    # init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
    cellDatatoPointData1Display.OSPRayScaleFunction.Points = [145.0, 0.0, 0.5, 0.0, 216.0, 1.0, 0.5, 0.0]
    cellDatatoPointData1Display.OSPRayScaleFunction.UseLogScale = 0

    # init the 'Arrow' selected for 'GlyphType'
    cellDatatoPointData1Display.GlyphType.TipResolution = 6
    cellDatatoPointData1Display.GlyphType.TipRadius = 0.1
    cellDatatoPointData1Display.GlyphType.TipLength = 0.35
    cellDatatoPointData1Display.GlyphType.ShaftResolution = 6
    cellDatatoPointData1Display.GlyphType.ShaftRadius = 0.03
    cellDatatoPointData1Display.GlyphType.Invert = 0

    # init the 'Piecewise Function' selected for 'ScaleTransferFunction'
    cellDatatoPointData1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    cellDatatoPointData1Display.ScaleTransferFunction.UseLogScale = 0

    # init the 'Piecewise Function' selected for 'OpacityTransferFunction'
    cellDatatoPointData1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    cellDatatoPointData1Display.OpacityTransferFunction.UseLogScale = 0

    # init the 'Grid Axes Representation' selected for 'DataAxesGrid'
    cellDatatoPointData1Display.DataAxesGrid.XTitle = 'X Axis'
    cellDatatoPointData1Display.DataAxesGrid.YTitle = 'Y Axis'
    cellDatatoPointData1Display.DataAxesGrid.ZTitle = 'Z Axis'
    cellDatatoPointData1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
    cellDatatoPointData1Display.DataAxesGrid.XTitleFontFile = ''
    cellDatatoPointData1Display.DataAxesGrid.XTitleBold = 0
    cellDatatoPointData1Display.DataAxesGrid.XTitleItalic = 0
    cellDatatoPointData1Display.DataAxesGrid.XTitleFontSize = 12
    cellDatatoPointData1Display.DataAxesGrid.XTitleShadow = 0
    cellDatatoPointData1Display.DataAxesGrid.XTitleOpacity = 1.0
    cellDatatoPointData1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
    cellDatatoPointData1Display.DataAxesGrid.YTitleFontFile = ''
    cellDatatoPointData1Display.DataAxesGrid.YTitleBold = 0
    cellDatatoPointData1Display.DataAxesGrid.YTitleItalic = 0
    cellDatatoPointData1Display.DataAxesGrid.YTitleFontSize = 12
    cellDatatoPointData1Display.DataAxesGrid.YTitleShadow = 0
    cellDatatoPointData1Display.DataAxesGrid.YTitleOpacity = 1.0
    cellDatatoPointData1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
    cellDatatoPointData1Display.DataAxesGrid.ZTitleFontFile = ''
    cellDatatoPointData1Display.DataAxesGrid.ZTitleBold = 0
    cellDatatoPointData1Display.DataAxesGrid.ZTitleItalic = 0
    cellDatatoPointData1Display.DataAxesGrid.ZTitleFontSize = 12
    cellDatatoPointData1Display.DataAxesGrid.ZTitleShadow = 0
    cellDatatoPointData1Display.DataAxesGrid.ZTitleOpacity = 1.0
    cellDatatoPointData1Display.DataAxesGrid.FacesToRender = 63
    cellDatatoPointData1Display.DataAxesGrid.CullBackface = 0
    cellDatatoPointData1Display.DataAxesGrid.CullFrontface = 1
    cellDatatoPointData1Display.DataAxesGrid.ShowGrid = 0
    cellDatatoPointData1Display.DataAxesGrid.ShowEdges = 1
    cellDatatoPointData1Display.DataAxesGrid.ShowTicks = 1
    cellDatatoPointData1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
    cellDatatoPointData1Display.DataAxesGrid.AxesToLabel = 63
    cellDatatoPointData1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
    cellDatatoPointData1Display.DataAxesGrid.XLabelFontFile = ''
    cellDatatoPointData1Display.DataAxesGrid.XLabelBold = 0
    cellDatatoPointData1Display.DataAxesGrid.XLabelItalic = 0
    cellDatatoPointData1Display.DataAxesGrid.XLabelFontSize = 12
    cellDatatoPointData1Display.DataAxesGrid.XLabelShadow = 0
    cellDatatoPointData1Display.DataAxesGrid.XLabelOpacity = 1.0
    cellDatatoPointData1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
    cellDatatoPointData1Display.DataAxesGrid.YLabelFontFile = ''
    cellDatatoPointData1Display.DataAxesGrid.YLabelBold = 0
    cellDatatoPointData1Display.DataAxesGrid.YLabelItalic = 0
    cellDatatoPointData1Display.DataAxesGrid.YLabelFontSize = 12
    cellDatatoPointData1Display.DataAxesGrid.YLabelShadow = 0
    cellDatatoPointData1Display.DataAxesGrid.YLabelOpacity = 1.0
    cellDatatoPointData1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
    cellDatatoPointData1Display.DataAxesGrid.ZLabelFontFile = ''
    cellDatatoPointData1Display.DataAxesGrid.ZLabelBold = 0
    cellDatatoPointData1Display.DataAxesGrid.ZLabelItalic = 0
    cellDatatoPointData1Display.DataAxesGrid.ZLabelFontSize = 12
    cellDatatoPointData1Display.DataAxesGrid.ZLabelShadow = 0
    cellDatatoPointData1Display.DataAxesGrid.ZLabelOpacity = 1.0
    cellDatatoPointData1Display.DataAxesGrid.XAxisNotation = 'Mixed'
    cellDatatoPointData1Display.DataAxesGrid.XAxisPrecision = 2
    cellDatatoPointData1Display.DataAxesGrid.XAxisUseCustomLabels = 0
    cellDatatoPointData1Display.DataAxesGrid.XAxisLabels = []
    cellDatatoPointData1Display.DataAxesGrid.YAxisNotation = 'Mixed'
    cellDatatoPointData1Display.DataAxesGrid.YAxisPrecision = 2
    cellDatatoPointData1Display.DataAxesGrid.YAxisUseCustomLabels = 0
    cellDatatoPointData1Display.DataAxesGrid.YAxisLabels = []
    cellDatatoPointData1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
    cellDatatoPointData1Display.DataAxesGrid.ZAxisPrecision = 2
    cellDatatoPointData1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
    cellDatatoPointData1Display.DataAxesGrid.ZAxisLabels = []
    cellDatatoPointData1Display.DataAxesGrid.UseCustomBounds = 0
    cellDatatoPointData1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

    # init the 'Polar Axes Representation' selected for 'PolarAxes'
    cellDatatoPointData1Display.PolarAxes.Visibility = 0
    cellDatatoPointData1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
    cellDatatoPointData1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
    cellDatatoPointData1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    cellDatatoPointData1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
    cellDatatoPointData1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    cellDatatoPointData1Display.PolarAxes.EnableCustomRange = 0
    cellDatatoPointData1Display.PolarAxes.CustomRange = [0.0, 1.0]
    cellDatatoPointData1Display.PolarAxes.AutoPole = 1
    cellDatatoPointData1Display.PolarAxes.PolarAxisVisibility = 1
    cellDatatoPointData1Display.PolarAxes.RadialAxesVisibility = 1
    cellDatatoPointData1Display.PolarAxes.DrawRadialGridlines = 1
    cellDatatoPointData1Display.PolarAxes.PolarArcsVisibility = 1
    cellDatatoPointData1Display.PolarAxes.DrawPolarArcsGridlines = 1
    cellDatatoPointData1Display.PolarAxes.NumberOfRadialAxes = 0
    cellDatatoPointData1Display.PolarAxes.DeltaAngleRadialAxes = 45.0
    cellDatatoPointData1Display.PolarAxes.NumberOfPolarAxes = 5
    cellDatatoPointData1Display.PolarAxes.DeltaRangePolarAxes = 0.0
    cellDatatoPointData1Display.PolarAxes.CustomMinRadius = 1
    cellDatatoPointData1Display.PolarAxes.MinimumRadius = 0.0
    cellDatatoPointData1Display.PolarAxes.CustomAngles = 1
    cellDatatoPointData1Display.PolarAxes.MinimumAngle = 0.0
    cellDatatoPointData1Display.PolarAxes.MaximumAngle = 90.0
    cellDatatoPointData1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
    cellDatatoPointData1Display.PolarAxes.PolarArcResolutionPerDegree = 0.2
    cellDatatoPointData1Display.PolarAxes.Ratio = 1.0
    cellDatatoPointData1Display.PolarAxes.EnableOverallColor = 1
    cellDatatoPointData1Display.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
    cellDatatoPointData1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    cellDatatoPointData1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    cellDatatoPointData1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    cellDatatoPointData1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    cellDatatoPointData1Display.PolarAxes.PolarAxisTitleVisibility = 1
    cellDatatoPointData1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
    cellDatatoPointData1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    cellDatatoPointData1Display.PolarAxes.PolarTitleOffset = [20.0, 20.0]
    cellDatatoPointData1Display.PolarAxes.PolarLabelVisibility = 1
    cellDatatoPointData1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
    cellDatatoPointData1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
    cellDatatoPointData1Display.PolarAxes.PolarLabelOffset = 10.0
    cellDatatoPointData1Display.PolarAxes.PolarExponentOffset = 5.0
    cellDatatoPointData1Display.PolarAxes.RadialTitleVisibility = 1
    cellDatatoPointData1Display.PolarAxes.RadialTitleFormat = '%-#3.1f'
    cellDatatoPointData1Display.PolarAxes.RadialTitleLocation = 'Bottom'
    cellDatatoPointData1Display.PolarAxes.RadialTitleOffset = [20.0, 0.0]
    cellDatatoPointData1Display.PolarAxes.RadialUnitsVisibility = 1
    cellDatatoPointData1Display.PolarAxes.ScreenSize = 10.0
    cellDatatoPointData1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
    cellDatatoPointData1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    cellDatatoPointData1Display.PolarAxes.PolarAxisTitleFontFile = ''
    cellDatatoPointData1Display.PolarAxes.PolarAxisTitleBold = 0
    cellDatatoPointData1Display.PolarAxes.PolarAxisTitleItalic = 0
    cellDatatoPointData1Display.PolarAxes.PolarAxisTitleShadow = 0
    cellDatatoPointData1Display.PolarAxes.PolarAxisTitleFontSize = 12
    cellDatatoPointData1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
    cellDatatoPointData1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    cellDatatoPointData1Display.PolarAxes.PolarAxisLabelFontFile = ''
    cellDatatoPointData1Display.PolarAxes.PolarAxisLabelBold = 0
    cellDatatoPointData1Display.PolarAxes.PolarAxisLabelItalic = 0
    cellDatatoPointData1Display.PolarAxes.PolarAxisLabelShadow = 0
    cellDatatoPointData1Display.PolarAxes.PolarAxisLabelFontSize = 12
    cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
    cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextFontFile = ''
    cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextBold = 0
    cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextItalic = 0
    cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextShadow = 0
    cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextFontSize = 12
    cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
    cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
    cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
    cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
    cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    cellDatatoPointData1Display.PolarAxes.EnableDistanceLOD = 1
    cellDatatoPointData1Display.PolarAxes.DistanceLODThreshold = 0.7
    cellDatatoPointData1Display.PolarAxes.EnableViewAngleLOD = 1
    cellDatatoPointData1Display.PolarAxes.ViewAngleLODThreshold = 0.7
    cellDatatoPointData1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
    cellDatatoPointData1Display.PolarAxes.PolarTicksVisibility = 1
    cellDatatoPointData1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
    cellDatatoPointData1Display.PolarAxes.TickLocation = 'Both'
    cellDatatoPointData1Display.PolarAxes.AxisTickVisibility = 1
    cellDatatoPointData1Display.PolarAxes.AxisMinorTickVisibility = 0
    cellDatatoPointData1Display.PolarAxes.AxisTickMatchesPolarAxes = 1
    cellDatatoPointData1Display.PolarAxes.DeltaRangeMajor = 1.0
    cellDatatoPointData1Display.PolarAxes.DeltaRangeMinor = 0.5
    cellDatatoPointData1Display.PolarAxes.ArcTickVisibility = 1
    cellDatatoPointData1Display.PolarAxes.ArcMinorTickVisibility = 0
    cellDatatoPointData1Display.PolarAxes.ArcTickMatchesRadialAxes = 1
    cellDatatoPointData1Display.PolarAxes.DeltaAngleMajor = 10.0
    cellDatatoPointData1Display.PolarAxes.DeltaAngleMinor = 5.0
    cellDatatoPointData1Display.PolarAxes.TickRatioRadiusSize = 0.02
    cellDatatoPointData1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
    cellDatatoPointData1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
    cellDatatoPointData1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
    cellDatatoPointData1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
    cellDatatoPointData1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    cellDatatoPointData1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    cellDatatoPointData1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    cellDatatoPointData1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    cellDatatoPointData1Display.PolarAxes.ArcMajorTickSize = 0.0
    cellDatatoPointData1Display.PolarAxes.ArcTickRatioSize = 0.3
    cellDatatoPointData1Display.PolarAxes.ArcMajorTickThickness = 1.0
    cellDatatoPointData1Display.PolarAxes.ArcTickRatioThickness = 0.5
    cellDatatoPointData1Display.PolarAxes.Use2DMode = 0
    cellDatatoPointData1Display.PolarAxes.UseLogAxis = 0

    # hide data in view
    Hide(clip1, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976

    # set scalar coloring
    ColorBy(cellDatatoPointData1Display, ('POINTS', 'Activation'))

    # rescale color and/or opacity maps used to include current data range
    cellDatatoPointData1Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, True)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976

    # Rescale transfer function
    activationLUT.RescaleTransferFunction(-0.004698578733950853, 242.50450134277344)

    # Rescale transfer function
    activationPWF.RescaleTransferFunction(-0.004698578733950853, 242.50450134277344)
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976

    # get layout
    layout1 = GetLayout()

    # layout/tab size in pixels
    layout1.SetSize(2893, 954)

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976

    Hide(displacementxdmf, renderView1)
    
    # save animation
    SaveAnimation(filename=outname, viewOrLayout=renderView1, location=16, ImageResolution=[2892, 952],
        FontScaling='Scale fonts proportionally',
        OverrideColorPalette='',
        StereoMode='No change',
        TransparentBackground=0,
        FrameRate=30,
        FrameStride=1,
        FrameWindow=[0, 284], 
        # FFMPEG options
        Compression=1,
        Quality='2')
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976

    # set active source
    SetActiveSource(clip1)

    # hide data in view
    Hide(cellDatatoPointData1, renderView1)

    # show data in view
    clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

    # show color bar/color legend
    clip1Display.SetScalarBarVisibility(renderView1, True)

    # destroy cellDatatoPointData1
    Delete(cellDatatoPointData1)
    del cellDatatoPointData1
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976

    # set active source
    SetActiveSource(warpByVector1)

    # hide data in view
    Hide(clip1, renderView1)

    # show data in view
    warpByVector1Display = Show(warpByVector1, renderView1, 'UnstructuredGridRepresentation')

    # show color bar/color legend
    warpByVector1Display.SetScalarBarVisibility(renderView1, True)

    # destroy clip1
    Delete(clip1)
    del clip1
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976

    # set active source
    SetActiveSource(appendAttributes1)

    # hide data in view
    Hide(warpByVector1, renderView1)

    # show data in view
    appendAttributes1Display = Show(appendAttributes1, renderView1, 'UnstructuredGridRepresentation')

    # destroy warpByVector1
    Delete(warpByVector1)
    del warpByVector1
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976

    # set active source
    SetActiveSource(activation_resultsxdmf)

    # hide data in view
    Hide(appendAttributes1, renderView1)

    # show data in view
    activation_resultsxdmfDisplay = Show(activation_resultsxdmf, renderView1, 'UnstructuredGridRepresentation')

    # show color bar/color legend
    activation_resultsxdmfDisplay.SetScalarBarVisibility(renderView1, True)

    # destroy appendAttributes1
    Delete(appendAttributes1)
    del appendAttributes1
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976

    # destroy activation_resultsxdmf
    Delete(activation_resultsxdmf)
    del activation_resultsxdmf
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976

    # destroy displacementxdmf
    Delete(displacementxdmf)
    del displacementxdmf
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976

    # update animation scene based on data timesteps
    animationScene1.UpdateAnimationUsingDataTimeSteps()
    # Adjust camera

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976

    #================================================================
    # addendum: following script captures some of the application
    # state to faithfully reproduce the visualization during playback
    #================================================================

    #--------------------------------
    # saving layout sizes for layouts

    # layout/tab size in pixels
    layout1.SetSize(2893, 954)

    #-----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
    renderView1.CameraPosition = [19.514307645521704, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraFocalPoint = [-3.3289607763290405, -0.0006878376007080078, -0.0002740621566772461]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 5.912272919963976


    ##--------------------------------------------
    ## You may need to add some code at the end of this python script depending on your usage, eg:
    #
    ## Render all views to see them appears
    # RenderAllViews()
    #
    ## Interact with the view, usefull when running from pvpython
    # Interact()
    #
    ## Save a screenshot of the active view
    # SaveScreenshot("path/to/screenshot.png")
    #
    ## Save a screenshot of a layout (multiple splitted view)
    # SaveScreenshot("path/to/screenshot.png", GetLayout())
    #
    ## Save all "Extractors" from the pipeline browser
    # SaveExtracts()
    #
    ## Save a animation of the current active view
    # SaveAnimation()
    #
    ## Please refer to the documentation of paraview.simple
    ## https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html
    ##--------------------------------------------
  
# Define your base directory and output directory
base_folder = "/Users/javad/Docker/TugOfWar/01_results_24_11_29/"
# base_folder = "/Users/javad/Docker/TugOfWar/test/"
#base_outdir = "/Users/javad/Library/CloudStorage/GoogleDrive-Sadeghinia@simula.no/My Drive/02_Tug of War/Presentations/Results_24_11_27/"
base_outdir = "/Users/javad/Docker/TugOfWar/"
# Create the output directory if it doesn't exist
outfolder = os.path.join(base_outdir, "01_results_24_11_29_video")
os.makedirs(outfolder, exist_ok=True)
print(f"====== Start Processing =========")
# Iterate over each folder in the base folder
for folder_name in os.listdir(base_folder):
    folder_path = os.path.join(base_folder, folder_name)

    # Skip if it's not a directory
    if not os.path.isdir(folder_path):
        continue

    # # Define potential file paths
    # lv_path = os.path.join(folder_path, "lv", "microstructure_viz.xdmf")
    # lv_coarse_path = os.path.join(folder_path, "lv_coarse", "microstructure_viz.xdmf")

    # # Determine which path to use
    # if os.path.exists(lv_coarse_path):
    #     fname = lv_coarse_path
    # elif os.path.exists(lv_path):
    #     fname = lv_path
    # else:
    #     print(f"No microstructure_viz.xdmf file found in {folder_path}")
    #     continue

    # Define the output file name
    # outname = os.path.join(base_outdir, "Fibers", f"{folder_name}_fibers.png")
    # # Run the plot_fibers function
    # plot_fibers(fname, outname)
    print(f"start processing {folder_name} ...")
    fname_act = os.path.join(folder_path, "Activation_results.xdmf")
    fname_disp = os.path.join(folder_path, "displacement.xdmf")
    outname = os.path.join(outfolder,f"{folder_name}_deformed_act.avi")
    save_ani_deformed_activation(fname_act, fname_disp, outname)
    outname = os.path.join(outfolder,f"{folder_name}_deformed_act_cross_mid.avi")
    save_ani_deformed_activation_cross(fname_act, fname_disp, outname, clip_origin=-1.59006)
    #outname = os.path.join(outfolder,f"{folder_name}_deformed_act_cross_apex.avi")
    #save_ani_deformed_activation_cross(fname_act, fname_disp, outname, clip_origin=-3.90184)
    #outname = os.path.join(outfolder,f"{folder_name}_deformed_act_cross_multislice.avi")
    #save_ani_deformed_activation_cross(fname_act, fname_disp, outname, clip_origin=-3.06505)
    print(f"Processed {folder_name} and saved output")