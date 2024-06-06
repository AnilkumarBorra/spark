import os, sys
import logging
from preprocess import preprocess_data
from analysis import analyze_data
logger = logging.getLogger(__name__)

def main():
    # logging.basicConfig(filename='./logs/info.log', level=logging.INFO)
    logger.info('Started')
    
    input_path = os.path.join(os.getcwd(), "data","input")
    # print(input_path)
    processed_path = os.path.join(os.getcwd(), "data","output","processed")
    output_path = os.path.join(os.getcwd(), "data","output","RESULTS")
    
    
    # Preprocess data
    preprocess_data(input_path, processed_path)
    
    # Analyze data
    analyze_data(processed_path, output_path)
    
    logger.info('Finished')
    

if __name__ == "__main__":
    main()
