import sys
from nlp.classfication.bilstm_att_classifier import BiLSTMAttentionClassifier
sys.path.append('/home/msg/workspace/pycharm/nlp-tutorials')


if __name__ == '__main__':
    model = BiLSTMAttentionClassifier('data/quora/GoogleNews-vectors-negative300.bin.gz', 'model/att',
                                      'model/att/config.pkl', train=True)
    print(model.predict('this is very good movie, i want to watch it again!'))
    print(model.predict('this is very bad movie, i hate it'))
