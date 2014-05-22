"""
Notes moreso than code. First session thinking about Kata01
May 22 2014


1. Things in supermarket have prices
2. Some price attributes are more complex
    a. 3 for 1 dollar -- which can be simply $0.333 (to some arbitrary precision), or can be 1 dollar for
       each quantity of three, strictly (such that price attribute follows an if/else), 
       or could be that price 
    b. 1.99/pound, price for 4 oz? -- this one doesn't strike me as being so deep. Simple dimensional 
       analysis; convert oz to pounds and calculate/store price with respect to pounds. You've gotta pick
       a primary base unit and have everything else be measured with respect to it. 
    c. Buy two, get one free -- price could be modified across all three (such that price is 2/3 of normal 
       value, this probably works best for cases like returns and the like), or could have one have a price 
       of 'None' or '$0.00', although I don't like this so much, for cases of returns or recalls you need some
       logic to determine which is the uniquely priced item.
3. Other features of price
    a. Does fractional money exist? -- It does at gas stations (they always have the 9/10ths of a penny after
       the displayed price.) I think that if there's a business incentive for it, fractional money exists.
    b. When (if ever) does rounding take place? -- Probably only right before a gross exchange of money between 
       two real-world parties. Very finely tuned prices exist in the real-world, although bank accounts and hard
       money only support currency exchanges to a specified precision (e.g. the cent/$0.01 for the US).
    c. Are costs and prices the same thing? -- This one could get really complicated. Do we want this code to track
       what comes into the store as well as what goes out? Do we want to use finely tuned prices? In an economic sense,
       cost should be the number attribute to get something on the shelf (this number may or may not include overhead).
       I'm guessing that most large supermarkets track the costs (again, number to get something on the shelf) as well
       as inventory flow (e.g. number of an item sold per week, let's say) and dynamically adjust the price to reflect 
       this. There's probably also something relating to total overhead that comes into the equation too (e.g. most of 
       us tend to notice that stores in high real-estate areas cost considerably more than stores elsewhere. My guess
       is that most of the price passed to the consumer is high real-estate areas is overhead, at least in most cases).
       Costs and price are related data types, and possibly of the same class (or otherwise highly related in terms of 
       datatype inheritence), but cost is ultimately an input variable for the function that determines price.
    d. If a shelf of 100 cans is priced using "buy two, get one free", how do you value the stock? -- I'm guessing that
       most supermarkets are interested in revenue flow, and have some kind of predictive model for determining the number
       of cans that are likely to flow through the shelves, given the store attributes and given the price. So while the price 
       of each can is ultimately (2/3) of normal, the store is probably most interested in the customer-price times the number 
       that are likely to be sold (as well as the past-tense version, which would probably be used against past predictions to 
       fine-tune the price modeling. (The customer-facing price needs to be a separate attribute from the 'normal' price, such 
       that 'sale' prices and 'normal prices can be switched to-and-fro without somesort of complicated 
       logic.)

4. Next Steps
    a. Revisit and revise. Read what I wrote, clarify where necessary, extend where necessary.
    b. Make a class diagram, save as .png. Build a data-model that feels 'bulletproof' and extensible with respect to the my 
       notes above.
    c. Mock up the class diagram as Python code. Keep it really simple, stupid. Fully capture (b) but do no more. Most of my 
       functions should have 'pass' in them.
"""
