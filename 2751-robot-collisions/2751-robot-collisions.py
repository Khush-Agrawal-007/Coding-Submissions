class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        # Bundle data: [position, health, direction, original_index]
        n = len(positions)
        robots = [[positions[i], healths[i], directions[i], i] for i in range(n)]
        
        # Sort by physical position (left to right)
        robots.sort(key=lambda x: x[0])
        
        stack = []
        
        for p, h, d, i in robots:
            if d == 'R':
                # Right-moving robots go straight to the stack
                stack.append([p, h, d, i])
            else:
                # Left-moving robot: check for collisions with Right-moving robots on the stack
                while stack and stack[-1][2] == 'R' and h > 0:
                    if stack[-1][1] < h:
                        # Stack robot is destroyed, current robot loses 1 HP and continues
                        stack.pop()
                        h -= 1
                    elif stack[-1][1] > h:
                        # Current robot is destroyed, stack robot loses 1 HP
                        stack[-1][1] -= 1
                        h = 0
                    else:
                        # Both are destroyed
                        stack.pop()
                        h = 0
                
                # If the Left-moving robot survived, add it to the stack
                if h > 0:
                    stack.append([p, h, d, i])
                    
        # Sort the survivors by their original index to match the required output format
        stack.sort(key=lambda x: x[3])
        
        # Return only the healths of the survivors
        return [robot[1] for robot in stack]