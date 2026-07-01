TeaAid: AI-Based Tea Leaf Disease Detection, Severity Estimation, and RAG Advisory System



TeaAid is an AI-based web application for tea leaf disease analysis. The system allows users to upload a tea leaf image, detect the disease class, estimate disease severity using segmentation, visualize infected regions, and receive disease- and severity-based treatment advice through a RAG-style advisory system.



Project Overview



Tea leaf diseases can reduce tea quality and production if they are not identified early. This project combines deep learning and retrieval-based advisory generation to support early disease analysis and decision-making.



The system performs four main tasks:



Tea leaf disease classification

Pixel-level severity estimation

Segmentation mask visualization

RAG-based treatment advisory generation

Supported Classes



The system supports the following tea leaf classes:



Healthy

Algal Leaf Spot

Brown Blight

Gray Blight

Helopeltis

Key Features

Upload tea leaf image through a web interface

Predict disease class using EfficientNet-B0

Estimate severity using SegFormer-B0 segmentation

Display segmentation output with infected and leaf regions

Show confidence score and severity percentage

Provide severity-based RAG advisory

Display Top-2 predictions for moderate-confidence cases

Show warning messages for uncertain or visually overlapping symptoms

Model Pipeline

1\. Classification



EfficientNet-B0 is used for disease classification. It predicts the disease class and confidence score from the uploaded tea leaf image.



2\. Severity Estimation



SegFormer-B0 is used for semantic segmentation. The model identifies infected pixels and leaf pixels.



Severity is calculated using:



Severity (%) = (Infected Pixels / Total Leaf Area) × 100



Severity levels:



Severity Level	Range

Healthy	0%

Mild	>0–15%

Moderate	>15–40%

Severe	>40%

3\. RAG-Based Advisory



A structured tea disease knowledge base is used to generate treatment advice. The advisory response is based on:



Predicted disease class

Severity percentage

Severity grade

Safety rules

Disease-specific treatment guidance



The system avoids giving unsafe pesticide dosages and recommends following local agricultural expert guidance, product labels, PPE requirements, and pre-harvest intervals.



Tech Stack

Frontend

React

Vite

CSS

Backend

FastAPI

Python

PyTorch

TorchVision

Transformers

pypdf

Models

EfficientNet-B0 for classification

SegFormer-B0 for severity estimation and segmentation

