from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple([Decimal(x) for x in coordinates])
			self.dimension = len(coordinates)

		except ValueError:
			raise ValueError('The coordinates must be nonempty')

		except TypeError:
			raise TypeError('The coordinates must be an iterable')


	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)


	def __eq__(self, v):
		return self.coordinates == v.coordinates

	def plus(self, v):
		new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordinates)

	def plus(self, v):
		new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordinates)

	def times_scalar(self, c):
		new_coordinates = [Decimal(c)*x for x in self.coordinates]
		return Vector(new_coordinates)

	def magnitude(self):
		coordinates_squared = [x**2 for x in self.coordinates]
		return Decimal(sqrt(sum(coordinates_squared)))

	def normalized(self):
		try:
			magnitude = self.magnitude()
			return self.times_scalar(Decimal('1.0') / magnitude)
		except ZeroDivisionError:
			raise Exception('Cannot normalize the zero vector')

	def dot(self, v):
		return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

	def angle_with(self, v, in_degrees=False):
		try:
			u1 = self.normalized()
			u2 = v.normalized()
			angle_in_radians = acos(round(u1.dot(u2), 3))


			if in_degrees:
				degrees_per_radian = 180/pi
				return angle_in_radians * degrees_per_radian
			else:
				return angle_in_radians

		except Exception as e:
			if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
				raise Exception('Canoot compute an angle with the zero vector')


	def is_orthogonal_to(self, v, tolerance=1e-10):
		return abs(self.dot(v)) < tolerance

	def is_parallel_to(self, v):
		return ( self.is_zero() or
			v.is_zero() or
			self.angle_with(v) == 0
			or self.angle_with(v) == pi )

	def is_zero(self, tolerance=1e-10): 
		return self.magnitude() < tolerance






v = Vector(['7.579', '7.88'])
w = Vector(['22.737', '23.64'])
print(v.is_parallel_to(w))
print(v.is_orthogonal_to(w))

