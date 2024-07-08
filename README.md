# Text Summarizer
This project implements a text summarization pipeline using the Hugging Face Transformers library. It aims to create concise and coherent summaries from long-form text, leveraging state-of-the-art NLP models.

### Workflows

The project is structured to follow a modular and configurable workflow, making it easy to update and extend. Key workflows include:

1. **Configuration**:
   - Update `config.yaml`: Contains general configuration parameters.

2. **Execution**:
   - Modify `params.yaml`: Adjust parameters for data processing and model training.
   - Manage entities: Update entities relevant to your project.
   - Configure the manager in `src/config`: Ensure proper configuration management.
   - Update components: Modify components involved in the pipeline.
   - Update `main.py` and `app.py`: Ensure the main and application scripts are updated according to project changes.

### Output
<img width="945" alt="Screenshot 2024-07-08 at 7 53 55 PM" src="https://github.com/sumithanwate3/Text-Summarizer/assets/96422074/e417bed2-e4c2-4ca7-9c40-6dc0a8b59d2c">



### Project Overview

#### Dataset
- **Dataset Used**: Samsum dataset containing approximately 16k messenger-like conversations with summaries.
- **Dataset Link**: [Samsum Dataset](https://aclanthology.org/D19-5409/)

#### Model
- **Model Used**: Transformer-based models, specifically Pegasus, for summarization tasks.
- **Model Link**: [Pegasus Model](https://huggingface.co/google/pegasus-cnn_dailymail)
- **Model Paper**: [Pegasus: Pre-training with Extracted Gap-sentences for Abstractive Summarization](https://arxiv.org/abs/1912.08777)

#### Components Implemented
1. **Data Ingestion**
   - Downloads and extracts the dataset if not already present.
   - Handles data paths and configurations for further processing.

2. **Data Transformation**
   - Tokenizes and preprocesses the data for model training.
   - Converts examples into features suitable for training.

3. **Data Validation**
   - Validates the existence of required data files after ingestion and transformation.

4. **Model Training**
   - Trains a Pegasus model for sequence-to-sequence tasks.
   - Configures training parameters and data collation.

5. **Model Evaluation**
   - Evaluates the trained model using ROUGE metrics on a test dataset.
   - Calculates ROUGE scores (ROUGE-1, ROUGE-2, ROUGE-L, ROUGE-Lsum) for model performance assessment.

#### Technical Details
- **Libraries Used**: Transformers, datasets, pandas, torch, tqdm, nltk, and other utility libraries.
- **Environment**: Utilizes GPU acceleration if available for faster computation.
- **Code Organization**: Modular approach with configuration management (`ConfigurationManager`) for handling paths and parameters.

#### Execution and Results
- **Execution**: Each component (Ingestion, Transformation, Validation, Training, Evaluation) is executed sequentially.
- **Results**: Outputs ROUGE scores to evaluate the model's performance in summarization tasks.

#### Project Structure
- Organized into directories (`src/text_summarizer`) for code files (`constants.py`, `utils/common.py`, etc.) and data artifacts (`artifacts`).

#### Next Steps
- Potential enhancements could include hyperparameter tuning, additional metrics evaluation, and deployment strategies for the trained model.


### Achnowledments
Jay Alammar Blog - [https://jalammar.github.io/illustrated-transformer/]
Transformers - [https://github.com/huggingface/transformers]
   Paper: [https://arxiv.org/abs/1706.03762]
Framework Used - [https://pytorch.org/]

