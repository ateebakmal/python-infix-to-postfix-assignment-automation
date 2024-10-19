# python-infix-to-postfix-assignment-automation

#### Had a DSA Assignment which contained a lot of infix to postfix conversion questions and i had to show all the steps. Making tables for each question was tedious and boring so I decided to automate this stuff using python and `docx` library.

#### To use this library:
- clone this repo or copy my code into some python file
- import it into another file
- make a list which contains all the questions in string format
- make sure there is no space in questions

For example:
```python
from PostixAssignmentSolver import PostixAssignmentSolver

question = ["(A+B)*(C-D)", "A^B*C-D+E/F", "A/(B+C*D-E)" , "A-B*C+D/E" , "(A+B)^2-(C-D)/2" ]
x = PostixAssignmentSolver()
x.solveInfixToPostfix(question)
```


And it would solve all the questions, and make a word doc for each question in your current directory like this:
<br>
![image](https://github.com/user-attachments/assets/8de39d83-3865-46f0-b131-f7b54f40afef)

<br>

And the word file would look like this:
![image](https://github.com/user-attachments/assets/fd522448-b07c-41f9-b49e-99360c00e1d1)
<br>
You can make changes to the table or rows however you want by tweaking some things in the original code

### Happy Coding ;)
