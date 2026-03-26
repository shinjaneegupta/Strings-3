# Time Complexity : O(log n to the base 10) -> O(1) (Not more than 4 iterations)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Approach : We split the number into 3-digit chunks from right to left and process each chunk separately.
# Each chunk is converted into words using simple rules—handle small numbers directly, combine tens and ones, or add “Hundred” if needed.
# Then we join the word parts with proper labels like "Thousand" or "Million", clean up spaces, and that's our final sentence.

class Solution:
    thousands = ["", " Thousand ", " Million ", " Billion "]
    below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy","Eighty", "Ninety"]

    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        i = 0
        result = []

        while num > 0:
            triplet = num % 1000
            if triplet > 0:
                result.insert(0, self.helper(triplet).strip() + self.thousands[i])
            num //= 1000
            i += 1

        return "".join(result).strip()

    def helper(self, num: int) -> str:
        result = []
        if num < 20:
            result.append(self.below_20[num])
        elif num < 100:
            result.append(self.tens[num // 10])
            result.append(" ")
            result.append(self.below_20[num % 10])
        else:
            result.append(self.below_20[num // 100])
            result.append(" Hundred ")
            result.append(self.helper(num % 100))
        return "".join(result)