# Amjad-GPT-LangChain

This is the backend part of https://ai.repl.page.  

The OpenAI model being used is `text-davinci-003`, trained with:
 - Major parts of the [Replit docs](https://docs.replit.com)
 - The [Replit blog](https://blog.replit.com)
 - The Replit [landing page](https://replit.com)
 - The Replit Employee Organization Chart
 - Amjad's [personal blog](https://amasad.me)
 - Amjad's [AmA Repl](https://replit.com/@amasad/AmA?v=1)
 - Amjad's Podcasts
 - Some of [Amjad's Tweets](https://twitter.com/amasad)
 - Replit's [Terms of Service](https://replit.com/site/terms) and [Community guidelines](https://welcome.moderation.repl.co)
 - Some random facts the AI should be aware of

All of the training data should go in the `facts` folder, and then run `python process_data.py` to populate the `.index` file.

For more information on how this works, check out [Zahid Khawaja's Tutorial](https://replit.com/@zahidkhawaja/Replit-Assistant?v=1).

 - [Frontend Source Code](https://github.com/Conner1115/Amjad-GPT)
 - [Live Demo](https://ai.repl.page)