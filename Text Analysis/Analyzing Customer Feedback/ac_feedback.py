# Jeph Mari Daligdig
# Customer Feedback Project
from Class.textAnalyzer_class import textAnalyzer

Customer1_Feedback = "I have been using the Cooler Master blue-switch Quick Fire Rapid mechanical keyboard for a while. I initially purchased it for my windows dedicated gaming PC, which I sold about three years ago. Overall, I've been happy with it, but it is the Windows version and over the last couple of years I've been using it on my 2020 MacBook Pro."
Customer2_Feedback = "I wanted a lighted tactical keyboard with bluetooth and USB connectivity. I found exactly that with this keyboard. I got an added bonus with the many different lighting schemes and the great versatility to use this for my MAC or Windows based system. So far I am very happy with this keyboard. I do not usually write reviews. The fact that I am writing a review should tell you how elated I am with this purchase. I would not hesitate to buy this product. "
Customer3_Feedback = "First off, unlike the other review currently up right now I don't find myself making any typing errors that I can blame on the keyboard. I use this mostly for work and as such I type A LOT, pretty much all I do is write e-mails all day, chat with coworkers and do some small amount of programming. Programming of course can't have typos in it, otherwise things simply don't work. Likewise, my e-mails and instructions to other people are very technical. A typo could make all the difference in the world with what I am trying to convey."
Customer4_Feedback = "I've had this keyboard for about 6 months; it is my first foray into modern mechanical keyboards. I've owned plenty of PS/2 style, old mechanical keyboards that worked great but looked hideous, and finally decided I needed an update for the sake of my office's aesthetic."
Customer5_Feedback = "I am not an LED nut but this kb is well appointed with choices for various LED displays. The weight and compact aspect of the kb is very nice as well as the wireless, Bluetooth and wired options all as a choice. The mechanical nature of this keyboard feels great while typing. Very responsive."
Customers_Feedback = (
    Customer1_Feedback
    + Customer2_Feedback
    + Customer3_Feedback
    + Customer4_Feedback
    + Customer5_Feedback
)


analyzed = textAnalyzer(Customers_Feedback)
print("Formatted Text:", analyzed.fmtText)
freqMap = analyzed.freqAll()
print(freqMap)

word = "keyboard"
frequency = analyzed.freqOf(word)
print("The word", word, "appears", frequency, "times")
