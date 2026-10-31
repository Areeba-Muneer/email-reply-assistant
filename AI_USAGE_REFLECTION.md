# AI Usage Reflection (draft; personalize to your real work)

I used an AI assistant as a learning aid while planning and implementing my AI-Powered Email Reply Assistant. It helped me divide the application into smaller modules: the visual interface, prompt construction, API communication, and output validation. I reviewed the code and used the assignment requirements to decide what the application needed.

Prompt engineering is important because the model needs clear information about the reply goal and tone. The application sends the original email with the selected purpose and tone. The prompt asks the model not to invent facts and to return only the email reply. The temperature slider lets a user choose between more consistent output and more varied wording.

The interface checks that the original email is not empty before calling the API. The API client also gives understandable errors for common problems such as a missing or rejected API key, quota limits, and connection failures. Generated text is checked before it is displayed.

AI-generated code still needs human review. I should run the application, test different examples, and correct any issues I find. Before sending a generated email, a person should verify names, dates, promises, and other important details. I will update this reflection to describe the tests I actually performed.
