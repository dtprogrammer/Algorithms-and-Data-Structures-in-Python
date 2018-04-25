class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        >>> s.fizzBuzz(15)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        """
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]


if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'s': Solution()})
