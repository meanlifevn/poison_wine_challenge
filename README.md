# Poison wine challenge

**Note: This is a simple code as I am just starting from scratch. I will improve my code in the future.**

In this repo, I try to code a solution to a puzzle. The question is as follows:

"The King of a small country invites 1000 senators to his annual party. As a tradition, each senator brings the King a bottle of wine. Soon after, the Queen discovers that one of the senators is trying to assassinate the King by giving him a bottle of poisoned wine. Unfortunately, they do not know which senator, nor which bottle of wine is poisoned, and the poison is completely indiscernible. However, the King has 10 prisoners he plans to execute. He decides to use them as taste testers to determine which bottle of wine contains the poison. The poison when taken has no effect on the prisoner until exactly 24 hours later when the infected prisoner suddenly dies. The King needs to determine which bottle of wine is poisoned by tomorrow so that the festivities can continue as planned. Hence he only has time for one round of testing. How can the King administer the wine to the prisoners to ensure that 24 hours from now he is guaranteed to have found the poisoned wine bottle?"

## The solution
The solution I used is to label each bottle with both its decimal number and binary equivalent.
In this question, I replace 'prisoners' with 'rats' to avoid human rights issues.

## Task 1: There are 1000 wine bottles, and 1 is poisoned. We use 10 rats to find the location of the poisoned wine.
There is no data available, so I will generate new data with 2 objects: Wine and Rat.\\

The 'Wine' object has 2 attributes: 'ID_wine', 'is_poisoned'.\\
In this case, I set the type of 'ID_wine' is <int class>. I think I will change its type to <string class> in next time.\\

Remember, 'ID_wine' is not an index that describes the location of wine.\\
And, I set the type of 'is_poisoned' is <bool class>. If this is poison wine, 'is_poisoned' is 'True' and vice versa.\\
The 'Rat' object has 3 attributes: 'ID_rat', 'is_poisoned', and 'tried_wine'.\\
In this case, the types of the attributes 'ID_rat' and 'is_poisoned' are similar to 'ID_wine' and 'is_poisoned'. But 'is_poisoned' is the state of the rat, describing whether the rat is poisoned or not.
As for 'tried_wine', I want to store a list of wine bottle IDs that the rat has tried. So the type of 'tried_wine' is <list>.
