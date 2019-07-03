import math

class Statistics():

    """
    Class has a single attribute for data, and a number of attributes for various
    statistics on that data.
    After creating instance, set data attribute and call calculate to populate statistics
    attributes.
    A single instance can therefore be used repeatedly on various data sets.
    Also has methods to print data and statistics.
    """

    def __init__(self):

        """
        Simply create a set of attributes with default values.
        """

        self.data = []
        self.count = 0
        self.total = 0
        self.arithmetic_mean = 0
        self.minimum = 0
        self.lower_quartile = 0
        self.median = 0
        self.upper_quartile = 0
        self.maximum = 0
        self.overall_range = 0
        self.inter_quartile_range = 0
        self.standard_deviation_population = 0
        self.standard_deviation_sample = 0
        self.variance_population = 0
        self.variance_sample = 0
        self.skew = 0

    def output_data(self):

        """
        Iterate and print data
        """

        print("Number of items: " + str(len(self.data)))

        for i, v in enumerate(self.data):
            print(str(i) + "\t" + str(v))

    def output_statistics(self):

        """
        Print statistics in a neat format.
        """

        print("Count:                         " + str(self.count))
        print("Total:                         " + str(self.total))
        print("Arithmetic mean:               " + str(self.arithmetic_mean))
        print("Minimum:                       " + str(self.minimum))
        print("Lower quartile:                " + str(self.lower_quartile))
        print("Median:                        " + str(self.median))
        print("Upper quartile:                " + str(self.upper_quartile))
        print("Maximum:                       " + str(self.maximum))
        print("Overall range:                 " + str(self.overall_range))
        print("Inter quartile range:          " + str(self.inter_quartile_range))
        print("Standard deviation population: " + str(self.standard_deviation_population))
        print("Standard deviation sample:     " + str(self.standard_deviation_sample))
        print("Variance population:           " + str(self.variance_population))
        print("Variance sample:               " + str(self.variance_sample))
        print("Skew:                          " + str(self.skew))

    def __is_even(self, n):
        return n % 2 == 0

    def calculate(self):

        """
        Calculate statistics from data.
        Individual calculations are described in comments.
        """

        sum_of_squares = 0;
        lower_quartile_index_1 = 0
        lower_quartile_index_2 = 0

        # data needs to be sorted for median etc
        self.data.sort()

        # count is just the size of the data set
        self.count = len(self.data)

        # initialize total to 0, and then iterate data
        # calculating total and sum of squares
        self.total = 0
        for i in self.data:
            self.total += i
            sum_of_squares += i ** 2

        # the arithmetic mean is simply the total divided by the count
        self.arithmetic_mean = self.total / self.count

        # method of calculating median and quartiles is different for odd and even count
        if self.__is_even(self.count):

            self.median = (self.data[int(((self.count) / 2) - 1)] + self.data[int(self.count / 2)]) / 2


            if self.__is_even(self.count / 2): # even / even

                lower_quartile_index_1 = (self.count / 2) / 2
                lower_quartile_index_2 = lower_quartile_index_1 - 1

                self.lower_quartile = (self.data[int(lower_quartile_index_1)] + self.data[int(lower_quartile_index_2)]) / 2
                self.upper_quartile = (self.data[int(self.count - 1 - lower_quartile_index_1)] + self.data[int(self.count - 1 - lower_quartile_index_2)]) / 2

            else: # even / odd

                lower_quartile_index_1 = ((self.count / 2) - 1) / 2

                self.lower_quartile = self.data[lower_quartile_index_1]
                self.upper_quartile = self.data[self.count - 1 - lower_quartile_index_1]

        else:

            self.median = self.data[((self.count + 1) / 2) - 1]

            if self.__is_even((self.count - 1) / 2): # odd / even
                lower_quartile_index_1 = ((self.count - 1) / 2) / 2
                lower_quartile_index_2 = lower_quartile_index_1 - 1

                self.lower_quartile = (self.data[lower_quartile_index_1] + self.data[lower_quartile_index_2]) / 2
                self.upper_quartile = (self.data[self.count - 1 - lower_quartile_index_1] + self.data[self.count - 1 - lower_quartile_index_2]) / 2

            else: # odd / odd
                lower_quartile_index_1 = (((self.count - 1) / 2) - 1) / 2

                self.lower_quartile = self.data[lower_quartile_index_1]
                self.upper_quartile = self.data[self.count - 1 - lower_quartile_index_1]

        # the data is sorted so the mimimum and maximum are the first and last values
        self.minimum = self.data[0]
        self.maximum = self.data[self.count - 1]

        # the range is difference between the minimum and the maximum
        self.overall_range = self.maximum - self.minimum
        # and the inter-quartile range is the difference between the upper and lower quartiles
        self.inter_quartile_range = self.upper_quartile - self.lower_quartile

        # this is the formula for the POPULATION variance
        self.variance_population = (sum_of_squares - ((self.total ** 2) / self.count)) / self.count

        # the standard deviation is the square root of the variance
        self.standard_deviation_population = math.sqrt(self.variance_population);

        # the formula for the sample variance is slightly different in that it use count -1
        self.variance_sample = (sum_of_squares - ((self.total ** 2) / self.count)) / (self.count - 1)

        # the sample standard deviation is the square root of the sample variance
        self.standard_deviation_sample = math.sqrt(self.variance_sample)

        # this is Pearson's second skewness coefficient, one of many measures of skewness
        self.skew = (3.0 * (self.arithmetic_mean - self.median)) / self.standard_deviation_population;
