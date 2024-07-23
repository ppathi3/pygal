from pygal.graph.graph import Graph
from pygal.util import alter, decorate, ident, swap


class Bar(Graph):
	"""Bar graph class"""

	_series_margin = .06  # Margin between series in the bar graph
	_serie_margin = .06  # Margin within a single series in the bar graph

	# Initialize a Bar graph instance.
	#
	# Parameters:
	# *args: Variable length argument list to pass to the parent class constructor.
	# **kwargs: Keyword arguments to customize the Bar graph.
	#
	# Keyword Arguments:
	# bar_spacing (list, optional): A list of floats representing the spacing between bars for each data point.
	#                               If not provided, default spacing is used.
	# bar_images (list, optional): A list of strings representing the URLs of images to be used as bar fills.
	#                              If not provided, default bar fills are used.
	#
	# Returns:
	# None
	def __init__(self, *args, **kwargs):
		self.bar_spacing = kwargs.pop('bar_spacing', None)  # Custom spacing between bars
		self.bar_images = kwargs.pop('bar_images', None)  # Custom images for bar fills
		super(Bar, self).__init__(*args, **kwargs)

	# Internal bar drawing function.
	#
	# This function is responsible for drawing a single bar in a bar graph. It calculates the position, size, and style of the bar based on the provided parameters.
	#
	# Parameters:
	# - serie: The data series for which the bar is being drawn.
	# - parent: The parent SVG node where the bar will be added.
	# - x: The x-coordinate of the bar's center.
	# - y: The y-coordinate of the bar's center.
	# - i: The index of the data point within the series.
	# - zero: The y-coordinate representing the zero value on the graph.
	# - cumulative_spacing: The cumulative spacing applied to the bars so far.
	# - secondary (optional): A boolean indicating whether the bar belongs to a secondary series. Default is False.
	#
	# Returns:
	# - A tuple (x, y, width, height) representing the position and size of the drawn bar.
	def _bar(self, serie, parent, x, y, i, zero, cumulative_spacing, secondary=False):
		"""Internal bar drawing function"""
		width = (self.view.x(1) - self.view.x(0)) / self._len  # Calculate width based on the graph's x-axis scale
		x, y = self.view((x, y))  # Convert to view coordinates
		series_margin = width * self._series_margin  # Margin between series
		x += series_margin
		width -= 2 * series_margin  # Adjust width for series margin
		width /= self._order  # Divide width by the number of series

		# Determine series index based on orientation
		if self.horizontal:
			serie_index = self._order - serie.index - 1
		else:
			serie_index = serie.index
		x += serie_index * width

		serie_margin = width * self._serie_margin  # Margin within series
		x += serie_margin
		width -= 2 * serie_margin  # Adjust width for serie margin
		height = self.view.y(zero) - y  # Calculate height of the bar
		r = serie.rounded_bars * 1 if serie.rounded_bars else 0  # Rounded corners if specified

		print("X value before bar spacing", x)
		# Apply cumulative bar spacing
		x += 50 * cumulative_spacing
		print("X value for bar spacing", x)

		# Check if image is provided for the bar fill
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

	# This function handles the tooltip and value printing for a bar graph.
	#
	# Parameters:
	# - serie_node (SVG node): The SVG node representing the series.
	# - serie (BarGraph.Series): The data series for which the values are being printed.
	# - parent (SVG node): The parent SVG node where the tooltip and value will be added.
	# - i (int): The index of the data point within the series.
	# - val (str): The formatted value to be printed.
	# - metadata (dict): Metadata associated with the data point.
	# - x (float): The x-coordinate of the bar's center.
	# - y (float): The y-coordinate of the bar's center.
	# - width (float): The width of the bar.
	# - height (float): The height of the bar.
	#
	# Returns:
	# None
	def _tooltip_and_print_values(
			self, serie_node, serie, parent, i, val, metadata, x, y, width,
			height
	):
		transpose = swap if self.horizontal else ident  # Transpose coordinates if horizontal
		x_center, y_center = transpose((x + width / 2, y + height / 2))  # Center of the bar
		x_top, y_top = transpose((x + width, y + height))  # Top corner of the bar
		x_bottom, y_bottom = transpose((x, y))  # Bottom corner of the bar

		# Get the value to determine the sign
		if self._dual:
			v = serie.values[i][0]
		else:
			v = serie.values[i]
		sign = -1 if v < self.zero else 1

		# Add tooltip data
		self._tooltip_data(
			parent, val, x_center, y_center, "centered", self._get_x_label(i)
		)

		# Determine position for printing values
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

# Draw a bar graph for a serie.

#     Parameters:
#     - serie (pygal.graph.graph.Graph.Series): The data series to be plotted.
#     - rescale (bool, optional): A flag indicating whether the series should be rescaled for secondary series. Default is False.

#     Returns:
#     None
	def bar(self, serie, rescale=False):
		"""Draw a bar graph for a serie"""
		serie_node = self.svg.serie(serie)
		bars = self.svg.node(serie_node['plot'], class_="bars")
		if rescale and self.secondary_series:
			points = self._rescale(serie.points)
		else:
			points = serie.points

		cumulative_spacing = 0

		for i, (x, y) in enumerate(points):
			if None in (x, y) or (self.logarithmic and y <= 0):
				continue
			metadata = serie.metadata.get(i)
			val = self._format(serie, i)

			bar = decorate(
				self.svg, self.svg.node(bars, class_='bar'), metadata
			)
			# Update cumulative spacing
			if self.bar_spacing and len(self.bar_spacing) > i:
				cumulative_spacing += self.bar_spacing[i]
			x_, y_, width, height = self._bar(
				serie, bar, x, y, i, self.zero, cumulative_spacing, secondary=rescale
			)

			self._confidence_interval(
				serie_node['overlay'], x_ + width / 2, y_, serie.values[i],
				metadata
			)
			self._tooltip_and_print_values(
				serie_node, serie, bar, i, val, metadata, x_, y_, width, height
			)

	# Compute y min and max, y scale, and set labels for the bar graph.

	# This function calculates the minimum and maximum values for the y-axis,
	# determines the y-scale, and computes the positions for the x-axis labels.
	# It also handles the cumulative spacing for the bars if provided.

	# Parameters:
	# None


	# Returns:
	# None
	def _compute(self):
			"""Compute y min and max and y scale and set labels"""
			if self._min:
				self._box.ymin = min(self._min, self.zero)  # Set minimum y value
			if self._max:
				self._box.ymax = max(self._max, self.zero)  # Set maximum y value

			cumulative_spacing = 0

			# Compute the positions for x-axis labels with spacing
			self._x_pos = []
			for i in range(self._len):
				# Update cumulative spacing if bar_spacing is provided
				if self.bar_spacing and len(self.bar_spacing) > i:
					cumulative_spacing += self.bar_spacing[i]
				# Adjust label position based on cumulative spacing
				pos = (i + .5) / self._len + cumulative_spacing / self._len
				print("x Position in compute", pos, i, self._len, cumulative_spacing)
				self._x_pos.append(pos)

			self._points(self._x_pos)


		# Draw bars for series and secondary series.
		#
		# This function iterates through the primary and secondary series,
		# and calls the `bar` method to draw the corresponding bars.
		# The `bar` method is responsible for drawing a single bar for a given data series.
		#
		# Parameters:
		# None
		#
		# Returns:
		# None
	def _plot(self):
		"""Draw bars for series and secondary series"""
		for serie in self.series:
			self.bar(serie)
		for serie in self.secondary_series:
			self.bar(serie, True)
