import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def confusion_matrix_heatmap(y_val, y_pred, y_labels, **kgArgs):
    '''Mapa de calor basado en la matriz de confucion'''
    # Matriz de confusión en un mapa de calor  
    sns.heatmap(confusion_matrix(y_val, y_pred, **kgArgs), vmin=0, square=True, annot=True, cbar=True, 
                cmap='coolwarm',xticklabels=y_labels, yticklabels=y_labels)
    plt.xlabel("Predicción")
    plt.ylabel("Valor real")
    plt.title("Matriz de Confusión")
    plt.show()