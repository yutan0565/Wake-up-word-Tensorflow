from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, LSTM
from tensorflow.keras.layers import BatchNormalization, LeakyReLU
from tensorflow.keras import Sequential
from configuration import Config

#######
#Trainable params: 372,166
def detection_model_01(sample_shape):
    model = Sequential([
        # conv layer 부분
        Conv2D(32, (3, 3), activation='relu', input_shape=sample_shape, kernel_initializer='he_normal'),
        MaxPooling2D(pool_size=(3, 3)),
        Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding="same"),
        MaxPooling2D(pool_size=(3, 3)),
        Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same'),
        MaxPooling2D(pool_size=(3, 3)),
        Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same'),
        # MaxPooling2D(pool_size=(3, 3)),

        # FC layer 부분
        Flatten(),
        Dense(256, activation='relu', kernel_initializer='he_normal'),
        Dense(256, activation='relu', kernel_initializer='he_normal'),
        Dropout(0.5),
        Dense(64, activation='relu'),
        Dense(len(Config.target_list), activation="softmax", kernel_initializer='he_normal')
    ])

    return model


# 모델 크기가 작은 거 !!!
def detection_model_02(sample_shape):
    model = Sequential([
        # conv layer 부분
        Conv2D(32, (3, 3), activation=LeakyReLU(alpha=0.3), input_shape=sample_shape, kernel_initializer='he_normal'),
        MaxPooling2D(pool_size=(3, 3)),
        Conv2D(128, (3, 3), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        MaxPooling2D(pool_size=(3, 3)),

        # FC layer 부분
        Flatten(),
        Dense(64, activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        Dropout(0.5),
        Dense(64, activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        Dense(len(Config.target_list), activation="softmax", kernel_initializer='he_normal')
    ])
    return model


# 인식 전용 모델
#######
# Trainable params: 565,731
def recog_model_01(sample_shape):
    model = Sequential([
        # conv layer 부분
        Conv2D(32, (3, 3), activation=LeakyReLU(alpha=0.3), input_shape=sample_shape, kernel_initializer='he_normal'),
        Conv2D(32, (3, 3), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        MaxPooling2D(pool_size=(3, 3)),
        Conv2D(64, (3, 3), activation=LeakyReLU(alpha=0.3), padding='same', kernel_initializer='he_normal'),
        Conv2D(64, (3, 3), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        MaxPooling2D(pool_size=(3, 3)),
        Conv2D(128, (3, 3), activation=LeakyReLU(alpha=0.3), padding='same', kernel_initializer='he_normal'),
        Conv2D(128, (3, 3), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        MaxPooling2D(pool_size=(3, 3)),

        # FC layer 부분
        Flatten(),
        Dense(256, activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        Dense(256, activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        Dropout(0.5),
        Dense(64, activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        Dense(len(Config.user_list), activation="softmax", kernel_initializer='he_normal')
    ])
    return model

# Trainable params: 730,563
def recog_model_02(sample_shape):
    model = Sequential([
        # conv layer 부분
        Conv2D(32, (4, 2), activation=LeakyReLU(alpha=0.3), input_shape=sample_shape, kernel_initializer='he_normal' ),
        Conv2D(32, (4, 2), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal', padding="same"),
        MaxPooling2D(pool_size=(4, 2)),
        Conv2D(64, (4, 2), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal', padding='same'),
        Conv2D(64, (4, 2), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal', padding='same'),
        MaxPooling2D(pool_size=(4, 2)),
        Conv2D(128, (3, 3), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal', padding='same'),
        Conv2D(128, (3, 3), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal', padding='same'),
        MaxPooling2D(pool_size=(4, 2)),
        Conv2D(128, (3, 3), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal', padding='same'),


        # FC layer 부분
        Flatten(),
        Dense(256, activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        Dense(256, activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        Dropout(0.5),
        Dense(64, activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        Dense(len(Config.user_list), activation="softmax")
    ])
    return model

def recog_model_03(sample_shape):
    model = Sequential([
        # conv layer 부분
        Conv2D(32, (4, 2), activation=LeakyReLU(alpha=0.3), input_shape=sample_shape, kernel_initializer='he_normal' ),
        Conv2D(32, (4, 2), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal', padding="same"),
        MaxPooling2D(pool_size=(4, 2)),
        Conv2D(64, (4, 2), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal', padding='same'),
        Conv2D(64, (4, 2), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal', padding='same'),
        MaxPooling2D(pool_size=(4, 2)),
        Conv2D(128, (3, 3), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal', padding='same'),
        Conv2D(128, (3, 3), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal', padding='same'),
        MaxPooling2D(pool_size=(4, 2)),
        Conv2D(128, (3, 3), activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal', padding='same'),


        # FC layer 부분
        Flatten(),
        Dense(256, activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        Dense(256, activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        Dropout(0.5),
        Dense(64, activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        Dense(len(Config.user_list), activation="softmax")
    ])
    return model





# https://sosal.kr/1105 이거로 수정 해보기
def recog_model_04(sample_shape):
    model = Sequential([
        # conv layer 부분
        LSTM(100, activation=LeakyReLU(alpha=0.3), input_shape=sample_shape, kernel_initializer='he_normal',
             return_sequences=True),
        LSTM(100, activation=LeakyReLU(alpha=0.3), return_sequences=True),
        LSTM(100, activation=LeakyReLU(alpha=0.3), return_sequences=True),
        LSTM(100, activation=LeakyReLU(alpha=0.3), return_sequences=True),
        LSTM(100, activation=LeakyReLU(alpha=0.3), return_sequences=True),
        LSTM(100, activation=LeakyReLU(alpha=0.3), return_sequences=True),
        LSTM(100, activation=LeakyReLU(alpha=0.3), return_sequences=True),
        LSTM(100, activation=LeakyReLU(alpha=0.3), return_sequences=True),
        LSTM(100, activation=LeakyReLU(alpha=0.3), return_sequences=True),
        LSTM(100, activation=LeakyReLU(alpha=0.3), return_sequences=True),
        LSTM(100, activation=LeakyReLU(alpha=0.3), return_sequences=True),
        LSTM(100, activation=LeakyReLU(alpha=0.3), return_sequences=True),
        LSTM(100, activation=LeakyReLU(alpha=0.3), return_sequences=True),
        LSTM(3),
        Dense(256, activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        Dense(256, activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        Dropout(0.5),
        Dense(64, activation=LeakyReLU(alpha=0.3), kernel_initializer='he_normal'),
        Dense(len(Config.user_list), activation="softmax")
    ])
    return model