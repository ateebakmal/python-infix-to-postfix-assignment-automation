from PostixAssignmentSolver import PostixAssignmentSolver

question = ["(A+B)*(C-D)", "A^B*C-D+E/F", "A/(B+C*D-E)" , "A-B*C+D/E" , "(A+B)^2-(C-D)/2" ]
x = PostixAssignmentSolver()
x.solveInfixToPostfix(question)