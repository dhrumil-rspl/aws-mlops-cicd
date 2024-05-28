from model import train_and_save_model

if __name__ == "__main__":
    data_path = '../data/raw/data.csv'
    model_path = 'model.pkl'
    train_and_save_model(data_path, model_path)
