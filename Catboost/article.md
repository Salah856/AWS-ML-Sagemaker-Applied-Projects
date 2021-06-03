
# Edelweiss improves cross-sell using machine learning on Amazon SageMaker


How are you being recommended a credit card based on your savings account behavior? How about a life insurance product when you buy car insurance, or a side dish when you order a main course on your food ordering app? These are done using a practice called cross-sell, which invites customers to buy related or complimentary items based on their current purchases. In the insurance business particularly, it’s often easier to cross-sell to existing customers than to acquire new customers. 

For example, the odds are better of selling an investment or retirement policy to an existing life insurance customer than trying to approach a random new lead.

However, if the cross-sell approach isn’t data driven, it often leads to the wrong selection of customers or policies. If you’re annoyed at times when an irrelevant product is being offered to you repeatedly, the cross-sell strategy didn’t do a good job. For businesses, this results in missed opportunities and diminished customer-satisfaction.

## Formulating an ML solution

While we were conceiving an accurate cross-sell solution, we were mindful of its ability to adapt with changing customer behavior and product (policy) features. ML was a natural choice in this context. We defined the solution as a combination of two different ML models:

#### Cross-sell propensity model 

When you have tens of thousands of customers to cross-sell to, your first priority is to find the most promising prospects from them. A supervised classification model was conceptualized for this purpose. It was designed to identify the cross-sell prospects along with a propensity score between 0–1, indicating the likelihood of conversion (1 being the highest). You can use the propensity scores to group the classified prospects into different priority segments for further perusal by business teams.

#### Policy recommendation model

After you identify a cross-sell prospect, you need to know what policies will serve them best. That is where the recommendation engine came into the picture. Its purpose was to rank and recommend the top three policies for each prospect.

## Early insights from the data
We started with around 100,000 records with over 200 attributes around customers and policies. Existing cross-sell cases could be labeled using a set of business rules.


## Building the propensity model using SageMaker

Data volume and the nature of the data were the primary considerations while deciding on the solution for the propensity classification model. Because the data was fully structured and not too high in volume, neural network-based variants weren’t the most suitable options. Ensemble method-based classifiers, on the other hand, seemed to be the apt choice, especially considering the high dimensionality of data and the large number of categorical features, many with high cardinality.

Because one-hot encoding fails to scale for high-cardinality features, we had to consider other options, such as label encoding, hash encoding, and target encoding. We used CatBoost, a gradient boosting-based, ensemble learning framework that offers a robust mechanism for handling and combining categorical data. Following the ensemble modeling principles, CatBoost combines many binary decision trees (weak learners) to form a unified model (strong learner). It estimates target statistic to represent the categories of each high-cardinality categorical feature and subsequently clusters those category values into a small number of groups. Then, the small number of groups representing the categorical features are one-hot encoded or label encoded.

This approach helps handle very high cardinality without losing their associations with the target variable. Other noteworthy benefits are ordered boosting, addressing the prediction shift (latent target leakage) problems due to greedy boosting in regular gradient boosting approaches, and feature combinations, which help generate new features by combining multiple categorical features, thereby improving the predictive power of the model.

