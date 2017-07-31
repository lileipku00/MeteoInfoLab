# coding=utf-8
#-----------------------------------------------------
# Author: Yaqiang Wang
# Date: 2017-3-25
# Purpose: MeteoInfoLab axes module
# Note: Jython
#-----------------------------------------------------

from org.meteoinfo.chart.plot import Plot2D, MapPlot, PolarPlot, PiePlot, Plot3D, GraphicFactory
from org.meteoinfo.map import MapView
from org.meteoinfo.legend import LegendManage, BreakTypes
from org.meteoinfo.shape import ShapeTypes

from java.awt import Font

from mipylib.numeric.dimarray import DimArray
from mipylib.numeric.miarray import MIArray
import plotutil
import miplot
import mipylib.numeric.minum as minum

class Axes():
    '''
    Axes with Cartesian coordinate.
    '''

    def __init__(self, axes=None):
        if axes is None:
            self.axes = Plot2D()
        else:
            self.axes = axes
            
    def get_type(self):
        '''
        Get axes type
        
        :returns: Axes type
        '''
        return self.axes.getPlotType()
            
    def get_position(self):
        '''
        Get axes position             

        :returns: Axes position [left, bottom, width, height] in normalized (0, 1) units
        '''
        pos = self.axes.getPosition()
        return [pos.x, pos.y, pos.width, pos.height]
        
    def set_position(self, pos):
        '''
        Set axes position
        
        :param pos: (*list*) Axes position specified by *position=* [left, bottom, width,
            height] in normalized (0, 1) units
        '''
        self.axes.setPosition(pos)
        
    def get_outerposition(self):
        '''
        Get axes outer position
        
        :returns: Axes outer position [left, bottom, width, height] in normalized (0, 1) units
        '''
        pos = self.axes.getPosition()
        return [pos.x, pos.y, pos.width, pos.height]
        
    def set_outerposition(self, pos):
        '''
        Set axes outer position
        
        :param pos: (*list*) Axes outer position specified by *position=* [left, bottom, width,
            height] in normalized (0, 1) units
        '''
        self.axes.setPosition(pos)
        
    def active_outerposition(self, active):
        '''
        Set axes outer position active or not.
        
        :param active: (*boolean*) Active or not
        '''
        self.axes.setOuterPosActive(active)     
    
    def get_axis(self, loc):
        '''
        Get axis by location.
        
        :param loc: (*Location*) Location enum.
        
        :returns: Axis
        '''
        return self.axes.getAxis(loc)
        
    def set_title(self, title):
        '''
        Set title
        
        :param title: (*string*) Title
        '''
        self.axes.setTitle(title)
    
    def add_graphic(self, graphic):
        '''
        Add a graphic
        
        :param graphic: (*Graphic*) The graphic to be added.
        '''
        self.axes.addGraphic(graphic)
        
##############################################
class PieAxes(Axes):
    '''
    Axes for pie plot.       
    '''
    
    def __init__(self, axes=None):
        if axes is None:        
            self.axes = PiePlot()
        else:
            self.axes = axes

##############################################        
class MapAxes(Axes):
    '''
    Axes with geological map coordinate.
    '''
    
    def __init__(self, axes=None, mapview=None):
        if axes is None:        
            if mapview is None:
                mapview = MapView()
                self.axes = MapPlot(mapview)
            else:
                self.axes = MapPlot(mapview)
        else:
            self.axes = axes
            
    def add_layer(self, layer, zorder=None):
        '''
        Add a map layer
        
        :param layer: (*MapLayer*) The map layer.
        :param zorder: (*int*) Layer z order.
        '''
        if zorder is None:
            self.axes.addLayer(layer)
        else:
            self.axes.addLayer(zorder, layer)
            
###############################################
class PolarAxes(Axes):
    '''
    Axes with polar coordinate.
    '''
    
    def __init__(self, axes=None):
        if axes is None:
            self.axes = PolarPlot()
        else:
            self.axes = axes
    
    def set_rmax(self, rmax):
        '''
        Set radial max circle.
        
        :param rmax: (*float*) Radial max value.
        '''
        self.axes.setRadius(rmax)
        
    def set_rlabel_position(self, pos):
        '''
        Updates the theta position of the radial labels.
        
        :param pos: (*float*) The angular position of the radial labels in degrees.
        '''
        if isinstance(pos, (DimArray, MIArray)):
            pos = pos.tolist()
        self.axes.setYTickLabelPos(pos)
        
    def set_rticks(self, ticks):
        '''
        Set radial ticks.
        
        :param ticks: (*string list*) Tick labels.
        '''
        self.axes.setYTickLabels(ticks)
        
    def set_rtick_format(self, fmt=''):
        '''
        Set radial tick format.
        
        :param ftm: (*string*) Tick format ['' | '%'].
        '''
        self.axes.setYTickFormat(fmt)
        
    def set_rtick_locations(self, loc):
        '''
        Set radial tick locations.
        
        :param loc: (*float list*) Tick locations.
        '''
        if isinstance(loc, (DimArray, MIArray)):
            loc = loc.tolist()
        self.axes.setYTickLocations(loc)
        
    def set_xtick_locations(self, loc):
        '''
        Set angular tick locations.
        
        :param loc: (*float list*) Tick locations.
        '''
        if isinstance(loc, (DimArray, MIArray)):
            loc = loc.tolist()
        self.axes.setXTickLocations(loc)
        
    def set_xticks(self, ticks):
        '''
        Set angular ticks.
        
        :param ticks: (*string list*) Tick labels.
        '''
        self.axes.setXTickLabels(ticks)
        
    def set_rtick_font(self, name=None, size=None, style=None):
        '''
        Set radial tick font.
        
        :param name: (*string*) Font name.
        :param size: (*int*) Font size.
        :param style: (*string*) Font style.
        '''
        font = self.axes.getYTickFont()
        if name is None:
            name = font.getName()
        if size is None:
            size = font.getSize()
        if style is None:
            style = font.getStyle()
        else:
            if style.lower() == 'bold':
                style = Font.BOLD
            elif style.lower() == 'italic':
                style = Font.ITALIC
            else:
                style = Font.PLAIN
        font = Font(name, style, size)
        self.axes.setYTickFont(font)
        
    def set_xtick_font(self, name=None, size=None, style=None):
        '''
        Set angular tick font.
        
        :param name: (*string*) Font name.
        :param size: (*int*) Font size.
        :param style: (*string*) Font style.
        '''
        font = self.axes.getXTickFont()
        if name is None:
            name = font.getName()
        if size is None:
            size = font.getSize()
        if style is None:
            style = font.getStyle()
        else:
            if style.lower() == 'bold':
                style = Font.BOLD
            elif style.lower() == 'italic':
                style = Font.ITALIC
            else:
                style = Font.PLAIN
        font = Font(name, style, size)
        self.axes.setXTickFont(font)
        
#########################################################
class Axes3D(Axes):
    '''
    Axes with 3 dimensional.
    '''
    
    def __init__(self, axes=None, **kwargs):
        if axes is None:        
            self.axes = Plot3D()
        else:
            self.axes = axes
        self.projector = self.axes.getProjector()
        #distance = kwargs.pop('distance', 10000)
        #self.projector.setDistance(distance)
        rotation_angle = kwargs.pop('rotation', 225)
        self.projector.setRotationAngle(rotation_angle)
        elevation_angle = kwargs.pop('elevation', 30)
        self.projector.setElevationAngle(elevation_angle)
        xyaxis = kwargs.pop('xyaxis', True)
        self.axes.setDisplayXY(xyaxis)
        zaxis = kwargs.pop('zaxis', True)
        self.axes.setDisplayZ(zaxis)
        grid = kwargs.pop('grid', True)
        self.axes.setDisplayGrids(grid)
        boxed = kwargs.pop('boxed', True)
        self.axes.setBoxed(boxed)
        bbox = kwargs.pop('bbox', False)
        self.axes.setDrawBoundingBox(bbox)
        
    def get_distance(self):
        '''
        Get distance to object.
        
        :returns: Distance to object.
        '''
        return self.projector.getDistance()
        
    def set_distance(self, dis):
        '''
        Set distance to object.
        
        :param dis: (*float*) Distance to object.
        '''
        self.projector.setDistance(dis)
        miplot.draw_if_interactive()
        
    def get_rotation(self):
        '''
        Get rotation angle.
        
        :returns: Rotation angle.
        '''
        return self.projector.getRotationAngle()
        
    def set_rotation(self, rotation):
        '''
        Set rotation angle.
        
        :param rotation: (*float*) Rotation angle.
        '''
        self.projector.setRotationAngle(rotation)
        miplot.draw_if_interactive()
        
    def get_elevation(self):
        '''
        Get elevation angle.
        
        :returns: Elevation angle.
        '''
        return self.projector.getElevationAngle()
        
    def set_elevation(self, elevation):
        '''
        Set elevation angle.
        
        :param elevation: (*float*) Elevation angle.
        '''
        self.projector.setElevationAngle(elevation)
        miplot.draw_if_interactive()
        
    def set_draw_xy(self, dxy):
        '''
        Set draw xy axis or not.
        
        :param dxy: (*boolean*) Draw xy axis or not.
        '''
        self.axes.setDisplayXY(dxy)
        miplot.draw_if_interactive()
        
    def set_draw_z(self, dz):
        '''
        Set draw z axis or not.
        
        :param dz: (*boolean*) Draw z axis or not.
        '''
        self.axes.setDisplayZ(dz)
        miplot.draw_if_interactive()
        
    def set_draw_box(self, db):
        '''
        Set draw 3D box or not.
        
        :param db: (*boolean*) Draw 3D box or not.
        '''
        self.axes.setBoxed(db)
        miplot.draw_if_interactive()
        
    def set_draw_bbox(self, bbox):
        '''
        Set draw bounding box or not.
        
        :param db: (*boolean*) Draw bounding box or not.
        '''
        self.axes.setDrawBoundingBox(bbox)
        miplot.draw_if_interactive()
        
    def plot(self, x, y, z, *args, **kwargs):
        """
        Plot 3D lines and/or markers to the axes. *args* is a variable length argument, allowing
        for multiple *x, y* pairs with an optional format string.
        
        :param x: (*array_like*) Input x data.
        :param y: (*array_like*) Input y data.
        :param z: (*array_like*) Input z data.
        :param style: (*string*) Line style for plot.
        
        :returns: Legend breaks of the lines.
        
        The following format string characters are accepted to control the line style or marker:
        
          =========  ===========
          Character  Description
          =========  ===========
          '-'         solid line style
          '--'        dashed line style
          '-.'        dash-dot line style
          ':'         dotted line style
          '.'         point marker
          ','         pixel marker
          'o'         circle marker
          'v'         triangle_down marker
          '^'         triangle_up marker
          '<'         triangle_left marker
          '>'         triangle_right marker
          's'         square marker
          'p'         pentagon marker
          '*'         star marker
          'x'         x marker
          'D'         diamond marker
          =========  ===========
          
        The following color abbreviations are supported:
          
          =========  =====
          Character  Color  
          =========  =====
          'b'        blue
          'g'        green
          'r'        red
          'c'        cyan
          'm'        magenta
          'y'        yellow
          'k'        black
          =========  =====
        """      
        xdata = plotutil.getplotdata(x)
        ydata = plotutil.getplotdata(y)
        zdata = plotutil.getplotdata(z)  
        style = None
        if len(args) > 0:
            style = args[0]
        
        #Set plot data styles
        label = kwargs.pop('label', 'S_1')
        if style is None:
            line = plotutil.getlegendbreak('line', **kwargs)[0]
            line.setCaption(label)
        else:
            line = plotutil.getplotstyle(style, label, **kwargs)   

        #Add graphics
        graphics = GraphicFactory.createLineString(xdata, ydata, zdata, line)
        visible = kwargs.pop('visible', True)
        if visible:
            self.add_graphic(graphics)
            miplot.draw_if_interactive()
        return graphics
        
    def scatter(self, x, y, z, s=8, c='b', marker='o', alpha=None, linewidth=None, 
                verts=None, **kwargs):
        """
        Make a 3D scatter plot of x, y and z, where x, y and z are sequence like objects of the same lengths.
        
        :param x: (*array_like*) Input x data.
        :param y: (*array_like*) Input y data.
        :param z: (*array_like*) Input z data.
        :param s: (*int*) Size of points.
        :param c: (*Color*) Color of the points. Or z vlaues.
        :param alpha: (*int*) The alpha blending value, between 0 (transparent) and 1 (opaque).
        :param marker: (*string*) Marker of the points.
        :param label: (*string*) Label of the points series.
        :param levs: (*array_like*) Optional. A list of floating point numbers indicating the level 
            points to draw, in increasing order.
        
        :returns: Points legend break.
        """        
        #Add data series
        label = kwargs.pop('label', 'S_0')
        xdata = plotutil.getplotdata(x)
        ydata = plotutil.getplotdata(y)
        zdata = plotutil.getplotdata(z)
        
        #Set plot data styles
        pb, isunique = plotutil.getlegendbreak('point', **kwargs)
        pb.setCaption(label)
        pstyle = plotutil.getpointstyle(marker)    
        pb.setStyle(pstyle)
        isvalue = False
        if len(c) > 1:
            if isinstance(c, (MIArray, DimArray)):
                isvalue = True
            elif isinstance(c[0], (int, long, float)):
                isvalue = True            
        if isvalue:
            ls = kwargs.pop('symbolspec', None)
            if ls is None:        
                if isinstance(c, (list, tuple)):
                    c = minum.array(c)
                levels = kwargs.pop('levs', None)
                if levels is None:
                    levels = kwargs.pop('levels', None)
                if levels is None:
                    cnum = kwargs.pop('cnum', None)
                    if cnum is None:
                        ls = plotutil.getlegendscheme([], c.min(), c.max(), **kwargs)
                    else:
                        ls = plotutil.getlegendscheme([cnum], c.min(), c.max(), **kwargs)
                else:
                    ls = plotutil.getlegendscheme([levels], c.min(), c.max(), **kwargs)
                ls = plotutil.setlegendscheme_point(ls, **kwargs)
                if isinstance(s, int):
                    for lb in ls.getLegendBreaks():
                        lb.setSize(s)
                else:
                    n = len(s)
                    for i in range(0, n):
                        ls.getLegendBreaks()[i].setSize(s[i])
            #Create graphics
            graphics = GraphicFactory.createPoints3D(xdata, ydata, zdata, c.asarray(), ls)
        else:
            colors = plotutil.getcolors(c, alpha)   
            pbs = []
            if isinstance(s, int):   
                pb.setSize(s)
                if len(colors) == 1:
                    pb.setColor(colors[0])
                    pbs.append(pb)
                else:
                    n = len(colors)
                    for i in range(0, n):
                        npb = pb.clone()
                        npb.setColor(colors[i])
                        pbs.append(npb)
            else:
                n = len(s)
                if len(colors) == 1:
                    pb.setColor(colors[0])
                    for i in range(0, n):
                        npb = pb.clone()
                        npb.setSize(s[i])
                        pbs.append(npb)
                else:
                    for i in range(0, n):
                        npb = pb.clone()
                        npb.setSize(s[i])
                        npb.setColor(colors[i])
                        pbs.append(npb)
            #Create graphics
            graphics = GraphicFactory.createPoints3D(xdata, ydata, zdata, pbs)
        
        visible = kwargs.pop('visible', True)
        if visible:
            self.add_graphic(graphics)
            miplot.draw_if_interactive()
        return graphics
        
    def plot_wireframe(self, *args, **kwargs):
        '''
        creates a three-dimensional wireframe plot
        
        :param x: (*array_like*) Optional. X coordinate array.
        :param y: (*array_like*) Optional. Y coordinate array.
        :param z: (*array_like*) 2-D z value array.
        :param cmap: (*string*) Color map string.
        :param xyaxis: (*boolean*) Draw x and y axis or not.
        :param zaxis: (*boolean*) Draw z axis or not.
        :param grid: (*boolean*) Draw grid or not.
        :param boxed: (*boolean*) Draw boxed or not.
        :param mesh: (*boolean*) Draw mesh line or not.
        
        :returns: Legend
        '''        
        if len(args) == 1:
            x = args[0].dimvalue(1)
            y = args[0].dimvalue(0)
            x, y = minum.meshgrid(x, y)
            z = args[0]    
            args = args[1:]
        else:
            x = args[0]
            y = args[1]
            z = args[2]
            args = args[3:]
 
        line = plotutil.getlegendbreak('line', **kwargs)[0]
        graphics = GraphicFactory.createWireframe(x.asarray(), y.asarray(), z.asarray(), line)
        visible = kwargs.pop('visible', True)
        if visible:
            self.add_graphic(graphics)
            miplot.draw_if_interactive()
        return graphics
        
    def plot_surface(self, *args, **kwargs):
        '''
        creates a three-dimensional surface plot
        
        :param x: (*array_like*) Optional. X coordinate array.
        :param y: (*array_like*) Optional. Y coordinate array.
        :param z: (*array_like*) 2-D z value array.
        :param cmap: (*string*) Color map string.
        :param xyaxis: (*boolean*) Draw x and y axis or not.
        :param zaxis: (*boolean*) Draw z axis or not.
        :param grid: (*boolean*) Draw grid or not.
        :param boxed: (*boolean*) Draw boxed or not.
        :param mesh: (*boolean*) Draw mesh line or not.
        
        :returns: Legend
        '''        
        if len(args) <= 2:
            x = args[0].dimvalue(1)
            y = args[0].dimvalue(0)
            x, y = minum.meshgrid(x, y)
            z = args[0]    
            args = args[1:]
        else:
            x = args[0]
            y = args[1]
            z = args[2]
            args = args[3:]
        cmap = plotutil.getcolormap(**kwargs)
        if len(args) > 0:
            level_arg = args[0]
            if isinstance(level_arg, int):
                cn = level_arg
                ls = LegendManage.createLegendScheme(z.min(), z.max(), cn, cmap)
            else:
                if isinstance(level_arg, MIArray):
                    level_arg = level_arg.aslist()
                ls = LegendManage.createLegendScheme(z.min(), z.max(), level_arg, cmap)
        else:    
            ls = LegendManage.createLegendScheme(z.min(), z.max(), cmap)
        ls = ls.convertTo(ShapeTypes.Polygon)
        edge = kwargs.pop('edge', True)
        kwargs['edge'] = edge
        plotutil.setlegendscheme(ls, **kwargs)
        graphics = GraphicFactory.createMeshPolygons(x.asarray(), y.asarray(), z.asarray(), ls)
        visible = kwargs.pop('visible', True)
        if visible:
            self.add_graphic(graphics)
            miplot.draw_if_interactive()
        return graphics
        
    def contour(self, *args, **kwargs):
        """
        Plot contours.
        
        :param x: (*array_like*) Optional. X coordinate array.
        :param y: (*array_like*) Optional. Y coordinate array.
        :param z: (*array_like*) 2-D z value array.
        :param levs: (*array_like*) Optional. A list of floating point numbers indicating the level curves 
            to draw, in increasing order.
        :param cmap: (*string*) Color map string.
        :param colors: (*list*) If None (default), the colormap specified by cmap will be used. If a 
            string, like ‘r’ or ‘red’, all levels will be plotted in this color. If a tuple of matplotlib 
            color args (string, float, rgb, etc), different levels will be plotted in different colors in 
            the order specified.
        :param smooth: (*boolean*) Smooth countour lines or not.
        
        :returns: (*VectoryLayer*) Contour VectoryLayer created from array data.
        """
        n = len(args)
        cmap = plotutil.getcolormap(**kwargs)
        fill_value = kwargs.pop('fill_value', -9999.0)
        offset = kwargs.pop('offset', 0)
        xaxistype = None
        if n <= 2:
            gdata = minum.asgriddata(args[0])
            if isinstance(args[0], DimArray):
                if args[0].islondim(1):
                    xaxistype = 'lon'
                elif args[0].islatdim(1):
                    xaxistype = 'lat'
                elif args[0].istimedim(1):
                    xaxistype = 'time'
            args = args[1:]
        elif n <=4:
            x = args[0]
            y = args[1]
            a = args[2]
            gdata = minum.asgriddata(a, x, y, fill_value)
            args = args[3:]
        if len(args) > 0:
            level_arg = args[0]
            if isinstance(level_arg, int):
                cn = level_arg
                ls = LegendManage.createLegendScheme(gdata.min(), gdata.max(), cn, cmap)
            else:
                if isinstance(level_arg, MIArray):
                    level_arg = level_arg.aslist()
                ls = LegendManage.createLegendScheme(gdata.min(), gdata.max(), level_arg, cmap)
        else:    
            ls = LegendManage.createLegendScheme(gdata.min(), gdata.max(), cmap)
        ls = ls.convertTo(ShapeTypes.Polyline)
        plotutil.setlegendscheme(ls, **kwargs)
        
        smooth = kwargs.pop('smooth', True)
        zdir = kwargs.pop('zdir', 'z')
        igraphic = GraphicFactory.createContourLines(gdata.data, offset, zdir, ls, smooth)
        visible = kwargs.pop('visible', True)
        if visible:
            self.add_graphic(igraphic)
            miplot.draw_if_interactive()
        return igraphic
        
    def contourf(self, *args, **kwargs):
        """
        Plot filled contours.
        
        :param x: (*array_like*) Optional. X coordinate array.
        :param y: (*array_like*) Optional. Y coordinate array.
        :param z: (*array_like*) 2-D z value array.
        :param levs: (*array_like*) Optional. A list of floating point numbers indicating the level curves 
            to draw, in increasing order.
        :param cmap: (*string*) Color map string.
        :param colors: (*list*) If None (default), the colormap specified by cmap will be used. If a 
            string, like ‘r’ or ‘red’, all levels will be plotted in this color. If a tuple of matplotlib 
            color args (string, float, rgb, etc), different levels will be plotted in different colors in 
            the order specified.
        :param smooth: (*boolean*) Smooth countour lines or not.
        
        :returns: (*VectoryLayer*) Contour VectoryLayer created from array data.
        """
        n = len(args)
        cmap = plotutil.getcolormap(**kwargs)
        fill_value = kwargs.pop('fill_value', -9999.0)
        offset = kwargs.pop('offset', 0)
        xaxistype = None
        if n <= 2:
            gdata = minum.asgriddata(args[0])
            if isinstance(args[0], DimArray):
                if args[0].islondim(1):
                    xaxistype = 'lon'
                elif args[0].islatdim(1):
                    xaxistype = 'lat'
                elif args[0].istimedim(1):
                    xaxistype = 'time'
            args = args[1:]
        elif n <=4:
            x = args[0]
            y = args[1]
            a = args[2]
            gdata = minum.asgriddata(a, x, y, fill_value)
            args = args[3:]
        if len(args) > 0:
            level_arg = args[0]
            if isinstance(level_arg, int):
                cn = level_arg
                ls = LegendManage.createLegendScheme(gdata.min(), gdata.max(), cn, cmap)
            else:
                if isinstance(level_arg, MIArray):
                    level_arg = level_arg.aslist()
                ls = LegendManage.createLegendScheme(gdata.min(), gdata.max(), level_arg, cmap)
        else:    
            ls = LegendManage.createLegendScheme(gdata.min(), gdata.max(), cmap)
        ls = ls.convertTo(ShapeTypes.Polygon)
        edge = kwargs.pop('edge', None)
        if edge is None:
            kwargs['edge'] = False
        else:
            kwargs['edge'] = edge
        plotutil.setlegendscheme(ls, **kwargs)
        
        smooth = kwargs.pop('smooth', True)
        zdir = kwargs.pop('zdir', 'z')
        igraphic = GraphicFactory.createContourPolygons(gdata.data, offset, zdir, ls, smooth)
        visible = kwargs.pop('visible', True)
        if visible:
            self.add_graphic(igraphic)
            miplot.draw_if_interactive()
        return igraphic
        
    def imshow(self, *args, **kwargs):
        """
        Display an image on the 3D axes.
        
        :param x: (*array_like*) Optional. X coordinate array.
        :param y: (*array_like*) Optional. Y coordinate array.
        :param z: (*array_like*) 2-D or 3-D (RGB) z value array.
        :param levs: (*array_like*) Optional. A list of floating point numbers indicating the level curves 
            to draw, in increasing order.
        :param cmap: (*string*) Color map string.
        :param colors: (*list*) If None (default), the colormap specified by cmap will be used. If a 
            string, like ‘r’ or ‘red’, all levels will be plotted in this color. If a tuple of matplotlib 
            color args (string, float, rgb, etc), different levels will be plotted in different colors in 
            the order specified.
        
        :returns: (*RasterLayer*) RasterLayer created from array data.
        """
        n = len(args)
        cmap = plotutil.getcolormap(**kwargs)
        fill_value = kwargs.pop('fill_value', -9999.0)
        xaxistype = None
        isrgb = False
        if n <= 2:
            if isinstance(args[0], (list, tuple)):
                isrgb = True
                rgbdata = args[0]
                if isinstance(rgbdata[0], MIArray):
                    x = minum.arange(0, rgbdata[0].shape[1])
                    y = minum.arange(0, rgbdata[0].shape[0])
                else:
                    x = rgbdata[0].dimvalue(1)
                    y = rgbdata[0].dimvalue(0)
            elif args[0].ndim > 2:
                isrgb = True
                rgbdata = args[0]
                if isinstance(rgbdata, MIArray):
                    x = minum.arange(0, rgbdata.shape[1])
                    y = minum.arange(0, rgbdata.shape[0])
                else:
                    x = rgbdata.dimvalue(1)
                    y = rgbdata.dimvalue(0)
            else:
                gdata = minum.asgridarray(args[0])
                if isinstance(args[0], DimArray):
                    if args[0].islondim(1):
                        xaxistype = 'lon'
                    elif args[0].islatdim(1):
                        xaxistype = 'lat'
                    elif args[0].istimedim(1):
                        xaxistype = 'time'
                args = args[1:]
        elif n <=4:
            x = args[0]
            y = args[1]
            a = args[2]
            if isinstance(a, (list, tuple)):
                isrgb = True
                rgbdata = a
            elif a.ndim > 2:
                isrgb = True
                rgbdata = a
            else:
                gdata = minum.asgridarray(a, x, y, fill_value)
                args = args[3:]   
        
        offset = kwargs.pop('offset', 0)
        zdir = kwargs.pop('zdir', 'z')
        if isrgb:
            if isinstance(rgbdata, (list, tuple)):
                rgbd = []
                for d in rgbdata:
                    rgbd.append(d.asarray())
                rgbdata = rgbd
            else:
                rgbdata = rgbdata.asarray()
            x = plotutil.getplotdata(x)
            y = plotutil.getplotdata(y)
            graphics = GraphicFactory.createImage(x, y, rgbdata, offset, zdir)
            ls = None
        else:
            if len(args) > 0:
                level_arg = args[0]
                if isinstance(level_arg, int):
                    cn = level_arg
                    ls = LegendManage.createImageLegend(gdata, cn, cmap)
                else:
                    if isinstance(level_arg, MIArray):
                        level_arg = level_arg.aslist()
                    ls = LegendManage.createImageLegend(gdata, level_arg, cmap)
            else:
                ls = plotutil.getlegendscheme(args, gdata.min(), gdata.max(), **kwargs)
            ls = ls.convertTo(ShapeTypes.Image)
            plotutil.setlegendscheme(ls, **kwargs)
                
            graphics = GraphicFactory.createImage(gdata, ls, offset, zdir)
                
        visible = kwargs.pop('visible', True)
        if visible:
            self.add_graphic(graphics)
            miplot.draw_if_interactive()
        return graphics
        
    def plot_layer(self, layer, **kwargs):
        '''
        Plot a layer in 3D axes.
        
        :param layer: (*MILayer*) The layer to be plotted.
        
        :returns: Graphics.
        '''
        ls = kwargs.pop('symbolspec', None)
        layer = layer.layer
        if ls is None:
            ls = layer.getLegendScheme()
            if len(kwargs) > 0 and layer.getLegendScheme().getBreakNum() == 1:
                lb = layer.getLegendScheme().getLegendBreaks().get(0)
                btype = lb.getBreakType()
                geometry = 'point'
                if btype == BreakTypes.PolylineBreak:
                    geometry = 'line'
                elif btype == BreakTypes.PolygonBreak:
                    geometry = 'polygon'
                lb, isunique = plotutil.getlegendbreak(geometry, **kwargs)
                ls.getLegendBreaks().set(0, lb)

        plotutil.setlegendscheme(ls, **kwargs)
        layer.setLegendScheme(ls)
            
        offset = kwargs.pop('offset', 0)
        graphics = GraphicFactory.createGraphicsFromLayer(layer, offset)
        
        visible = kwargs.pop('visible', True)
        if visible:
            self.add_graphic(graphics)
            miplot.draw_if_interactive()
        return graphics