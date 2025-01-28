import sys 
from dataclass import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OnehotEncoder, StandardScaler

from src.exceptions import CustomException
from src.logger import Logging 
import os
 from src.utils import save_object

 @dataclass
 class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        ''' this function is responsiable for the data transformation'''
        try:
            numerical_columns = ['writing_score','reading_score']
            categorical_columns = ['gender',
            'race_ethnicity',
            'parental_level_of_education',
            'lunch',
            'test_preparation_course']

            num_pipeline = pipeline(
                steps=[
                    ("imputer", simpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )

            cat_pipeline = pipeline(
                steps=[
                ("imputer", simpleImputer(strategy='most_frequent')),
                ('one_hot_encoder',one_hot_encoder()),
                ('scaler',scaler())
            ])
            logging.info(f'numerical_columns:{numerical_columns}')
            logging.info(f'Categorical columns:{categorical_columns}')

            preprocessors = ColumnTransformer(
                [('num_pipeline',num_pipeline,numerical_columns),
                ('cat_pipeline',cat_pipeline,categorical_columns)]
            )

            return preprocessors
        except:
            raise CustomException(e,sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info('Read the train and test data')

            preprocesing_obj = self.get_data_tranformation_object()

            targed_column_name="math_score"
            numerical_columns_name=['writing_score', 'reading_score']

            input_feacture_train_df = train_df.drop(columns=[targed_column_name],axis=1)
            target_feacture_train_df = train_df[targed_column_name]

            input_feacture_test_df = test_df.drop(columns=[targed_column_name],axis=1)
            target_feacture_test_df = test_df[targed_column_name]

            loggin.info(f'Applying the preprocessing object on training and testing data frame. ')

            input_feacture_train_arr = proprocessing_obj.fit_transform(input_feacture_train_df)
            input_feacture_test_arr = proprocessing_obj.transform(input_feacture_test_df)

            train_arr = np.c_[
                input_feacture_train_arr, np.array(target_feacture_train_df)
            ]
            test_arr = np.c_[
                input_feacture_test_arr, np.array(target_feacture_test_df)  
            ]

            logging.info(f'Savined the preprocessing object.')
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,)
        except Exception as e:
            raise CustomException (e,sys)
