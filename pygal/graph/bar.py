# from pygal.graph.graph import Graph
# from pygal.util import alter, decorate, ident, swap

# class Bar(Graph):
# 	"""Bar graph class"""

# 	_series_margin = .06  # Margin between series in the bar graph
# 	_serie_margin = .06  # Margin within a single series in the bar graph

# 	def __init__(self, *args, **kwargs):
# 		self.bar_spacing = kwargs.pop('bar_spacing', None)
# 		self.bar_images = kwargs.pop('bar_images', None)
# 		super(Bar, self).__init__(*args, **kwargs)

# 	def _bar(self, serie, parent, x, y, i, zero, secondary=False):
# 		"""Internal bar drawing function"""
# 		width = (self.view.x(1) - self.view.x(0)) / self._len
# 		print("Width", width)
#         # Apply bar spacing dynamically
# 		x, y = self.view((x, y))
# 		print("X and Y", x, y)
# 		series_margin = width * self._series_margin
# 		print("Seriesmargin", series_margin)
# 		x += series_margin
# 		print("x after seriesmargin", x)
# 		width -= 2 * series_margin
# 		print("width after seriesmargin multiplication", width)
# 		width /= self._order
# 		print("width after order division", width, self._order)

# 		if self.horizontal:
# 			serie_index = self._order - serie.index - 1
# 		else:
# 			serie_index = serie.index
# 		x += serie_index * width
# 		print("X after adding series index width", x, serie_index)
# 		serie_margin = width * self._serie_margin
# 		x += serie_margin
# 		print("X after adding serie margin", x, serie_margin)
# 		width -= 2 * serie_margin
# 		height = self.view.y(zero) - y
# 		r = serie.rounded_bars * 1 if serie.rounded_bars else 0

# 		if self.bar_images and len(self.bar_images) > i:
# 			image_url = self.bar_images[i]
# 			self.svg.node(
# 				parent,
# 				'image',
# 				href=image_url,
# 				x=x,
# 				y=y,
# 				width=width,
# 				height=height,
# 				preserveAspectRatio='none',
# 				class_='rect reactive tooltip-trigger'
# 			)
# 		else:
# 			alter(
# 				self.svg.transposable_node(
# 					parent,
# 					'rect',
# 					x=x,
# 					y=y,
# 					rx=r,
# 					ry=r,
# 					width=width,
# 					height=height,
# 					class_='rect reactive tooltip-trigger'
# 				), serie.metadata.get(i)
# 			)

# 		return x, y, width, height

# 	def _tooltip_and_print_values(
# 			self, serie_node, serie, parent, i, val, metadata, x, y, width,
# 			height
# 	):
# 		transpose = swap if self.horizontal else ident
# 		x_center, y_center = transpose((x + width / 2, y + height / 2))
# 		x_top, y_top = transpose((x + width, y + height))
# 		x_bottom, y_bottom = transpose((x, y))

# 		if self._dual:
# 			v = serie.values[i][0]
# 		else:
# 			v = serie.values[i]
# 		sign = -1 if v < self.zero else 1

# 		self._tooltip_data(
# 			parent, val, x_center, y_center, "centered", self._get_x_label(i)
# 		)

# 		if self.print_values_position == 'top':
# 			if self.horizontal:
# 				x = x_bottom + sign * self.style.value_font_size / 2
# 				y = y_center
# 			else:
# 				x = x_center
# 				y = y_bottom - sign * self.style.value_font_size / 2
# 		elif self.print_values_position == 'bottom':
# 			if self.horizontal:
# 				x = x_top + sign * self.style.value_font_size / 2
# 				y = y_center
# 			else:
# 				x = x_center
# 				y = y_top - sign * self.style.value_font_size / 2
# 		else:
# 			x = x_center
# 			y = y_center

# 		self._static_value(serie_node, val, x, y, metadata, "middle")

# 	def bar(self, serie, rescale=False):
# 		"""Draw a bar graph for a serie"""
# 		serie_node = self.svg.serie(serie)
# 		bars = self.svg.node(serie_node['plot'], class_="bars")
# 		if rescale and self.secondary_series:
# 			points = self._rescale(serie.points)
# 		else:
# 			points = serie.points

# 		for i, (x, y) in enumerate(points):
# 			if None in (x, y) or (self.logarithmic and y <= 0):
# 				continue
# 			metadata = serie.metadata.get(i)
# 			val = self._format(serie, i)

# 			bar = decorate(
# 				self.svg, self.svg.node(bars, class_='bar'), metadata
# 			)
# 			x_, y_, width, height = self._bar(
# 				serie, bar, x, y, i, self.zero, secondary=rescale
# 			)

# 			self._confidence_interval(
# 				serie_node['overlay'], x_ + width / 2, y_, serie.values[i],
# 				metadata
# 			)
# 			self._tooltip_and_print_values(
# 				serie_node, serie, bar, i, val, metadata, x_, y_, width, height
# 			)

# 	def _compute(self):
# 		"""
# 		Compute y min and max, y scale, and set labels for the bar graph.

# 		This function calculates the minimum and maximum values for the y-axis,
# 		determines the scale for the y-axis, and sets the labels for the x-axis.
# 		It also computes the positions for the bars based on the specified bar spacing.

# 		Parameters:
# 		None

# 		Returns:
# 		None
# 		"""
# 		print("\n================================In compute function================================")
# 		if self._min:
# 			self._box.ymin = min(self._min, self.zero)
# 		if self._max:
# 			self._box.ymax = max(self._max, self.zero)

# 		cumulative_spacing = 0
# 		self._x_pos = []

# 		if self.bar_spacing:
# 			total_spacing = sum(self.bar_spacing)
# 		else:
# 			total_spacing = 0

# 		# Ensure the spacing fits within the total width
# 		if total_spacing >= 1.0:
# 			scale_factor = 1.0 / total_spacing
# 			scaled_spacing = [s * scale_factor for s in self.bar_spacing]
# 		else:
# 			scaled_spacing = self.bar_spacing

# 		for i in range(self._len):
# 			if scaled_spacing and len(scaled_spacing) > i and i != 0:
# 				cumulative_spacing += scaled_spacing[i-1] / sum(scaled_spacing) * (self._len - 1)
# 			pos = (i + .5) / self._len + cumulative_spacing / self._len
# 			self._x_pos.append(pos)

# 		self._points(self._x_pos)

# 		total_spacing = sum(scaled_spacing) if scaled_spacing else 0
# 		self._box.xmax = (self._len + total_spacing) / self._len


# 	def _plot(self):
# 		"""Draw bars for series and secondary series"""
# 		for serie in self.series:
# 			self.bar(serie)
# 		for serie in self.secondary_series:
# 			self.bar(serie, True)
from pygal.graph.graph import Graph
from pygal.util import alter, decorate, ident, swap

class Bar(Graph):
    """Bar graph class"""

    # Margin between different series in the bar graph
    _series_margin = .06  
    # Margin within a single series in the bar graph
    _serie_margin = .06  

    def __init__(self, *args, **kwargs):
        # Initialize bar_spacing and bar_images from kwargs
        self.bar_spacing = kwargs.pop('bar_spacing', None)
        self.bar_images = kwargs.pop('bar_images', None)
        # Call the parent class constructor
        super(Bar, self).__init__(*args, **kwargs)

    def _bar(self, serie, parent, x, y, i, zero, secondary=False):
        """Internal bar drawing function"""
        # Calculate the width of each bar
        width = (self.view.x(1) - self.view.x(0)) / self._len
        print("Width", width)

        # Apply bar spacing dynamically
        x, y = self.view((x, y))
        print("X and Y", x, y)

        # Adjust for the margin between series
        series_margin = width * self._series_margin
        print("Series margin", series_margin)
        x += series_margin
        print("x after series margin", x)
        width -= 2 * series_margin
        print("width after series margin multiplication", width)
        width /= self._order
        print("width after order division", width, self._order)

        # Determine the position of the bar based on its index in the series
        if self.horizontal:
            serie_index = self._order - serie.index - 1
        else:
            serie_index = serie.index
        x += serie_index * width
        print("X after adding series index width", x, serie_index)

        # Adjust for the margin within a single series
        serie_margin = width * self._serie_margin
        x += serie_margin
        print("X after adding serie margin", x, serie_margin)
        width -= 2 * serie_margin

        # Calculate the height of the bar
        height = self.view.y(zero) - y
        # Determine if the bar should have rounded corners
        r = serie.rounded_bars * 1 if serie.rounded_bars else 0

        # Check if a bar image should be used instead of a regular bar
        if self.bar_images and len(self.bar_images) > i:
            image_url = self.bar_images[i]
            self.svg.node(
                parent,
                'image',
                href=image_url,
                x=x,
                y=y,
                width=width,
                height=height,
                preserveAspectRatio='none',
                class_='rect reactive tooltip-trigger'
            )
        else:
            # Create a regular bar with the specified attributes
            alter(
                self.svg.transposable_node(
                    parent,
                    'rect',
                    x=x,
                    y=y,
                    rx=r,
                    ry=r,
                    width=width,
                    height=height,
                    class_='rect reactive tooltip-trigger'
                ), serie.metadata.get(i)
            )

        return x, y, width, height

    def _tooltip_and_print_values(
            self, serie_node, serie, parent, i, val, metadata, x, y, width, height):
        """Add tooltip and print values on the bars"""
        # Determine the center and edges of the bar for placing tooltips
        transpose = swap if self.horizontal else ident
        x_center, y_center = transpose((x + width / 2, y + height / 2))
        x_top, y_top = transpose((x + width, y + height))
        x_bottom, y_bottom = transpose((x, y))

        # Get the value of the bar
        if self._dual:
            v = serie.values[i][0]
        else:
            v = serie.values[i]
        sign = -1 if v < self.zero else 1

        # Add tooltip data
        self._tooltip_data(
            parent, val, x_center, y_center, "centered", self._get_x_label(i)
        )

        # Determine the position to print the value based on the configuration
        if self.print_values_position == 'top':
            if self.horizontal:
                x = x_bottom + sign * self.style.value_font_size / 2
                y = y_center
            else:
                x = x_center
                y = y_bottom - sign * self.style.value_font_size / 2
        elif self.print_values_position == 'bottom':
            if self.horizontal:
                x = x_top + sign * self.style.value_font_size / 2
                y = y_center
            else:
                x = x_center
                y = y_top - sign * self.style.value_font_size / 2
        else:
            x = x_center
            y = y_center

        # Print the value on the bar
        self._static_value(serie_node, val, x, y, metadata, "middle")

    def bar(self, serie, rescale=False):
        """Draw a bar graph for a series"""
        serie_node = self.svg.serie(serie)
        bars = self.svg.node(serie_node['plot'], class_="bars")
        if rescale and self.secondary_series:
            points = self._rescale(serie.points)
        else:
            points = serie.points

        # Iterate over points and draw bars
        for i, (x, y) in enumerate(points):
            if None in (x, y) or (self.logarithmic and y <= 0):
                continue
            metadata = serie.metadata.get(i)
            val = self._format(serie, i)

            bar = decorate(
                self.svg, self.svg.node(bars, class_='bar'), metadata
            )
            x_, y_, width, height = self._bar(
                serie, bar, x, y, i, self.zero, secondary=rescale
            )

            self._confidence_interval(
                serie_node['overlay'], x_ + width / 2, y_, serie.values[i],
                metadata
            )
            self._tooltip_and_print_values(
                serie_node, serie, bar, i, val, metadata, x_, y_, width, height
            )

    def _compute(self):
        """
        Compute y min and max, y scale, and set labels for the bar graph.

        This function calculates the minimum and maximum values for the y-axis,
        determines the scale for the y-axis, and sets the labels for the x-axis.
        It also computes the positions for the bars based on the specified bar spacing.

        Parameters:
        None

        Returns:
        None
        """
        print("\n================================In compute function================================")
        if self._min:
            self._box.ymin = min(self._min, self.zero)
        if self._max:
            self._box.ymax = max(self._max, self.zero)

        cumulative_spacing = 0
        self._x_pos = []

        # Calculate total spacing if bar_spacing is specified
        if self.bar_spacing:
            total_spacing = sum(self.bar_spacing)
        else:
            total_spacing = 0

        # Ensure the spacing fits within the total width
        if total_spacing >= 1.0:
            scale_factor = 1.0 / total_spacing
            scaled_spacing = [s * scale_factor for s in self.bar_spacing]
        else:
            scaled_spacing = self.bar_spacing

        # Compute positions for bars with the scaled spacing
        for i in range(self._len):
            if scaled_spacing and len(scaled_spacing) > i and i != 0:
                cumulative_spacing += scaled_spacing[i-1] / sum(scaled_spacing) * (self._len - 1)
            pos = (i + .5) / self._len + cumulative_spacing / self._len
            self._x_pos.append(pos)

        self._points(self._x_pos)

        # Set the xmax value for the x-axis based on the total spacing
        total_spacing = sum(scaled_spacing) if scaled_spacing else 0
        self._box.xmax = (self._len + total_spacing) / self._len

    def _plot(self):
        """Draw bars for series and secondary series"""
        for serie in self.series:
            self.bar(serie)
        for serie in self.secondary_series:
            self.bar(serie, True)
