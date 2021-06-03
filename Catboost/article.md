
# Edelweiss improves cross-sell using machine learning on Amazon SageMaker


How are you being recommended a credit card based on your savings account behavior? How about a life insurance product when you buy car insurance, or a side dish when you order a main course on your food ordering app? These are done using a practice called cross-sell, which invites customers to buy related or complimentary items based on their current purchases. In the insurance business particularly, it’s often easier to cross-sell to existing customers than to acquire new customers. 

For example, the odds are better of selling an investment or retirement policy to an existing life insurance customer than trying to approach a random new lead.

However, if the cross-sell approach isn’t data driven, it often leads to the wrong selection of customers or policies. If you’re annoyed at times when an irrelevant product is being offered to you repeatedly, the cross-sell strategy didn’t do a good job. For businesses, this results in missed opportunities and diminished customer-satisfaction.

## Formulating an ML solution

While we were conceiving an accurate cross-sell solution, we were mindful of its ability to adapt with changing customer behavior and product (policy) features. ML was a natural choice in this context. We defined the solution as a combination of two different ML models:

### Cross-sell propensity model 

When you have tens of thousands of customers to cross-sell to, your first priority is to find the most promising prospects from them. A supervised classification model was conceptualized for this purpose. It was designed to identify the cross-sell prospects along with a propensity score between 0–1, indicating the likelihood of conversion (1 being the highest). You can use the propensity scores to group the classified prospects into different priority segments for further perusal by business teams.

### Policy recommendation model

After you identify a cross-sell prospect, you need to know what policies will serve them best. That is where the recommendation engine came into the picture. Its purpose was to rank and recommend the top three policies for each prospect.

## Early insights from the data
We started with around 100,000 records with over 200 attributes around customers and policies. Existing cross-sell cases could be labeled using a set of business rules.

