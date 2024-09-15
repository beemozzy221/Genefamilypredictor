from sklearn.model_selection import train_test_split
import keras
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Input
import encoder 

def neural_nets(X, y,no_of_g_fam,testX):
    
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)
    
    n1,n2,n3=X.shape;

    y_train=encoder.encodery(y_train)
    y_test=encoder.encoderytest(y_test)
    
    # Initialize the model
    model = Sequential()

    # Flatten the rows and columns into a linear dimensional vector
    model.add(Input(shape=(n2,n3)))

    # Add a fully connected layer with 128 neurons and ReLU activation
    model.add(Dense(64, activation='relu'))

    # Add another fully connected layer with 64 neurons and ReLU activation
    model.add(Dense(10, activation='relu'))

    # Add another fully connected layer with 64 neurons and ReLU activation
    model.add(Dense(10, activation='relu'))

    model.add(Flatten())

    # Add the output layer with the number of gene families (one for each class) and softmax activation
    model.add(Dense(no_of_g_fam, activation='softmax'))

    # Compile the model
    model.compile(optimizer='adam', 
                  loss='categorical_crossentropy', 
                  metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

    # Evaluate the model on the test set
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print(f'Test accuracy: {test_acc}')

    results=model.predict(testX, batch_size=32)

    model.summary()

    print(results[0])
