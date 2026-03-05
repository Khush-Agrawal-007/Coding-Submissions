from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_counts = Counter(words)
        results = []

        # Iterate through all possible starting offsets
        for i in range(word_len):
            left = i
            right = i
            current_counts = Counter()
            count = 0
            
            # Slide the window across the string
            while right + word_len <= len(s):
                # Get the word from the right side of the window
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_counts:
                    current_counts[word] += 1
                    count += 1
                    
                    # If we have more of 'word' than needed, shrink from the left
                    while current_counts[word] > word_counts[word]:
                        left_word = s[left:left + word_len]
                        current_counts[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # If count matches num_words, we found a valid starting index
                    if count == num_words:
                        results.append(left)
                else:
                    # Invalid word: reset the window
                    current_counts.clear()
                    count = 0
                    left = right
                    
        return results