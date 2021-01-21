# Standarise the Data
 X_org = image_matrix.copy()
 sc = StandardScaler()
 X = sc.fit_transform(X_org)
 # this is the size of our encoded representations
 encoding_dim = reduced_pixel
 # this is our input placeholder
 input_img = Input(shape=(img.width,))
 # "encoded" is the encoded representation of the input
 encoded = Dense(encoding_dim, activation='linear')(input_img)
 # "decoded" is the lossy reconstruction of the input
 decoded = Dense(img.width, activation=None)(encoded)
 # this model maps an input to its reconstruction
 autoencoder = Model(input_img, decoded)
 #Encoder
 encoder = Model(input_img, encoded)
 # create a placeholder for an encoded (32-dimensional) input
 encoded_input = Input(shape=(encoding_dim,))
 # retrieve the last layer of the autoencoder model
 decoder_layer = autoencoder.layers[-1]
 # create the decoder model
 decoder = Model(encoded_input, decoder_layer(encoded_input))
 autoencoder.compile(optimizer='adadelta', loss='mean_squared_error')
 autoencoder.fit(X, X,
                 epochs=500,
                 batch_size=16,
                 shuffle=True)
 encoded_imgs = encoder.predict(X)
 decoded_imgs = decoder.predict(encoded_imgs)