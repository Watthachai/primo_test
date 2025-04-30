#https://neetcode.io/problems/anagram-groups

# Given an array of strings, group the anagrams together. You can return the answer in any order.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# An example of an anagram is "anagram" and "nagaram".
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# 1 <= strs[i].length <= 100
# 0 <= sum(strs[i].length) <= 10^4
# 1 <= strs[i].length <= 100
# 0 <= sum(strs[i].length) <= 10^4

"""
โจทย์:
ข้อนี้คือ Group Anagrams จาก NeetCode ให้ list ของคำมา ให้จัดกลุ่มคำที่เป็น anagram ของกันและกัน

แนวคิด:
ผมใช้หลักการว่า “ถ้าคำไหนเป็น anagram กัน เมื่อนำตัวอักษรในคำนั้นมาเรียงลำดับ (sort) แล้วจะได้ผลลัพธ์เหมือนกัน”
ดังนั้นผมจะวนลูปแต่ละคำใน list แล้วนำตัวอักษรมาเรียงลำดับ จากนั้นใช้ string ที่เรียงแล้วเป็น key ใน dictionary
ถ้า key นี้ยังไม่เคยมีใน dictionary ก็สร้าง list ใหม่ขึ้นมา แล้วเอาคำเดิมไป append ใน list ของ key นั้น
สุดท้าย return เฉพาะค่าของ dictionary ซึ่งจะเป็น list ของ list ที่แต่ละ list คือกลุ่ม anagram

อธิบายโค้ด:

- สร้าง dictionary สำหรับเก็บกลุ่ม anagram
- วนลูปแต่ละคำใน list
- ใช้ sorted() เพื่อเรียงตัวอักษร แล้วแปลงกลับเป็น string เพื่อใช้เป็น key
- ถ้า key ยังไม่มีใน dictionary ให้สร้าง list ใหม่
- เอาคำเดิมไปใส่ใน list ของ key นั้น
- สุดท้าย return เฉพาะค่าของ dictionary

ตัวอย่าง:
เช่น input ["eat", "tea", "tan", "ate", "nat", "bat"]

"eat", "tea", "ate" เมื่อ sort แล้วจะได้ "aet" เหมือนกัน
"tan", "nat" เมื่อ sort แล้วจะได้ "ant"
"bat" เมื่อ sort แล้วจะได้ "abt"
ผลลัพธ์คือ [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Time Complexity:
O(N * K log K)

N คือจำนวนคำ
K คือความยาวเฉลี่ยของแต่ละคำ (เพราะต้อง sort ตัวอักษรแต่ละคำ)

Space Complexity:
O(N * K) สำหรับเก็บผลลัพธ์และ dictionary

สรุป:
"ผมใช้การ sort ตัวอักษรในแต่ละคำเพื่อสร้าง key สำหรับ grouping anagram ใน dictionary 
ทำให้สามารถจัดกลุ่ม anagram ได้อย่างมีประสิทธิภาพและรวดเร็วครับ"

"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to hold the anagrams
        anagrams = {}
        
        # Iterate through each string in the input list
        for s in strs:
            # Sort the string and use it as a key
            key = ''.join(sorted(s))
            # If the key is not in the dictionary, add it with an empty list
            if key not in anagrams:
                anagrams[key] = []
                # Append the original string to the list for this key
            anagrams[key].append(s)
            
        # Return the values of the dictionary as a list of lists
        return list(anagrams.values())
            
# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    test1 = ["act", "pots", "tops", "cat", "stop", "hat"]
    result1 = solution.groupAnagrams(test1)
    print("Test 1 input:", test1)
    print("Test 1 output:", result1)
    
    # Test case 2
    test2 = ["x"]
    result2 = solution.groupAnagrams(test2)
    print("\nTest 2 input:", test2)
    print("Test 2 output:", result2)
    
    # Test case 3
    test3 = [""]
    result3 = solution.groupAnagrams(test3)
    print("\nTest 3 input:", test3)
    print("Test 3 output:", result3)
    
    # Additional test case
    test4 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result4 = solution.groupAnagrams(test4)
    print("\nTest 4 input:", test4)
    print("Test 4 output:", result4)