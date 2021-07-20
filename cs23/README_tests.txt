Read Me for FSM Test Cases:
Disclaimer: Professor Hodges has not verified these solutions or these FSM's. The diagrams may be incorrect.
Or the way I drew them may be incorrect.
Use at your own risk.

These are the solutions I got, possible there are errors!!!

FSM_simple_Nondeterministic:
	Nondeterministic
	Any combination of 0's and 1's that has a minimum of two 0's and ends with one or more 0's
	Language {0, 1}
	Solutions:
		State-Set | Solution
		{0, 1, 2, 3} Accepted
		{4} Rejected
		{2, 3, 4} Accepted
		{3, 4} Accepted
		{0, 1, 2, 3} Accepted
		{3, 4} Accepted
		{2, 3, 4} Accepted
		{1, 4} Rejected
		{0, 1, 2} Rejected
		{1, 4} Rejected

Grid_FSM:
	Deterministic
	In theory if you have a 3x3 square grid, and you lay out copies of this grid end to end infinitely
        in all directions (making a larger grid, composed on the smaller grids), accepting state is when you
	end in the center of a smaller grid. I didn't work out the RegEx for this one.
	Assume that 0 is up, 1 is to the right, 2 is down, and 3 is to the left
	Language{0, 1, 2, 3}
	Solutions:
		State-Set | Solution
		{0} Accepted
		{0} Accepted
		{0} Accepted
		{0} Accepted
		{0} Accepted
		{8} Rejected
		{8} Rejected
		{8} Rejected
		{4} Rejected
		{5} Rejected
		{1} Rejected
		{1} Rejected
		{3} Rejected
		{2} Rejected

Email_FSM:
	Nondeterministic
	This finite state machine takes a string and determines if it is a .com or .net email address (restrictions for
	this FSM are less accepting than real RegEx for email addresses). The rules this FSM operates on are:
		1. There can be at most 1 @ character
		2. The email must end in .com or .net
		3. There is no requirement for length before @ or between @ and .net/.com
			(@.net or @.com are accepted)
	The alphabetical characters checked by the FSM {a-z, ., @} are translated numerically meaning:
	Language={0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}
	Solutions:
		State-Set | Solution
		{1, 2, 6} Accepted
		{1, 2, 9} Accepted
		{10} Rejected
		{1, 2, 9} Accepted
		{1, 2, 6} Accepted
