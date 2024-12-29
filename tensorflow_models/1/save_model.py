import os
import tensorflow as tf

# Vérification de la version de TensorFlow
print(f"Version de TensorFlow : {tf.__version__}")

# Définir le chemin de sauvegarde et s'assurer qu'il existe
save_path = os.path.join(os.getcwd(), 'tensorflow_models', 'mnist_model', '1')
os.makedirs(save_path, exist_ok=True)
print(f"Le chemin de sauvegarde est : {save_path}")

# Charger le dataset MNIST
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Créer un modèle simple
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compiler le modèle
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entraîner le modèle
model.fit(x_train, y_train, epochs=5)

# Sauvegarder le modèle
tf.saved_model.save(model, save_path)


# Vérifier le contenu du dossier de sauvegarde
print("\nContenu du dossier de sauvegarde :")
for root, dirs, files in os.walk(save_path):
    level = root.replace(save_path, '').count(os.sep)
    indent = ' ' * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    sub_indent = ' ' * 4 * (level + 1)
    for f in files:
        print(f"{sub_indent}{f}")
