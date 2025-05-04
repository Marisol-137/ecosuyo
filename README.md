# Ecosuyo

## Description 
Our app equips Peruvian micro and small enterprises (MYPES) with an innovative AI-powered financial management tool designed to simplify financial analysis and boost profitability through personalized insights based on real data from sales, expenses, and products. It delivers timely alerts, clear diagnostics, and actionable strategies to help businesses optimize spending, adjust pricing, identify their most profitable products, and forecast financial trends, enabling sustainable and informed growth.

Ecosuyo also promotes linguistic and cultural inclusion by incorporating interfaces and voice recognition in Quechua, Aymara, and indigenous languages of the Peruvian Amazon which are often overlooked in financial education, which is typically offered only in Spanish or English. This approach reduces the technological gap for older adults accustomed to managing their finances on paper, fostering broader accessibility.

By combining innovation with inclusivity, Ecosuyo directly contributes to the United Nations Sustainable Development Goals (SDGs), particularly Goal 8: Decent Work and Economic Growth and Goal 9: Industry, Innovation, and Infrastructure, supporting entrepreneurship, technological advancement, and increased economic productivity across diverse communities in Peru.

## Problem and solution statement 
Peruvian micro and small enterprises (MYPES), especially in rural and indigenous regions, face major challenges in managing their finances due to limited access to inclusive financial tools, language barriers, and a reliance on paper-based methods. Most available financial education and technologies are offered only in Spanish or English, excluding speakers of Quechua, Aymara, and Amazonian languages. This linguistic gap, combined with low digital literacy particularly among older adults, leads to poor financial decision-making, inefficient resource use, and limited business growth.

Ecosuyo is an AI-powered financial assistant designed specifically for Peruvian MYPES, offering personalized recommendations based on real data from sales, expenses, and products to improve profitability and financial sustainability. The platform provides timely alerts, practical insights, and strategic forecasts, while promoting inclusion through voice recognition and interfaces in Quechua, Aymara, and Amazonian languages. By bridging the gap between advanced financial tools and culturally relevant accessibility, Ecosuyo empowers diverse entrepreneurs to manage their businesses more effectively and contributes directly to SDG 8 (Decent Work and Economic Growth) and SDG 9 (Industry, Innovation, and Infrastructure).

## AI-powered virtual agent using IBM watsonx.ai 
Ecosuyo is an AI-powered financial assistant specifically designed to support micro and small enterprises (MYPES) in Peru. Its modular architecture combines data preprocessing, intelligent inference, multilingual interaction, and an intuitive user interface to deliver accessible, personalized financial analysis and inclusive decision-making support.

The data processing layer is built using Python, where libraries such as Pandas and NumPy are employed to structure, clean, and transform financial information provided by users via CSV uploads, forms, or APIs. This stage enables the calculation of derived metrics such as profit margins, expenditure classifications, and monthly variations, producing a clean and standardized dataset ready for AI analysis.

The system’s intelligence lies in its integration with IBM Watsonx.ai, specifically the Granite model, connected through the LangChain library. This foundation model interprets both structured and unstructured data to provide contextual financial diagnostics, detect anomalies such as cost overruns or consistent losses, and generate personalized recommendations for each business. Unlike traditional tools based on rigid rules, Granite applies deep learning and natural language processing techniques, allowing it to adapt dynamically to each enterprise’s historical patterns and context.

Ecosuyo also promotes technological and linguistic inclusion by incorporating voice recognition capabilities in indigenous languages such as Quechua, Aymara, and Amazonian dialects. This is achieved using fine-tuned Whisper models and Hugging Face Transformers, trained with language-specific corpora. The system interprets spoken questions like “Am I making a profit?” in native languages and translates them into financial queries processed by the AI model, reducing barriers for elderly or rural entrepreneurs who may not be familiar with Spanish or digital interfaces.

The user interface is built with Streamlit. It offers interactive dashboards where users can upload financial records, monitor their income and expenses, compare product profitability, receive automatic alerts, and access tailored strategies. Firebase handles secure authentication, data storage, and cloud synchronization on the backend, ensuring scalability and data protection across user sessions.

Lastly, Ecosuyo features a feedback mechanism through which users can validate, reject, or adjust the recommendations they receive. This information is periodically sent back to the AI system to improve prediction accuracy and adaptability. Through this ongoing learning process, Ecosuyo evolves with each business, enhancing its responses to shifting financial conditions.


## Video demonstration URL 
Video demonstration:

## Demo
Live Demo: 
Video Demo:
