#Computer Vision RPS
The model has been trained with for different classes “Rock”, “Paper”, “Scissors”, and “Nothing”. 
For each class the camera of the computer has been used to makes around 100 images for each class where:
1.	 “Rock” is the hand in Rock position, 
2.	“Paper” is an open hand, 
3.	“Scissors” are fingers in scissors shape, and 
4.	“Nothing” is no hand included.
Needs to be said that background information is presents in the images, and it is expected that it may have a high impact on the model accuracy.
All photos have been taken using different angles and positions of my hand. 
After that, the model has been trained and exported.
There are build four functions:
1.	get_computer_choice()
2.	get_user_choice()
3.	get_winner()
4.	play()
get_computer_choice() randomly select an option between elements of the list rsp= ["Rock", "Paper","Scissors"]. And return the selected option.
get_user_choice() get an input from user which should be one of the options "Rock", "Paper", and "Scissors".
get_winner() is the function that determines which is the winner computer or user. If the winner is computer, then the output is “You lost!”, or if the winner is the user then the output is “you won!”, otherwise, the output is “It is a tie!”.


For more information how the “Rock”, “Paper”, “Scissors” works, it is described as follow based on https://en.wikipedia.org/wiki/Rock_paper_scissors:
 A player who decides to play rock will beat another player who has chosen scissors ("rock crushes scissors"), but will lose to one who has played paper ("paper covers rock"); a play of paper will lose to a play of scissors ("scissors cuts paper"). If both players choose the same shape, the game is tied and is usually immediately replayed to break the tie.
 
 
Play() function wraps all the functions get_computer_choice(), get_user_choice(), get_winner() and it returns get_winner(). Note that here it is demonstrated that a function can be called inside a function. To use the output of a function than return should be used, for example, outputs of get_computer_choice(), get_user_choice() are used as input of get_winner(), for that both of functions get_computer_choice(), get_user_choice() have return.


