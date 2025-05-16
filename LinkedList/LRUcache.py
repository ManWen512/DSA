M a n W a n
man_wan
Invisible

Never — 9/28/2024 5:21 PM
NEXT_PUBLIC_API_BASE_URL=http://localhost:8080/api
M a n W a n — 9/28/2024 5:47 PM
Image
PEARL
 just slid into the server. — 9/29/2024 2:59 PM
M a n W a n — 9/29/2024 4:00 PM
https://github.com/ManWen512/easy_budget_MW
GitHub
GitHub - ManWen512/easy_budget_MW
Contribute to ManWen512/easy_budget_MW development by creating an account on GitHub.
GitHub - ManWen512/easy_budget_MW
Never — 9/30/2024 10:13 PM
@M a n W a n
hyg
Never — 10/19/2024 4:23 PM
@echo off
setlocal

:: Define directories
set BACKEND_DIR=path\to\your\backend
set FRONTEND_DIR=path\to\your\frontend

:: Run backend in a new command window
echo Starting backend...
start "Backend" cmd /c "cd /d %BACKEND_DIR% && mvn spring-boot:run"

:: Run frontend in a new command window
echo Starting frontend...
start "Frontend" cmd /c "cd /d %FRONTEND_DIR% && npm run dev"

:: Open localhost:3000 in default browser
echo Opening localhost:3000 in your default web browser...
start http://localhost:3000/

:: Wait for user to press Ctrl+C
echo Press Ctrl+C to stop both applications.
pause >nul

:: Cleanup processes (assumes Maven and Node.js are running)
taskkill /IM java.exe /F
taskkill /IM node.exe /F

endlocal
Never — 10/19/2024 4:46 PM
timeout /t 5 /nobreak
echo Waiting for 5 seconds...
:: Define Chrome path (replace with the actual path to chrome.exe)
set CHROME_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
start "" %CHROME_PATH% http://localhost:3000/
Never — 10/19/2024 5:14 PM
75@#5%Hq82*$^6%7
burmeseapp_next
Never — 10/19/2024 5:21 PM
burmeseapp_spring
Never — 10/22/2024 10:41 PM
https://nextjs.org/docs/pages/api-reference/components/image
Components:  | Next.js
Optimize Images in your Next.js Application using the built-in `next/image` Component.
Components:  | Next.js
min laptop mhr fb/msgr/viber shi lr?
discord ka line kya nay loz
msgr ka call lite
M a n W a n — 11/27/2024 7:01 PM
updated notion
PEARL — 1/22/2025 10:15 PM
https://learnenglishkids.britishcouncil.org/fun-games/games
PEARL — 1/22/2025 10:31 PM
https://pbskids.org/daniel/games/stargazing
PEARL — 1/22/2025 10:50 PM
https://pbskids.org/wombats/games/toy-maker
Work It Out Wombats! . Games . Toy Maker | PBS KIDS
Create toys with Zadie and Gramma Super! Kids and grown-ups, play together to create, test, and improve toys for the Everything Emporium.
M a n W a n — 1/22/2025 10:57 PM
https://elevenlabs.io/app/speech-synthesis/text-to-speech
ElevenLabs
AI Voice Generator & Text to Speech
Rated the best text to speech (TTS) software online. Create premium AI voices for free and generate text to speech voiceovers in minutes with our character AI voice generator. Use free text to speech AI to convert text to mp3 in 29 languages with 100+ voices.
AI Voice Generator & Text to Speech
PEARL — 1/22/2025 11:04 PM
https://www.numuki.com/games/dora-the-explorer/
Dora the Explorer Games | Play Online for Free | NuMuKi
Practice Spanish, spelling, math, and music with the Dora the Explorer Games! Join Dora, Boots, and their friends for fun and educational adventures!
Dora the Explorer Games | Play Online for Free | NuMuKi
M a n W a n — 1/25/2025 7:58 PM
Image
Never — 1/25/2025 8:53 PM
@M a n W a n
Never — 1/25/2025 9:05 PM
https://www.flaticon.com/
https://particles.js.org/
tsParticles
tsParticles - JavaScript Particles, Confetti and Fireworks animatio...
Easily create highly customizable particles, confetti and fireworks animations and use them as animated backgrounds for your website. Ready to use components available for React, Vue.js (2.x and 3.x), Angular, Ember.js, Svelte, jQuery, Preact, Inferno.
tsParticles - JavaScript Particles, Confetti and Fireworks animatio...
PEARL — 1/25/2025 9:17 PM
Image
M a n W a n — 1/25/2025 9:40 PM
Image
Image
Image
PEARL — 1/25/2025 10:22 PM
https://youtu.be/7Nwj3w-54rg?si=wnPhmZ1wE1zty63r
YouTube
ToughGamingGuy
Dora the Explorer™: Backpack Adventure (PC 2002) - Full Game HD Wal...
Image
Never — 2/2/2025 7:57 PM
https://scratch.mit.edu/projects/597244481
M a n W a n — 2/7/2025 7:34 PM
hi
Image
M a n W a n — 2/7/2025 8:02 PM
https://themewagon.com/theme-tag/portfolio-template/
ThemeWagon
Portfolio Template Archives
Give your portfolio template an exciting look. Visit a huge collection of Free & responsive portfolio templates of ThemeWagon.
M a n W a n — 2/28/2025 7:58 PM
https://stellar-flan-44e7bb.netlify.app/
M a n W a n — 3/5/2025 12:11 AM
athan ma kyrr ya bu
Never — 3/9/2025 7:07 PM
@M a n W a n
Never — 3/23/2025 7:44 PM
https://www.cs.usfca.edu/~galles/visualization/Algorithms.html
Never — 3/23/2025 8:24 PM
Definition for a binary tree node.
class TreeNode:
def init(self, val=0, left=None, right=None):
self.val = val
self.left = left
self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        queue = deque([root])

        while queue:
            cur_node = queue.popleft()

            if cur_node and (cur_node.left or cur_node.right):
                diff = abs(maxHeight(cur_node.left) - maxHeight(cur_node.right))
                # print(maxHeight(root.left), maxHeight(root.right))

                if diff > 1:
                    return False

                queue.append(cur_node.left)
                queue.append(cur_node.right)

        return True

def maxHeight(root):

        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        return max(maxHeight(root.left), maxHeight(root.right)) + 1
Never — 3/30/2025 9:23 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        row_len = len(grid)
        col_len = len(grid[0])
        count = 0
        for row in range(row_len):
            for col in range(col_len):
                cur_str = str(row) + "," + str(col)
                if cur_str not in visited:
                    if grid[row][col] == "1":
                        self.check(row, col, visited, grid)
                        count += 1

        return count

    def check(self, row, col, visited, grid):
        cur_str = str(row) + "," + str(col)
        if cur_str in visited:
            return

        visited.add(cur_str)

        if grid[row][col] != "1":
            return
        else:
            # up
            if row - 1 >= 0:
                self.check(row-1, col, visited, grid)

            # down
            if row + 1 < len(grid):
                self.check(row+1, col, visited, grid)

            # left
            if col - 1 >= 0:
                self.check(row, col-1, visited, grid)

            #  right
            if col + 1 < len(grid[0]):
                self.check(row, col+1, visited, grid)
M a n W a n — 3/30/2025 10:02 PM
Image
Never — 3/31/2025 8:21 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        queue = deque([])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append([row, col])

        while queue:
            print(queue)
            rot_change = False
            for i in range(len(queue)):
                cur_list = queue.popleft()
                cur_row = cur_list[0]
                cur_col = cur_list[1]

                if grid[cur_row][cur_col] == -1 or grid[cur_row][cur_col] == 0:
                    continue

                if grid[cur_row][cur_col] == 1:
                    rot_change = True
                grid[cur_row][cur_col] = -1 # for both 2 and 1

                # up
                if cur_row - 1 >= 0:
                    queue.append([cur_row-1, cur_col])

down
                if cur_row + 1 < len(grid):
                    queue.append([cur_row+1, cur_col])

                # left
                if cur_col - 1 >= 0:
                    queue.append([cur_row, cur_col-1])

                # right
                if cur_col + 1 < len(grid[0]):
                    queue.append([cur_row, cur_col+1])

            if rot_change == True:
                mins += 1

        print(grid)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        return mins
Never — 4/13/2025 7:43 PM
Definition for singly-linked list.
class ListNode:
def init(self, val=0, next=None):
self.val = val
self.next = next
class Solution:
    # recursive is basically dfs
    # goes to the last node first before doing any operation
    # think operation: 1 <- 2 <- 3 <- 4 <- 5
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # for empty node edge case and last node case
        if not head or not head.next:
            return head

this result is to carry last node to first call stack
call dfs here so the program goes to the last node first before doing any reversing
        result = self.reverseList(head.next)

        # reverse part
        head.next.next = head
        head.next = None

        return result
Never — 4/15/2025 5:35 PM
@M a n W a n
hyg
ngr yauk p naw
Never — 4/28/2025 7:07 PM
@M a n W a n
hi
Never — 5/14/2025 2:06 AM
https://achavezmixco.com/
Alvaro Chavez Mixco, Game Developer
Alvaro Chavez Mixco, Game Developer
A game developer specialising on programming, with experience coding in both C# and C++
Image
Kevin
 just slid into the server. — 5/14/2025 6:33 PM
Never — 8:52 PM
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
Expand
message.txt
4 KB
﻿
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def move_front(self, move_node):
        # if head
        if self.head == move_node:
            return

        # if tail
        if self.tail == move_node:
            self.tail = move_node.prev

        # remove node
        # Remove from current position
        if move_node.prev:
            move_node.prev.next = move_node.next
        if move_node.next:
            move_node.next.prev = move_node.prev

        # move to head
        self.head.prev = move_node
        move_node.next = self.head
        move_node.prev = None
        self.head = move_node

    def get(self, key: int) -> int:
        
        # linked_list = []
        # cur_node = self.head
        # while cur_node:
        #     linked_list.append(cur_node.value)
        #     cur_node = cur_node.next
        # print("linked_list: ", linked_list) 
        # if self.head and self.tail:
        #     print("head: ", self.head.value)
        #     print("tail: ", self.tail.value)
        # print("get node: ", key)
        # print()

        if key in self.cache:
            # print("get node: ", key)
            cur_node = self.cache[key]
            self.move_front(cur_node)
            return cur_node.value
        return -1

    def put(self, key: int, value: int) -> None:
        
        # linked_list = []
        # cur_node = self.head
        # while cur_node:
        #     linked_list.append(cur_node.value)
        #     cur_node = cur_node.next
        # print("linked_list: ", linked_list) 
        # if self.head and self.tail:
        #     print("head: ", self.head.value)
        #     print("tail: ", self.tail.value)
        # print("put node: ", key)
        # print()

        # found case
        if key in self.cache:
            cur_node = self.cache[key]
            cur_node.value = value
            print("found > move front")
            self.move_front(cur_node)
            return

        # not found case
        if len(self.cache) >= self.capacity:
            self.cache.pop(self.tail.key)
            # edge case
            if self.capacity == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            
        new_node = Node(key, value)

        # first node
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        # other nodes
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        # all nodes
        self.cache[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)