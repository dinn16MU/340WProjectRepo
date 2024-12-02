# 340WProjectRepo
Predicting Player Performance and Market Value

Overview

This project aims to predict football player performance and market valuation using machine learning models. It addresses the inefficiencies of traditional scouting and valuation methods by providing data-driven insights for player evaluation and team management. By leveraging advanced analytics, the project supports scouts, coaches, and managers in making more informed decisions.
Features

    Comprehensive Data Analysis: Processes over 1,400 players' performance metrics from top leagues worldwide.
    Position-Specific Insights: Models tailored to player roles, emphasizing critical attributes like finishing for attackers and passing accuracy for midfielders.
    Advanced Machine Learning Models: Utilizes Gradient Boosting and supervised linear regression for market value prediction with a mean accuracy of 87.2%.
    Data Processing and Reduction: Employs techniques like PCA to optimize dataset relevance and performance.
    Visual and Statistical Evaluations: Heatmaps, correlation analysis, and performance metrics (MSE, RMSE) validate the models.

Dataset

The project utilizes datasets from:

    Fbref.com: Player performance statistics.
    Transfermarkt: Market valuation data.

Key Attributes

    Attackers: Goals, Shots on Target, xG (Expected Goals), and npxG (Non-Penalty Expected Goals).
    Midfielders: Pass Completion Rate, Key Passes, xA (Expected Assists), and Carries.
    Defenders: Tackles, Interceptions, and Clearances.

Methodology

    Data Collection:
        Web-scraped statistics from Fbref and Transfermarkt.
        Normalized and preprocessed to remove missing or irrelevant data.

    Dimensionality Reduction:
        PCA applied to retain over 90% of data variance.
        Key attributes selected based on correlation analysis.

    Model Training:
        Gradient Boosting: Effective for predicting market valuation with log-transformed data.
        Neural Networks: Superior for overall performance prediction using position-specific features.

    Evaluation Metrics:
        R², MSE, and RMSE used to validate the models.
        Visual evaluations via scatter plots and residual analysis.

Results

    Market Valuation:
        Achieved an average accuracy of 87.2%.
        Gradient Boosting effectively captured non-linear relationships in market data.
    Performance Prediction:
        TensorFlow-based neural networks achieved an R² of 0.8410, outperforming traditional models.

Applications

    Team Management: Enhances decision-making for team composition and player recruitment.
    Scouting: Provides objective and updated market valuations for better negotiation.
    Coaching: Supports training strategies with performance insights.

Requirements

    Python 3.7+
    Libraries: TensorFlow, Scikit-learn, Pandas, Matplotlib, Seaborn, BeautifulSoup


